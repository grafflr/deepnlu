
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

class SkillsGrafflNER(object):

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
 'time': '2022-04-27 21:15:54.386855'}

    __data = {
    'ability': ['ABLE'],
    'academic': ['ROLE'],
    'activism': ['ROLE'],
    'activist': ['ROLE'],
    'advisor': ['ROLE'],
    'advocate': ['ROLE'],
    'agenda': ['ARTIFACT'],
    'artifact': ['ARTIFACT'],
    'author': ['ROLE'],
    'beginner': ['SKILL'],
    'board chair': ['ROLE'],
    'business academic': ['ROLE'],
    'business creativity': ['ABLE', 'SKILL'],
    'business role': ['ROLE'],
    'business school': ['LEARN'],
    'ceo': ['ROLE'],
    'chief executive officer': ['ROLE'],
    'chief technical officer': ['ROLE'],
    'communication': ['ABLE', 'SKILL'],
    'company': ['INC'],
    'creative': ['ABLE', 'SKILL'],
    'cto': ['ROLE'],
    'deliver': ['EVENT'],
    'delivery': ['ABLE', 'SKILL'],
    'economic policy': ['ARTIFACT'],
    'empathy': ['ABLE', 'SKILL'],
    'entrepreneur': ['ABLE', 'SKILL'],
    'event': ['EVENT'],
    'expert': ['SKILL'],
    'facilitate': ['ABLE', 'SKILL'],
    'facilitator': ['ROLE'],
    'forbes': ['PUB'],
    'forbes.com': ['PUB'],
    'founder': ['ROLE'],
    'government': ['GOV'],
    'harvard business school': ['LEARN'],
    'harvard university': ['LEARN'],
    'inagural member': ['ROLE'],
    'influence': ['EVENT'],
    'influencer': ['ABLE', 'SKILL'],
    'innovation agenda': ['ARTIFACT'],
    'innovator': ['ABLE', 'SKILL'],
    'innovator agenda': ['ARTIFACT'],
    'inventor': ['ABLE', 'SKILL'],
    'law': ['ARTIFACT', 'LAW'],
    'lecturer': ['ROLE'],
    'lectures, lectured, lecturing at': ['ROLE'],
    'legislation': ['ARTIFACT', 'LAW'],
    'master inventor': ['ABLE', 'SKILL'],
    'mediate': ['ABLE', 'SKILL'],
    'mentor': ['MENTOR', 'ROLE'],
    'musician': ['ROLE'],
    'national economic policy': ['ARTIFACT'],
    'negotiate': ['ABLE', 'SKILL'],
    'novice': ['SKILL'],
    'personal touch': ['ABLE', 'SKILL'],
    'perspective': ['ABLE', 'SKILL'],
    'policy': ['ARTIFACT'],
    'practitioner': ['ROLE'],
    'producer': ['ABLE', 'SKILL'],
    'professor': ['ROLE'],
    'psychiatrist': ['ROLE'],
    'publisher': ['PUB'],
    'role': ['ROLE'],
    'school': ['LEARN'],
    'senior advisor': ['ROLE'],
    'senior inventor': ['ABLE', 'SKILL'],
    'serial innovator': ['ABLE', 'SKILL'],
    'serial inventor': ['ABLE', 'SKILL'],
    'she lectures, he lectures, she has lectured, he has lectured': ['ROLE'],
    'skill': ['ABLE', 'SKILL'],
    'skill level': ['SKILL'],
    'social media influencer': ['ABLE', 'SKILL'],
    'soft skill': ['ABLE', 'SKILL'],
    'startup': ['INC'],
    'the economist': ['PUB'],
    'thought leader': ['SKILL'],
    'to support those': ['MENTOR', 'ROLE'],
    'trusted advisor': ['ROLE'],
    'university': ['LEARN'],
    'writer': ['ROLE']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
