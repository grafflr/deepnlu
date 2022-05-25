
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

class MedicalTypes(object):

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
 'time': '2022-04-27 21:15:55.975355'}

    __data = {
    'adrenal_gland': ['gland'],
    'artery': ['organ'],
    'baby': ['qualified_age_bucket'],
    'birth': ['bodily_event'],
    'blood': ['fluid_discharge'],
    'blood_transfusion': ['transfusion'],
    'bodily_event': ['health_event'],
    'brain': ['organ'],
    'breast': ['organ'],
    'breast_milk': ['fluid_discharge'],
    'child': ['qualified_age_bucket'],
    'congenital_cytomegalovirus': ['cytomegalovirus'],
    'cytomegalovirus': ['virus'],
    'discharge': ['bodily_event'],
    'ear': ['organ'],
    'emotional_condition': ['state_of_being'],
    'esophagus': ['organ'],
    'eye': ['organ'],
    'fluid_discharge': ['discharge'],
    'gland': ['organ'],
    'happy': ['mental_condition'],
    'health_event': ['event'],
    'health_gain': ['health_event'],
    'health_loss': ['health_event'],
    'health_problem': ['problem'],
    'healthy': ['physical_condition'],
    'healthy_immunity': ['immune_condition'],
    'hearing': ['state_of_capability'],
    'hearing_loss': ['health_loss'],
    'illness': ['health_problem'],
    'immune_condition': ['state_of_being'],
    'immune_system': ['system'],
    'infect': ['health_event'],
    'infection': ['health_problem'],
    'intestines': ['organ'],
    'liver': ['organ'],
    'long_term': ['qualifiable_time'],
    'lung': ['organ'],
    'mammary_gland': ['gland'],
    'medical_test': ['medical_procedure'],
    'mental_condition': ['state_of_being'],
    'mild': ['qualifiable_state'],
    'muscle': ['organ'],
    'nose': ['organ'],
    'organ': ['part_of_body'],
    'organ_transplant': ['transplant'],
    'parathyroid_gland': ['gland'],
    'person': ['agent'],
    'physical_condition': ['state_of_being'],
    'pituitary_gland': ['gland'],
    'qualifiable_state': ['state'],
    'qualifiable_time': ['time'],
    'qualified_age_bucket': ['age_bucket'],
    'quantifiable_state': ['state'],
    'quantifiable_time': ['time'],
    'quantified_age_bucket': ['age_bucket'],
    'saliva': ['fluid_discharge'],
    'semen': ['fluid_discharge'],
    'severe': ['qualifiable_state'],
    'short_term': ['qualifiable_time'],
    'sight': ['state_of_capability'],
    'skeletal_muscle': ['muscle'],
    'smell': ['state_of_capability'],
    'spleen': ['organ'],
    'state_of_being': ['state'],
    'state_of_capability': ['condition'],
    'stomach': ['organ'],
    'symptom': ['health_event'],
    'taste': ['state_of_capability'],
    'taste_loss': ['health_loss'],
    'tears': ['fluid_discharge'],
    'toddler': ['child'],
    'tongue': ['organ'],
    'touch': ['state_of_capability'],
    'transfusion': ['medical_procedure'],
    'transplant': ['medical_procedure'],
    'urine': ['fluid_discharge'],
    'vision_loss': ['health_loss'],
    'weak_immunity': ['immune_condition'],
    'young_child': ['child']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
