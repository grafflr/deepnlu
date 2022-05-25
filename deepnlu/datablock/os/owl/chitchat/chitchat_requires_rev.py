
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

class ChitchatRequiresRev(object):

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
 'time': '2022-04-27 21:17:15.118355'}

    __data = {
    'adorkable_response': ['adorkable'],
    'agreeable_deflection': [   'conditional_state_deflection',
                                'disagreeable_deflection',
                                'good_weather_response',
                                'adorkable'],
    'bad_weather_response': ['bad_weather'],
    'cliche_deflection': ['monday_response', 'late_transport_response'],
    'conditional_state_deflection': [   'unknown_response',
                                        'bad_weather_response',
                                        'monday_response',
                                        'state_greeting_response',
                                        'weather_response'],
    'disagreeable_deflection': ['agreeable_deflection'],
    'friday_response': ['friday'],
    'good_weather_response': ['good_weather'],
    'greeting_response': ['greeting'],
    'hello_response': ['hello'],
    'insult_response': ['insult'],
    'late_transport_response': ['late_transport'],
    'meet_and_greet': ['hello_response'],
    'monday': ['monday_response'],
    'monday_response': ['monday'],
    'state_greeting': ['meet_and_greet'],
    'state_greeting_response': ['state_greeting'],
    'sympathy_deflection': ['late_transport_response'],
    'weather_response': ['weather']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
