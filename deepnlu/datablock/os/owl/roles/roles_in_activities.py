
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

class RolesInActivities(object):

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
 'config': {'classname': 'RolesInActivities',
            'filename': 'roles_in_activities',
            'queries': ['roles_in_activities.sparql % $PREFIX=roles'],
            'restrict': ['roles'],
            'reverse': True,
            'transformers': ['lowercase']},
 'source': 'roles.owl',
 'time': '2022-04-27 21:17:15.373855'}

    __data = {
    'accountant': ['tax preparation', 'risk analysis'],
    'analyst': [   'knowledge organization',
                   'historical analysis',
                   'model generation',
                   'data gathering',
                   'forecasting',
                   'reporting'],
    'auditor': [   'financial statement preparation',
                   'inventory analysis',
                   'record maintenance',
                   'auditing'],
    'communication manager': ['event marketing'],
    'financial analyst': ['trend analysis'],
    'hiring manager': [   'employee onboarding',
                          'conduct interviews',
                          'recruitment'],
    'inventory manager': [   'stock level reporting',
                             'retail replenishment',
                             'inventory tracking'],
    'marketing director': ['budget allocation', 'trend analysis'],
    'order processing': ['delivery coordination', 'invoice preparation'],
    'researcher': ['model development', 'ip protection'],
    'support agent': ['software support'],
    'technical_support': ['software support'],
    'transport operator': [   'vehicle maintenance',
                              'freight shipping',
                              'employee safety']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
