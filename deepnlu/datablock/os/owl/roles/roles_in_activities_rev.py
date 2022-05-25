
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

class RolesInActivitiesRev(object):

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
 'time': '2022-04-27 21:17:15.375355'}

    __data = {
    'auditing': ['auditor'],
    'budget allocation': ['marketing director'],
    'conduct interviews': ['hiring manager'],
    'data gathering': ['analyst'],
    'delivery coordination': ['order processing'],
    'employee onboarding': ['hiring manager'],
    'employee safety': ['transport operator'],
    'event marketing': ['communication manager'],
    'financial statement preparation': ['auditor'],
    'forecasting': ['analyst'],
    'freight shipping': ['transport operator'],
    'historical analysis': ['analyst'],
    'inventory analysis': ['auditor'],
    'inventory tracking': ['inventory manager'],
    'invoice preparation': ['order processing'],
    'ip protection': ['researcher'],
    'knowledge organization': ['analyst'],
    'model development': ['researcher'],
    'model generation': ['analyst'],
    'record maintenance': ['auditor'],
    'recruitment': ['hiring manager'],
    'reporting': ['analyst'],
    'retail replenishment': ['inventory manager'],
    'risk analysis': ['accountant'],
    'software support': ['technical_support', 'support agent'],
    'stock level reporting': ['inventory manager'],
    'tax preparation': ['accountant'],
    'trend analysis': ['marketing director', 'financial analyst'],
    'vehicle maintenance': ['transport operator']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
