
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

class ChitchatRequires(object):

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
 'config': {'classname': 'ChitchatRequires',
            'filename': 'chitchat_requires',
            'queries': ['requires.sparql % $PREFIX=chitchat'],
            'reverse': True,
            'transformers': ['effects']},
 'source': 'chitchat.owl',
 'time': '2022-04-27 21:17:15.117855'}

    __data = {
    'adorkable': ['adorkable_response', 'agreeable_deflection'],
    'agreeable_deflection': ['disagreeable_deflection'],
    'bad_weather': ['bad_weather_response'],
    'bad_weather_response': ['conditional_state_deflection'],
    'conditional_state_deflection': ['agreeable_deflection'],
    'disagreeable_deflection': ['agreeable_deflection'],
    'friday': ['friday_response'],
    'good_weather': ['good_weather_response'],
    'good_weather_response': ['agreeable_deflection'],
    'greeting': ['greeting_response'],
    'hello': ['hello_response'],
    'hello_response': ['meet_and_greet'],
    'insult': ['insult_response'],
    'late_transport': ['late_transport_response'],
    'late_transport_response': ['cliche_deflection', 'sympathy_deflection'],
    'meet_and_greet': ['state_greeting'],
    'monday': ['monday_response'],
    'monday_response': [   'conditional_state_deflection',
                           'cliche_deflection',
                           'monday'],
    'state_greeting': ['state_greeting_response'],
    'state_greeting_response': ['conditional_state_deflection'],
    'unknown_response': ['conditional_state_deflection'],
    'weather': ['weather_response'],
    'weather_response': ['conditional_state_deflection']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
