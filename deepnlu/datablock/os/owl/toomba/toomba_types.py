
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

class ToombaTypes(object):

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
 'config': {'classname': 'ToombaTypes',
            'filename': 'toomba_types',
            'queries': ['subclass.sparql'],
            'reverse': True,
            'transformers': ['types']},
 'source': 'toomba.owl',
 'time': '2022-04-27 21:15:54.202355'}

    __data = {
    'channel': ['target'],
    'clean': ['action'],
    'clean_channel': ['command_classification'],
    'command_classification': ['classification'],
    'question_classification': ['classification']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
