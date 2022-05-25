
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

class EthicsLookup(object):

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
 'config': {'classname': 'EthicsLookup',
            'filename': 'ethics_lookup',
            'files': ['ethics.txt'],
            'queries': ['lookup.sparql'],
            'transformers': ['lowercase', 'lookup']},
 'source': 'ethics.owl',
 'time': '2022-04-27 21:15:55.172855'}

    __data = {
    1: ['philosophy', 'ethicals', 'ethical', 'inquiry', 'ethics', 'ethic'],
    2: ['intellectual inquiry', 'moral philosophy', 'data ethics'],
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
