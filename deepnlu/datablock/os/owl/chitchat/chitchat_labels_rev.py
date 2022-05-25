
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

class ChitchatLabelsRev(object):

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
 'time': '2022-04-27 21:17:15.292855'}

    __data = {
    'Ability Action': ['ability_action'],
    'Action': ['action'],
    'Adorkable': ['adorkable'],
    'Adorkable Response': ['adorkable_response'],
    'Agreeable Deflection': ['agreeable_deflection'],
    'Animal': ['animal'],
    'Animal Slack Emoji': ['animal_slack_emoji'],
    'Bad Weather': ['bad_weather'],
    'Bad Weather Response': ['bad_weather_response'],
    'Big Cat Slack Emoji': ['big_cat_slack_emoji'],
    'Busy State Action': ['busy_state_action'],
    'Cat': ['cat'],
    'Cat Slack Emoji': ['cat_slack_emoji'],
    'Cliche Deflection': ['cliche_deflection'],
    'Conditional State Deflection': ['conditional_state_deflection'],
    'Deflection Response': ['deflection_response'],
    'Disagreeable Deflection': ['disagreeable_deflection'],
    'Dog': ['dog'],
    'Dog Slack Emoji': ['dog_slack_emoji'],
    'Early': ['early'],
    'Emoji': ['emoji'],
    'Emotion': ['emotion'],
    'Experience': ['experience'],
    'Favorable Emotion': ['favorable_emotion'],
    'Favorite Animal Response': ['favorite_animal_response'],
    'Free State Action': ['free_state_action'],
    'Friday': ['friday'],
    'Friday Response': ['friday_response'],
    'General State Action': ['general_state_action'],
    'Good Weather': ['good_weather'],
    'Good Weather Response': ['good_weather_response'],
    'Greeting': ['greeting'],
    'Greeting Action': ['greeting_action'],
    'Greeting Response': ['greeting_response'],
    'Greeting Slack Emoji': ['greeting_slack_emoji'],
    'Hello': ['hello'],
    'Hello Response': ['hello_response'],
    'Horse': ['horse'],
    'Horse Slack Emoji': ['horse_slack_emoji'],
    'Insult': ['insult'],
    'Insult Response': ['insult_response'],
    'Insult Slack Emoji': ['insult_slack_emoji'],
    'Interrogation Response': ['interrogation_response'],
    'Kitten': ['kitten'],
    'Late': ['late'],
    'Late Transport': ['late_transport'],
    'Late Transport Response': ['late_transport_response'],
    'Like Animal': ['like_animal'],
    'Location Question': ['location_question'],
    'Location Response': ['location_response'],
    'Meet And Greet': ['meet_and_greet'],
    'Monday': ['monday'],
    'Monday Response': ['monday_response'],
    'Negative Experience': ['negative_experience'],
    'Negative Slack Emoji': ['negative_slack_emoji'],
    'Neutral Slack Emoji': ['neutral_slack_emoji'],
    'Ocelot': ['ocelot'],
    'Otter': ['otter'],
    'Otter Slack Emoji': ['otter_slack_emoji'],
    'Packed Transport': ['packed_transport'],
    'Positive Experience': ['positive_experience'],
    'Positive Slack Emoji': ['positive_slack_emoji'],
    'Pronoun': ['pronoun'],
    'Puppy': ['puppy'],
    'Response': ['response'],
    'Reverse Deflection': ['reverse_deflection'],
    'Slack Emoji': ['slack_emoji'],
    'State': ['state'],
    'State Greeting': ['state_greeting'],
    'State Greeting Response': ['state_greeting_response'],
    'Sympathy Deflection': ['sympathy_deflection'],
    'Time Greeting': ['time_greeting'],
    'Transport Response': ['transport_response'],
    'Unknown Response': ['unknown_response'],
    'Weather Response': ['weather_response']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
