
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

class KaoLookup(object):

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
 'config': {'classname': 'KaoLookup',
            'filename': 'kao_lookup',
            'files': ['kao.txt'],
            'queries': ['lookup.sparql'],
            'transformers': ['lowercase', 'lookup']},
 'source': 'kao.owl',
 'time': '2022-04-27 22:07:10.824070'}

    __data = {
    1: [   'determination',
           'inspiration',
           'improvement',
           'successful',
           'inspiring',
           'inspirers',
           'inspired',
           'inspirer',
           'inspires',
           'learning',
           'success',
           'failure',
           'inspire',
           'dreams',
           'grit'],
    2: [   'prt_f53b69f5_c68d_11ec_b2ff 4c1d96716627',
           'learning_from_our failures',
           'learning_by failure',
           'okay_with failing',
           "michael jordan's",
           'learning process',
           'michael jordan',
           'become better',
           'never_give up',
           'taking risks',
           'risk taking'],
    3: [   'learning by failure',
           'willingness to fail',
           'leads to greatness',
           'okay with failing',
           'never give up',
           'okay to fail'],
    4: ['learning from our failures'],
    5: [],
    6: ['prt f53b69f5 c68d 11ec b2ff 4c1d96716627'],
    7: ['failure is part of the learning process'],
    18: [   "michael jordan's video is a great example of why taking risks is "
            'important for learning and being successful.',
            "michael jordan's video is a great example of why taking risks is "
            'important for learning and being successful']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
