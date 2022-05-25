
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

class ChitchatTypesRev(object):

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
 'config': {'classname': 'ChitchatTypes',
            'filename': 'chitchat_types',
            'queries': ['subclass.sparql'],
            'reverse': True,
            'transformers': ['types']},
 'source': 'chitchat.owl',
 'time': '2022-04-27 21:17:15.277355'}

    __data = {
    'action': ['ability_action', 'greeting_action'],
    'animal': ['horse', 'cat', 'otter', 'ocelot', 'dog'],
    'animal_slack_emoji': [   'cat_slack_emoji',
                              'dog_slack_emoji',
                              'otter_slack_emoji',
                              'big_cat_slack_emoji',
                              'horse_slack_emoji'],
    'cat': ['kitten'],
    'deflection_response': [   'unknown_response',
                               'cliche_deflection',
                               'conditional_state_deflection',
                               'agreeable_deflection',
                               'disagreeable_deflection',
                               'sympathy_deflection',
                               'reverse_deflection'],
    'dog': ['puppy'],
    'emoji': ['slack_emoji'],
    'emotion': ['favorable_emotion'],
    'experience': ['negative_experience', 'positive_experience'],
    'favorable_emotion': ['like_animal'],
    'greeting': ['meet_and_greet', 'hello', 'state_greeting', 'time_greeting'],
    'greeting_action': [   'free_state_action',
                           'busy_state_action',
                           'general_state_action'],
    'greeting_response': [   'monday_response',
                             'hello_response',
                             'friday_response',
                             'state_greeting_response',
                             'weather_response'],
    'insult': ['adorkable'],
    'insult_response': ['adorkable_response'],
    'interrogation_response': ['favorite_animal_response'],
    'negative_experience': [   'packed_transport',
                               'monday',
                               'late_transport',
                               'bad_weather'],
    'positive_experience': ['friday', 'good_weather'],
    'response': [   'greeting_response',
                    'location_response',
                    'insult_response',
                    'transport_response',
                    'deflection_response',
                    'interrogation_response'],
    'slack_emoji': [   'insult_slack_emoji',
                       'negative_slack_emoji',
                       'greeting_slack_emoji',
                       'neutral_slack_emoji',
                       'animal_slack_emoji',
                       'positive_slack_emoji'],
    'state': ['late', 'early'],
    'transport': ['plane', 'bus', 'train'],
    'transport_response': ['late_transport_response'],
    'weather_response': ['bad_weather_response', 'good_weather_response']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
