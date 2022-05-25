
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

class SkillsTypesRev(object):

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
 'time': '2022-04-27 21:15:54.412855'}

    __data = {
    'ability': ['skill'],
    'academic': ['business_academic'],
    'advisor': ['senior_advisor'],
    'agenda': ['innovation_agenda'],
    'artifact': ['agenda', 'law', 'policy'],
    'business_role': ['ceo', 'board_chair', 'cto'],
    'business_school': ['harvard_business_school'],
    'company': ['startup'],
    'council': ['global_innovation_council'],
    'creative': ['business_creativity'],
    'cxo': ['chief_strategy_officer'],
    'economic_policy': ['national_economic_policy'],
    'event': ['influence', 'deliver', 'produce'],
    'forum': ['world_economic_forum'],
    'influencer': ['social_media_influencer'],
    'inventor': ['senior_inventor', 'master_inventor'],
    'organization': [   'council',
                        'forum',
                        'publisher',
                        'government',
                        'school',
                        'company'],
    'policy': ['economic_policy'],
    'publisher': ['forbes', 'the_economist'],
    'role': [   'academic',
                'founder',
                'advisor',
                'business_role',
                'activist',
                'professor',
                'psychiatrist',
                'lecturer',
                'mentor',
                'musician',
                'writer',
                'facilitator',
                'advocate',
                'practitioner'],
    'school': ['university', 'business_school'],
    'senior_advisor': ['trusted_advisor'],
    'skill': [   'perspective',
                 'innovator',
                 'delivery',
                 'soft_skill',
                 'negotiate',
                 'influencer',
                 'entrepreneur',
                 'mediate',
                 'facilitate',
                 'inventor',
                 'creative',
                 'producer',
                 'communication'],
    'skill_level': ['thought_leader', 'expert', 'beginner'],
    'soft_skill': ['empathy', 'personal_touch'],
    'title': ['cxo', 'president', 'vice_president'],
    'university': ['harvard_university'],
    'writer': ['author']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
