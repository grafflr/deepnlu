
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

class MedicalSynonymsRev(object):

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
 'config': {'classname': 'MedicalSynonyms',
            'filename': 'medical_synonyms',
            'files': ['medical.txt'],
            'queries': ['synonyms.sparql'],
            'reverse': True,
            'transformers': ['lowercase', 'synonyms']},
 'source': 'medical.owl',
 'time': '2022-04-27 21:15:55.968855'}

    __data = {
    'adrenal gland': ['adrenal_gland'],
    'affect': ['affect'],
    'age bucket': ['age_bucket'],
    'agent': ['agent'],
    'arteries': ['artery'],
    'artery': ['artery'],
    'babies': ['baby'],
    'baby': ['baby'],
    'birth': ['birth'],
    'blood': ['blood'],
    'blood transfusion': ['blood_transfusion'],
    'bodily event': ['bodily_event'],
    'body fluid': ['fluid_discharge'],
    'brain': ['brain'],
    'breast': ['breast'],
    'breast milk': ['breast_milk'],
    'child': ['child'],
    'childhood': ['child'],
    'children': ['child'],
    'cmv': ['cytomegalovirus'],
    'condition': ['condition'],
    'congenital cytomegalovirus': ['congenital_cytomegalovirus'],
    'cytomegalovirus': ['cytomegalovirus'],
    'discharge': ['discharge'],
    'ear': ['ear'],
    'ears': ['ear'],
    'effect': ['effect'],
    'emotional condition': ['emotional_condition'],
    'emotional state': ['emotional_condition'],
    'esophagus': ['esophagus'],
    'event': ['event'],
    'eye': ['eye'],
    'eyes': ['eye'],
    'fluid discharge': ['fluid_discharge'],
    'gland': ['gland'],
    'glands': ['gland'],
    'happy': ['happy'],
    'health event': ['health_event'],
    'health gain': ['health_gain'],
    'health loss': ['health_loss'],
    'health problem': ['health_problem'],
    'healthy': ['healthy'],
    'healthy immunity': ['healthy_immunity'],
    'healthy person immune system': ['healthy_immunity'],
    'hearing': ['hearing'],
    'hearing loss': ['hearing_loss'],
    'illness': ['illness'],
    'immune condition': ['immune_condition'],
    'immune system': ['immune_system'],
    'infant': ['baby'],
    'infect': ['infect'],
    'infection': ['infection'],
    'intestines': ['intestines'],
    'liver': ['liver'],
    'livers': ['liver'],
    'long term': ['long_term'],
    'lung': ['lung'],
    'lungs': ['lung'],
    'mammary gland': ['mammary_gland'],
    'medical procedure': ['medical_procedure'],
    'medical test': ['medical_test'],
    'mental condition': ['mental_condition'],
    'mental state': ['mental_condition'],
    'mild': ['mild'],
    'muscle': ['muscle'],
    'muscles': ['muscle'],
    'organ': ['organ'],
    'organ transplant': ['organ_transplant'],
    'organs': ['organ'],
    'parathyroid gland': ['parathyroid_gland'],
    'part of body': ['part_of_body'],
    'person': ['person'],
    'physical condition': ['physical_condition'],
    'physical state': ['physical_condition'],
    'pituitary gland': ['pituitary_gland'],
    'problem': ['problem'],
    'qualifiable state': ['qualifiable_state'],
    'qualifiable time': ['qualifiable_time'],
    'qualified age bucket': ['qualified_age_bucket'],
    'quantifiable state': ['quantifiable_state'],
    'quantifiable time': ['quantifiable_time'],
    'quantified age bucket': ['quantified_age_bucket'],
    'saliva': ['saliva'],
    'semen': ['semen'],
    'serious': ['severe'],
    'severe': ['severe'],
    'short term': ['short_term'],
    'sight': ['sight'],
    'skeletal muscle': ['skeletal_muscle'],
    'smell': ['smell'],
    'spleen': ['spleen'],
    'state': ['state'],
    'state of being': ['state_of_being'],
    'state of capability': ['state_of_capability'],
    'stomach': ['stomach'],
    'symptom': ['symptom'],
    'symptoms': ['symptom'],
    'system': ['system'],
    'taste': ['taste'],
    'taste loss': ['taste_loss'],
    'tears': ['tears'],
    'time': ['time'],
    'toddler': ['toddler'],
    'tongue': ['tongue'],
    'touch': ['touch'],
    'transfusion': ['transfusion'],
    'transfusions': ['transfusion'],
    'transplant': ['transplant'],
    'transplanted': ['transplant'],
    'transplanting': ['transplant'],
    'transplants': ['transplant'],
    'urine': ['urine'],
    'virus': ['virus'],
    'vision': ['sight'],
    'vision loss': ['vision_loss'],
    'weak immunity': ['weak_immunity'],
    'weakened immune systems': ['weak_immunity'],
    'young child': ['young_child']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
