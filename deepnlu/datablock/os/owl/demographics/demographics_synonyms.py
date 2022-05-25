
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

class DemographicsSynonyms(object):

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
 'config': {'classname': 'DemographicsSynonyms',
            'filename': 'demographics_synonyms',
            'files': ['demographics.txt'],
            'queries': ['synonyms.sparql'],
            'reverse': True,
            'transformers': ['lowercase', 'synonyms']},
 'source': 'demographics.owl',
 'time': '2022-05-13 12:10:56.701093'}

    __data = {
    'age': ['age'],
    'ethnicity': ['ethnicity'],
    'gender': ['gender'],
    'height': ['height'],
    'location': ['location'],
    'weight': ['weight']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
