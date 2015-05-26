from django.core import serializers
import copy
import json
from pymongo import MongoClient
import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_save
from django.dispatch import receiver
import pycountry
import registry.groups.models
from registry.utils import get_working_groups, get_registries
from rdrf.models import Registry
from registry.utils import stripspaces
from django.conf import settings
from rdrf.utils import mongo_db_name
from rdrf.utils import requires_feature
from rdrf.dynamic_data import DynamicDataWrapper
from rdrf.models import Section
from rdrf.models import ConsentQuestion
from registry.groups.models import CustomUser
from rdrf.hooking import run_hooks
from django.db.models.signals import m2m_changed

import logging
logger = logging.getLogger('registry_log')

file_system = FileSystemStorage(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)

_MONGO_PATIENT_DATABASE = 'patients'
_MONGO_PATIENT_COLLECTION = 'patient'

_6MONTHS_IN_DAYS = 183


class State(models.Model):
    short_name = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=30)
    country_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name


class Doctor(models.Model):
    # TODO: Is it possible for one doctor to work with multiple working groups?
    family_name = models.CharField(max_length=100, db_index=True)
    given_names = models.CharField(max_length=100, db_index=True)
    surgery_name = models.CharField(max_length=100, blank=True)
    speciality = models.CharField(max_length=100)
    address = models.TextField()
    suburb = models.CharField(max_length=50, verbose_name="Suburb/Town")
    state = models.ForeignKey(State, verbose_name="State/Province/Territory")
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ['family_name']

    def __unicode__(self):
        return "%s %s" % (self.family_name.upper(), self.given_names)


class NextOfKinRelationship(models.Model):
    relationship = models.CharField(max_length=100, verbose_name="Relationship")

    class Meta:
        verbose_name = 'Next of Kin Relationship'

    def __unicode__(self):
        return self.relationship


class PatientManager(models.Manager):
    def get_by_registry(self, registry):
        return self.model.objects.filter(rdrf_registry__in=registry)

    def get_by_working_group(self, user):
        return self.model.objects.filter(working_groups__in=get_working_groups(user))

    def get_filtered(self, user):
        return self.model.objects.filter(rdrf_registry__id__in=get_registries(user)).filter(working_groups__in=get_working_groups(user)).distinct()

    def get_filtered_unallocated(self, user):
        return self.model.objects.filter(working_groups__in=get_working_groups(user)).exclude(rdrf_registry__isnull=False)


class Patient(models.Model):
    if settings.INSTALL_NAME == 'dm1':   # Trac #16 item 9
        SEX_CHOICES = (("M", "Male"), ("F", "Female"))
    else:
        SEX_CHOICES = (("M", "Male"), ("F", "Female"), ("X", "Other/Intersex"))

    ETHNIC_ORIGIN = (
        ("New Zealand European", "New Zealand European"),
        ("Australian", "Australian"),
        ("Other Caucasian/European", "Other Caucasian/European"),
        ("Aboriginal", "Aboriginal"),
        ("Person from the Torres Strait Islands", "Person from the Torres Strait Islands"),
        ("Maori", "Maori"),
        ("NZ European / Maori", "NZ European / Maori"),
        ("Samoan", "Samoan"),
        ("Cook Islands Maori", "Cook Islands Maori"),
        ("Tongan", "Tongan"),
        ("Niuean", "Niuean"),
        ("Tokelauan", "Tokelauan"),
        ("Fijian", "Fijian"),
        ("Other Pacific Peoples", "Other Pacific Peoples"),
        ("Southeast Asian", "Southeast Asian"),
        ("Chinese", "Chinese"),
        ("Indian", "Indian"),
        ("Other Asian", "Other Asian"),
        ("Middle Eastern", "Middle Eastern"),
        ("Latin American", "Latin American"),
        ("Black African/African American", "Black African/African American"),
        ("Other Ethnicity", "Other Ethnicity"),
        ("Decline to Answer", "Decline to Answer"),
    )

    objects = PatientManager()
    rdrf_registry = models.ManyToManyField(Registry)
    working_groups = models.ManyToManyField(registry.groups.models.WorkingGroup, related_name="my_patients", verbose_name="Centre")
    consent = models.BooleanField(null=False, blank=False, help_text="The patient consents to be part of the registry and have data retained and shared in accordance with the information provided to them.", verbose_name="consent given")
    consent_clinical_trials = models.BooleanField(null=False, blank=False, help_text="Consent given to be contacted about clinical trials or other studies related to their condition.", default=False)
    consent_sent_information = models.BooleanField(null=False, blank=False, help_text="Consent given to be sent information on their condition", verbose_name="consent to be sent information given", default=False)
    consent_provided_by_parent_guardian = models.BooleanField(null=False, blank=False, help_text="Parent/Guardian consent provided on behalf of the patient.", default=False)
    family_name = models.CharField(max_length=100, db_index=True)
    given_names = models.CharField(max_length=100, db_index=True)
    maiden_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Maiden Name")
    umrn = models.CharField(max_length=50, null=True, blank=True, db_index=True, verbose_name="Hospital/Clinic ID")
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100, null=True, blank=True, verbose_name="Place of Birth")
    country_of_birth = models.CharField(max_length=100, null=True, blank=True, verbose_name="Country of Birth")
    ethnic_origin = models.CharField(choices=ETHNIC_ORIGIN, max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    home_phone = models.CharField(max_length=30, blank=True, null=True)
    mobile_phone = models.CharField(max_length=30, blank=True, null=True)
    work_phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    next_of_kin_family_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="family name")
    next_of_kin_given_names = models.CharField(max_length=100, blank=True, null=True, verbose_name="given names")
    next_of_kin_relationship = models.ForeignKey(NextOfKinRelationship, verbose_name="Relationship", blank=True, null=True, on_delete=models.SET_NULL)
    next_of_kin_address = models.TextField(blank=True, null=True, verbose_name="Address")
    next_of_kin_suburb = models.CharField(max_length=50, blank=True, null=True, verbose_name="Suburb/Town")
    next_of_kin_state = models.ForeignKey(State, verbose_name="State/Province/Territory", related_name="next_of_kin_set", blank=True, null=True, on_delete=models.SET_NULL)
    next_of_kin_postcode = models.IntegerField(verbose_name="Postcode", blank=True, null=True)
    next_of_kin_home_phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="home phone")
    next_of_kin_mobile_phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="mobile phone")
    next_of_kin_work_phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="work phone")
    next_of_kin_email = models.EmailField(blank=True, null=True, verbose_name="email")
    next_of_kin_parent_place_of_birth = models.CharField(max_length=100, verbose_name="Place of birth of parents", blank=True, null=True)
    doctors = models.ManyToManyField(Doctor, through="PatientDoctor")
    active = models.BooleanField(default=True, help_text="Ticked if active in the registry, ie not a deleted record, or deceased patient.")
    inactive_reason = models.TextField(blank=True, null=True, verbose_name="Reason", help_text="Please provide reason for deactivating the patient")
    clinician = models.ForeignKey(CustomUser, blank=True, null=True)
    user = models.ForeignKey(CustomUser, blank=True, null=True, related_name="user_object", on_delete=models.SET_NULL)

    @property
    def age(self):
        """ in years """
        from datetime import date
        def calculate_age(born):
            today = date.today()
            try:
                birthday = born.replace(year=today.year)
            except ValueError: # raised when birth date is February 29 and the current year is not a leap year
                birthday = born.replace(year=today.year, month=born.month+1, day=1)
            if birthday > today:
                return today.year - born.year - 1
            else:
                return today.year - born.year

        try:
            age_in_years = calculate_age(self.date_of_birth)
            return age_in_years
        except:
            return None

    def has_feature(self, feature):
        return any([r.has_feature(feature) for r in self.rdrf_registry.all()])

    @property
    def working_groups_display(self):
        return ",".join([wg.display_name for wg in self.working_groups.all()])

    @property
    def diagnosis_progress(self):
        """
        returns a map of reg code to an integer between 0-100 (%)
        """
        registry_diagnosis_progress = {}

        for registry_model in self.rdrf_registry.all():
            total_number_filled_in = 0
            total_number_required_for_completion = 0
            for form_model in registry_model.forms:
                # hack
                if not "genetic" in form_model.name.lower():
                    number_filled_in, total_number_for_completion = self.form_progress(form_model, numbers_only=True)
                    total_number_filled_in += number_filled_in
                    total_number_required_for_completion += total_number_for_completion
            try:
                registry_diagnosis_progress[registry_model.code] = int(100.0 * float(total_number_filled_in) / float(total_number_required_for_completion))
            except ZeroDivisionError, zderr:
                pass  # don't have progress? skip

        return registry_diagnosis_progress

    def clinical_data_currency(self, days=365):
        """
        If some clinical form ( non genetic ) has been updated  in the window
        then the data for that registry is considered "current" - this mirrors
        """
        time_window_start = datetime.datetime.now() - datetime.timedelta(days=days)
        currency_map = {}
        for registry_model in self.rdrf_registry.all():
            last_updated_in_window = False
            for form_model in registry_model.forms:
                if "genetic" in form_model.name.lower():
                    continue
                form_timestamp = self.get_form_timestamp(form_model)
                logger.debug("form timestamp %s = %s" % (form_model, form_timestamp))
                if form_timestamp and form_timestamp >= time_window_start:
                    last_updated_in_window = True
                    break
            currency_map[registry_model.code] = last_updated_in_window

        return currency_map

    @property
    def genetic_data_map(self):
        """
        map of reg code to Boolean iff patient has some genetic data filled in
        """
        registry_genetic_progress = {}

        class Sentinel(Exception):
            pass

        for registry_model in self.rdrf_registry.all():
            has_data = False
            try:
                for form_model in registry_model.forms:
                    if "genetic" in form_model.name.lower():
                        for section_model in  form_model.section_models:
                            for cde_model in section_model.cde_models:
                                try:
                                    value = self.get_form_value(registry_model.code,
                                                                form_model.name,
                                                                section_model.code,
                                                                cde_model.code,
                                                                section_model.allow_multiple)

                                    # got value for at least one field
                                    raise Sentinel()
                                except KeyError:
                                    pass
            except Sentinel:
                has_data = True

            registry_genetic_progress[registry_model.code] = has_data
        return registry_genetic_progress


    def get_form_value(self, registry_code, form_name, section_code, data_element_code, multisection=False):
        from rdrf.dynamic_data import DynamicDataWrapper
        from rdrf.utils import mongo_key
        wrapper = DynamicDataWrapper(self)
        mongo_data = wrapper.load_dynamic_data(registry_code, "cdes")
        key = mongo_key(form_name, section_code, data_element_code)
        if mongo_data is None:
            # no mongo data
            raise KeyError(key)
        else:
            if multisection:
                sections = mongo_data[section_code]
                values = []
                for section in sections:
                    if key in section and section[key]:
                        values.append(section[key])
                return values
            else:
                return mongo_data[key]

    def set_form_value(self, registry_code, form_name, section_code, data_element_code, value):
        from rdrf.dynamic_data import DynamicDataWrapper
        from rdrf.utils import mongo_key
        wrapper = DynamicDataWrapper(self)
        mongo_data = wrapper.load_dynamic_data(registry_code, "cdes")
        key = mongo_key(form_name, section_code, data_element_code)
        if mongo_data is None:
            # No dynamic data has been persisted yet
            wrapper.save_dynamic_data(registry_code, "cdes", {key: value})
        else:
            mongo_data[key] = value
            wrapper.save_dynamic_data(registry_code, "cdes", mongo_data)

    def in_registry(self, reg_code):
        """
        returns True if patient belongs to the registry with reg code provided
        """
        for registry in self.rdrf_registry.all():
            if registry.code == reg_code:
                return True


    @property
    def my_index(self):
        # This property is only applicable to FH
        if self.in_registry("fh"):
            # try to find patient relative object corresponding to this patient and
            # then locate that relative's index patient
            try:
                patient_relative = PatientRelative.objects.get(relative_patient=self)
                if patient_relative.patient:
                    return patient_relative.patient
            except PatientRelative.DoesNotExist:
                pass

        return None

    def set_consent(self, consent_model, answer=True, commit=True):
        patient_registries = [r for r in self.rdrf_registry.all()]
        if consent_model.section.registry not in patient_registries:
            return   # error?
        cv, created = ConsentValue.objects.get_or_create(consent_question=consent_model, patient=self)
        cv.answer = answer
        if cv.first_save:
            cv.last_update = datetime.datetime.now()
        else:
            cv.first_save = datetime.datetime.now()
        if commit:
            cv.save()
        return cv

    def get_consent(self, consent_model):
        patient_registries = [r for r in self.rdrf_registry.all()]
        if consent_model.section.registry not in patient_registries:
            return False    # ?
        try:
            cv = ConsentValue.objects.get(patient=self, consent_question=consent_model)
            return cv.answer
        except ConsentValue.DoesNotExist:
            return False    # ?


    @property
    def consent_questions_data(self):
        d = {}
        for consent_value in ConsentValue.objects.filter(patient=self):
            consent_question_model = consent_value.consent_question
            d[consent_question_model.field_key] = consent_value.answer
        return d

    def clean_consents(self):
        my_registries = [r for r in self.rdrf_registry.all() ]
        for consent_value in ConsentValue.objects.filter(patient=self):
            if consent_value.consent_question.section.registry not in my_registries:
                consent_value.delete()

    @property
    def is_index(self):
        if not self.in_registry("fh"):
            return False
        else:
            if not self.my_index:
                return True
            else:
                return False

    @property
    def has_guardian(self):
        return ParentGuardian.objects.filter(patient=self).count() > 0

    @property
    def combined_name(self):
        if self.has_guardian:
            guardians = [pg for pg in ParentGuardian.objects.filter(patient=self)]
            g = guardians[0]
            name = "%s on behalf of %s" % (g, self)
            return name
        else:
            return "%s" % self



    class Meta:
        ordering = ["family_name", "given_names", "date_of_birth"]
        verbose_name_plural = "Patient List"

    def __unicode__(self):
        if self.active:
            return "%s %s" % (self.family_name, self.given_names)
        else:
            return "%s %s (Archived)" % (self.family_name, self.given_names)

    def save(self, *args, **kwargs):
        if hasattr(self, 'family_name'):
            self.family_name = stripspaces(self.family_name).upper()

        if hasattr(self, 'given_names'):
            self.given_names = stripspaces(self.given_names)

        if not self.pk:
            self.active = True

        super(Patient, self).save(*args, **kwargs)
        #regs = self._save_patient_mongo()

    def delete(self, *args, **kwargs):
        """
        If a user deletes a patient it's active flag will be true, so we should set it to false.
        If a superuser deletes a patient it's active flag is false, so we should delete the object.
        """
        if self.active:
            logger.debug("Archiving patient record.")
            self.active = False
            self.save()
        else:
            logger.debug("Deleting patient record.")
            super(Patient, self).delete(*args, **kwargs)

    def get_reg_list(self):
        return ', '.join([r.name for r in self.rdrf_registry.all()])
    get_reg_list.short_description = 'Registry'

    def form_progress(self, registry_form, numbers_only=False):
        if not registry_form.has_progress_indicator:
            if numbers_only:
                return 0, 0

            return [], 0

        dynamic_store = DynamicDataWrapper(self)
        cde_registry = registry_form.registry.code
        section_array = registry_form.sections.split(",")

        cde_complete = registry_form.complete_form_cdes.values()
        set_count = 0

        cdes_status = {}

        for cde in cde_complete:
            cde_section = ""
            for s in section_array:
                section = Section.objects.get(code=s)
                if cde["code"] in section.elements.split(","):
                    cde_section = s
            try:
                cde_value = self.get_form_value(cde_registry, registry_form.name, cde_section, cde['code'], section.allow_multiple)
            except KeyError:
                cde_value = None

            cdes_status[cde["name"]] = False
            if cde_value:
                cdes_status[cde["name"]] = True
                set_count += 1

        if numbers_only:
            return set_count, len(cde_complete)

        return cdes_status, (float(set_count) / float(len(registry_form.complete_form_cdes.values_list())) * 100)

    def get_form_timestamp(self, registry_form):
        dynamic_store = DynamicDataWrapper(self)
        timestamp = dynamic_store.get_form_timestamp(registry_form)
        if timestamp:
            if "timestamp" in timestamp:
                ts = timestamp["timestamp"]
                return ts

    def form_currency(self, registry_form):
        dynamic_store = DynamicDataWrapper(self)
        timestamp = dynamic_store.get_form_timestamp(registry_form)
        if timestamp:
            if "timestamp" in timestamp:
                ts = timestamp["timestamp"]
                delta = datetime.datetime.now() - ts
                return True if delta.days < _6MONTHS_IN_DAYS else False
            else:
                return True
        else:
            return False

    def as_json(self):
        return dict(
            obj_id=self.id,
            given_names=self.given_names,
            family_name=self.family_name,
            working_group=self.working_group.name,
            date_of_birth=str(self.date_of_birth)
        )


class ParentGuardian(models.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, null=True, blank=True, verbose_name="Place of Birth")
    date_of_migration = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    suburb = models.CharField(max_length=50, verbose_name="Suburb/Town")
    state = models.CharField(max_length=20, verbose_name="State/Province/Territory")
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20)
    patient = models.ManyToManyField(Patient)


class AddressType(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.type)


class PatientAddress(models.Model):
    patient = models.ForeignKey(Patient)
    address_type = models.ForeignKey(AddressType, default=1)
    address = models.TextField()
    suburb = models.CharField(max_length=100, verbose_name="Suburb/Town")
    state = models.CharField(max_length=50, verbose_name="State/Province/Territory", blank=True, null=True)
    postcode = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Patient Addresses"

    def __unicode__(self):
        return ""

class PatientConsent(models.Model):
    patient = models.ForeignKey(Patient)
    form = models.FileField(upload_to='consents', storage=file_system, verbose_name="Consent form", blank=True, null=True)


class PatientDoctor(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    relationship = models.CharField(max_length=50)

    class Meta:
        verbose_name = "medical professionals for patient"
        verbose_name_plural = "medical professionals for patient"



def get_countries():
        return [(c.alpha2, c.name) for c in sorted(pycountry.countries, cmp=lambda a, b: a.name < b.name)]


class PatientRelative(models.Model):

    RELATIVE_TYPES = (
        ("1st Degree", "1st Degree"),
        ("2nd Degree", "2nd Degree"),
        ("3rd Degree", "3rd Degree"),
    )

    RELATIVE_LOCATIONS = [
        ("AU - WA", "AU - WA"),
        ("AU - SA", "AU - SA"),
        ("AU - NSW", "AU - NSW"),
        ("AU - QLD", "AU - QLD"),
        ("AU - NT", "AU - NT"),
        ("AU - VIC", "AU - VIC"),
        ("AU - TAS", "AU - TAS"),

    ]

    LIVING_STATES = (('Alive', 'Alive'), ('Deceased', 'Deceased'))

    SEX_CHOICES = (("M", "Male"), ("F", "Female"), ("X", "Other/Intersex"))
    patient = models.ForeignKey(Patient, related_name="relatives")
    family_name = models.CharField(max_length=100)
    given_names = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    relationship = models.CharField(choices=RELATIVE_TYPES, max_length=80)
    location = models.CharField(choices=RELATIVE_LOCATIONS + get_countries(), max_length=80)
    living_status = models.CharField(choices=LIVING_STATES, max_length=80)
    relative_patient = models.OneToOneField(to=Patient, null=True, blank=True, related_name="as_a_relative", verbose_name="Create Patient?")



@receiver(post_save, sender=Patient)
def save_patient_mongo(sender, instance, **kwargs):
    patient_obj = Patient.objects.prefetch_related('rdrf_registry').get(pk=instance.pk)
    _save_patient_mongo(patient_obj)


@receiver(post_save, sender=Patient)
def clean_consents(sender, instance, **kwargs):
    instance.clean_consents()


def _save_patient_mongo(patient_obj):
    client = MongoClient(settings.MONGOSERVER, settings.MONGOPORT)
    patient_db = client[mongo_db_name(_MONGO_PATIENT_DATABASE)]
    patient_coll = patient_db[_MONGO_PATIENT_COLLECTION]

    json_str = serializers.serialize("json", [patient_obj])
    json_obj = json.loads(json_str)

    mongo_doc = patient_coll.find_one({'django_id': json_obj[0]['pk']})

    if mongo_doc:
        _update_mongo_obj(mongo_doc, json_obj[0]['fields'])
        patient_coll.save(mongo_doc)
    else:
        json_obj[0]['fields']['django_id'] = json_obj[0]['pk']
        json_obj[0]['fields']['rdrf_registry'] = _get_registry_for_mongo(patient_obj.rdrf_registry.all())
        patient_coll.save(json_obj[0]['fields'])


def _update_mongo_obj(mongo_doc, patient_model):
    keys_to_delete = []
    for key, value in mongo_doc.iteritems():
        if key in ['rdrf_registry', ]:
            mongo_doc[key] = _get_registry_for_mongo(patient_model[key])
        if key not in ['django_id', '_id', 'rdrf_registry']:
            if key in patient_model:
                logger.info("key %s is not present in patient_model and will be deleted from the mongo doc ..." % key)
                mongo_doc[key] = patient_model[key]
            else:
                keys_to_delete.append(key)

    for key in keys_to_delete:
        del mongo_doc[key]


def _get_registry_for_mongo(regs):
    registry_obj = Registry.objects.filter(pk__in=regs)
    json_str = serializers.serialize("json", registry_obj)
    json_obj = json.loads(json_str)

    json_final = []

    for reg in json_obj:
        reg['fields']['id'] = reg['pk']
        del reg['fields']['splash_screen']
        json_final.append(reg['fields'])

    return json_final


@receiver(post_save, sender=Patient)
@requires_feature('email_notification')
def send_notification(sender, instance, created, **kwargs):
    if created:
        try:
            from django.core.mail import send_mail
            from django.conf import settings
            logger.debug("about to send welcome email to %s patient %s" % (instance.email, instance))
            name = "%s %s" % (instance.given_names, instance.family_name)
            send_mail('Welcome to FKRP!', 'Dear %s\nYou have been added to the FKRP registry.\nPlease note this is a test of the email subsystem only!' % name, settings.DEFAULT_FROM_EMAIL,
                      [instance.email], fail_silently=False)
            logger.debug("sent email ok to %s" % instance.email)
        except Exception, ex:
            logger.error("Error sending welddcome email  to %s with email %s: %s" % (instance, instance.email,  ex))



@receiver(post_save, sender=Patient)
def save_patient_hooks(sender, instance, created, **kwargs):
    if created:
        run_hooks('patient_created', instance)
    else:
        run_hooks('existing_patient_saved', instance)


@receiver(m2m_changed, sender=Patient.rdrf_registry.through)
def registry_changed_on_patient(sender, **kwargs):
    logger.debug("registry changed on patient %s: kwargs = %s" % (kwargs['instance'], kwargs))
    if kwargs["action"] == "post_add":
        instance = kwargs['instance']
        registry_ids = kwargs['pk_set']
        run_hooks('registry_added', instance, registry_ids)


class ConsentValue(models.Model):
    patient = models.ForeignKey(Patient, related_name="consents")
    consent_question = models.ForeignKey(ConsentQuestion)
    answer = models.BooleanField(default=False)
    first_save = models.DateField(null=True, blank=True)
    last_update = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "Consent Value for %s question %s is %s" % (self.patient, self.consent_question, self.answer)
