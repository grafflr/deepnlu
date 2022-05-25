
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

class AppraisalRecommendations(object):

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
 'config': {'classname': 'AppraisalRecommendations',
            'filename': 'appraisal_recommendations',
            'queries': ['recommendations.sparql % $PREFIX=appraisal'],
            'restrict': ['appraisal'],
            'reverse': True,
            'transformers': ['lowercase']},
 'source': 'appraisal.owl',
 'time': '2022-04-27 21:14:33.399283'}

    __data = {
    'awards like employee of the month are of no value for employees like you who perform well every single day of the year. thank you': [   'employee',
                                                                                                                                             'perform',
                                                                                                                                             'value',
                                                                                                                                             'well'],
    'from friendship to mentorship to leadership, you have given this company so much': [   'leadership'],
    'i envy any organization that has access to your talent': [   'organization',
                                                                  'access',
                                                                  'talent'],
    'i extend my formal appreciation for your excellent work': [   'anticipate',
                                                                   'excel',
                                                                   'work'],
    'i have enjoyed working with you over the past few years': ['work'],
    'i have no hesitation in recommending you as an outstanding individual who would be a huge asset to any company': [   'valuable_asset',
                                                                                                                          'recommend'],
    'i hope i can continue to work with you in the future': [   'continue',
                                                                'future',
                                                                'work'],
    'i know you will be a valuable asset to any team you choose to join': [   'valuable_asset',
                                                                              'valuable',
                                                                              'know'],
    'i look forward to -- and hope -- i can work with you again in the future': [   'forward',
                                                                                    'future',
                                                                                    'look',
                                                                                    'work'],
    'i look forward to continuing to work with you on future engagements': [   'engagement',
                                                                               'continue',
                                                                               'forward',
                                                                               'future',
                                                                               'work',
                                                                               'look'],
    'i look forward to future collaboration with you': [   'collaborate',
                                                           'forward',
                                                           'future',
                                                           'look'],
    'i look forward to future project opportunities with you': [   'opportunity',
                                                                   'forward',
                                                                   'project',
                                                                   'future',
                                                                   'look'],
    'i would consider it a real privilege to work with you again': [   'consider',
                                                                       'work'],
    'i would like to extend appreciation for your sincere help and effort in our last project': [   'anticipate',
                                                                                                    'sincere',
                                                                                                    'project',
                                                                                                    'effort',
                                                                                                    'help'],
    'i would recommend you to any company without hesitation': ['recommend'],
    "i'm looking forward to working with you again in the future": [   'forward',
                                                                       'future',
                                                                       'look',
                                                                       'work'],
    'in summary, your commitment to all-around excellence has been inspirational. i hope our paths cross again in future': [   'excellence',
                                                                                                                               'inspire',
                                                                                                                               'commit',
                                                                                                                               'future'],
    'it has been a great pleasure working with a colleague like you.': [   'colleague',
                                                                           'great',
                                                                           'work'],
    'it was a pleasure working with you': ['work'],
    "it's been an absolute pleasure working with you": ['work'],
    'our business survives on the commitment and dedication of passionate employees like you': [   'employee',
                                                                                                   'business',
                                                                                                   'dedicate',
                                                                                                   'survive',
                                                                                                   'commit'],
    'our entire team joins together in wishing you every success in all your future endeavors': [   'success',
                                                                                                    'future',
                                                                                                    'team'],
    'thank you for bringing your best to work every single day': [   'bring',
                                                                     'work'],
    'thank you for bringing your positive attitude to work every day': [   'positive_attitude',
                                                                           'bring',
                                                                           'work'],
    'thank you for your hard work': ['hard_work'],
    'thank you for your time and dedication': ['dedicate', 'time'],
    'thanks for backing up the credentials in your resume with hard work, perseverance, and loyalty to the company': [   'persevere',
                                                                                                                         'hard_work',
                                                                                                                         'loyal'],
    'thanks for being my inspiration': ['inspiration'],
    'the world will be a better place because of your efforts': [   'better',
                                                                    'effort',
                                                                    'place',
                                                                    'world'],
    'you are a genuinely great colleague and an asset to any team': [   'valuable_asset',
                                                                        'colleague',
                                                                        'genuine',
                                                                        'great'],
    'you are a real asset to any project': ['valuable_asset', 'project'],
    'you are a source of inspiration for your colleagues': [   'inspiration',
                                                               'colleague',
                                                               'source'],
    'you are the epitome of professionalism. thank you for bringing your best to work every single day': [   'professional',
                                                                                                             'bring',
                                                                                                             'work'],
    'you were a wonderful coworker': ['unknown'],
    'your contributions to the organization are well-known and will only increase in value as time goes on': [   'organization',
                                                                                                                 'contribute',
                                                                                                                 'increase',
                                                                                                                 'value',
                                                                                                                 'time',
                                                                                                                 'well'],
    'your hard work and dedication were an essential part of our team': [   'hard_work',
                                                                            'essential',
                                                                            'dedicate',
                                                                            'team'],
    'your service is greatly valued, and you have been a great colleague': [   'colleague',
                                                                               'valuable',
                                                                               'service',
                                                                               'great']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
