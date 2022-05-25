
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

class KaoSynonyms(object):

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
 'config': {'classname': 'KaoSynonyms',
            'filename': 'kao_synonyms',
            'files': ['kao.txt'],
            'queries': ['synonyms.sparql'],
            'reverse': True,
            'transformers': ['lowercase', 'synonyms']},
 'source': 'kao.owl',
 'time': '2022-04-27 22:07:10.938070'}

    __data = {
    'determination': ['never give up', 'determination', 'grit'],
    'dreams': ['dreams'],
    'failure': ['failure'],
    'improvement': ['become better', 'improvement'],
    'inspiration': [   'inspiration',
                       'inspiring',
                       'inspirers',
                       'inspired',
                       'inspirer',
                       'inspires',
                       'inspire'],
    'learning': ['learning process', 'learning'],
    'learning_by_failure': [   'failure is part of the learning process',
                               'learning from our failures',
                               'learning by failure',
                               'okay with failing',
                               'okay to fail'],
    'michael_jordan': ["michael jordan's", 'michael jordan'],
    'prt_f53b69f5_c68d_11ec_b2ff_4c1d96716627': [   "michael jordan's video is "
                                                    'a great example of why '
                                                    'taking risks is important '
                                                    'for learning and being '
                                                    'successful.',
                                                    "michael jordan's video is "
                                                    'a great example of why '
                                                    'taking risks is important '
                                                    'for learning and being '
                                                    'successful'],
    'risk_taking': ['willingness to fail', 'taking risks', 'risk taking'],
    'success': ['leads to greatness', 'successful', 'success']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
