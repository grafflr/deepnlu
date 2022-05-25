
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

class DemographicsLookup(object):

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
 'config': {'classname': 'DemographicsLookup',
            'filename': 'demographics_lookup',
            'files': ['demographics.txt'],
            'queries': ['lookup.sparql'],
            'transformers': ['lowercase', 'lookup']},
 'source': 'demographics.owl',
 'time': '2022-05-13 12:10:56.595593'}

    __data = {
    1: ['ethnicity', 'location', 'weight', 'gender', 'height', 'age'],
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
