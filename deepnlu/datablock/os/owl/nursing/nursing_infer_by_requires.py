
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

class NursingInferByRequires(object):

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
 'config': {'classname': 'NursingInferByRequires',
            'filename': 'nursing_infer_by_requires',
            'queries': ['infer_by_requires.sparql % $PREFIX=nursing'],
            'transformers': ['infer_by_requires']},
 'source': 'nursing.owl',
 'time': '2022-05-20 17:02:25.043203'}

    __data = {
    'building': [   {   'context': ['closure'],
                        'id': '4b879b8e-d899-11ec-ac02-4c1d96716627',
                        'replace': 'closure',
                        'with': 'facility_closure'}],
    'closure': [   {   'context': ['building'],
                       'id': '4b879b8e-d899-11ec-ac02-4c1d96716627',
                       'replace': 'closure',
                       'with': 'facility_closure'}],
    'diploma': [   {   'context': ['nursing_education'],
                       'id': '4b879b92-d899-11ec-bc8d-4c1d96716627',
                       'replace': 'diploma',
                       'with': 'nursing_diploma'}],
    'facility_closure': [   {   'context': ['medical_building'],
                                'id': '4b879b91-d899-11ec-be4b-4c1d96716627',
                                'replace': 'facility_closure',
                                'with': 'medical_facility_closure'}],
    'health_care': [   {   'context': ['health_care_specialist'],
                           'id': '4b879b8f-d899-11ec-b0de-4c1d96716627',
                           'replace': 'health_care',
                           'with': 'patient_care'},
                       {   'context': ['patient'],
                           'id': '4b879b90-d899-11ec-9365-4c1d96716627',
                           'replace': 'health_care',
                           'with': 'patient_care'}],
    'health_care_specialist': [   {   'context': ['nursing_diploma'],
                                      'id': '4b879b8d-d899-11ec-bc05-4c1d96716627',
                                      'replace': 'health_care_specialist',
                                      'with': 'nurse'},
                                  {   'context': ['health_care'],
                                      'id': '4b879b8f-d899-11ec-b0de-4c1d96716627',
                                      'replace': 'health_care',
                                      'with': 'patient_care'}],
    'medical_building': [   {   'context': ['facility_closure'],
                                'id': '4b879b91-d899-11ec-be4b-4c1d96716627',
                                'replace': 'facility_closure',
                                'with': 'medical_facility_closure'}],
    'nurse_educator': [   {   'context': ['school'],
                              'id': '4b879b8c-d899-11ec-adc7-4c1d96716627',
                              'replace': 'school',
                              'with': 'nursing_school'}],
    'nursing_diploma': [   {   'context': ['health_care_specialist'],
                               'id': '4b879b8d-d899-11ec-bc05-4c1d96716627',
                               'replace': 'health_care_specialist',
                               'with': 'nurse'}],
    'nursing_education': [   {   'context': ['diploma'],
                                 'id': '4b879b92-d899-11ec-bc8d-4c1d96716627',
                                 'replace': 'diploma',
                                 'with': 'nursing_diploma'}],
    'patient': [   {   'context': ['health_care'],
                       'id': '4b879b90-d899-11ec-9365-4c1d96716627',
                       'replace': 'health_care',
                       'with': 'patient_care'}],
    'school': [   {   'context': ['nurse_educator'],
                      'id': '4b879b8c-d899-11ec-adc7-4c1d96716627',
                      'replace': 'school',
                      'with': 'nursing_school'}]}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
