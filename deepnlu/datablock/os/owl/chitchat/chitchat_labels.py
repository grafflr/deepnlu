
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

class ChitchatLabels(object):

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
 'config': {'classname': 'ChitchatLabels',
            'filename': 'chitchat_labels',
            'queries': ['labels.sparql'],
            'reverse': True,
            'transformers': ['labels']},
 'source': 'chitchat.owl',
 'time': '2022-04-27 21:17:15.291355'}

    __data = {
    'ability_action': ['Ability Action'],
    'action': ['Action'],
    'adorkable': ['Adorkable'],
    'adorkable_response': ['Adorkable Response'],
    'agreeable_deflection': ['Agreeable Deflection'],
    'animal': ['Animal'],
    'animal_slack_emoji': ['Animal Slack Emoji'],
    'bad_weather': ['Bad Weather'],
    'bad_weather_response': ['Bad Weather Response'],
    'big_cat_slack_emoji': ['Big Cat Slack Emoji'],
    'busy_state_action': ['Busy State Action'],
    'cat': ['Cat'],
    'cat_slack_emoji': ['Cat Slack Emoji'],
    'cliche_deflection': ['Cliche Deflection'],
    'conditional_state_deflection': ['Conditional State Deflection'],
    'deflection_response': ['Deflection Response'],
    'disagreeable_deflection': ['Disagreeable Deflection'],
    'dog': ['Dog'],
    'dog_slack_emoji': ['Dog Slack Emoji'],
    'early': ['Early'],
    'emoji': ['Emoji'],
    'emotion': ['Emotion'],
    'experience': ['Experience'],
    'favorable_emotion': ['Favorable Emotion'],
    'favorite_animal_response': ['Favorite Animal Response'],
    'free_state_action': ['Free State Action'],
    'friday': ['Friday'],
    'friday_response': ['Friday Response'],
    'general_state_action': ['General State Action'],
    'good_weather': ['Good Weather'],
    'good_weather_response': ['Good Weather Response'],
    'greeting': ['Greeting'],
    'greeting_action': ['Greeting Action'],
    'greeting_response': ['Greeting Response'],
    'greeting_slack_emoji': ['Greeting Slack Emoji'],
    'hello': ['Hello'],
    'hello_response': ['Hello Response'],
    'horse': ['Horse'],
    'horse_slack_emoji': ['Horse Slack Emoji'],
    'insult': ['Insult'],
    'insult_response': ['Insult Response'],
    'insult_slack_emoji': ['Insult Slack Emoji'],
    'interrogation_response': ['Interrogation Response'],
    'kitten': ['Kitten'],
    'late': ['Late'],
    'late_transport': ['Late Transport'],
    'late_transport_response': ['Late Transport Response'],
    'like_animal': ['Like Animal'],
    'location_question': ['Location Question'],
    'location_response': ['Location Response'],
    'meet_and_greet': ['Meet And Greet'],
    'monday': ['Monday'],
    'monday_response': ['Monday Response'],
    'negative_experience': ['Negative Experience'],
    'negative_slack_emoji': ['Negative Slack Emoji'],
    'neutral_slack_emoji': ['Neutral Slack Emoji'],
    'ocelot': ['Ocelot'],
    'otter': ['Otter'],
    'otter_slack_emoji': ['Otter Slack Emoji'],
    'packed_transport': ['Packed Transport'],
    'positive_experience': ['Positive Experience'],
    'positive_slack_emoji': ['Positive Slack Emoji'],
    'pronoun': ['Pronoun'],
    'puppy': ['Puppy'],
    'response': ['Response'],
    'reverse_deflection': ['Reverse Deflection'],
    'slack_emoji': ['Slack Emoji'],
    'state': ['State'],
    'state_greeting': ['State Greeting'],
    'state_greeting_response': ['State Greeting Response'],
    'sympathy_deflection': ['Sympathy Deflection'],
    'time_greeting': ['Time Greeting'],
    'transport_response': ['Transport Response'],
    'unknown_response': ['Unknown Response'],
    'weather_response': ['Weather Response']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
