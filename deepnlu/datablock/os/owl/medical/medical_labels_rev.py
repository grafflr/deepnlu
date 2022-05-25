
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

class MedicalLabelsRev(object):

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
 'time': '2022-04-27 21:15:55.991355'}

    __data = {
    'Adrenal Gland': ['adrenal_gland'],
    'Affect': ['affect'],
    'Age Bucket': ['age_bucket'],
    'Agent': ['agent'],
    'Artery': ['artery'],
    'Baby': ['baby'],
    'Birth': ['birth'],
    'Blood': ['blood'],
    'Blood Transfusion': ['blood_transfusion'],
    'Bodily Event': ['bodily_event'],
    'Brain': ['brain'],
    'Breast': ['breast'],
    'Breast Milk': ['breast_milk'],
    'Child': ['child'],
    'Condition': ['condition'],
    'Congenital Cytomegalovirus': ['congenital_cytomegalovirus'],
    'Cytomegalovirus': ['cytomegalovirus'],
    'Discharge': ['discharge'],
    'Ear': ['ear'],
    'Effect': ['effect'],
    'Emotional Condition': ['emotional_condition'],
    'Esophagus': ['esophagus'],
    'Event': ['event'],
    'Eye': ['eye'],
    'Fluid Discharge': ['fluid_discharge'],
    'Gland': ['gland'],
    'Happy': ['happy'],
    'Health Event': ['health_event'],
    'Health Gain': ['health_gain'],
    'Health Loss': ['health_loss'],
    'Health Problem': ['health_problem'],
    'Healthy': ['healthy'],
    'Healthy Immunity': ['healthy_immunity'],
    'Hearing': ['hearing'],
    'Hearing Loss': ['hearing_loss'],
    'Illness': ['illness'],
    'Immune Condition': ['immune_condition'],
    'Immune System': ['immune_system'],
    'Infect': ['infect'],
    'Infection': ['infection'],
    'Intestines': ['intestines'],
    'Liver': ['liver'],
    'Long Term': ['long_term'],
    'Lung': ['lung'],
    'Mammary Gland': ['mammary_gland'],
    'Medical Procedure': ['medical_procedure'],
    'Medical Test': ['medical_test'],
    'Mental Condition': ['mental_condition'],
    'Mild': ['mild'],
    'Muscle': ['muscle'],
    'Organ': ['organ'],
    'Organ Transplant': ['organ_transplant'],
    'Parathyroid Gland': ['parathyroid_gland'],
    'Part of Body': ['part_of_body'],
    'Person': ['person'],
    'Physical Condition': ['physical_condition'],
    'Pituitary Gland': ['pituitary_gland'],
    'Problem': ['problem'],
    'Qualifiable State': ['qualifiable_state'],
    'Qualifiable Time': ['qualifiable_time'],
    'Qualified Age Bucket': ['qualified_age_bucket'],
    'Quantifiable State': ['quantifiable_state'],
    'Quantifiable Time': ['quantifiable_time'],
    'Quantified Age Bucket': ['quantified_age_bucket'],
    'Saliva': ['saliva'],
    'Semen': ['semen'],
    'Severe': ['severe'],
    'Short Term': ['short_term'],
    'Sight': ['sight'],
    'Skeletal Muscle': ['skeletal_muscle'],
    'Smell': ['smell'],
    'Spleen': ['spleen'],
    'State': ['state'],
    'State of Being': ['state_of_being'],
    'State of Capability': ['state_of_capability'],
    'Stomach': ['stomach'],
    'Symptom': ['symptom'],
    'System': ['system'],
    'Taste': ['taste'],
    'Taste Loss': ['taste_loss'],
    'Tears': ['tears'],
    'Time': ['time'],
    'Toddler': ['toddler'],
    'Tongue': ['tongue'],
    'Touch': ['touch'],
    'Transfusion': ['transfusion'],
    'Transplant': ['transplant'],
    'Urine': ['urine'],
    'Virus': ['virus'],
    'Vision Loss': ['vision_loss'],
    'Weak Immunity': ['weak_immunity'],
    'Young Child': ['young_child']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
