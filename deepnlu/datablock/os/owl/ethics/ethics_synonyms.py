
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

class EthicsSynonyms(object):

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
 'config': {'classname': 'EthicsSynonyms',
            'filename': 'ethics_synonyms',
            'files': ['ethics.txt'],
            'queries': ['synonyms.sparql'],
            'reverse': True,
            'transformers': ['lowercase', 'synonyms']},
 'source': 'ethics.owl',
 'time': '2022-04-27 21:15:55.232856'}

    __data = {
    'data_ethics': ['data ethics'],
    'ethics': ['ethicals', 'ethical', 'ethics', 'ethic'],
    'inquiry': ['inquiry'],
    'intellectual_inquiry': ['intellectual inquiry'],
    'moral_philosophy': ['moral philosophy'],
    'philosophy': ['philosophy']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
