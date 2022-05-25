
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

class EthicsLabelsRev(object):

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
 'config': {'classname': 'EthicsLabels',
            'filename': 'ethics_labels',
            'queries': ['labels.sparql'],
            'reverse': True,
            'transformers': ['labels']},
 'source': 'ethics.owl',
 'time': '2022-04-27 21:15:55.244356'}

    __data = {
    'Data Ethics': ['data_ethics'],
    'Ethics': ['ethics'],
    'Inquiry': ['inquiry'],
    'Intellectual Inquiry': ['intellectual_inquiry'],
    'Moral Philosophy': ['moral_philosophy'],
    'Philosophy': ['philosophy']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
