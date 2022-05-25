
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

class OntologicaTypesRev(object):

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
 'time': '2022-05-03 17:49:06.734947'}

    __data = {
    'action_understood': ['action_confirmation'],
    'ancestor_of': ['parent_of'],
    'bucket': ['all', 'partial'],
    'cardinal': ['one', 'three', 'two'],
    'classification': [   'query_classification',
                          'text_classification',
                          'taxonomical_classification'],
    'datasource': ['ontology', 'model'],
    'descendant_of': ['child_of'],
    'list_response': [   'three_item_response',
                         'one_item_response',
                         'multi_item_response',
                         'two_item_response'],
    'model': [   'speech_disorder_model',
                 'speech_pathology_model',
                 'john_kao_model'],
    'no_ancestor_of': ['no_parent_of'],
    'no_descendant_of': ['no_child_of'],
    'no_quantity': ['no_descendant_of', 'no_ancestor_of'],
    'ontology': [   'ontologica_ontology',
                    'appraisal_ontology',
                    'skills_ontology',
                    'nursing_ontology'],
    'ordinal': ['second', 'third', 'first'],
    'people': ['john_kao'],
    'quantity': ['ordinal', 'count', 'bucket', 'cardinal'],
    'query_classification': ['list_query', 'random_query'],
    'question_not_understood': ['action_not_understood'],
    'question_understood': ['action_understood'],
    'response': [   'list_response',
                    'question_understood',
                    'question_not_understood',
                    'no_quantity'],
    'taxonomical_classification': ['ancestor_of', 'descendant_of'],
    'text_classification': ['comment', 'category']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
