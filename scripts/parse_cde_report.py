import django
django.setup()

from rdrf.models import Registry, RegistryForm, Section ,CDEPermittedValueGroup, CDEPermittedValue, CommonDataElement
from lxml import etree
import sys

class ParserError(Exception):
    pass



class NINDSReportParser:
    CDE_CODE = 'textbox12'
    CDE_NAME = 'VariableName'
    CDE_DEFINITION = 'Definition'
    CDE_DATATYPE = 'textbox26'
    CDE_INSTRUCTIONS = 'textbox57'
    CDE_REFERENCES = 'textbox58'
    CDE_POPULATION = 'textbox81'
    CDE_CLASSIFICATION = 'textbox59'
    CDE_VERSION = 'VersionNumber'
    CDE_VERSION_DATE = 'VersionDate'
    CDE_VARIABLE_NAME = 'textbox74'
    CDE_VARIABLE_NAME_ALIASES = 'textbox67'
    CDE_SUBDOMAIN = 'textbox62'
    CDE_CRF_MODULE = 'textbox63'
    CDE_DOMAIN = 'textbox87'
    CDE_PV_CODE = 'textbox34'
    PVG_CODE = 'textbox22'
    PV_CODE = 'textbox34'
    PV_VALUE = 'textbox7'
    PV_DESC = 'textbox90'

    DATATYPE_MAPPING = {
    }

    def __init__(self, command):
        if command == "new":
            self.registry_model = None
        else:
            try:
                self.registry_model = Registry.objects.get(code=command)
            except Registry.DoesNotExist:
                raise ParserError("Target registry %s does not exist" % command)
            

    def parse_pvg(self, elem):
        pvg_code = elem.get(self.PVG_CODE)
        # dummy element
        if pvg_code is None:
            return
        try:
            CDEPermittedValueGroup.objects.get(code__exact=pvg_code)
            print "PVG %s already exists." % pvg_code
            return
        except CDEPermittedValueGroup.DoesNotExist:
            pass

        pvg = CDEPermittedValueGroup(code=pvg_code)
        pvg.save()

        print "Created: ", pvg

        for detail in etree.ETXPath('./{rptAllCDE}Detail_Collection/{rptAllCDE}Detail')(elem):
            pv_code = detail.get(self.PV_CODE)
            if pv_code is None:
                continue
            pv = CDEPermittedValue(
                code=detail.get(self.PV_CODE),
                value=detail.get(self.PV_VALUE),
                desc=detail.get(self.PV_DESC),
                pv_group=pvg)
            print "Created:", pv
            pv.save()

        return pvg

    def parse_cde(self, elem, pvg):
        cde_code = elem.get(self.CDE_CODE)
        try:
            CommonDataElement.objects.get(code__exact=cde_code)
            print "CDE %s already exists." % cde_code
            return
        except CommonDataElement.DoesNotExist:
            pass
        new_obj = CommonDataElement(
            code=cde_code,
            name=elem.get(self.CDE_NAME),
            desc=elem.get(self.CDE_DEFINITION),
            datatype=elem.get(self.CDE_DATATYPE),
            
            instructions=elem.get(self.CDE_INSTRUCTIONS),
            references=elem.get(self.CDE_REFERENCES),
            population=elem.get(self.CDE_POPULATION),
            classification=elem.get(self.CDE_CLASSIFICATION),
            version=elem.get(self.CDE_VERSION),
            version_date=(elem.get(self.CDE_VERSION_DATE).split('T', 1))[0],
            variable_name=elem.get(self.CDE_VARIABLE_NAME),
            aliases_for_variable_name=elem.get(self.CDE_VARIABLE_NAME_ALIASES),
            crf_module=elem.get(self.CDE_CRF_MODULE),
            subdomain=elem.get(self.CDE_SUBDOMAIN),
            domain=elem.get(self.CDE_DOMAIN),
            pv_group=pvg,
        )

        cde_model = CommonDataElement(code=cde_code)
        ninds_datatype = elem.get(self.CDE_DATATYPE)
        rdrf_datatype = self.DATATYPE_MAPPING.get(ninds_datatype, None)
        if rdrf_datatype is None:
            raise ParserError("Unknown datatype: %s" % ninds_datatype)

        cde_model.datatype = rdrf_datatype
        
        if rdrf_datatype == "range":
            pvg_model = self._get_or_create_pvg(elem)
            cde_model.pvg = pvg_model

        # set other cde fields ..

        cde_model.save()

        section_model = self._get_or_create_section(elem)
        form_model = self._get_or_create_form(elem)
        self._update_section(section_model, cde_model)
        self._update_form(form_model, section_model)



    def _get_or_create_pvg(self, elem):
        value_list = None
        descriptions_list = None
        existing_pvg_model = self._find_existing_pvg(value_list, descriptions_list)
        if existing_pvg_model is None:
            pvg_model = self._create_pvg(value_list, descriptions_list)
            return pvg_model
        else:
            return existing_pvg_model

    def _find_existing_pvg(self, value_list, descriptions_list):
        # not sure good idea to reuse pvgs anyway
        return None

    def _create_pvg(self, cde_code, value_list, description_list):
        pvg_group = CDEPermittedValueGroup()
        pvg_group.code = self._generate_pvg_code(

        
        
        
            

    
    def parse_file(self, xml_file):
        print "Parsing: " + xml_file
        with open(xml_file, 'r') as fd:
            et = etree.parse(fd)
        for table1_group1 in etree.ETXPath(
                './{rptAllCDE}table1/{rptAllCDE}table1_Group1_Collection/{rptAllCDE}table1_Group1')(et.getroot()):
            pvg = None
            for table1_group2 in etree.ETXPath(
                    './{rptAllCDE}table1_Group2_Collection/{rptAllCDE}table1_Group2')(table1_group1):
                pvg = NINDSReportParser.parse_pvg(table1_group2)
            NINDSReportParser.parse_cde(table1_group1, pvg)

if __name__ == '__main__':
    command = sys.argv[1]
    parser = NINDSReportParser(command)
    for report_file in sys.argv[2:]:
        NINDSReportParser.parse_file(report_file)
