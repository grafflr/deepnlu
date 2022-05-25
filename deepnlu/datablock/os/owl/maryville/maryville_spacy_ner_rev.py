
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

class MaryvilleSpacyNERRev(object):

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
 'config': {'classname': 'MaryvilleSpacyNER',
            'filename': 'maryville_spacy_ner',
            'firstonly': True,
            'queries': ['ner.sparql % $PREFIX=maryville $NER=spacyNER'],
            'reverse': True,
            'transformers': ['ner']},
 'source': 'maryville.owl',
 'time': '2022-05-17 11:15:54.689593'}

    __data = {
    'CARDINAL': ['cardinal'],
    'DATE': ['date'],
    'EVENT': [   'evaluation',
                 'history',
                 'pay',
                 'event',
                 'readmission',
                 'century',
                 'closure',
                 'quality',
                 'outcome',
                 'strike',
                 'competency',
                 'course',
                 'admission',
                 'shortage',
                 'staffing',
                 'reform',
                 'health care reform',
                 'reformation',
                 'clinical competency',
                 'patient care coordination',
                 'salary',
                 'long-term health care',
                 'medical facility closure',
                 'set to close',
                 'patient care',
                 'clinical outcome',
                 'outcome evaluation',
                 'clinical evaluation',
                 'primary care',
                 'fair pay',
                 'treatment event',
                 'acute care',
                 'facility closure',
                 'care event',
                 'training event',
                 'patient treatment',
                 'clinical outcome evaluation',
                 'long term health care',
                 'health care',
                 'staffing shortage',
                 'peer review',
                 'health care quality',
                 'periodic peer review',
                 'labor event'],
    'FAC': [   'home',
               'airport',
               'hospital',
               'room',
               'pharmacy',
               'college',
               'building',
               'department',
               'site',
               'clinic',
               'school',
               'surgery',
               'medical building',
               'urgent care',
               'urgent care clinic',
               'spanish hospital',
               'er',
               'public health department',
               'urgent care site',
               'emergency room',
               'edifice',
               'nursing school',
               'nursing home',
               'health department'],
    'GEO': ['spain', 'city', 'country', 'geopolitical entity'],
    'LANGUAGE': ['language'],
    'LOC': ['location', 'europe', 'continent'],
    'MONEY': ['money'],
    'NORP': [   'nationality',
                'american',
                'spanish',
                'church',
                'political group',
                'protestant church',
                'religious group',
                'catholic church'],
    'ORDINAL': ['ordinal'],
    'ORG': [   'company',
               'organization',
               'j&j',
               'johnson and johnson',
               'johnson & johnson'],
    'PERCENT': ['percent'],
    'PERSON': ['person', 'florence nightingale'],
    'PRODUCT': ['product'],
    'QUANTITY': [   'quantity',
                    'fail to rescue rate',
                    'mortality rate',
                    'failure-to-rescue rates',
                    'staffing level',
                    'readmission rate',
                    'quantifiable measurement'],
    'TIME': [   'temporary',
                'time',
                'permanent',
                'temporarily',
                'duration',
                'elapsed time'],
    'WORK_OF_ART': ['work of art']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
