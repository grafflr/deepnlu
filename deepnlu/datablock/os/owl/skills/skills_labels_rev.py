
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

class SkillsLabelsRev(object):

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
 'time': '2022-04-27 21:15:54.427855'}

    __data = {
    'Ability': ['ability'],
    'Academic': ['academic'],
    'Activist': ['activist'],
    'Advisor': ['advisor'],
    'Advocate': ['advocate'],
    'Agenda': ['agenda'],
    'Artifact': ['artifact'],
    'Author': ['author'],
    'Beginner': ['beginner'],
    'Board Chair': ['board_chair'],
    'Business Academic': ['business_academic'],
    'Business Creativity': ['business_creativity'],
    'Business Role': ['business_role'],
    'Business School': ['business_school'],
    'Ceo': ['ceo'],
    'Chief Strategy Officer': ['chief_strategy_officer'],
    'Communication': ['communication'],
    'Company': ['company'],
    'Council': ['council'],
    'Creative': ['creative'],
    'Cto': ['cto'],
    'Cxo': ['cxo'],
    'Deliver': ['deliver'],
    'Delivery': ['delivery'],
    'Economic Policy': ['economic_policy'],
    'Empathy': ['empathy'],
    'Entrepreneur': ['entrepreneur'],
    'Event': ['event'],
    'Expert': ['expert'],
    'Facilitate': ['facilitate'],
    'Facilitator': ['facilitator'],
    'Forbes': ['forbes'],
    'Forum': ['forum'],
    'Founder': ['founder'],
    'Global Innovation Council': ['global_innovation_council'],
    'Government': ['government'],
    'Harvard Business School': ['harvard_business_school'],
    'Harvard University': ['harvard_university'],
    'Influence': ['influence'],
    'Influencer': ['influencer'],
    'Innovation Agenda': ['innovation_agenda'],
    'Innovator': ['innovator'],
    'Inventor': ['inventor'],
    'Law': ['law'],
    'Lecturer': ['lecturer'],
    'Master Inventor': ['master_inventor'],
    'Mediate': ['mediate'],
    'Mentor': ['mentor'],
    'Musician': ['musician'],
    'National Economic Policy': ['national_economic_policy'],
    'Negotiate': ['negotiate'],
    'Organization': ['organization'],
    'Personal Touch': ['personal_touch'],
    'Perspective': ['perspective'],
    'Policy': ['policy'],
    'Practitioner': ['practitioner'],
    'Producer': ['producer'],
    'Professor': ['professor'],
    'Psychiatrist': ['psychiatrist'],
    'Publisher': ['publisher'],
    'Role': ['role'],
    'School': ['school'],
    'Senior Advisor': ['senior_advisor'],
    'Senior Inventor': ['senior_inventor'],
    'Skill': ['skill'],
    'Skill Level': ['skill_level'],
    'Social Media Influencer': ['social_media_influencer'],
    'Soft Skill': ['soft_skill'],
    'Startup': ['startup'],
    'The Economist': ['the_economist'],
    'Thought Leader': ['thought_leader'],
    'Trusted Advisor': ['trusted_advisor'],
    'University': ['university'],
    'World Economic Forum': ['world_economic_forum'],
    'Writer': ['writer']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
