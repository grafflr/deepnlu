
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

class OntologicaSynonymsRev(object):

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
 'config': {'classname': 'OntologicaSynonyms',
            'filename': 'ontologica_synonyms',
            'files': ['ontologica.txt'],
            'queries': ['synonyms.sparql'],
            'reverse': True,
            'transformers': ['lowercase', 'synonyms']},
 'source': 'ontologica.owl',
 'time': '2022-05-03 17:49:06.728446'}

    __data = {
    'all': ['all'],
    'ancestor nodes': ['ancestor_of'],
    'ancestor of': ['ancestor_of'],
    'ancestors for': ['ancestor_of'],
    'ancestors of': ['ancestor_of'],
    'appraisal ontology': ['appraisal_ontology'],
    'bucket': ['bucket'],
    'can you show me': ['list_response'],
    'cardinal': ['cardinal'],
    'categories': ['category'],
    'category': ['category'],
    'child': ['child_of'],
    'child nodes': ['child_of'],
    'child of': ['child_of'],
    'children': ['child_of'],
    'classification': ['classification'],
    'close to': ['similar'],
    'comment': ['comment'],
    'comments': ['comment'],
    'count': ['count'],
    'count elements': ['count'],
    'count nodes': ['count'],
    'count total': ['count'],
    'datasource': ['datasource'],
    'descendant': ['descendant_of'],
    'descendant nodes': ['descendant_of'],
    'descendant of': ['descendant_of'],
    'descendants': ['descendant_of'],
    'descendants of': ['descendant_of'],
    'first': ['first'],
    'how many': ['count'],
    'i want to see': ['list_response'],
    'john kao': ['john_kao'],
    'john kao model': ['john_kao_model'],
    'kind of like': ['similar'],
    'kinda like': ['similar'],
    'like this': ['similar'],
    'list': ['list_query'],
    'list all of': ['list_query'],
    'list for me': ['list_response'],
    'list query': ['list_query'],
    'list response': ['list_response'],
    'list the': ['list_query'],
    'list the items for': ['list_query'],
    'model': ['model'],
    'multi item response': ['multi_item_response'],
    'no ancestor of': ['no_ancestor_of'],
    'no descendant of': ['no_descendant_of'],
    'no descendants of': ['no_descendant_of'],
    'no parent of': ['no_parent_of'],
    'no parents of': ['no_parent_of'],
    'no quantity': ['no_quantity'],
    'not a parent of': ['no_parent_of'],
    'not an ancestor of': ['no_ancestor_of'],
    'not ancestor of': ['no_ancestor_of'],
    'not the descendants of': ['no_descendant_of'],
    'not the parents of': ['no_parent_of'],
    'nursing ontology': ['nursing_ontology'],
    'one': ['one'],
    'one item response': ['one_item_response'],
    'ontologica ontology': ['ontologica_ontology'],
    'ontology': ['ontology'],
    'ordinal': ['ordinal'],
    'parent nodes': ['parent_of'],
    'parent of': ['parent_of'],
    'parents': ['parent_of'],
    'parents for': ['parent_of'],
    'partial': ['partial'],
    'pathology': ['speech_pathology_model'],
    'people': ['people'],
    'quantity': ['quantity'],
    'query classification': ['query_classification'],
    'question': ['question'],
    'question not understood': ['question_not_understood'],
    'question understood': ['question_understood'],
    'random': ['random_query'],
    'random query': ['random_query'],
    'second': ['second'],
    'show me': ['list_query', 'list_response'],
    'show me all of the': ['list_query'],
    'show me the': ['list_query'],
    'show me the items': ['list_query'],
    'similar': ['similar'],
    'similar to': ['similar'],
    'skills ontology': ['skills_ontology'],
    'slp': ['speech_pathology_model'],
    'speech disorder': ['speech_disorder_model'],
    'speech disorder model': ['speech_disorder_model'],
    'speech pathology': ['speech_pathology_model'],
    'speech pathology model': ['speech_pathology_model'],
    'taxonomical classification': ['taxonomical_classification'],
    'text classification': ['text_classification'],
    'the ancestors of': ['ancestor_of'],
    'the parent for': ['parent_of'],
    'third': ['third'],
    'three': ['three'],
    'three item response': ['three_item_response'],
    'total number': ['count'],
    'two': ['two'],
    'two item response': ['two_item_response']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
