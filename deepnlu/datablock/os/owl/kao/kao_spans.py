
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

class KaoSpans(object):

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
 'config': {'classname': 'KaoSpans',
            'filename': 'kao_spans',
            'queries': ['spans.sparql'],
            'transformers': ['spans']},
 'source': 'kao.owl',
 'time': '2022-04-27 22:07:10.847070'}

    __data = {
    'failure': [   {   'canon': 'learning_by_failure',
                       'content': {'part', 'learning', 'process'},
                       'distance': 3,
                       'forward': True,
                       'reverse': True}],
    'learning': [   {   'canon': 'learning_by_failure',
                        'content': {'failure'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True},
                    {   'canon': 'learning_by_failure',
                        'content': {'failures'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True}],
    'michael': [   {   'canon': 'prt_f53b69f5_c68d_11ec_b2ff_4c1d96716627',
                       'content': {   'being',
                                      'example',
                                      'great',
                                      'important',
                                      "jordan's",
                                      'learning',
                                      'risks',
                                      'successful.',
                                      'taking',
                                      'video'},
                       'distance': 3,
                       'forward': True,
                       'reverse': True},
                   {   'canon': 'michael_jordan',
                       'content': {'jordan'},
                       'distance': 3,
                       'forward': True,
                       'reverse': True},
                   {   'canon': 'michael_jordan',
                       'content': {"jordan's"},
                       'distance': 3,
                       'forward': True,
                       'reverse': True}],
    'okay': [   {   'canon': 'learning_by_failure',
                    'content': {'fail'},
                    'distance': 3,
                    'forward': True,
                    'reverse': True},
                {   'canon': 'learning_by_failure',
                    'content': {'failing'},
                    'distance': 3,
                    'forward': True,
                    'reverse': True}],
    'prt': [   {   'canon': 'prt_f53b69f5_c68d_11ec_b2ff_4c1d96716627',
                   'content': {   '11ec',
                                  '4c1d96716627',
                                  'b2ff',
                                  'c68d',
                                  'f53b69f5'},
                   'distance': 3,
                   'forward': True,
                   'reverse': True}],
    'risk': [   {   'canon': 'risk_taking',
                    'content': {'taking'},
                    'distance': 3,
                    'forward': True,
                    'reverse': True}],
    'taking': [   {   'canon': 'risk_taking',
                      'content': {'risks'},
                      'distance': 3,
                      'forward': True,
                      'reverse': True}],
    'willingness': [   {   'canon': 'risk_taking',
                           'content': {'fail'},
                           'distance': 3,
                           'forward': True,
                           'reverse': True}]}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
