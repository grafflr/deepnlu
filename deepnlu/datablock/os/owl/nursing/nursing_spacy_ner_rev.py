
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

class NursingSpacyNERRev(object):

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
 'config': {'classname': 'NursingSpacyNER',
            'filename': 'nursing_spacy_ner',
            'firstonly': True,
            'queries': ['ner.sparql % $PREFIX=nursing $NER=spacyNER'],
            'reverse': True,
            'transformers': ['ner']},
 'source': 'nursing.owl',
 'time': '2022-05-20 17:02:25.532705'}

    __data = {
    'CARDINAL': ['cardinal'],
    'DATE': ['date'],
    'EVENT': [   'admission',
                 'strike',
                 'staffing',
                 'pay',
                 'shortage',
                 'closure',
                 'course',
                 'readmission',
                 'competency',
                 'history',
                 'outcome',
                 'event',
                 'quality',
                 'century',
                 'evaluation',
                 'reform',
                 'acute care',
                 'periodic peer review',
                 'medical facility closure',
                 'health care quality',
                 'long-term health care',
                 'clinical outcome evaluation',
                 'training event',
                 'patient care',
                 'fair pay',
                 'reformation',
                 'care event',
                 'treatment event',
                 'health care',
                 'clinical outcome',
                 'patient treatment',
                 'patient care coordination',
                 'set to close',
                 'long term health care',
                 'health care reform',
                 'salary',
                 'facility closure',
                 'clinical competency',
                 'labor event',
                 'primary care',
                 'peer review',
                 'staffing shortage',
                 'outcome evaluation',
                 'clinical evaluation'],
    'FAC': [   'building',
               'home',
               'department',
               'pharmacy',
               'hospital',
               'surgery',
               'site',
               'college',
               'airport',
               'room',
               'clinic',
               'school',
               'urgent care',
               'urgent care site',
               'medical building',
               'health department',
               'urgent care clinic',
               'edifice',
               'public health department',
               'spanish hospital',
               'nursing home',
               'er',
               'nursing school',
               'emergency room'],
    'GEO': ['city', 'country', 'spain', 'geopolitical entity'],
    'LANGUAGE': ['language'],
    'LOC': ['europe', 'continent', 'location'],
    'MONEY': ['money'],
    'NORP': [   'nationality',
                'church',
                'american',
                'spanish',
                'political group',
                'religious group',
                'catholic church',
                'protestant church'],
    'ORDINAL': ['ordinal'],
    'ORG': [   'organization',
               'company',
               'johnson and johnson',
               'j&j',
               'johnson & johnson'],
    'PERCENT': ['percent'],
    'PERSON': ['person', 'florence nightingale'],
    'PRODUCT': ['product'],
    'QUANTITY': [   'quantity',
                    'mortality rate',
                    'staffing level',
                    'failure-to-rescue rates',
                    'quantifiable measurement',
                    'readmission rate',
                    'fail to rescue rate'],
    'TIME': [   'time',
                'temporary',
                'permanent',
                'duration',
                'elapsed time',
                'temporarily'],
    'WORK_OF_ART': ['work of art']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
