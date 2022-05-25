
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

class ChitchatTypes(object):

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
 'time': '2022-04-27 21:17:15.275855'}

    __data = {
    'ability_action': ['action'],
    'adorkable': ['insult'],
    'adorkable_response': ['insult_response'],
    'agreeable_deflection': ['deflection_response'],
    'animal_slack_emoji': ['slack_emoji'],
    'bad_weather': ['negative_experience'],
    'bad_weather_response': ['weather_response'],
    'big_cat_slack_emoji': ['animal_slack_emoji'],
    'bus': ['transport'],
    'busy_state_action': ['greeting_action'],
    'cat': ['animal'],
    'cat_slack_emoji': ['animal_slack_emoji'],
    'cliche_deflection': ['deflection_response'],
    'conditional_state_deflection': ['deflection_response'],
    'deflection_response': ['response'],
    'disagreeable_deflection': ['deflection_response'],
    'dog': ['animal'],
    'dog_slack_emoji': ['animal_slack_emoji'],
    'early': ['state'],
    'favorable_emotion': ['emotion'],
    'favorite_animal_response': ['interrogation_response'],
    'free_state_action': ['greeting_action'],
    'friday': ['positive_experience'],
    'friday_response': ['greeting_response'],
    'general_state_action': ['greeting_action'],
    'good_weather': ['positive_experience'],
    'good_weather_response': ['weather_response'],
    'greeting_action': ['action'],
    'greeting_response': ['response'],
    'greeting_slack_emoji': ['slack_emoji'],
    'hello': ['greeting'],
    'hello_response': ['greeting_response'],
    'horse': ['animal'],
    'horse_slack_emoji': ['animal_slack_emoji'],
    'insult_response': ['response'],
    'insult_slack_emoji': ['slack_emoji'],
    'interrogation_response': ['response'],
    'kitten': ['cat'],
    'late': ['state'],
    'late_transport': ['negative_experience'],
    'late_transport_response': ['transport_response'],
    'like_animal': ['favorable_emotion'],
    'location_response': ['response'],
    'meet_and_greet': ['greeting'],
    'monday': ['negative_experience'],
    'monday_response': ['greeting_response'],
    'negative_experience': ['experience'],
    'negative_slack_emoji': ['slack_emoji'],
    'neutral_slack_emoji': ['slack_emoji'],
    'ocelot': ['animal'],
    'otter': ['animal'],
    'otter_slack_emoji': ['animal_slack_emoji'],
    'packed_transport': ['negative_experience'],
    'plane': ['transport'],
    'positive_experience': ['experience'],
    'positive_slack_emoji': ['slack_emoji'],
    'puppy': ['dog'],
    'reverse_deflection': ['deflection_response'],
    'slack_emoji': ['emoji'],
    'state_greeting': ['greeting'],
    'state_greeting_response': ['greeting_response'],
    'sympathy_deflection': ['deflection_response'],
    'time_greeting': ['greeting'],
    'train': ['transport'],
    'transport_response': ['response'],
    'unknown_response': ['deflection_response'],
    'weather_response': ['greeting_response']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
