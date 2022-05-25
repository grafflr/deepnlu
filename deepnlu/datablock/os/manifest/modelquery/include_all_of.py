
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

include_all_of_provenance = {
 'action': ['router.py',
            'plac_core.py',
            'manifestgen_orchestrator.py',
            'index_writer.py',
            'common_utils.py'],
 'source': 'portendo-classifications',
 'time': '2022-05-17 16:54:38.402938'}

include_all_of = {
    'age': [   {   'mappings': ['WhatIsYourAge'],
                   'terms': ['what_is_your_question']}],
    'john_kao': [{'mappings': ['HandleJohnKao'], 'terms': []}],
    'random_query': [   {   'mappings': ['HandleRandomSpeechDisorderQuestion'],
                            'terms': ['speech_disorder_model']},
                        {   'mappings': ['HandleRandomPathologyQuestion'],
                            'terms': ['speech_pathology_model']}],
    'speech_disorder_model': [   {   'mappings': ['HandleOpenAISpeechDisorder'],
                                     'terms': []}],
    'speech_pathology_model': [   {   'mappings': ['HandleOpenAIPathology'],
                                      'terms': []}]}
