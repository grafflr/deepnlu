
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

class ChitchatTrie(object):

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
 'config': {'classname': 'ChitchatTrie',
            'filename': 'chitchat_trie',
            'queries': ['trie.sparql'],
            'transformers': ['lowercase', 'trie']},
 'source': 'chitchat.owl',
 'time': '2022-04-27 21:17:15.284356'}

    __data = {
    1: [   'adorkable',
           'friday',
           'ocelot',
           'kitten',
           'monday',
           'otter',
           'train',
           'early',
           'plane',
           'puppy',
           'horse',
           'hello',
           'late',
           'bus',
           'cat',
           'dog'],
    2: [   'interrogation',
           'disagreeable',
           'deflection',
           'favorable',
           'agreeable',
           'adorkable',
           'transport',
           'negative',
           'sympathy',
           'positive',
           'greeting',
           'location',
           'unknown',
           'weather',
           'reverse',
           'ability',
           'friday',
           'cliche',
           'packed',
           'monday',
           'insult',
           'hello',
           'state',
           'slack',
           'good',
           'like',
           'time',
           'late',
           'bad'],
    3: [   'conditional',
           'negative',
           'favorite',
           'positive',
           'greeting',
           'general',
           'neutral',
           'insult',
           'animal',
           'horse',
           'otter',
           'state',
           'good',
           'free',
           'late',
           'meet',
           'busy',
           'bad',
           'dog',
           'cat'],
    4: ['big'],
    5: [],
    6: []}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
