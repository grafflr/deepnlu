
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

class RolesTrie(object):

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
 'config': {'classname': 'RolesTrie',
            'filename': 'roles_trie',
            'queries': ['trie.sparql'],
            'transformers': ['lowercase', 'trie']},
 'source': 'roles.owl',
 'time': '2022-04-27 21:17:15.532356'}

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
           'accounting',
           'purchasing',
           'researcher',
           'marketing',
           'reporting',
           'logistics',
           'developer',
           'architect',
           'research',
           'engineer',
           'designer',
           'director',
           'auditing',
           'accounts',
           'finance',
           'service',
           'auditor',
           'imports',
           'analyst',
           'manager',
           'export',
           'agent',
           'sales',
           'edp',
           'it'],
    2: [   'administrative',
           'communication',
           'historical',
           'technical',
           'inventory',
           'marketing',
           'knowledge',
           'financial',
           'materials',
           'transport',
           'external',
           'software',
           'employee',
           'internal',
           'customer',
           'delivery',
           'quality',
           'freight',
           'invoice',
           'conduct',
           'vehicle',
           'support',
           'hiring',
           'record',
           'budget',
           'retail',
           'public',
           'trend',
           'human',
           'model',
           'order',
           'sales',
           'event',
           'risk',
           'data',
           'tax',
           'ip'],
    3: ['financial', 'senior', 'stock'],
    4: [],
    5: [],
    6: []}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
