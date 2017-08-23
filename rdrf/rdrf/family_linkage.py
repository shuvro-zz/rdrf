from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.template.context_processors import csrf
from django.http import Http404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.db import transaction

from rdrf.models import Registry
from registry.patients.models import Patient, PatientRelative

import logging

logger = logging.getLogger(__name__)


def fml_log(msg):
    logger.info("***FAMILY LINKAGE: %s" % msg)


class FamilyLinkageError(Exception):
    pass


class FamilyLinkageType:
    index = "fh_is_index"
    relative = "fh_is_relative"


class MongoUndo(object):

    def __init__(self, patient, linkage_type):
        self.patient = patient
        self.linkage_type = linkage_type
        self.reverse_op = {FamilyLinkageType.index: FamilyLinkageType.relative,
                           FamilyLinkageType.relative: FamilyLinkageType.index}

    def __call__(self):
        reversed_value = self.reverse_op[self.linkage_type]
        self.patient.set_form_value("fh", "ClinicalData", "fhDateSection", "CDEIndexOrRelative", reversed_value)


class FamilyLinkageManager(object):

    def __init__(self, registry_model, packet):
        self.registry_model = registry_model
        self.packet = packet
        if not registry_model.has_feature("family_linkage"):
            raise FamilyLinkageError("need family linkages feature to use FamilyManager")
        self.index_dict = self.packet["index"]
        self.original_index_dict = self.packet["original_index"]
        self.original_index = int(self.original_index_dict["pk"])

        self.relatives = self.packet["relatives"]
        self.index_patient = self._get_index_patient()

        self.working_groups = [wg for wg in self.index_patient.working_groups.all()]
        self.mongo_undos = []

    def _get_index_patient(self):
        try:
            return Patient.objects.get(pk=self.original_index)
        except Patient.DoesNotExist:
            raise FamilyLinkageError("original index patient does not exist")

    def run(self):
        if self._index_changed():
            fml_log("index has changed")
            self._update_index()
        else:
            fml_log("index unchanged")
            self._update_relatives()

    def _update_relatives(self):
        for relative_dict in self.relatives:
            if relative_dict['class'] == "PatientRelative":
                rel = PatientRelative.objects.get(pk=relative_dict["pk"])
                if rel.relationship != relative_dict["relationship"]:
                    rel.relationship = relative_dict["relationship"]
                    rel.save()
            elif relative_dict['class'] == "Patient":
                patient = Patient.objects.get(pk=relative_dict["pk"])
                rel = PatientRelative()
                rel.date_of_birth = patient.date_of_birth
                rel.patient = self.index_patient
                rel.given_names = relative_dict["given_names"]
                rel.family_name = relative_dict["family_name"]
                rel.relationship = relative_dict["relationship"]
                rel.relative_patient = patient
                rel.save()
                self._set_as_relative(patient)

    def _index_changed(self):
        if self.original_index_dict["class"] != self.index_dict["class"]:
            # ie patient relative being dragged to become an index
            fml_log("index class changed")
            return True
        else:
            return self.original_index != int(self.index_dict["pk"])

    def _update_index(self):
        fml_log("updating index")
        old_index_patient = self.index_patient
        fml_log("old index = %s" % old_index_patient)

        if self.index_dict["class"] == "Patient":
            fml_log("updating index from Patient")
            new_index_patient = Patient.objects.get(pk=self.index_dict["pk"])
            fml_log("new_index_patient = %s" % new_index_patient)
            self._change_index(old_index_patient, new_index_patient)

        elif self.index_dict["class"] == "PatientRelative":
            patient_relative = PatientRelative.objects.get(pk=self.index_dict["pk"])
            fml_log("updating index from patient_relative %s" % patient_relative)
            if patient_relative.relative_patient:
                fml_log("patient has been created from this relative so setting index to it")
                self._change_index(old_index_patient, patient_relative.relative_patient)
                fml_log("deleting patient relative %s" % patient_relative)
                # set a flag on patient_relative so the delete signal doesn't archive the patient..
                fml_log("setting skip_archiving attribute on PatientRelative")
                patient_relative.skip_archiving = True
                patient_relative.delete()
                fml_log("deleted patient relative")
            else:
                # create a new patient from relative first
                fml_log("setting PatientRelatibe with no patient to index - need to create patient first")
                new_patient = patient_relative.create_patient_from_myself(self.registry_model, self.working_groups)
                fml_log("new patient created from relative = %s" % new_patient)
                self._change_index(old_index_patient, new_patient)
                fml_log("changed index ok to new patient")
                patient_relative.skip_archiving = True
                patient_relative.delete()
                fml_log("deleted old patient relative")

    def _change_index(self, old_index_patient, new_index_patient):
        self._set_as_index_patient(new_index_patient)
        updated_rels = set([])
        original_relatives = set([r.pk for r in old_index_patient.relatives.all()])
        for relative_dict in self.relatives:
            if relative_dict["class"] == "PatientRelative":
                patient_relative = PatientRelative.objects.get(pk=relative_dict["pk"])
                patient_relative.patient = new_index_patient
                patient_relative.relationship = relative_dict["relationship"]
                patient_relative.save()
                updated_rels.add(patient_relative.pk)

            elif relative_dict["class"] == "Patient":
                # index 'demoted' : create patient rel object
                patient = Patient.objects.get(pk=relative_dict["pk"])

                new_patient_relative = PatientRelative()
                new_patient_relative.date_of_birth = patient.date_of_birth
                new_patient_relative.patient = new_index_patient
                new_patient_relative.relative_patient = patient
                new_patient_relative.given_names = relative_dict["given_names"]
                new_patient_relative.family_name = relative_dict["family_name"]
                self._set_as_relative(patient)
                new_patient_relative.relationship = relative_dict["relationship"]
                new_patient_relative.save()
                updated_rels.add(new_patient_relative.pk)
            else:
                fml_log("???? %s" % relative_dict)

        promoted_relatives = original_relatives - updated_rels
        fml_log("promoted rels = %s" % promoted_relatives)

    def _get_new_relationship(self, relative_pk):
        for item in self.relatives:
            if item["class"] == "PatientRelative" and item["pk"] == relative_pk:
                updated_relationship = item["relationship"]
                return updated_relationship

        return None

    def _add_undo(self, patient, value):
        undo = MongoUndo(patient, value)
        self.mongo_undos.append(undo)

    def _set_as_relative(self, patient):
        main_context_model = self._get_main_context(patient)
        patient.set_form_value("fh", "ClinicalData", "fhDateSection",
                               "CDEIndexOrRelative", "fh_is_relative", main_context_model)
        fml_log("set patient %s to relative" % patient)
        self._add_undo(patient, "fh_is_relative")

    def _set_as_index_patient(self, patient):
        main_context_model = self._get_main_context(patient)
        patient.set_form_value("fh", "ClinicalData", "fhDateSection",
                               "CDEIndexOrRelative", "fh_is_index", main_context_model)
        fml_log("set patient %s to index" % patient)
        self._add_undo(patient, "fh_is_index")

    def _get_main_context(self, patient_model):
        # return the correct context which contains the clinical form we need to update
        main_context_group = self.registry_model.default_context_form_group
        for context_model in patient_model.context_models:
            if context_model.context_form_group and context_model.context_form_group.pk == main_context_group.pk:
                return context_model

        raise Exception("Can't get main context group")


class FamilyLinkageView(View):

    @method_decorator(login_required)
    def get(self, request, registry_code, initial_index=None):

        try:
            registry_model = Registry.objects.get(code=registry_code)
            if not registry_model.has_feature("family_linkage"):
                raise Http404("Registry does not support family linkage")

        except Registry.DoesNotExist:
            raise Http404("Registry does not exist")

        context = {}
        context.update(csrf(request))

        context['registry_code'] = registry_code
        context['index_lookup_url'] = reverse("v1:index-list", args=(registry_code,))
        context["initial_index"] = initial_index
        context["location"] = "Family Linkage"

        return render(request, 'rdrf_cdes/family_linkage.html', context)

    @method_decorator(login_required)
    def post(self, request, registry_code, initial_index=None):
        try:
            import json
            registry_model = Registry.objects.get(code=registry_code)
            packet = json.loads(request.POST["packet_json"])
            fml_log("packet = %s" % packet)
            self._process_packet(registry_model, packet)
            #messages.add_message(request, messages.SUCCESS, "Linkages updated successfully")
            return HttpResponse("OK")

        except Exception as err:
            #messages.add_message(request, messages.ERROR, "Linkage update failed: %s" % err)
            return HttpResponse("FAIL: %s" % err)

    def _process_packet(self, registry_model, packet):
        fml_log("packet = %s" % packet)
        flm = FamilyLinkageManager(registry_model, packet)
        try:
            with transaction.atomic():
                flm.run()

        except Exception as ex:
            for undo in flm.mongo_undos:
                try:
                    undo()
                except Exception as ex:
                    logger.error("could not undo %s" % undo)

            raise ex



class FamilyLinkageOperations:
    # Assumes registry_model has feature family_linkage 
    def __init__(self, registry_model, patient_model):
        self.registry_model = registry_model
        self.patient_model = patient_model
        # Which form.section, cde , stores index/relative flag
        self.indicator_form = self._get_clinical_data_form()
        self.indicator_section = self._get_indicator_section()
        self.indicator_cde = self._get_indicator_cde()
        self.index_value = self._get_index_value()
        self.relative_value = self._get_relative_value()
        self.default_context = get_main_context(self.registry_model,
                                                self.patient_model)

    def mark_as_relative(self):
        self.patient_model.set_form_value(self.registry_model.code,
                               self.indicator_form.name,
                               self.indicator_section.code,
                               self.indicator_cde.code,
                               self.relative_value,
                               context_model=self.default_context)


    def mark_as_index(self):
        # only mark when first created
        if self._has_no_dynamic_data:
            self.patient_model.set_form_value("fh",
                                   "ClinicalData",
                                   "fhDateSection",
                                   "CDEIndexOrRelative",
                                  "fh_is_index",
                                   context_model=default_context)

            # form progress/currency wasn't being updated correctly
            # The following line mimics what happens on a normal form save
            patient_wrapper = DynamicDataWrapper(patient, rdrf_context_id=default_context.pk)
            patient_wrapper.save_form_progress(fh.code, default_context)

            logger.debug("marked patient as index ok")

        except Exception as ex:
            logger.error("error running hook: %s" % ex)

            

    def has_no_mongo_data(patient, registry_model):
        logger.debug("checking mongo data")
        context_model = get_main_context(registry_model, patient)
        if context_model is None:
            logger.debug("context model is None")
            # true when a new patient
            return True
        wrapper = DynamicDataWrapper(patient, rdrf_context_id=context_model.pk)
        data = wrapper.load_dynamic_data(registry_model.code, 'cdes')
        logger.debug("loaded dynamic data = %s" % data)
        if data is None:
            logger.debug("mongo data None")
            return True
        else:
            logger.debug("mongo record exists")
            return False

    fh = Registry.objects.get(code="fh")

    if fh.has_feature('family_linkage') and fh.pk in registry_ids and has_no_mongo_data(patient, fh):
        logger.debug("marking patient %s as index .." % patient.pk)

        # patient has just been added to fh
        # get the current context form group
        try:
            logger.debug("fh registry added hook running setting to index")
            default_context = get_main_context(fh, patient)
            logger.debug("main context for patient %s is %s" % (patient, default_context.pk))

            if default_context is None:
                pass

            patient.set_form_value("fh",
                                   "ClinicalData",
                                   "fhDateSection",
                                   "CDEIndexOrRelative",
                                  "fh_is_index",
                                   context_model=default_context)

            # form progress/currency wasn't being updated correctly
            # The following line mimics what happens on a normal form save
            patient_wrapper = DynamicDataWrapper(patient, rdrf_context_id=default_context.pk)
            patient_wrapper.save_form_progress(fh.code, default_context)

            logger.debug("marked patient as index ok")

        except Exception as ex:
            logger.error("error running hook: %s" % ex)

    
        


def get_default_context(fh_registry_model, patient_model):
    # clinical form is member of default form group
    cfg = fh_registry_model.default_context_form_group
    # can't use usual get_or_create as generic
    try:
        default_context = RDRFContext.objects.get(registry=fh_registry_model,
                                                  context_form_group=cfg,
                                                  object_id=patient_model.pk)
    except RDRFContext.DoesNotExist:
        default_context = RDRFContext(registry=fh_registry_model,
                                      context_form_group=cfg,
                                      content_object=patient_model)

        default_context.display_name = cfg.get_default_name(patient_model)
        default_context.save()

    logger.debug("default context = %s" % default_context)
    return default_context


def get_main_context(fh_registry_model, patient_model):
    """
    Return the context where we need to stick the index/relative field value
    I.e. the context which has that non-multiple (static) form group containing
    the main clinical form
    """
    for context_model in patient_model.context_models:
        if context_model.context_form_group:
            if context_model.context_form_group.is_default:
                return context_model

    logger.debug("no main context - ???? - returning None")


@hook("patient_created_from_relative")
def mark_as_relative_in_clinical_form(patient):
    # Ensure that a patient created from a relative is marked as a relative in the clinical form
   


@hook("registry_added")

