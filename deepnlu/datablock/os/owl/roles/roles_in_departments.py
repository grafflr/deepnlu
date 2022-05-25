
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

class RolesInDepartments(object):

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
 'time': '2022-04-27 21:17:15.387858'}

    __data = {
    'accountant': ['accounting', 'accounts'],
    'agent': ['service'],
    'architect': ['it'],
    'auditor': ['quality assurance', 'accounting'],
    'communication manager': ['public relations'],
    'communication technician': ['public relations'],
    'data analyst': ['it'],
    'designer': ['it'],
    'developer': ['it'],
    'engineer': ['engineering'],
    'external auditor': ['quality assurance', 'accounting'],
    'financial analyst': ['finance'],
    'hiring manager': ['human resources'],
    'internal auditor': ['quality assurance', 'accounting'],
    'inventory manager': ['warehousing', 'logistics'],
    'marketing director': ['marketing'],
    'order processing': ['logistics'],
    'researcher': ['research'],
    'sales person': ['sales'],
    'sales role': ['sales'],
    'senior support agent': ['service'],
    'specialist': ['customer service'],
    'support agent': ['service'],
    'technical role': ['it'],
    'technical_support': ['service'],
    'transport operator': ['logistics']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
