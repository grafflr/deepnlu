
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

class SkillsTrie(object):

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
 'config': {'classname': 'SkillsTrie',
            'filename': 'skills_trie',
            'queries': ['trie.sparql'],
            'transformers': ['lowercase', 'trie']},
 'source': 'skills.owl',
 'time': '2022-04-27 21:15:54.419855'}

    __data = {
    1: [   'communication',
           'practitioner',
           'psychiatrist',
           'entrepreneur',
           'facilitator',
           'perspective',
           'facilitate',
           'government',
           'university',
           'influencer',
           'negotiate',
           'publisher',
           'professor',
           'innovator',
           'influence',
           'president',
           'producer',
           'activist',
           'academic',
           'advocate',
           'musician',
           'creative',
           'inventor',
           'lecturer',
           'beginner',
           'delivery',
           'company',
           'mediate',
           'deliver',
           'produce',
           'advisor',
           'empathy',
           'startup',
           'council',
           'founder',
           'forbes',
           'expert',
           'school',
           'writer',
           'mentor',
           'author',
           'policy',
           'agenda',
           'skill',
           'forum',
           'law',
           'cxo',
           'cto',
           'ceo'],
    2: [   'innovation',
           'economic',
           'business',
           'personal',
           'trusted',
           'thought',
           'harvard',
           'senior',
           'master',
           'board',
           'vice',
           'soft',
           'the'],
    3: ['national', 'harvard', 'global', 'social', 'world', 'chief'],
    4: [],
    5: [],
    6: []}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
