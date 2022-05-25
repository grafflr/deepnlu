
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

class MedicalSynonyms(object):

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
 'time': '2022-04-27 21:15:55.967356'}

    __data = {
    'adrenal_gland': ['adrenal gland'],
    'affect': ['affect'],
    'age_bucket': ['age bucket'],
    'agent': ['agent'],
    'artery': ['arteries', 'artery'],
    'baby': ['infant', 'babies', 'baby'],
    'birth': ['birth'],
    'blood': ['blood'],
    'blood_transfusion': ['blood transfusion'],
    'bodily_event': ['bodily event'],
    'brain': ['brain'],
    'breast': ['breast'],
    'breast_milk': ['breast milk'],
    'child': ['childhood', 'children', 'child'],
    'condition': ['condition'],
    'congenital_cytomegalovirus': ['congenital cytomegalovirus'],
    'cytomegalovirus': ['cytomegalovirus', 'cmv'],
    'discharge': ['discharge'],
    'ear': ['ears', 'ear'],
    'effect': ['effect'],
    'emotional_condition': ['emotional condition', 'emotional state'],
    'esophagus': ['esophagus'],
    'event': ['event'],
    'eye': ['eyes', 'eye'],
    'fluid_discharge': ['fluid discharge', 'body fluid'],
    'gland': ['glands', 'gland'],
    'happy': ['happy'],
    'health_event': ['health event'],
    'health_gain': ['health gain'],
    'health_loss': ['health loss'],
    'health_problem': ['health problem'],
    'healthy': ['healthy'],
    'healthy_immunity': ['healthy person immune system', 'healthy immunity'],
    'hearing': ['hearing'],
    'hearing_loss': ['hearing loss'],
    'illness': ['illness'],
    'immune_condition': ['immune condition'],
    'immune_system': ['immune system'],
    'infect': ['infect'],
    'infection': ['infection'],
    'intestines': ['intestines'],
    'liver': ['livers', 'liver'],
    'long_term': ['long term'],
    'lung': ['lungs', 'lung'],
    'mammary_gland': ['mammary gland'],
    'medical_procedure': ['medical procedure'],
    'medical_test': ['medical test'],
    'mental_condition': ['mental condition', 'mental state'],
    'mild': ['mild'],
    'muscle': ['muscles', 'muscle'],
    'organ': ['organs', 'organ'],
    'organ_transplant': ['organ transplant'],
    'parathyroid_gland': ['parathyroid gland'],
    'part_of_body': ['part of body'],
    'person': ['person'],
    'physical_condition': ['physical condition', 'physical state'],
    'pituitary_gland': ['pituitary gland'],
    'problem': ['problem'],
    'qualifiable_state': ['qualifiable state'],
    'qualifiable_time': ['qualifiable time'],
    'qualified_age_bucket': ['qualified age bucket'],
    'quantifiable_state': ['quantifiable state'],
    'quantifiable_time': ['quantifiable time'],
    'quantified_age_bucket': ['quantified age bucket'],
    'saliva': ['saliva'],
    'semen': ['semen'],
    'severe': ['serious', 'severe'],
    'short_term': ['short term'],
    'sight': ['vision', 'sight'],
    'skeletal_muscle': ['skeletal muscle'],
    'smell': ['smell'],
    'spleen': ['spleen'],
    'state': ['state'],
    'state_of_being': ['state of being'],
    'state_of_capability': ['state of capability'],
    'stomach': ['stomach'],
    'symptom': ['symptoms', 'symptom'],
    'system': ['system'],
    'taste': ['taste'],
    'taste_loss': ['taste loss'],
    'tears': ['tears'],
    'time': ['time'],
    'toddler': ['toddler'],
    'tongue': ['tongue'],
    'touch': ['touch'],
    'transfusion': ['transfusions', 'transfusion'],
    'transplant': [   'transplanting',
                      'transplanted',
                      'transplants',
                      'transplant'],
    'urine': ['urine'],
    'virus': ['virus'],
    'vision_loss': ['vision loss'],
    'weak_immunity': ['weakened immune systems', 'weak immunity'],
    'young_child': ['young child']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
