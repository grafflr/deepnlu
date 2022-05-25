
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# pylint:disable=bad-whitespace
# pylint:disable=line-too-long
# pylint:disable=too-many-lines
# pylint:disable=invalid-name

# #########################################################
#
#       ************** !! WARNING !! ***************
#       ******* THIS FILE WAS AUTO-GENERATED *******
#       ********* DO NOT MODIFY THIS FILE **********
#
# #########################################################

class RolesSynonymsRev(object):

    @staticmethod
    def prov() -> dict:
        return {
 'action': ['router.py',
            'plac_core.py',
            'owl2py_orchestrator.py',
            'generate_runtime_dictionaries.py',
            'generate_runtime_dictionary.py',
            'owl_data_load_dict.py',
            'common_utils.py'],
 'config': {'classname': 'RolesSynonyms',
            'filename': 'roles_synonyms',
            'files': ['roles.txt'],
            'queries': ['synonyms.sparql'],
            'reverse': True,
            'transformers': ['lowercase', 'synonyms']},
 'source': 'roles.owl',
 'time': '2022-04-27 21:17:15.517355'}

    __data = {
    'accountant': ['accountant'],
    'accounting': ['accounting'],
    'accounts': ['accounts'],
    'activity': ['activity'],
    'administration': ['administration'],
    'administrative accounting': ['administrative_accounting'],
    'agent': ['agent'],
    'analyst': ['analyst'],
    'architect': ['architect'],
    'auditing': ['auditing'],
    'auditor': ['auditor'],
    'budget allocation': ['budget_allocation'],
    'communication manager': ['communication_manager'],
    'communication technician': ['communication_technician'],
    'conduct interviews': ['conduct_interviews'],
    'customer service': ['customer_service'],
    'data analyst': ['data_analyst'],
    'data gathering': ['data_gathering'],
    'delivery coordination': ['delivery_coordination'],
    'department': ['department'],
    'designer': ['designer'],
    'developer': ['developer'],
    'director': ['director'],
    'dispatch': ['export'],
    'edp': ['edp'],
    'employee onboarding': ['employee_onboarding'],
    'employee safety': ['employee_safety'],
    'engineer': ['engineer'],
    'engineering': ['engineering'],
    'event marketing': ['event_marketing'],
    'export': ['export'],
    'export sales': ['export'],
    'external auditor': ['external_auditor'],
    'finance': ['finance'],
    'financial analyst': ['financial_analyst'],
    'financial statement preparation': ['financial_statement_preparation'],
    'forecasting': ['forecasting'],
    'freight shipping': ['freight_shipping'],
    'hiring manager': ['hiring_manager'],
    'historical analysis': ['historical_analysis'],
    'hr': ['human_resources'],
    'human resources': ['human_resources'],
    'imports': ['imports'],
    'internal auditor': ['internal_auditor'],
    'inventory analysis': ['inventory_analysis'],
    'inventory manager': ['inventory_manager'],
    'inventory tracking': ['inventory_tracking'],
    'invoice preparation': ['invoice_preparation'],
    'ip protection': ['ip_protection'],
    'it': ['it'],
    'knowledge organization': ['knowledge_organization'],
    'logistics': ['logistics'],
    'manager': ['manager'],
    'manufacturing': ['manufacturing'],
    'marketing': ['marketing'],
    'marketing director': ['marketing_director'],
    'materials administration': ['materials_administration'],
    'model development': ['model_development'],
    'model generation': ['model_generation'],
    'order processing': ['order_processing'],
    'personnel': ['human_resources'],
    'pr': ['public_relations'],
    'production': ['production'],
    'public relations': ['public_relations'],
    'purchasing': ['purchasing'],
    'qa': ['quality_assurance'],
    'quality assurance': ['quality_assurance'],
    'r&d': ['research'],
    'record maintenance': ['record_maintenance'],
    'recruitment': ['recruitment'],
    'reporting': ['reporting'],
    'research': ['research'],
    'research and development': ['research'],
    'researcher': ['researcher'],
    'retail replenishment': ['retail_replenishment'],
    'risk analysis': ['risk_analysis'],
    'sales': ['sales'],
    'sales person': ['sales_person'],
    'sales role': ['sales_role'],
    'senior support agent': ['senior_support_agent'],
    'service': ['service'],
    'shipping': ['export'],
    'software support': ['software_support'],
    'specialist': ['specialist'],
    'staff': ['human_resources'],
    'staffing': ['human_resources'],
    'stock level reporting': ['stock_level_reporting'],
    'support agent': ['support_agent'],
    'tax preparation': ['tax_preparation'],
    'technical role': ['technical_role'],
    'technical support': ['technical_support'],
    'technical_support': ['support_agent', 'senior_support_agent'],
    'transport operator': ['transport_operator'],
    'trend analysis': ['trend_analysis'],
    'vehicle maintenance': ['vehicle_maintenance'],
    'warehousing': ['warehousing']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
