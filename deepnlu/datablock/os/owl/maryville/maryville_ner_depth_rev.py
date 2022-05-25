
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

class MaryvilleNerDepthRev(object):

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
 'time': '2022-05-17 11:15:53.310093'}

    __data = {
    '0': ['NER'],
    '1': [   'EVENT',
             'DATE',
             'BIAS',
             'PRODUCT',
             'TIME',
             'ORDINAL',
             'MONEY',
             'CARDINAL',
             'ACTIVITY',
             'LANGUAGE',
             'SKILL',
             'PROFESSION',
             'ARTIFACT',
             'AGENT',
             'QUANTITY',
             'PERCENT',
             'WORK_OF_ART',
             'FAC',
             'COND',
             'EDU',
             'GEO',
             'LOC',
             'ORG'],
    '2': [   'DIPLOMA',
             'QUALITY',
             'PERSON',
             'GROUP',
             'RULE',
             'REG',
             'CARE',
             'EVAL',
             'MEASURE'],
    '3': ['ASSOC'],
    '7': ['NORP']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
