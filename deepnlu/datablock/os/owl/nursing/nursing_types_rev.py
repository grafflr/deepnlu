
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

class NursingTypesRev(object):

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
 'config': {'classname': 'NursingTypes',
            'filename': 'nursing_types',
            'queries': ['subclass.sparql'],
            'reverse': True,
            'transformers': ['types']},
 'source': 'nursing.owl',
 'time': '2022-05-20 17:02:25.347706'}

    __data = {
    'activity': ['practice', 'political_activity'],
    'admission': ['readmission'],
    'advanced_practice_registered_nurse': ['nurse_practitioner'],
    'agent': ['provider', 'person', 'receiver', 'group'],
    'artifact': ['plan', 'rule', 'diploma', 'regulation'],
    'association': [   'american_nurses_association',
                       'american_association_of_colleges_of_nursing'],
    'bachelor_of_science': ['bachelor_of_science_in_nursing'],
    'bachelors_degree': ['bachelor_of_arts', 'bachelor_of_science'],
    'bias': ['gender_bias', 'racial_bias'],
    'building': [   'home',
                    'department',
                    'medical_building',
                    'site',
                    'airport',
                    'room',
                    'clinic',
                    'school'],
    'care_event': ['health_care'],
    'certification': ['national_certification'],
    'church': ['catholic_church', 'protestant_church'],
    'clinical_evaluation': ['clinical_outcome_evaluation'],
    'closure': ['facility_closure'],
    'company': ['johnson_and_johnson'],
    'competency': ['clinical_competency'],
    'condition': ['health'],
    'continent': ['europe'],
    'country': ['spain'],
    'department': ['health_department'],
    'development': ['professional_development'],
    'diploma': [   'associates_degree',
                   'doctoral_degree',
                   'bachelors_degree',
                   'nursing_diploma',
                   'masters_degree'],
    'education': [   'training',
                     'learning',
                     'health_care_education',
                     'development'],
    'educator': ['nurse_educator'],
    'elapsed_time': ['temporary', 'permanent'],
    'evaluation': ['outcome_evaluation', 'clinical_evaluation', 'peer_review'],
    'event': [   'admission',
                 'care_event',
                 'staffing',
                 'pay',
                 'shortage',
                 'treatment_event',
                 'closure',
                 'history',
                 'labor_event',
                 'outcome',
                 'quality',
                 'century',
                 'evaluation',
                 'training_event',
                 'reform'],
    'facility_closure': ['medical_facility_closure'],
    'geopolitical_entity': ['city', 'country'],
    'group': ['political_group', 'association', 'religious_group'],
    'health': ['mental_health'],
    'health_care': [   'primary_care',
                       'long_term_health_care',
                       'patient_care',
                       'acute_care'],
    'health_care_education': ['nursing_education'],
    'health_care_specialist': ['nurse', 'pharmacist', 'physician'],
    'health_department': ['public_health_department'],
    'home': ['nursing_home'],
    'hospital': ['spanish_hospital'],
    'labor_event': ['strike'],
    'learning': ['continuous_learning'],
    'location': ['continent'],
    'master_of_science': ['master_of_science_in_nursing'],
    'masters_degree': ['master_of_science', 'master_of_arts'],
    'medical_building': ['pharmacy', 'urgent_care', 'hospital', 'surgery'],
    'nationality': ['american', 'spanish'],
    'nurse': ['registered_nurse'],
    'nurse_practitioner': [   'psychiatric_mental_health_nurse_practitioner',
                              'family_nurse_practitioner'],
    'nursing': ['historical_nursing', 'modern_nursing'],
    'organization': ['company'],
    'outcome': ['clinical_outcome'],
    'patient': [   'elderly_patient',
                   'male_patient',
                   'female_patient',
                   'pediactric_patient'],
    'pay': ['fair_pay'],
    'person': ['florence_nightingale'],
    'pharmacist': ['apothecary'],
    'plan': ['patient_treatment_plan'],
    'practice': ['ethical_practice'],
    'profession': ['nursing'],
    'provider': [   'health_care_provider',
                    'surgeon',
                    'specialist',
                    'staff',
                    'educator',
                    'chemist'],
    'quality': ['competency', 'health_care_quality'],
    'quantifiable_measurement': [   'staffing_level',
                                    'mortality_rate',
                                    'readmission_rate',
                                    'fail_to_rescue_rate'],
    'quantity': ['quantifiable_measurement'],
    'receiver': ['student', 'patient'],
    'reform': ['health_care_reform'],
    'registered_nurse': ['advanced_practice_registered_nurse'],
    'religious_group': ['church'],
    'room': ['emergency_room'],
    'school': ['nursing_school', 'college'],
    'shortage': ['staffing_shortage'],
    'skill': ['soft_skill'],
    'soft_skill': ['empathy', 'personal_touch'],
    'specialist': ['health_care_specialist'],
    'student': ['nursing_student'],
    'time': ['elapsed_time'],
    'training': ['clinical_training', 'certification'],
    'training_event': ['course'],
    'treatment_event': ['patient_treatment']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
