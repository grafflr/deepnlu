
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

class NursingNerDepthRev(object):

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
 'config': {'classname': 'NursingNerDepth',
            'filename': 'nursing_ner_depth',
            'firstonly': True,
            'queries': ['depth.sparql'],
            'reverse': True,
            'transformers': ['depth']},
 'source': 'nursing.owl',
 'time': '2022-05-20 17:02:25.129203'}

    __data = {
    '0': ['NER'],
    '1': [   'ARTIFACT',
             'PRODUCT',
             'MONEY',
             'PROFESSION',
             'ACTIVITY',
             'SKILL',
             'TIME',
             'CARDINAL',
             'AGENT',
             'WORK_OF_ART',
             'LANGUAGE',
             'EVENT',
             'ORDINAL',
             'PERCENT',
             'DATE',
             'BIAS',
             'QUANTITY',
             'FAC',
             'COND',
             'EDU',
             'GEO',
             'LOC',
             'ORG'],
    '2': [   'RULE',
             'DIPLOMA',
             'PERSON',
             'GROUP',
             'QUALITY',
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
