
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

class KaoSynonymsRev(object):

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
 'time': '2022-04-27 22:07:10.939570'}

    __data = {
    'become better': ['improvement'],
    'determination': ['determination'],
    'dreams': ['dreams'],
    'failure': ['failure'],
    'failure is part of the learning process': ['learning_by_failure'],
    'grit': ['determination'],
    'improvement': ['improvement'],
    'inspiration': ['inspiration'],
    'inspire': ['inspiration'],
    'inspired': ['inspiration'],
    'inspirer': ['inspiration'],
    'inspirers': ['inspiration'],
    'inspires': ['inspiration'],
    'inspiring': ['inspiration'],
    'leads to greatness': ['success'],
    'learning': ['learning'],
    'learning by failure': ['learning_by_failure'],
    'learning from our failures': ['learning_by_failure'],
    'learning process': ['learning'],
    'michael jordan': ['michael_jordan'],
    "michael jordan's": ['michael_jordan'],
    "michael jordan's video is a great example of why taking risks is important for learning and being successful": [   'prt_f53b69f5_c68d_11ec_b2ff_4c1d96716627'],
    "michael jordan's video is a great example of why taking risks is important for learning and being successful.": [   'prt_f53b69f5_c68d_11ec_b2ff_4c1d96716627'],
    'never give up': ['determination'],
    'okay to fail': ['learning_by_failure'],
    'okay with failing': ['learning_by_failure'],
    'risk taking': ['risk_taking'],
    'success': ['success'],
    'successful': ['success'],
    'taking risks': ['risk_taking'],
    'willingness to fail': ['risk_taking']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
