
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

class SkillsNerDepth(object):

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
 'time': '2022-04-27 21:15:54.321355'}

    __data = {
    'ABLE': ['1'],
    'ARTIFACT': ['1'],
    'EVENT': ['1'],
    'GOV': ['2'],
    'INC': ['2'],
    'LAW': ['2'],
    'LEARN': ['2'],
    'MENTOR': ['2'],
    'NER': ['0'],
    'ORG': ['1'],
    'PUB': ['2'],
    'ROLE': ['1'],
    'SKILL': ['3']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
