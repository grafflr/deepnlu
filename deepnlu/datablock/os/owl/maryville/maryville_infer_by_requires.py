
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

class MaryvilleInferByRequires(object):

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
 'config': {'classname': 'MaryvilleInferByRequires',
            'filename': 'maryville_infer_by_requires',
            'queries': ['infer_by_requires.sparql % $PREFIX=maryville'],
            'transformers': ['infer_by_requires']},
 'source': 'maryville.owl',
 'time': '2022-05-17 11:15:52.985593'}

    __data = {
    'building': [   {   'context': ['closure'],
                        'id': '63422529-d60d-11ec-95ce-4c1d96716627',
                        'replace': 'closure',
                        'with': 'facility_closure'}],
    'closure': [   {   'context': ['building'],
                       'id': '63422529-d60d-11ec-95ce-4c1d96716627',
                       'replace': 'closure',
                       'with': 'facility_closure'}],
    'diploma': [   {   'context': ['nursing_education'],
                       'id': '6342252a-d60d-11ec-8526-4c1d96716627',
                       'replace': 'diploma',
                       'with': 'nursing_diploma'}],
    'facility_closure': [   {   'context': ['medical_building'],
                                'id': '63422527-d60d-11ec-af4b-4c1d96716627',
                                'replace': 'facility_closure',
                                'with': 'medical_facility_closure'}],
    'health_care': [   {   'context': ['health_care_specialist'],
                           'id': '6342119c-d60d-11ec-bb80-4c1d96716627',
                           'replace': 'health_care',
                           'with': 'patient_care'},
                       {   'context': ['patient'],
                           'id': '63422525-d60d-11ec-8143-4c1d96716627',
                           'replace': 'health_care',
                           'with': 'patient_care'}],
    'health_care_specialist': [   {   'context': ['health_care'],
                                      'id': '6342119c-d60d-11ec-bb80-4c1d96716627',
                                      'replace': 'health_care',
                                      'with': 'patient_care'},
                                  {   'context': ['nursing_diploma'],
                                      'id': '63422528-d60d-11ec-8351-4c1d96716627',
                                      'replace': 'health_care_specialist',
                                      'with': 'nurse'}],
    'medical_building': [   {   'context': ['facility_closure'],
                                'id': '63422527-d60d-11ec-af4b-4c1d96716627',
                                'replace': 'facility_closure',
                                'with': 'medical_facility_closure'}],
    'nurse_educator': [   {   'context': ['school'],
                              'id': '63422526-d60d-11ec-a84d-4c1d96716627',
                              'replace': 'school',
                              'with': 'nursing_school'}],
    'nursing_diploma': [   {   'context': ['health_care_specialist'],
                               'id': '63422528-d60d-11ec-8351-4c1d96716627',
                               'replace': 'health_care_specialist',
                               'with': 'nurse'}],
    'nursing_education': [   {   'context': ['diploma'],
                                 'id': '6342252a-d60d-11ec-8526-4c1d96716627',
                                 'replace': 'diploma',
                                 'with': 'nursing_diploma'}],
    'patient': [   {   'context': ['health_care'],
                       'id': '63422525-d60d-11ec-8143-4c1d96716627',
                       'replace': 'health_care',
                       'with': 'patient_care'}],
    'school': [   {   'context': ['nurse_educator'],
                      'id': '63422526-d60d-11ec-a84d-4c1d96716627',
                      'replace': 'school',
                      'with': 'nursing_school'}]}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
