
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

class QuestionsTrie(object):

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
 'config': {'classname': 'QuestionsTrie',
            'filename': 'questions_trie',
            'queries': ['trie.sparql'],
            'transformers': ['lowercase', 'trie']},
 'source': 'questions.owl',
 'time': '2022-05-13 12:06:42.640345'}

    __data = {
    1: [   'organization',
           'redirection',
           'clarifying',
           'refocusing',
           'prompting',
           'ourselves',
           'yourself',
           'myself',
           'your',
           'mine',
           'they',
           'them',
           'our',
           'her',
           'you',
           'she',
           'him',
           'my',
           'we',
           'it',
           'he',
           'me',
           'us',
           'i'],
    2: [   'deductive',
           'critical',
           'simple',
           'where',
           'what',
           'when',
           'who',
           'how',
           'why',
           'do'],
    3: ['present', 'perfect', 'future', 'second', 'third', 'first', 'past'],
    4: ['present', 'future', 'closed', 'what', 'past', 'open'],
    5: ['present', 'future', 'closed', 'past', 'open'],
    6: []}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
