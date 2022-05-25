
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

class OntologicaInferByRequires(object):

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
 'config': {'classname': 'OntologicaInferByRequires',
            'filename': 'ontologica_infer_by_requires',
            'queries': ['infer_by_requires.sparql % $PREFIX=ontologica'],
            'transformers': ['infer_by_requires']},
 'source': 'ontologica.owl',
 'time': '2022-05-03 17:49:06.596446'}

    __data = {
    'ancestor_of': [   {   'context': ['no_quantity'],
                           'id': '005d08a5-cb44-11ec-86cb-4c1d96716627',
                           'replace': 'no_quantity',
                           'with': 'no_ancestor_of'}],
    'child_of': [   {   'context': ['no_descendant_of'],
                        'id': '005d08a4-cb44-11ec-a02a-4c1d96716627',
                        'replace': 'no_descendant_of',
                        'with': 'no_child_of'}],
    'descendant_of': [   {   'context': ['no_quantity'],
                             'id': '005d08a3-cb44-11ec-bdd8-4c1d96716627',
                             'replace': 'no_quantity',
                             'with': 'no_descendant_of'}],
    'no_ancestor_of': [   {   'context': ['parent_of'],
                              'id': '005d08a2-cb44-11ec-8524-4c1d96716627',
                              'replace': 'no_ancestor_of',
                              'with': 'no_parent_of'}],
    'no_descendant_of': [   {   'context': ['child_of'],
                                'id': '005d08a4-cb44-11ec-a02a-4c1d96716627',
                                'replace': 'no_descendant_of',
                                'with': 'no_child_of'}],
    'no_quantity': [   {   'context': ['descendant_of'],
                           'id': '005d08a3-cb44-11ec-bdd8-4c1d96716627',
                           'replace': 'no_quantity',
                           'with': 'no_descendant_of'},
                       {   'context': ['ancestor_of'],
                           'id': '005d08a5-cb44-11ec-86cb-4c1d96716627',
                           'replace': 'no_quantity',
                           'with': 'no_ancestor_of'}],
    'parent_of': [   {   'context': ['no_ancestor_of'],
                         'id': '005d08a2-cb44-11ec-8524-4c1d96716627',
                         'replace': 'no_ancestor_of',
                         'with': 'no_parent_of'}]}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
