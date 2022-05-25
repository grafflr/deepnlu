
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

class RolesTypes(object):

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
 'config': {'classname': 'RolesTypes',
            'filename': 'roles_types',
            'queries': ['subclass.sparql'],
            'reverse': True,
            'transformers': ['types']},
 'source': 'roles.owl',
 'time': '2022-04-27 21:17:15.524355'}

    __data = {
    'accountant': ['role'],
    'accounting': ['department'],
    'accounts': ['department'],
    'administration': ['department'],
    'administrative_accounting': ['accounting'],
    'agent': ['role'],
    'analyst': ['role'],
    'architect': ['technical_role'],
    'auditing': ['activity'],
    'auditor': ['role'],
    'budget_allocation': ['activity'],
    'communication_manager': ['manager'],
    'communication_technician': ['role'],
    'conduct_interviews': ['activity'],
    'customer_service': ['service'],
    'data_analyst': ['technical_role'],
    'data_gathering': ['activity'],
    'delivery_coordination': ['activity'],
    'designer': ['technical_role'],
    'developer': ['technical_role'],
    'director': ['role'],
    'edp': ['department'],
    'employee_onboarding': ['activity'],
    'employee_safety': ['activity'],
    'engineer': ['role'],
    'engineering': ['department'],
    'event_marketing': ['activity'],
    'export': ['department'],
    'external_auditor': ['auditor'],
    'finance': ['department'],
    'financial_analyst': ['analyst'],
    'financial_statement_preparation': ['auditing'],
    'forecasting': ['activity'],
    'freight_shipping': ['activity'],
    'hiring_manager': ['manager'],
    'historical_analysis': ['activity'],
    'human_resources': ['department'],
    'imports': ['department'],
    'internal_auditor': ['auditor'],
    'inventory_analysis': ['auditing'],
    'inventory_manager': ['manager'],
    'inventory_tracking': ['activity'],
    'invoice_preparation': ['activity'],
    'ip_protection': ['activity'],
    'it': ['department'],
    'knowledge_organization': ['activity'],
    'logistics': ['department'],
    'manager': ['role'],
    'manufacturing': ['department'],
    'marketing': ['department'],
    'marketing_director': ['director'],
    'materials_administration': ['administration'],
    'model_development': ['activity'],
    'model_generation': ['activity'],
    'order_processing': ['role'],
    'production': ['department'],
    'public_relations': ['department'],
    'purchasing': ['department'],
    'quality_assurance': ['department'],
    'record_maintenance': ['activity'],
    'recruitment': ['activity'],
    'reporting': ['activity'],
    'research': ['department'],
    'researcher': ['role'],
    'retail_replenishment': ['activity'],
    'risk_analysis': ['activity'],
    'sales': ['department'],
    'sales_person': ['sales_role'],
    'sales_role': ['role'],
    'senior_support_agent': ['support_agent'],
    'service': ['department'],
    'software_support': ['activity'],
    'specialist': ['role'],
    'stock_level_reporting': ['activity'],
    'support_agent': ['agent'],
    'tax_preparation': ['activity'],
    'technical_role': ['role'],
    'technical_support': ['service'],
    'transport_operator': ['role'],
    'trend_analysis': ['activity'],
    'vehicle_maintenance': ['activity'],
    'warehousing': ['department']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
