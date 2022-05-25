
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

class RolesInDepartmentsRev(object):

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
 'config': {'classname': 'RolesInDepartments',
            'filename': 'roles_in_departments',
            'queries': ['roles_in_departments.sparql % $PREFIX=roles'],
            'restrict': ['roles'],
            'reverse': True,
            'transformers': ['lowercase']},
 'source': 'roles.owl',
 'time': '2022-04-27 21:17:15.388855'}

    __data = {
    'accounting': [   'auditor',
                      'accountant',
                      'external auditor',
                      'internal auditor'],
    'accounts': ['accountant'],
    'customer service': ['specialist'],
    'engineering': ['engineer'],
    'finance': ['financial analyst'],
    'human resources': ['hiring manager'],
    'it': [   'developer',
              'architect',
              'designer',
              'data analyst',
              'technical role'],
    'logistics': [   'inventory manager',
                     'order processing',
                     'transport operator'],
    'marketing': ['marketing director'],
    'public relations': ['communication technician', 'communication manager'],
    'quality assurance': ['auditor', 'external auditor', 'internal auditor'],
    'research': ['researcher'],
    'sales': ['sales role', 'sales person'],
    'service': [   'technical_support',
                   'agent',
                   'support agent',
                   'senior support agent'],
    'warehousing': ['inventory manager']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
