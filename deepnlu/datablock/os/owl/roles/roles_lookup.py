
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

class RolesLookup(object):

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
 'config': {'classname': 'RolesLookup',
            'filename': 'roles_lookup',
            'files': ['roles.txt'],
            'queries': ['lookup.sparql'],
            'transformers': ['lowercase', 'lookup']},
 'source': 'roles.owl',
 'time': '2022-04-27 21:17:15.404855'}

    __data = {
    1: [   'administration',
           'manufacturing',
           'recruitment',
           'forecasting',
           'engineering',
           'warehousing',
           'specialist',
           'accountant',
           'production',
           'department',
           'accounting',
           'purchasing',
           'researcher',
           'marketing',
           'personnel',
           'reporting',
           'logistics',
           'developer',
           'architect',
           'staffing',
           'research',
           'activity',
           'engineer',
           'dispatch',
           'designer',
           'director',
           'auditing',
           'accounts',
           'shipping',
           'finance',
           'service',
           'auditor',
           'imports',
           'analyst',
           'manager',
           'export',
           'staff',
           'agent',
           'sales',
           'edp',
           'r&d',
           'qa',
           'pr',
           'hr',
           'it'],
    2: [   'financial_statement preparation',
           'administrative accounting',
           'communication technician',
           'materials administration',
           'knowledge organization',
           'stock_level reporting',
           'delivery coordination',
           'communication manager',
           'senior_support agent',
           'retail replenishment',
           'vehicle maintenance',
           'invoice preparation',
           'employee onboarding',
           'historical analysis',
           'inventory analysis',
           'marketing director',
           'transport operator',
           'inventory tracking',
           'conduct interviews',
           'record maintenance',
           'model development',
           'financial analyst',
           'inventory manager',
           'budget allocation',
           'quality assurance',
           'technical support',
           'order processing',
           'customer service',
           'model generation',
           'external auditor',
           'public relations',
           'internal auditor',
           'software support',
           'freight shipping',
           'event marketing',
           'tax preparation',
           'employee safety',
           'human resources',
           'technical role',
           'trend analysis',
           'hiring manager',
           'data gathering',
           'support agent',
           'ip protection',
           'risk analysis',
           'export sales',
           'sales person',
           'data analyst',
           'sales role'],
    3: [   'financial statement preparation',
           'research and development',
           'stock level reporting',
           'senior support agent'],
    4: [],
    5: [],
    6: []}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
