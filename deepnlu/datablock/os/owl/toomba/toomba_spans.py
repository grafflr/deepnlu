
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

class ToombaSpans(object):

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
 'config': {'classname': 'ToombaSpans',
            'filename': 'toomba_spans',
            'queries': ['spans.sparql'],
            'transformers': ['spans']},
 'source': 'toomba.owl',
 'time': '2022-04-27 21:15:54.154857'}

    __data = {
    'clean': [   {   'canon': 'clean_channel',
                     'content': {'channel'},
                     'distance': 3,
                     'forward': True,
                     'reverse': True}],
    'command': [   {   'canon': 'command_classification',
                       'content': {'classification'},
                       'distance': 3,
                       'forward': True,
                       'reverse': True}],
    'question': [   {   'canon': 'question_classification',
                        'content': {'classification'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True}]}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
