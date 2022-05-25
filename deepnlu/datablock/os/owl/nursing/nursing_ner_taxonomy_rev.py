
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

class NursingNerTaxonomyRev(object):

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
 'config': {'classname': 'NursingNerTaxonomy',
            'filename': 'nursing_ner_taxonomy',
            'queries': ['ner-taxonomy.sparql % $PREFIX=nursing $NER_1=spacyNER '
                        '$NER_2=grafflNER'],
            'reverse': True,
            'transformers': ['ner_taxonomy']},
 'source': 'nursing.owl',
 'time': '2022-05-20 17:02:25.152705'}

    __data = {
    'ACTIVITY': ['ACTIVITY'],
    'AGENT': ['PERSON', 'AGENT', 'GROUP', 'NORP', 'ASSOC'],
    'ARTIFACT': ['ARTIFACT', 'RULE', 'DIPLOMA', 'REG'],
    'BIAS': ['BIAS'],
    'CARDINAL': ['CARDINAL'],
    'COND': ['COND'],
    'DATE': ['DATE'],
    'EDU': ['EDU'],
    'EVENT': ['EVENT', 'QUALITY', 'CARE', 'EVAL'],
    'FAC': ['FAC'],
    'GEO': ['GEO'],
    'LANGUAGE': ['LANGUAGE'],
    'LOC': ['LOC'],
    'MONEY': ['MONEY'],
    'ORDINAL': ['ORDINAL'],
    'ORG': ['ORG'],
    'PERCENT': ['PERCENT'],
    'PRODUCT': ['PRODUCT'],
    'PROFESSION': ['PROFESSION'],
    'QUANTITY': ['QUANTITY', 'MEASURE'],
    'SKILL': ['SKILL'],
    'TIME': ['TIME'],
    'WORK_OF_ART': ['WORK_OF_ART']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
