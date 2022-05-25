
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

class OntologicaRequiresRev(object):

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
 'config': {'classname': 'OntologicaRequires',
            'filename': 'ontologica_requires',
            'queries': ['requires.sparql % $PREFIX=ontologica'],
            'reverse': True,
            'transformers': ['effects']},
 'source': 'ontologica.owl',
 'time': '2022-05-03 17:49:06.583446'}

    __data = {
    'ancestor_of': ['no_ancestor_of'],
    'child_of': ['no_child_of'],
    'descendant_of': ['no_descendant_of'],
    'parent_of': ['no_parent_of']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
