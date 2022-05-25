
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

class OntologicaLabels(object):

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
 'config': {'classname': 'OntologicaLabels',
            'filename': 'ontologica_labels',
            'queries': ['labels.sparql'],
            'reverse': True,
            'transformers': ['labels']},
 'source': 'ontologica.owl',
 'time': '2022-05-03 17:49:06.745947'}

    __data = {
    'all': ['All'],
    'ancestor_of': ['Ancestor of'],
    'appraisal_ontology': ['Appraisal Ontology'],
    'bucket': ['Bucket'],
    'cardinal': ['Cardinal'],
    'category': ['Category'],
    'child_of': ['Child of'],
    'classification': ['Classification'],
    'comment': ['Comment'],
    'count': ['Count'],
    'datasource': ['Datasource'],
    'descendant_of': ['Descendant of'],
    'first': ['First'],
    'john_kao': ['John Kao'],
    'john_kao_model': ['John Kao Model'],
    'list_query': ['List Query'],
    'list_response': ['List Response'],
    'model': ['Model'],
    'multi_item_response': ['Multi Item Response'],
    'no_ancestor_of': ['No Ancestor of'],
    'no_descendant_of': ['No Descendant of'],
    'no_parent_of': ['No Parent of'],
    'no_quantity': ['No Quantity'],
    'nursing_ontology': ['Nursing Ontology'],
    'one': ['One'],
    'one_item_response': ['One Item Response'],
    'ontologica_ontology': ['Ontologica Ontology'],
    'ontology': ['Ontology'],
    'ordinal': ['Ordinal'],
    'parent_of': ['Parent of'],
    'partial': ['Partial'],
    'people': ['People'],
    'quantity': ['Quantity'],
    'query_classification': ['Query Classification'],
    'question': ['Question'],
    'question_not_understood': ['Question Not Understood'],
    'question_understood': ['Question Understood'],
    'random_query': ['Random Query'],
    'second': ['Second'],
    'similar': ['Similar'],
    'skills_ontology': ['Skills Ontology'],
    'speech_disorder_model': ['Speech Disorder Model'],
    'speech_pathology_model': ['Speech Pathology Model'],
    'taxonomical_classification': ['Taxonomical Classification'],
    'text_classification': ['Text Classification'],
    'third': ['Third'],
    'three': ['Three'],
    'three_item_response': ['Three Item Response'],
    'two': ['Two'],
    'two_item_response': ['Two Item Response']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
