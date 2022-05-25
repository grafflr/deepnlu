
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

class AskadaLookup(object):

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
 'config': {'classname': 'AskadaLookup',
            'filename': 'askada_lookup',
            'files': ['askada.txt'],
            'queries': ['lookup.sparql'],
            'transformers': ['lowercase', 'lookup']},
 'source': 'askada.owl',
 'time': '2022-04-27 21:15:54.032355'}

    __data = {
    1: ['classification', 'action', 'target', 'toomba', 'clean', 'hint'],
    2: [],
    3: [],
    4: [],
    5: [],
    6: []}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
