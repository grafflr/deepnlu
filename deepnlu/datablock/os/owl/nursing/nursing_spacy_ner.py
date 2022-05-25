
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

class NursingSpacyNER(object):

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
 'time': '2022-05-20 17:02:25.531204'}

    __data = {
    'acute care': ['EVENT'],
    'admission': ['EVENT'],
    'airport': ['FAC'],
    'american': ['NORP'],
    'building': ['FAC'],
    'cardinal': ['CARDINAL'],
    'care event': ['EVENT'],
    'catholic church': ['NORP'],
    'century': ['EVENT'],
    'church': ['NORP'],
    'city': ['GEO'],
    'clinic': ['FAC'],
    'clinical competency': ['EVENT'],
    'clinical evaluation': ['EVENT'],
    'clinical outcome': ['EVENT'],
    'clinical outcome evaluation': ['EVENT'],
    'closure': ['EVENT'],
    'college': ['FAC'],
    'company': ['ORG'],
    'competency': ['EVENT'],
    'continent': ['LOC'],
    'country': ['GEO'],
    'course': ['EVENT'],
    'date': ['DATE'],
    'department': ['FAC'],
    'duration': ['TIME'],
    'edifice': ['FAC'],
    'elapsed time': ['TIME'],
    'emergency room': ['FAC'],
    'er': ['FAC'],
    'europe': ['LOC'],
    'evaluation': ['EVENT'],
    'event': ['EVENT'],
    'facility closure': ['EVENT'],
    'fail to rescue rate': ['QUANTITY'],
    'failure-to-rescue rates': ['QUANTITY'],
    'fair pay': ['EVENT'],
    'florence nightingale': ['PERSON'],
    'geopolitical entity': ['GEO'],
    'health care': ['EVENT'],
    'health care quality': ['EVENT'],
    'health care reform': ['EVENT'],
    'health department': ['FAC'],
    'history': ['EVENT'],
    'home': ['FAC'],
    'hospital': ['FAC'],
    'j&j': ['ORG'],
    'johnson & johnson': ['ORG'],
    'johnson and johnson': ['ORG'],
    'labor event': ['EVENT'],
    'language': ['LANGUAGE'],
    'location': ['LOC'],
    'long term health care': ['EVENT'],
    'long-term health care': ['EVENT'],
    'medical building': ['FAC'],
    'medical facility closure': ['EVENT'],
    'money': ['MONEY'],
    'mortality rate': ['QUANTITY'],
    'nationality': ['NORP'],
    'nursing home': ['FAC'],
    'nursing school': ['FAC'],
    'ordinal': ['ORDINAL'],
    'organization': ['ORG'],
    'outcome': ['EVENT'],
    'outcome evaluation': ['EVENT'],
    'patient care': ['EVENT'],
    'patient care coordination': ['EVENT'],
    'patient treatment': ['EVENT'],
    'pay': ['EVENT'],
    'peer review': ['EVENT'],
    'percent': ['PERCENT'],
    'periodic peer review': ['EVENT'],
    'permanent': ['TIME'],
    'person': ['PERSON'],
    'pharmacy': ['FAC'],
    'political group': ['NORP'],
    'primary care': ['EVENT'],
    'product': ['PRODUCT'],
    'protestant church': ['NORP'],
    'public health department': ['FAC'],
    'quality': ['EVENT'],
    'quantifiable measurement': ['QUANTITY'],
    'quantity': ['QUANTITY'],
    'readmission': ['EVENT'],
    'readmission rate': ['QUANTITY'],
    'reform': ['EVENT'],
    'reformation': ['EVENT'],
    'religious group': ['NORP'],
    'room': ['FAC'],
    'salary': ['EVENT'],
    'school': ['FAC'],
    'set to close': ['EVENT'],
    'shortage': ['EVENT'],
    'site': ['FAC'],
    'spain': ['GEO'],
    'spanish': ['NORP'],
    'spanish hospital': ['FAC'],
    'staffing': ['EVENT'],
    'staffing level': ['QUANTITY'],
    'staffing shortage': ['EVENT'],
    'strike': ['EVENT'],
    'surgery': ['FAC'],
    'temporarily': ['TIME'],
    'temporary': ['TIME'],
    'time': ['TIME'],
    'training event': ['EVENT'],
    'treatment event': ['EVENT'],
    'urgent care': ['FAC'],
    'urgent care clinic': ['FAC'],
    'urgent care site': ['FAC'],
    'work of art': ['WORK_OF_ART']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
