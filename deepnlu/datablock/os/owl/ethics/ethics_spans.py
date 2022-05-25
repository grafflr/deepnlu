
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

class EthicsSpans(object):

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
 'config': {'classname': 'EthicsSpans',
            'filename': 'ethics_spans',
            'queries': ['spans.sparql'],
            'transformers': ['spans']},
 'source': 'ethics.owl',
 'time': '2022-04-27 21:15:55.189355'}

    __data = {
    'data': [   {   'canon': 'data_ethics',
                    'content': {'ethics'},
                    'distance': 3,
                    'forward': True,
                    'reverse': True}],
    'intellectual': [   {   'canon': 'intellectual_inquiry',
                            'content': {'inquiry'},
                            'distance': 3,
                            'forward': True,
                            'reverse': True}],
    'moral': [   {   'canon': 'moral_philosophy',
                     'content': {'philosophy'},
                     'distance': 3,
                     'forward': True,
                     'reverse': True}]}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
