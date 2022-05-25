
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

class MedicalTypesRev(object):

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
 'config': {'classname': 'MedicalTypes',
            'filename': 'medical_types',
            'queries': ['subclass.sparql'],
            'reverse': True,
            'transformers': ['types']},
 'source': 'medical.owl',
 'time': '2022-04-27 21:15:55.976856'}

    __data = {
    'age_bucket': ['qualified_age_bucket', 'quantified_age_bucket'],
    'agent': ['person'],
    'bodily_event': ['discharge', 'birth'],
    'child': ['toddler', 'young_child'],
    'condition': ['state_of_capability'],
    'cytomegalovirus': ['congenital_cytomegalovirus'],
    'discharge': ['fluid_discharge'],
    'event': ['health_event'],
    'fluid_discharge': [   'tears',
                           'semen',
                           'breast_milk',
                           'urine',
                           'blood',
                           'saliva'],
    'gland': [   'adrenal_gland',
                 'mammary_gland',
                 'pituitary_gland',
                 'parathyroid_gland'],
    'health_event': [   'bodily_event',
                        'health_loss',
                        'symptom',
                        'infect',
                        'health_gain'],
    'health_loss': ['vision_loss', 'hearing_loss', 'taste_loss'],
    'health_problem': ['infection', 'illness'],
    'immune_condition': ['weak_immunity', 'healthy_immunity'],
    'medical_procedure': ['transplant', 'medical_test', 'transfusion'],
    'mental_condition': ['happy'],
    'muscle': ['skeletal_muscle'],
    'organ': [   'eye',
                 'muscle',
                 'nose',
                 'artery',
                 'gland',
                 'liver',
                 'brain',
                 'ear',
                 'lung',
                 'tongue',
                 'esophagus',
                 'breast',
                 'spleen',
                 'intestines',
                 'stomach'],
    'part_of_body': ['organ'],
    'physical_condition': ['healthy'],
    'problem': ['health_problem'],
    'qualifiable_state': ['severe', 'mild'],
    'qualifiable_time': ['long_term', 'short_term'],
    'qualified_age_bucket': ['baby', 'child'],
    'state': ['state_of_being', 'quantifiable_state', 'qualifiable_state'],
    'state_of_being': [   'physical_condition',
                          'mental_condition',
                          'emotional_condition',
                          'immune_condition'],
    'state_of_capability': ['hearing', 'taste', 'smell', 'sight', 'touch'],
    'system': ['immune_system'],
    'time': ['quantifiable_time', 'qualifiable_time'],
    'transfusion': ['blood_transfusion'],
    'transplant': ['organ_transplant'],
    'virus': ['cytomegalovirus']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
