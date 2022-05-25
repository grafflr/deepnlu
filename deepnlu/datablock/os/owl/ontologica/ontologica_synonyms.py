
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

class OntologicaSynonyms(object):

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
 'time': '2022-05-03 17:49:06.726446'}

    __data = {
    'all': ['all'],
    'ancestor_of': [   'the ancestors of',
                       'ancestor nodes',
                       'ancestors for',
                       'ancestors of',
                       'ancestor of'],
    'appraisal_ontology': ['appraisal ontology'],
    'bucket': ['bucket'],
    'cardinal': ['cardinal'],
    'category': ['categories', 'category'],
    'child_of': ['child nodes', 'child of', 'children', 'child'],
    'classification': ['classification'],
    'comment': ['comments', 'comment'],
    'count': [   'count elements',
                 'total number',
                 'count nodes',
                 'count total',
                 'how many',
                 'count'],
    'datasource': ['datasource'],
    'descendant_of': [   'descendant nodes',
                         'descendants of',
                         'descendant of',
                         'descendants',
                         'descendant'],
    'first': ['first'],
    'john_kao': ['john kao'],
    'john_kao_model': ['john kao model'],
    'list_query': [   'show me all of the',
                      'list the items for',
                      'show me the items',
                      'show me the',
                      'list all of',
                      'list query',
                      'list the',
                      'show me',
                      'list'],
    'list_response': [   'can you show me',
                         'list response',
                         'i want to see',
                         'list for me',
                         'show me'],
    'model': ['model'],
    'multi_item_response': ['multi item response'],
    'no_ancestor_of': [   'not an ancestor of',
                          'not ancestor of',
                          'no ancestor of'],
    'no_descendant_of': [   'not the descendants of',
                            'no descendants of',
                            'no descendant of'],
    'no_parent_of': [   'not the parents of',
                        'not a parent of',
                        'no parents of',
                        'no parent of'],
    'no_quantity': ['no quantity'],
    'nursing_ontology': ['nursing ontology'],
    'one': ['one'],
    'one_item_response': ['one item response'],
    'ontologica_ontology': ['ontologica ontology'],
    'ontology': ['ontology'],
    'ordinal': ['ordinal'],
    'parent_of': [   'the parent for',
                     'parent nodes',
                     'parents for',
                     'parent of',
                     'parents'],
    'partial': ['partial'],
    'people': ['people'],
    'quantity': ['quantity'],
    'query_classification': ['query classification'],
    'question': ['question'],
    'question_not_understood': ['question not understood'],
    'question_understood': ['question understood'],
    'random_query': ['random query', 'random'],
    'second': ['second'],
    'similar': [   'kind of like',
                   'similar to',
                   'kinda like',
                   'like this',
                   'close to',
                   'similar'],
    'skills_ontology': ['skills ontology'],
    'speech_disorder_model': ['speech disorder model', 'speech disorder'],
    'speech_pathology_model': [   'speech pathology model',
                                  'speech pathology',
                                  'pathology',
                                  'slp'],
    'taxonomical_classification': ['taxonomical classification'],
    'text_classification': ['text classification'],
    'third': ['third'],
    'three': ['three'],
    'three_item_response': ['three item response'],
    'two': ['two'],
    'two_item_response': ['two item response']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
