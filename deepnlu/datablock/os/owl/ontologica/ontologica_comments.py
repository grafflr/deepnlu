
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

class OntologicaComments(object):

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
 'config': {'classname': 'OntologicaComments',
            'filename': 'ontologica_comments',
            'queries': ['comments.sparql'],
            'transformers': ['comments']},
 'source': 'ontologica.owl',
 'time': '2022-05-03 17:49:06.755946'}

    __data = {
    'action_confirmation': [   'Let me find that information for you.',
                               'i would be happy to do that'],
    'action_not_understood': [   "I'm not certain which action to take.",
                                 'I understand your question but not how to '
                                 'act on it.'],
    'action_understood': ['I understand what you want to do'],
    'multi_item_response': ["Here's what i have: items"],
    'no_ancestor_of': ['There are no further ancestors'],
    'no_child_of': ['There are no further children'],
    'no_descendant_of': ['There are no further descendants'],
    'no_parent_of': ['There are no further parents'],
    'one_item_response': ['The answer is item1'],
    'question_not_understood': [   'Err',
                                   'Sorry.  no can do.',
                                   "I didn't catch  that - sorry!",
                                   "I don't understood your question well "
                                   'enough.'],
    'question_understood': ['I understood your question'],
    'three_item_response': ['The answer is item1', 'Item2 and item3'],
    'two_item_response': ['The answer is item1 and item2']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
