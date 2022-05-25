
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

class ChitchatUses(object):

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
 'config': {'classname': 'ChitchatUses',
            'filename': 'chitchat_uses',
            'queries': ['uses.sparql % $PREFIX=chitchat'],
            'reverse': True,
            'transformers': ['effects']},
 'source': 'chitchat.owl',
 'time': '2022-04-27 21:17:15.122855'}

    __data = {
    'agreeable_deflection': ['positive_slack_emoji'],
    'bad_weather': ['neutral_slack_emoji'],
    'bad_weather_response': ['neutral_slack_emoji'],
    'cat': ['cat_slack_emoji'],
    'disagreeable_deflection': ['positive_slack_emoji'],
    'dog': ['dog_slack_emoji'],
    'friday_response': ['positive_slack_emoji'],
    'good_weather_response': ['positive_slack_emoji'],
    'greeting_slack_emoji': ['greeting_slack_emoji'],
    'hello': ['greeting_slack_emoji'],
    'horse': ['horse_slack_emoji'],
    'late_transport': ['sympathy_deflection'],
    'late_transport_response': ['negative_slack_emoji'],
    'monday': ['negative_slack_emoji'],
    'negative_experience': ['negative_slack_emoji'],
    'ocelot': ['big_cat_slack_emoji'],
    'otter': ['otter_slack_emoji'],
    'positive_experience': ['positive_slack_emoji'],
    'state_greeting': ['greeting_slack_emoji'],
    'state_greeting_response': ['greeting_slack_emoji']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
