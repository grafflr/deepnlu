
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

class AppraisalKnockoutListRev(object):

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
 'config': {'classname': 'AppraisalKnockoutList',
            'filename': 'appraisal_knockout_list',
            'queries': ['knockout_list.sparql'],
            'restrict': ['appraisal'],
            'reverse': True,
            'transformers': ['knockout_list']},
 'source': 'appraisal.owl',
 'time': '2022-04-27 21:14:33.623283'}

    __data = {
    'Crazy Effective': ['maximum effectiveness'],
    'Creatively': ['creative'],
    'Dependably': ['dependable'],
    'Effortlessly': ['effort'],
    'Herculean Effort': ['maximum effort'],
    'Highly': ['high'],
    'Imaginatively': ['imagination'],
    'Incredible Contributor': ['maximum contribution'],
    'Innovatively': ['innovation'],
    'Insanely Productive': ['maximum productivity'],
    'Ridiculously Efficient': ['maximum efficiency'],
    'Strongly': ['strong']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
