
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

class KaoLabels(object):

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
 'config': {'classname': 'KaoLabels',
            'filename': 'kao_labels',
            'queries': ['labels.sparql'],
            'reverse': True,
            'transformers': ['labels']},
 'source': 'kao.owl',
 'time': '2022-04-27 22:07:10.950570'}

    __data = {
    'determination': ['Determination'],
    'dreams': ['Dreams'],
    'failure': ['Failure'],
    'improvement': ['Improvement'],
    'inspiration': ['Inspiration'],
    'learning': ['Learning'],
    'learning_by_failure': ['Learning By Failure'],
    'michael_jordan': ['Michael Jordan'],
    'prt_f53b69f5_c68d_11ec_b2ff_4c1d96716627': [   "Michael Jordan's Video Is "
                                                    'a Great Example of Why '
                                                    'Taking Risks Is Important '
                                                    'For Learning And Being '
                                                    'Successful.'],
    'risk_taking': ['Risk Taking'],
    'success': ['Success']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
