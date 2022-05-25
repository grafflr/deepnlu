
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
 'source': 'portendo-classifications',
 'time': '2022-05-17 16:54:38.400936'}

mapping = {
    'HandleJohnKao': [{'include_all_of': ['john_kao']}],
    'HandleOpenAIPathology': [   {'include_all_of': ['speech_pathology_model']},
                                 {'exclude_one_of': ['random_query']}],
    'HandleOpenAISpeechDisorder': [   {   'include_all_of': [   'speech_disorder_model']},
                                      {'exclude_one_of': ['random_query']}],
    'HandleRandomPathologyQuestion': [   {   'include_all_of': [   'random_query',
                                                                   'speech_pathology_model']}],
    'HandleRandomSpeechDisorderQuestion': [   {   'include_all_of': [   'random_query',
                                                                        'speech_disorder_model']}],
    'WhatIsYourAge': [{'include_all_of': ['what_is_your_question', 'age']}]}
