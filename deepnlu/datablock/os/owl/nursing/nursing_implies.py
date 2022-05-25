
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

class NursingImplies(object):

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
            'config': {'classname': 'NursingImplies',
                       'filename': 'nursing_implies',
                       'queries': ['implies.sparql % $PREFIX=nursing'],
                       'reverse': True,
                       'transformers': ['lowercase', 'implies']},
            'source': 'nursing.owl',
            'time': '2022-05-20 17:18:46.039203'}

    __data = {
        'master_of_science_in_nursing': ['bachelor_of_science_in_nursing'],
        'nursing_school': ['nurse_educator'],
        'staffing': ['staff']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
