
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

class SkillsGrafflNERRev(object):

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
 'config': {'classname': 'SkillsGrafflNER',
            'filename': 'skills_graffl_ner',
            'firstonly': False,
            'queries': ['ner.sparql % $PREFIX=skills $NER=grafflNER'],
            'reverse': True,
            'transformers': ['ner']},
 'source': 'skills.owl',
 'time': '2022-04-27 21:15:54.387858'}

    __data = {
    'ABLE': [   'perspective',
                'innovator',
                'delivery',
                'skill',
                'negotiate',
                'influencer',
                'entrepreneur',
                'mediate',
                'facilitate',
                'ability',
                'inventor',
                'creative',
                'empathy',
                'producer',
                'communication',
                'business creativity',
                'soft skill',
                'personal touch',
                'serial innovator',
                'master inventor',
                'serial inventor',
                'social media influencer',
                'senior inventor'],
    'ARTIFACT': [   'agenda',
                    'artifact',
                    'law',
                    'policy',
                    'innovator agenda',
                    'economic policy',
                    'national economic policy',
                    'innovation agenda',
                    'legislation'],
    'EVENT': ['influence', 'event', 'deliver'],
    'GOV': ['government'],
    'INC': ['startup', 'company'],
    'LAW': ['law', 'legislation'],
    'LEARN': [   'university',
                 'school',
                 'harvard university',
                 'business school',
                 'harvard business school'],
    'MENTOR': ['mentor', 'to support those'],
    'PUB': ['publisher', 'forbes', 'forbes.com', 'the economist'],
    'ROLE': [   'academic',
                'founder',
                'advisor',
                'ceo',
                'role',
                'activist',
                'professor',
                'psychiatrist',
                'lecturer',
                'mentor',
                'musician',
                'writer',
                'author',
                'facilitator',
                'advocate',
                'cto',
                'practitioner',
                'to support those',
                'trusted advisor',
                'chief executive officer',
                'board chair',
                'she lectures, he lectures, she has lectured, he has lectured',
                'business academic',
                'lectures, lectured, lecturing at',
                'inagural member',
                'activism',
                'business role',
                'senior advisor',
                'chief technical officer'],
    'SKILL': [   'perspective',
                 'innovator',
                 'delivery',
                 'skill',
                 'expert',
                 'negotiate',
                 'influencer',
                 'entrepreneur',
                 'mediate',
                 'facilitate',
                 'beginner',
                 'inventor',
                 'creative',
                 'empathy',
                 'producer',
                 'communication',
                 'business creativity',
                 'soft skill',
                 'personal touch',
                 'serial innovator',
                 'master inventor',
                 'serial inventor',
                 'social media influencer',
                 'senior inventor',
                 'skill level',
                 'novice',
                 'thought leader']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
