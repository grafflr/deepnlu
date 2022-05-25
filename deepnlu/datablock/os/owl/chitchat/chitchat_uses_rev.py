
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

class ChitchatUsesRev(object):

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
 'time': '2022-04-27 21:17:15.123856'}

    __data = {
    'big_cat_slack_emoji': ['ocelot'],
    'cat_slack_emoji': ['cat'],
    'dog_slack_emoji': ['dog'],
    'greeting_slack_emoji': [   'greeting_slack_emoji',
                                'hello',
                                'state_greeting_response',
                                'state_greeting'],
    'horse_slack_emoji': ['horse'],
    'negative_slack_emoji': [   'monday',
                                'late_transport_response',
                                'negative_experience'],
    'neutral_slack_emoji': ['bad_weather_response', 'bad_weather'],
    'otter_slack_emoji': ['otter'],
    'positive_slack_emoji': [   'agreeable_deflection',
                                'disagreeable_deflection',
                                'friday_response',
                                'good_weather_response',
                                'positive_experience'],
    'sympathy_deflection': ['late_transport']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
