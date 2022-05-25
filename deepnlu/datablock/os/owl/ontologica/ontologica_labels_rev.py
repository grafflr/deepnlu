
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

class OntologicaLabelsRev(object):

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
 'time': '2022-05-03 17:49:06.747446'}

    __data = {
    'All': ['all'],
    'Ancestor of': ['ancestor_of'],
    'Appraisal Ontology': ['appraisal_ontology'],
    'Bucket': ['bucket'],
    'Cardinal': ['cardinal'],
    'Category': ['category'],
    'Child of': ['child_of'],
    'Classification': ['classification'],
    'Comment': ['comment'],
    'Count': ['count'],
    'Datasource': ['datasource'],
    'Descendant of': ['descendant_of'],
    'First': ['first'],
    'John Kao': ['john_kao'],
    'John Kao Model': ['john_kao_model'],
    'List Query': ['list_query'],
    'List Response': ['list_response'],
    'Model': ['model'],
    'Multi Item Response': ['multi_item_response'],
    'No Ancestor of': ['no_ancestor_of'],
    'No Descendant of': ['no_descendant_of'],
    'No Parent of': ['no_parent_of'],
    'No Quantity': ['no_quantity'],
    'Nursing Ontology': ['nursing_ontology'],
    'One': ['one'],
    'One Item Response': ['one_item_response'],
    'Ontologica Ontology': ['ontologica_ontology'],
    'Ontology': ['ontology'],
    'Ordinal': ['ordinal'],
    'Parent of': ['parent_of'],
    'Partial': ['partial'],
    'People': ['people'],
    'Quantity': ['quantity'],
    'Query Classification': ['query_classification'],
    'Question': ['question'],
    'Question Not Understood': ['question_not_understood'],
    'Question Understood': ['question_understood'],
    'Random Query': ['random_query'],
    'Second': ['second'],
    'Similar': ['similar'],
    'Skills Ontology': ['skills_ontology'],
    'Speech Disorder Model': ['speech_disorder_model'],
    'Speech Pathology Model': ['speech_pathology_model'],
    'Taxonomical Classification': ['taxonomical_classification'],
    'Text Classification': ['text_classification'],
    'Third': ['third'],
    'Three': ['three'],
    'Three Item Response': ['three_item_response'],
    'Two': ['two'],
    'Two Item Response': ['two_item_response']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
