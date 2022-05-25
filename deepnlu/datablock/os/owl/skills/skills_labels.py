
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

class SkillsLabels(object):

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
 'config': {'classname': 'SkillsLabels',
            'filename': 'skills_labels',
            'queries': ['labels.sparql'],
            'reverse': True,
            'transformers': ['labels']},
 'source': 'skills.owl',
 'time': '2022-04-27 21:15:54.426355'}

    __data = {
    'ability': ['Ability'],
    'academic': ['Academic'],
    'activist': ['Activist'],
    'advisor': ['Advisor'],
    'advocate': ['Advocate'],
    'agenda': ['Agenda'],
    'artifact': ['Artifact'],
    'author': ['Author'],
    'beginner': ['Beginner'],
    'board_chair': ['Board Chair'],
    'business_academic': ['Business Academic'],
    'business_creativity': ['Business Creativity'],
    'business_role': ['Business Role'],
    'business_school': ['Business School'],
    'ceo': ['Ceo'],
    'chief_strategy_officer': ['Chief Strategy Officer'],
    'communication': ['Communication'],
    'company': ['Company'],
    'council': ['Council'],
    'creative': ['Creative'],
    'cto': ['Cto'],
    'cxo': ['Cxo'],
    'deliver': ['Deliver'],
    'delivery': ['Delivery'],
    'economic_policy': ['Economic Policy'],
    'empathy': ['Empathy'],
    'entrepreneur': ['Entrepreneur'],
    'event': ['Event'],
    'expert': ['Expert'],
    'facilitate': ['Facilitate'],
    'facilitator': ['Facilitator'],
    'forbes': ['Forbes'],
    'forum': ['Forum'],
    'founder': ['Founder'],
    'global_innovation_council': ['Global Innovation Council'],
    'government': ['Government'],
    'harvard_business_school': ['Harvard Business School'],
    'harvard_university': ['Harvard University'],
    'influence': ['Influence'],
    'influencer': ['Influencer'],
    'innovation_agenda': ['Innovation Agenda'],
    'innovator': ['Innovator'],
    'inventor': ['Inventor'],
    'law': ['Law'],
    'lecturer': ['Lecturer'],
    'master_inventor': ['Master Inventor'],
    'mediate': ['Mediate'],
    'mentor': ['Mentor'],
    'musician': ['Musician'],
    'national_economic_policy': ['National Economic Policy'],
    'negotiate': ['Negotiate'],
    'organization': ['Organization'],
    'personal_touch': ['Personal Touch'],
    'perspective': ['Perspective'],
    'policy': ['Policy'],
    'practitioner': ['Practitioner'],
    'producer': ['Producer'],
    'professor': ['Professor'],
    'psychiatrist': ['Psychiatrist'],
    'publisher': ['Publisher'],
    'role': ['Role'],
    'school': ['School'],
    'senior_advisor': ['Senior Advisor'],
    'senior_inventor': ['Senior Inventor'],
    'skill': ['Skill'],
    'skill_level': ['Skill Level'],
    'social_media_influencer': ['Social Media Influencer'],
    'soft_skill': ['Soft Skill'],
    'startup': ['Startup'],
    'the_economist': ['The Economist'],
    'thought_leader': ['Thought Leader'],
    'trusted_advisor': ['Trusted Advisor'],
    'university': ['University'],
    'world_economic_forum': ['World Economic Forum'],
    'writer': ['Writer']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
