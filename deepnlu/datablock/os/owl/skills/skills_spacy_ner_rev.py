
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

class SkillsSpacyNERRev(object):

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
 'config': {'classname': 'SkillsSpacyNER',
            'filename': 'skills_spacy_ner',
            'firstonly': True,
            'queries': ['ner.sparql % $PREFIX=skills $NER=spacyNER'],
            'reverse': True,
            'transformers': ['ner']},
 'source': 'skills.owl',
 'time': '2022-04-27 21:15:54.485855'}

    __data = {
    'ORG': [   'university',
               'startup',
               'council',
               'forum',
               'publisher',
               'forbes',
               'government',
               'school',
               'organization',
               'company',
               'harvard university',
               'the economist',
               'business school',
               'global innovation council',
               'forbes.com',
               'harvard business school',
               'world economic forum']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]