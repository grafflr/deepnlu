
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

class SkillsTypes(object):

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
 'config': {'classname': 'SkillsTypes',
            'filename': 'skills_types',
            'queries': ['subclass.sparql'],
            'reverse': True,
            'transformers': ['types']},
 'source': 'skills.owl',
 'time': '2022-04-27 21:15:54.411855'}

    __data = {
    'academic': ['role'],
    'activist': ['role'],
    'advisor': ['role'],
    'advocate': ['role'],
    'agenda': ['artifact'],
    'author': ['writer'],
    'beginner': ['skill_level'],
    'board_chair': ['business_role'],
    'business_academic': ['academic'],
    'business_creativity': ['creative'],
    'business_role': ['role'],
    'business_school': ['school'],
    'ceo': ['business_role'],
    'chief_strategy_officer': ['cxo'],
    'communication': ['skill'],
    'company': ['organization'],
    'council': ['organization'],
    'creative': ['skill'],
    'cto': ['business_role'],
    'cxo': ['title'],
    'deliver': ['event'],
    'delivery': ['skill'],
    'economic_policy': ['policy'],
    'empathy': ['soft_skill'],
    'entrepreneur': ['skill'],
    'expert': ['skill_level'],
    'facilitate': ['skill'],
    'facilitator': ['role'],
    'forbes': ['publisher'],
    'forum': ['organization'],
    'founder': ['role'],
    'global_innovation_council': ['council'],
    'government': ['organization'],
    'harvard_business_school': ['business_school'],
    'harvard_university': ['university'],
    'influence': ['event'],
    'influencer': ['skill'],
    'innovation_agenda': ['agenda'],
    'innovator': ['skill'],
    'inventor': ['skill'],
    'law': ['artifact'],
    'lecturer': ['role'],
    'master_inventor': ['inventor'],
    'mediate': ['skill'],
    'mentor': ['role'],
    'musician': ['role'],
    'national_economic_policy': ['economic_policy'],
    'negotiate': ['skill'],
    'personal_touch': ['soft_skill'],
    'perspective': ['skill'],
    'policy': ['artifact'],
    'practitioner': ['role'],
    'president': ['title'],
    'produce': ['event'],
    'producer': ['skill'],
    'professor': ['role'],
    'psychiatrist': ['role'],
    'publisher': ['organization'],
    'school': ['organization'],
    'senior_advisor': ['advisor'],
    'senior_inventor': ['inventor'],
    'skill': ['ability'],
    'social_media_influencer': ['influencer'],
    'soft_skill': ['skill'],
    'startup': ['company'],
    'the_economist': ['publisher'],
    'thought_leader': ['skill_level'],
    'trusted_advisor': ['senior_advisor'],
    'university': ['school'],
    'vice_president': ['title'],
    'world_economic_forum': ['forum'],
    'writer': ['role']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
