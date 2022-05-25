
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

class OntologicaTrie(object):

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
 'config': {'classname': 'OntologicaTrie',
            'filename': 'ontologica_trie',
            'queries': ['trie.sparql'],
            'transformers': ['lowercase', 'trie']},
 'source': 'ontologica.owl',
 'time': '2022-05-03 17:49:06.740947'}

    __data = {
    1: [   'cardinal',
           'category',
           'ontology',
           'partial',
           'ordinal',
           'comment',
           'second',
           'bucket',
           'model',
           'three',
           'third',
           'first',
           'count',
           'two',
           'one',
           'all'],
    2: [   'taxonomical',
           'ontologica',
           'descendant',
           'appraisal',
           'ancestor',
           'question',
           'nursing',
           'parent',
           'skills',
           'action',
           'random',
           'query',
           'child',
           'john',
           'text',
           'list',
           'no'],
    3: [   'question',
           'action',
           'speech',
           'multi',
           'three',
           'john',
           'two',
           'one',
           'no'],
    4: [],
    5: [],
    6: []}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
