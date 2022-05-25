
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

class SkillsSpans(object):

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
 'config': {'classname': 'SkillsSpans',
            'filename': 'skills_spans',
            'queries': ['spans.sparql'],
            'transformers': ['spans']},
 'source': 'skills.owl',
 'time': '2022-04-27 21:15:54.290356'}

    __data = {
    'board': [   {   'canon': 'board_chair',
                     'content': {'chair'},
                     'distance': 3,
                     'forward': True,
                     'reverse': True}],
    'business': [   {   'canon': 'business_role',
                        'content': {'role'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True},
                    {   'canon': 'business_school',
                        'content': {'school'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True},
                    {   'canon': 'business_academic',
                        'content': {'academic'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True},
                    {   'canon': 'business_creativity',
                        'content': {'creativity'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True}],
    'chief': [   {   'canon': 'chief_strategy_officer',
                     'content': {'strategy', 'officer'},
                     'distance': 3,
                     'forward': True,
                     'reverse': True}],
    'economic': [   {   'canon': 'economic_policy',
                        'content': {'policy'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True}],
    'global': [   {   'canon': 'global_innovation_council',
                      'content': {'council', 'innovation'},
                      'distance': 3,
                      'forward': True,
                      'reverse': True}],
    'harvard': [   {   'canon': 'harvard_university',
                       'content': {'university'},
                       'distance': 3,
                       'forward': True,
                       'reverse': True},
                   {   'canon': 'harvard_business_school',
                       'content': {'school', 'business'},
                       'distance': 3,
                       'forward': True,
                       'reverse': True}],
    'innovation': [   {   'canon': 'innovation_agenda',
                          'content': {'agenda'},
                          'distance': 3,
                          'forward': True,
                          'reverse': True}],
    'innovator': [   {   'canon': 'innovation_agenda',
                         'content': {'agenda'},
                         'distance': 3,
                         'forward': True,
                         'reverse': True}],
    'master': [   {   'canon': 'master_inventor',
                      'content': {'inventor'},
                      'distance': 3,
                      'forward': True,
                      'reverse': True}],
    'national': [   {   'canon': 'national_economic_policy',
                        'content': {'policy', 'economic'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True}],
    'personal': [   {   'canon': 'personal_touch',
                        'content': {'touch'},
                        'distance': 3,
                        'forward': True,
                        'reverse': True}],
    'senior': [   {   'canon': 'senior_inventor',
                      'content': {'inventor'},
                      'distance': 3,
                      'forward': True,
                      'reverse': True},
                  {   'canon': 'senior_advisor',
                      'content': {'advisor'},
                      'distance': 3,
                      'forward': True,
                      'reverse': True}],
    'skill': [   {   'canon': 'skill_level',
                     'content': {'level'},
                     'distance': 3,
                     'forward': True,
                     'reverse': True}],
    'social': [   {   'canon': 'social_media_influencer',
                      'content': {'media', 'influencer'},
                      'distance': 3,
                      'forward': True,
                      'reverse': True}],
    'soft': [   {   'canon': 'soft_skill',
                    'content': {'skill'},
                    'distance': 3,
                    'forward': True,
                    'reverse': True}],
    'the': [   {   'canon': 'the_economist',
                   'content': {'economist'},
                   'distance': 3,
                   'forward': True,
                   'reverse': True}],
    'thought': [   {   'canon': 'thought_leader',
                       'content': {'leader'},
                       'distance': 3,
                       'forward': True,
                       'reverse': True}],
    'trusted': [   {   'canon': 'trusted_advisor',
                       'content': {'advisor'},
                       'distance': 3,
                       'forward': True,
                       'reverse': True}],
    'world': [   {   'canon': 'world_economic_forum',
                     'content': {'economic', 'forum'},
                     'distance': 3,
                     'forward': True,
                     'reverse': True}]}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
