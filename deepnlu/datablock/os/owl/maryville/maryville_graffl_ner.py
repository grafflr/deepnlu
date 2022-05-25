
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

class MaryvilleGrafflNER(object):

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
 'config': {'classname': 'MaryvilleGrafflNER',
            'filename': 'maryville_graffl_ner',
            'firstonly': False,
            'queries': ['ner.sparql % $PREFIX=maryville $NER=grafflNER'],
            'reverse': True,
            'transformers': ['ner']},
 'source': 'maryville.owl',
 'time': '2022-05-17 11:15:53.850093'}

    __data = {
    'aa degree': ['ARTIFACT', 'DIPLOMA'],
    'aacn': ['AGENT', 'ASSOC', 'GROUP'],
    'action': ['ACTIVITY'],
    'activity': ['ACTIVITY'],
    'acute care': ['CARE'],
    'advanced clinical training': ['EDU'],
    'advanced practice registered nurse': ['AGENT'],
    'agent': ['AGENT'],
    'american association of colleges of nursing': ['AGENT', 'ASSOC', 'GROUP'],
    'american nurses association': ['AGENT', 'ASSOC', 'GROUP'],
    'american nursing association': ['AGENT', 'ASSOC', 'GROUP'],
    'ana': ['AGENT', 'ASSOC', 'GROUP'],
    'apothecary': ['AGENT'],
    'aprn': ['AGENT'],
    'artefact': ['ARTIFACT'],
    'artifact': ['ARTIFACT'],
    'associate degree': ['ARTIFACT', 'DIPLOMA'],
    "associate's degree": ['ARTIFACT', 'DIPLOMA'],
    'association': ['AGENT', 'ASSOC', 'GROUP'],
    'baccalaureate level': ['ARTIFACT', 'DIPLOMA'],
    'bachelor degree': ['ARTIFACT', 'DIPLOMA'],
    'bachelor of arts': ['ARTIFACT', 'DIPLOMA'],
    'bachelor of science': ['ARTIFACT', 'DIPLOMA'],
    'bachelor of science in nursing': ['ARTIFACT', 'DIPLOMA'],
    "bachelor's degree": ['ARTIFACT', 'DIPLOMA'],
    'bias': ['BIAS'],
    'bsn': ['ARTIFACT', 'DIPLOMA'],
    'care event': ['CARE'],
    'catholic church': ['AGENT', 'GROUP'],
    'certification': ['EDU'],
    'chemist': ['AGENT'],
    'church': ['AGENT', 'GROUP'],
    'clinical competency': ['QUALITY'],
    'clinical course': ['EDU'],
    'clinical evaluation': ['EVAL'],
    'clinical outcome evaluation': ['EVAL'],
    'clinical training': ['EDU'],
    'code for ethical practice': ['ACTIVITY'],
    'competency': ['QUALITY'],
    'condition': ['COND'],
    'continued learning': ['EDU'],
    'continuous learning': ['EDU'],
    'development': ['EDU'],
    'diploma': ['ARTIFACT', 'DIPLOMA'],
    'doctoral': ['ARTIFACT', 'DIPLOMA'],
    'doctoral degree': ['ARTIFACT', 'DIPLOMA'],
    'doctoral degree program': ['ARTIFACT', 'DIPLOMA'],
    'education': ['EDU'],
    'educator': ['AGENT'],
    'elderly patient': ['AGENT'],
    'empathy': ['SKILL'],
    'ethical practice': ['ACTIVITY'],
    'evaluation': ['EVAL'],
    'fail to rescue rate': ['MEASURE'],
    'failure-to-rescue rates': ['MEASURE'],
    'family nurse practitioner': ['AGENT'],
    'female patient': ['AGENT'],
    'florence nightingale': ['AGENT'],
    'fnp': ['AGENT'],
    'gender bias': ['BIAS'],
    'group': ['AGENT', 'GROUP'],
    'health': ['COND'],
    'health care': ['CARE'],
    'health care education': ['EDU'],
    'health care provider': ['AGENT'],
    'health care quality': ['QUALITY'],
    'health care specialist': ['AGENT'],
    'historical nursing': ['PROFESSION'],
    'learning': ['EDU'],
    'long term health care': ['CARE'],
    'long-term health care': ['CARE'],
    'male patient': ['AGENT'],
    'master degree': ['ARTIFACT', 'DIPLOMA'],
    'master of arts': ['ARTIFACT', 'DIPLOMA'],
    'master of science': ['ARTIFACT', 'DIPLOMA'],
    'master of science in nursing': ['ARTIFACT', 'DIPLOMA'],
    "master's": ['ARTIFACT', 'DIPLOMA'],
    "master's degree": ['ARTIFACT', 'DIPLOMA'],
    'mental health': ['COND'],
    'modern nursing': ['PROFESSION'],
    'mortality rate': ['MEASURE'],
    'msc': ['ARTIFACT', 'DIPLOMA'],
    'msn': ['ARTIFACT', 'DIPLOMA'],
    'national certification': ['EDU'],
    'np': ['AGENT'],
    'nps': ['AGENT'],
    'nurse': ['AGENT'],
    'nurse educator': ['AGENT'],
    'nurse practitioner': ['AGENT'],
    'nursing': ['PROFESSION'],
    'nursing diploma': ['ARTIFACT', 'DIPLOMA'],
    'nursing education': ['EDU'],
    'nursing student': ['AGENT'],
    'outcome evaluation': ['EVAL'],
    'patient': ['AGENT'],
    'patient care': ['CARE'],
    'patient care coordination': ['CARE'],
    'patient treatment plan': ['ARTIFACT'],
    'pediactric patient': ['AGENT'],
    'peer review': ['EVAL'],
    'periodic peer review': ['EVAL'],
    'person': ['AGENT'],
    'personal touch': ['SKILL'],
    'pharmacist': ['AGENT'],
    'phd': ['ARTIFACT', 'DIPLOMA'],
    'physician': ['AGENT'],
    'plan': ['ARTIFACT'],
    'pmhnp': ['AGENT'],
    'political activity': ['ACTIVITY'],
    'political group': ['AGENT', 'GROUP'],
    'practice': ['ACTIVITY'],
    'primary care': ['CARE'],
    'profession': ['PROFESSION'],
    'professional development': ['EDU'],
    'protestant church': ['AGENT', 'GROUP'],
    'provider': ['AGENT'],
    'psychiatric mental health nurse practitioner': ['AGENT'],
    'quality': ['QUALITY'],
    'quantifiable measurement': ['MEASURE'],
    'race bias': ['BIAS'],
    'racial bias': ['BIAS'],
    'readmission rate': ['MEASURE'],
    'receiver': ['AGENT'],
    'registered nurse': ['AGENT'],
    'regulation': ['ARTIFACT', 'REG'],
    'religious group': ['AGENT', 'GROUP'],
    'rn': ['AGENT'],
    'rns': ['AGENT'],
    'rule': ['ARTIFACT', 'RULE'],
    'skill': ['SKILL'],
    'soft skill': ['SKILL'],
    'specialist': ['AGENT'],
    'staff': ['AGENT'],
    'staffing level': ['MEASURE'],
    'student': ['AGENT'],
    'surgeon': ['AGENT'],
    'training': ['EDU']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
