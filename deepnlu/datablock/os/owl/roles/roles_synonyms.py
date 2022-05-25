
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

class RolesSynonyms(object):

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
 'time': '2022-04-27 21:17:15.515855'}

    __data = {
    'accountant': ['accountant'],
    'accounting': ['accounting'],
    'accounts': ['accounts'],
    'activity': ['activity'],
    'administration': ['administration'],
    'administrative_accounting': ['administrative accounting'],
    'agent': ['agent'],
    'analyst': ['analyst'],
    'architect': ['architect'],
    'auditing': ['auditing'],
    'auditor': ['auditor'],
    'budget_allocation': ['budget allocation'],
    'communication_manager': ['communication manager'],
    'communication_technician': ['communication technician'],
    'conduct_interviews': ['conduct interviews'],
    'customer_service': ['customer service'],
    'data_analyst': ['data analyst'],
    'data_gathering': ['data gathering'],
    'delivery_coordination': ['delivery coordination'],
    'department': ['department'],
    'designer': ['designer'],
    'developer': ['developer'],
    'director': ['director'],
    'edp': ['edp'],
    'employee_onboarding': ['employee onboarding'],
    'employee_safety': ['employee safety'],
    'engineer': ['engineer'],
    'engineering': ['engineering'],
    'event_marketing': ['event marketing'],
    'export': ['export sales', 'dispatch', 'shipping', 'export'],
    'external_auditor': ['external auditor'],
    'finance': ['finance'],
    'financial_analyst': ['financial analyst'],
    'financial_statement_preparation': ['financial statement preparation'],
    'forecasting': ['forecasting'],
    'freight_shipping': ['freight shipping'],
    'hiring_manager': ['hiring manager'],
    'historical_analysis': ['historical analysis'],
    'human_resources': [   'human resources',
                           'personnel',
                           'staffing',
                           'staff',
                           'hr'],
    'imports': ['imports'],
    'internal_auditor': ['internal auditor'],
    'inventory_analysis': ['inventory analysis'],
    'inventory_manager': ['inventory manager'],
    'inventory_tracking': ['inventory tracking'],
    'invoice_preparation': ['invoice preparation'],
    'ip_protection': ['ip protection'],
    'it': ['it'],
    'knowledge_organization': ['knowledge organization'],
    'logistics': ['logistics'],
    'manager': ['manager'],
    'manufacturing': ['manufacturing'],
    'marketing': ['marketing'],
    'marketing_director': ['marketing director'],
    'materials_administration': ['materials administration'],
    'model_development': ['model development'],
    'model_generation': ['model generation'],
    'order_processing': ['order processing'],
    'production': ['production'],
    'public_relations': ['public relations', 'pr'],
    'purchasing': ['purchasing'],
    'quality_assurance': ['quality assurance', 'qa'],
    'record_maintenance': ['record maintenance'],
    'recruitment': ['recruitment'],
    'reporting': ['reporting'],
    'research': ['research and development', 'research', 'r&d'],
    'researcher': ['researcher'],
    'retail_replenishment': ['retail replenishment'],
    'risk_analysis': ['risk analysis'],
    'sales': ['sales'],
    'sales_person': ['sales person'],
    'sales_role': ['sales role'],
    'senior_support_agent': ['senior support agent', 'technical_support'],
    'service': ['service'],
    'software_support': ['software support'],
    'specialist': ['specialist'],
    'stock_level_reporting': ['stock level reporting'],
    'support_agent': ['technical_support', 'support agent'],
    'tax_preparation': ['tax preparation'],
    'technical_role': ['technical role'],
    'technical_support': ['technical support'],
    'transport_operator': ['transport operator'],
    'trend_analysis': ['trend analysis'],
    'vehicle_maintenance': ['vehicle maintenance'],
    'warehousing': ['warehousing']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
