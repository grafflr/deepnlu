
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

class MaryvilleNerTaxonomy(object):

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
 'config': {'classname': 'MaryvilleNerTaxonomy',
            'filename': 'maryville_ner_taxonomy',
            'queries': ['ner-taxonomy.sparql % $PREFIX=maryville '
                        '$NER_1=spacyNER $NER_2=grafflNER'],
            'reverse': True,
            'transformers': ['ner_taxonomy']},
 'source': 'maryville.owl',
 'time': '2022-05-17 11:15:53.380093'}

    __data = {
    'ACTIVITY': ['ACTIVITY'],
    'AGENT': ['AGENT'],
    'ARTIFACT': ['ARTIFACT'],
    'ASSOC': ['AGENT'],
    'BIAS': ['BIAS'],
    'CARDINAL': ['CARDINAL'],
    'CARE': ['EVENT'],
    'COND': ['COND'],
    'DATE': ['DATE'],
    'DIPLOMA': ['ARTIFACT'],
    'EDU': ['EDU'],
    'EVAL': ['EVENT'],
    'EVENT': ['EVENT'],
    'FAC': ['FAC'],
    'GEO': ['GEO'],
    'GROUP': ['AGENT'],
    'LANGUAGE': ['LANGUAGE'],
    'LOC': ['LOC'],
    'MEASURE': ['QUANTITY'],
    'MONEY': ['MONEY'],
    'NORP': ['AGENT'],
    'ORDINAL': ['ORDINAL'],
    'ORG': ['ORG'],
    'PERCENT': ['PERCENT'],
    'PERSON': ['AGENT'],
    'PRODUCT': ['PRODUCT'],
    'PROFESSION': ['PROFESSION'],
    'QUALITY': ['EVENT'],
    'QUANTITY': ['QUANTITY'],
    'REG': ['ARTIFACT'],
    'RULE': ['ARTIFACT'],
    'SKILL': ['SKILL'],
    'TIME': ['TIME'],
    'WORK_OF_ART': ['WORK_OF_ART']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]