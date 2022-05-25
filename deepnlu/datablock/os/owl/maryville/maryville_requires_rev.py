
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

class MaryvilleRequiresRev(object):

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
 'config': {'classname': 'MaryvilleRequires',
            'filename': 'maryville_requires',
            'queries': ['requires.sparql % $PREFIX=maryville'],
            'reverse': True,
            'transformers': ['effects']},
 'source': 'maryville.owl',
 'time': '2022-05-17 11:15:52.954593'}

    __data = {
    'building': ['facility_closure'],
    'health_care_specialist': ['patient_care'],
    'medical_building': ['medical_facility_closure'],
    'nurse_educator': ['nursing_school'],
    'nursing_diploma': ['nurse'],
    'nursing_education': ['nursing_diploma'],
    'patient': ['patient_care']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
