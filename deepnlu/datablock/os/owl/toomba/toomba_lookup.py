
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

class ToombaLookup(object):

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
 'config': {'classname': 'ToombaLookup',
            'filename': 'toomba_lookup',
            'files': ['toomba.txt'],
            'queries': ['lookup.sparql'],
            'transformers': ['lowercase', 'lookup']},
 'source': 'toomba.owl',
 'time': '2022-04-27 21:15:54.137855'}

    __data = {
    1: [   'classification',
           'cleaners',
           'cleaning',
           'channels',
           'channel',
           'cleaned',
           'cleaner',
           'cleanup',
           'action',
           'target',
           'cleans',
           'clean'],
    2: ['question classification', 'command classification', 'clean channel'],
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
