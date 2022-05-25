
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

class ToombaSynonyms(object):

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
 'config': {'classname': 'ToombaSynonyms',
            'filename': 'toomba_synonyms',
            'files': ['toomba.txt'],
            'queries': ['synonyms.sparql'],
            'reverse': True,
            'transformers': ['lowercase', 'synonyms']},
 'source': 'toomba.owl',
 'time': '2022-04-27 21:15:54.197855'}

    __data = {
    'action': ['action'],
    'channel': ['channels', 'channel'],
    'classification': ['classification'],
    'clean': [   'cleaners',
                 'cleaning',
                 'cleaned',
                 'cleaner',
                 'cleanup',
                 'cleans',
                 'clean'],
    'clean_channel': ['clean channel'],
    'command_classification': ['command classification'],
    'question_classification': ['question classification'],
    'target': ['target']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
