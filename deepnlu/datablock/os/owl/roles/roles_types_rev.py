
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

class RolesTypesRev(object):

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
 'time': '2022-04-27 21:17:15.525855'}

    __data = {
    'accounting': ['administrative_accounting'],
    'activity': [   'budget_allocation',
                    'event_marketing',
                    'conduct_interviews',
                    'data_gathering',
                    'inventory_tracking',
                    'recruitment',
                    'auditing',
                    'vehicle_maintenance',
                    'model_generation',
                    'reporting',
                    'delivery_coordination',
                    'model_development',
                    'trend_analysis',
                    'retail_replenishment',
                    'forecasting',
                    'ip_protection',
                    'stock_level_reporting',
                    'employee_onboarding',
                    'employee_safety',
                    'tax_preparation',
                    'risk_analysis',
                    'freight_shipping',
                    'invoice_preparation',
                    'software_support',
                    'record_maintenance',
                    'knowledge_organization',
                    'historical_analysis'],
    'administration': ['materials_administration'],
    'agent': ['support_agent'],
    'analyst': ['financial_analyst'],
    'auditing': ['financial_statement_preparation', 'inventory_analysis'],
    'auditor': ['external_auditor', 'internal_auditor'],
    'department': [   'export',
                      'imports',
                      'service',
                      'human_resources',
                      'edp',
                      'public_relations',
                      'administration',
                      'sales',
                      'purchasing',
                      'warehousing',
                      'finance',
                      'accounts',
                      'it',
                      'quality_assurance',
                      'accounting',
                      'manufacturing',
                      'logistics',
                      'research',
                      'marketing',
                      'production',
                      'engineering'],
    'director': ['marketing_director'],
    'manager': ['hiring_manager', 'inventory_manager', 'communication_manager'],
    'role': [   'communication_technician',
                'engineer',
                'auditor',
                'analyst',
                'sales_role',
                'transport_operator',
                'director',
                'specialist',
                'researcher',
                'order_processing',
                'accountant',
                'technical_role',
                'agent',
                'manager'],
    'sales_role': ['sales_person'],
    'service': ['customer_service', 'technical_support'],
    'support_agent': ['senior_support_agent'],
    'technical_role': ['developer', 'data_analyst', 'architect', 'designer']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
