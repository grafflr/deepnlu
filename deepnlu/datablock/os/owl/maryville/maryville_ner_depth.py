
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

class MaryvilleNerDepth(object):

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
 'config': {'classname': 'MaryvilleNerDepth',
            'filename': 'maryville_ner_depth',
            'firstonly': True,
            'queries': ['depth.sparql'],
            'reverse': True,
            'transformers': ['depth']},
 'source': 'maryville.owl',
 'time': '2022-05-17 11:15:53.308594'}

    __data = {
    'ACTIVITY': ['1'],
    'AGENT': ['1'],
    'ARTIFACT': ['1'],
    'ASSOC': ['3'],
    'BIAS': ['1'],
    'CARDINAL': ['1'],
    'CARE': ['2'],
    'COND': ['1'],
    'DATE': ['1'],
    'DIPLOMA': ['2'],
    'EDU': ['1'],
    'EVAL': ['2'],
    'EVENT': ['1'],
    'FAC': ['1'],
    'GEO': ['1'],
    'GROUP': ['2'],
    'LANGUAGE': ['1'],
    'LOC': ['1'],
    'MEASURE': ['2'],
    'MONEY': ['1'],
    'NER': ['0'],
    'NORP': ['7'],
    'ORDINAL': ['1'],
    'ORG': ['1'],
    'PERCENT': ['1'],
    'PERSON': ['2'],
    'PRODUCT': ['1'],
    'PROFESSION': ['1'],
    'QUALITY': ['2'],
    'QUANTITY': ['1'],
    'REG': ['2'],
    'RULE': ['2'],
    'SKILL': ['1'],
    'TIME': ['1'],
    'WORK_OF_ART': ['1']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
