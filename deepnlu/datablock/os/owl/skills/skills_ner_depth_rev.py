
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

class SkillsNerDepthRev(object):

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
 'config': {'classname': 'SkillsNerDepth',
            'filename': 'skills_ner_depth',
            'firstonly': True,
            'queries': ['depth.sparql'],
            'reverse': True,
            'transformers': ['depth']},
 'source': 'skills.owl',
 'time': '2022-04-27 21:15:54.322357'}

    __data = {
    '0': ['NER'],
    '1': ['ROLE', 'EVENT', 'ARTIFACT', 'ABLE', 'ORG'],
    '2': ['MENTOR', 'LAW', 'INC', 'GOV', 'PUB', 'LEARN'],
    '3': ['SKILL']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
