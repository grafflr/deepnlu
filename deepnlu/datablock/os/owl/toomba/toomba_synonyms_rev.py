
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

class ToombaSynonymsRev(object):

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
 'time': '2022-04-27 21:15:54.198857'}

    __data = {
    'action': ['action'],
    'channel': ['channel'],
    'channels': ['channel'],
    'classification': ['classification'],
    'clean': ['clean'],
    'clean channel': ['clean_channel'],
    'cleaned': ['clean'],
    'cleaner': ['clean'],
    'cleaners': ['clean'],
    'cleaning': ['clean'],
    'cleans': ['clean'],
    'cleanup': ['clean'],
    'command classification': ['command_classification'],
    'question classification': ['question_classification'],
    'target': ['target']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
