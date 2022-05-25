
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

class MedicalLabels(object):

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
 'config': {'classname': 'MedicalLabels',
            'filename': 'medical_labels',
            'queries': ['labels.sparql'],
            'reverse': True,
            'transformers': ['labels']},
 'source': 'medical.owl',
 'time': '2022-04-27 21:15:55.989355'}

    __data = {
    'adrenal_gland': ['Adrenal Gland'],
    'affect': ['Affect'],
    'age_bucket': ['Age Bucket'],
    'agent': ['Agent'],
    'artery': ['Artery'],
    'baby': ['Baby'],
    'birth': ['Birth'],
    'blood': ['Blood'],
    'blood_transfusion': ['Blood Transfusion'],
    'bodily_event': ['Bodily Event'],
    'brain': ['Brain'],
    'breast': ['Breast'],
    'breast_milk': ['Breast Milk'],
    'child': ['Child'],
    'condition': ['Condition'],
    'congenital_cytomegalovirus': ['Congenital Cytomegalovirus'],
    'cytomegalovirus': ['Cytomegalovirus'],
    'discharge': ['Discharge'],
    'ear': ['Ear'],
    'effect': ['Effect'],
    'emotional_condition': ['Emotional Condition'],
    'esophagus': ['Esophagus'],
    'event': ['Event'],
    'eye': ['Eye'],
    'fluid_discharge': ['Fluid Discharge'],
    'gland': ['Gland'],
    'happy': ['Happy'],
    'health_event': ['Health Event'],
    'health_gain': ['Health Gain'],
    'health_loss': ['Health Loss'],
    'health_problem': ['Health Problem'],
    'healthy': ['Healthy'],
    'healthy_immunity': ['Healthy Immunity'],
    'hearing': ['Hearing'],
    'hearing_loss': ['Hearing Loss'],
    'illness': ['Illness'],
    'immune_condition': ['Immune Condition'],
    'immune_system': ['Immune System'],
    'infect': ['Infect'],
    'infection': ['Infection'],
    'intestines': ['Intestines'],
    'liver': ['Liver'],
    'long_term': ['Long Term'],
    'lung': ['Lung'],
    'mammary_gland': ['Mammary Gland'],
    'medical_procedure': ['Medical Procedure'],
    'medical_test': ['Medical Test'],
    'mental_condition': ['Mental Condition'],
    'mild': ['Mild'],
    'muscle': ['Muscle'],
    'organ': ['Organ'],
    'organ_transplant': ['Organ Transplant'],
    'parathyroid_gland': ['Parathyroid Gland'],
    'part_of_body': ['Part of Body'],
    'person': ['Person'],
    'physical_condition': ['Physical Condition'],
    'pituitary_gland': ['Pituitary Gland'],
    'problem': ['Problem'],
    'qualifiable_state': ['Qualifiable State'],
    'qualifiable_time': ['Qualifiable Time'],
    'qualified_age_bucket': ['Qualified Age Bucket'],
    'quantifiable_state': ['Quantifiable State'],
    'quantifiable_time': ['Quantifiable Time'],
    'quantified_age_bucket': ['Quantified Age Bucket'],
    'saliva': ['Saliva'],
    'semen': ['Semen'],
    'severe': ['Severe'],
    'short_term': ['Short Term'],
    'sight': ['Sight'],
    'skeletal_muscle': ['Skeletal Muscle'],
    'smell': ['Smell'],
    'spleen': ['Spleen'],
    'state': ['State'],
    'state_of_being': ['State of Being'],
    'state_of_capability': ['State of Capability'],
    'stomach': ['Stomach'],
    'symptom': ['Symptom'],
    'system': ['System'],
    'taste': ['Taste'],
    'taste_loss': ['Taste Loss'],
    'tears': ['Tears'],
    'time': ['Time'],
    'toddler': ['Toddler'],
    'tongue': ['Tongue'],
    'touch': ['Touch'],
    'transfusion': ['Transfusion'],
    'transplant': ['Transplant'],
    'urine': ['Urine'],
    'virus': ['Virus'],
    'vision_loss': ['Vision Loss'],
    'weak_immunity': ['Weak Immunity'],
    'young_child': ['Young Child']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
