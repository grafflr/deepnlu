
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

class SkillsInferByRequires(object):

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
 'config': {'classname': 'SkillsInferByRequires',
            'filename': 'skills_infer_by_requires',
            'queries': ['infer_by_requires.sparql % $PREFIX=skills'],
            'transformers': ['infer_by_requires']},
 'source': 'skills.owl',
 'time': '2022-04-27 21:15:54.282355'}

    __data = {
    'communication': [   {   'context': ['role'],
                             'id': 'e5712771-c6a9-11ec-90bf-4c1d96716627',
                             'replace': 'role',
                             'with': 'lecturer'}],
    'role': [   {   'context': ['communication'],
                    'id': 'e5712771-c6a9-11ec-90bf-4c1d96716627',
                    'replace': 'role',
                    'with': 'lecturer'}]}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
