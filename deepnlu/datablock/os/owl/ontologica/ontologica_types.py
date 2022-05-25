
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

class OntologicaTypes(object):

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
 'config': {'classname': 'OntologicaTypes',
            'filename': 'ontologica_types',
            'queries': ['subclass.sparql'],
            'reverse': True,
            'transformers': ['types']},
 'source': 'ontologica.owl',
 'time': '2022-05-03 17:49:06.733946'}

    __data = {
    'action_confirmation': ['action_understood'],
    'action_not_understood': ['question_not_understood'],
    'action_understood': ['question_understood'],
    'all': ['bucket'],
    'ancestor_of': ['taxonomical_classification'],
    'appraisal_ontology': ['ontology'],
    'bucket': ['quantity'],
    'cardinal': ['quantity'],
    'category': ['text_classification'],
    'child_of': ['descendant_of'],
    'comment': ['text_classification'],
    'count': ['quantity'],
    'descendant_of': ['taxonomical_classification'],
    'first': ['ordinal'],
    'john_kao': ['people'],
    'john_kao_model': ['model'],
    'list_query': ['query_classification'],
    'list_response': ['response'],
    'model': ['datasource'],
    'multi_item_response': ['list_response'],
    'no_ancestor_of': ['no_quantity'],
    'no_child_of': ['no_descendant_of'],
    'no_descendant_of': ['no_quantity'],
    'no_parent_of': ['no_ancestor_of'],
    'no_quantity': ['response'],
    'nursing_ontology': ['ontology'],
    'one': ['cardinal'],
    'one_item_response': ['list_response'],
    'ontologica_ontology': ['ontology'],
    'ontology': ['datasource'],
    'ordinal': ['quantity'],
    'parent_of': ['ancestor_of'],
    'partial': ['bucket'],
    'query_classification': ['classification'],
    'question_not_understood': ['response'],
    'question_understood': ['response'],
    'random_query': ['query_classification'],
    'second': ['ordinal'],
    'skills_ontology': ['ontology'],
    'speech_disorder_model': ['model'],
    'speech_pathology_model': ['model'],
    'taxonomical_classification': ['classification'],
    'text_classification': ['classification'],
    'third': ['ordinal'],
    'three': ['cardinal'],
    'three_item_response': ['list_response'],
    'two': ['cardinal'],
    'two_item_response': ['list_response']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
