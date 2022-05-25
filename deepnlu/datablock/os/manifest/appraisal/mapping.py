
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

mapping_provenance = {
 'action': ['router.py',
            'plac_core.py',
            'manifestgen_orchestrator.py',
            'index_writer.py',
            'common_utils.py'],
 'source': 'appraisal-intents',
 'time': '2022-02-16 16:34:23.294288'}

mapping = {
    'RANDOM_CATEGORIES#1': [{'include_all_of': ['category', 'random_query']}],
    'RANDOM_CATEGORIES#2': [{'include_all_of': ['category', 'generate']}],
    'RANDOM_CATEGORIES#3': [{'include_all_of': ['category']}, {'score': -25}],
    'RANDOM_COMMENTS#1': [{'include_all_of': ['comment', 'random_query']}],
    'RANDOM_COMMENTS#2': [{'include_all_of': ['comment', 'generate']}],
    'RANDOM_COMMENTS#3': [{'include_all_of': ['comment']}, {'score': -25}],
    'SIMILARITY#1': [{'include_all_of': ['similar']}]}
