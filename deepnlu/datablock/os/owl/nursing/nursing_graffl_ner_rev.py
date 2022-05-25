
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

class NursingGrafflNERRev(object):

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
 'config': {'classname': 'NursingGrafflNER',
            'filename': 'nursing_graffl_ner',
            'firstonly': False,
            'queries': ['ner.sparql % $PREFIX=nursing $NER=grafflNER'],
            'reverse': True,
            'transformers': ['ner']},
 'source': 'nursing.owl',
 'time': '2022-05-20 17:02:25.304704'}

    __data = {
    'ACTIVITY': [   'activity',
                    'practice',
                    'code for ethical practice',
                    'ethical practice',
                    'action',
                    'political activity'],
    'AGENT': [   'association',
                 'nurse',
                 'pharmacist',
                 'provider',
                 'student',
                 'surgeon',
                 'person',
                 'agent',
                 'apothecary',
                 'receiver',
                 'group',
                 'church',
                 'physician',
                 'specialist',
                 'staff',
                 'patient',
                 'educator',
                 'chemist',
                 'registered nurse',
                 'catholic church',
                 'psychiatric mental health nurse practitioner',
                 'advanced practice registered nurse',
                 'florence nightingale',
                 'aacn',
                 'health care specialist',
                 'religious group',
                 'aprn',
                 'female patient',
                 'np',
                 'nurse practitioner',
                 'political group',
                 'nursing student',
                 'health care provider',
                 'family nurse practitioner',
                 'nurse educator',
                 'american association of colleges of nursing',
                 'ana',
                 'protestant church',
                 'elderly patient',
                 'male patient',
                 'rn',
                 'american nurses association',
                 'nps',
                 'pediactric patient',
                 'rns',
                 'american nursing association',
                 'pmhnp',
                 'fnp'],
    'ARTIFACT': [   'artifact',
                    'plan',
                    'rule',
                    'diploma',
                    'regulation',
                    'artefact',
                    "bachelor's degree",
                    'bachelor degree',
                    'master of arts',
                    'doctoral degree',
                    'patient treatment plan',
                    'phd',
                    "associate's degree",
                    'bachelor of science in nursing',
                    "master's",
                    'aa degree',
                    'bsn',
                    "master's degree",
                    'nursing diploma',
                    'baccalaureate level',
                    'bachelor of arts',
                    'bachelor of science',
                    'master degree',
                    'msn',
                    'doctoral degree program',
                    'doctoral',
                    'msc',
                    'master of science',
                    'master of science in nursing',
                    'associate degree'],
    'ASSOC': [   'association',
                 'aacn',
                 'american association of colleges of nursing',
                 'ana',
                 'american nurses association',
                 'american nursing association'],
    'BIAS': ['bias', 'race bias', 'racial bias', 'gender bias'],
    'CARE': [   'patient care coordination',
                'health care',
                'care event',
                'patient care',
                'acute care',
                'long-term health care',
                'primary care',
                'long term health care'],
    'COND': ['condition', 'health', 'mental health'],
    'DIPLOMA': [   'diploma',
                   "bachelor's degree",
                   'bachelor degree',
                   'master of arts',
                   'doctoral degree',
                   'phd',
                   "associate's degree",
                   'bachelor of science in nursing',
                   "master's",
                   'aa degree',
                   'bsn',
                   "master's degree",
                   'nursing diploma',
                   'baccalaureate level',
                   'bachelor of arts',
                   'bachelor of science',
                   'master degree',
                   'msn',
                   'doctoral degree program',
                   'doctoral',
                   'msc',
                   'master of science',
                   'master of science in nursing',
                   'associate degree'],
    'EDU': [   'training',
               'learning',
               'certification',
               'education',
               'development',
               'health care education',
               'clinical training',
               'continuous learning',
               'national certification',
               'clinical course',
               'continued learning',
               'professional development',
               'nursing education',
               'advanced clinical training'],
    'EVAL': [   'evaluation',
                'periodic peer review',
                'clinical outcome evaluation',
                'peer review',
                'clinical evaluation',
                'outcome evaluation'],
    'GROUP': [   'association',
                 'group',
                 'church',
                 'catholic church',
                 'aacn',
                 'religious group',
                 'political group',
                 'american association of colleges of nursing',
                 'ana',
                 'protestant church',
                 'american nurses association',
                 'american nursing association'],
    'MEASURE': [   'failure-to-rescue rates',
                   'quantifiable measurement',
                   'readmission rate',
                   'fail to rescue rate',
                   'staffing level',
                   'mortality rate'],
    'PROFESSION': [   'nursing',
                      'profession',
                      'modern nursing',
                      'historical nursing'],
    'QUALITY': [   'competency',
                   'quality',
                   'clinical competency',
                   'health care quality'],
    'REG': ['regulation'],
    'RULE': ['rule'],
    'SKILL': ['skill', 'empathy', 'soft skill', 'personal touch']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]