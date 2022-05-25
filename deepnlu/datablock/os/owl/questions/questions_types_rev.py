
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

class QuestionsTypesRev(object):

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
 'config': {'classname': 'QuestionsTypes',
            'filename': 'questions_types',
            'queries': ['subclass.sparql'],
            'reverse': True,
            'transformers': ['types']},
 'source': 'questions.owl',
 'time': '2022-05-13 12:06:42.630340'}

    __data = {
    'close_ended': ['closed_present_simple_question'],
    'continuous_question': [   'past_continuous_question',
                               'future_continuous_question',
                               'perfect_continuous_question'],
    'do_question': [   'closed_present_simple_do_question',
                       'present_simple_do_question'],
    'factual': ['organization', 'simple_recall'],
    'first_person_pronoun': [   'me',
                                'our',
                                'us',
                                'we',
                                'mine',
                                'ourselves',
                                'my',
                                'myself',
                                'i'],
    'future_continuous_question': [   'future_continuous_why_question',
                                      'future_continuous_where_question'],
    'future_perfect_continuous_question': [   'future_perfect_continuous_how_question'],
    'future_perfect_question': ['future_perfect_when_question'],
    'future_tense_question': [   'future_perfect_continuous_question',
                                 'future_perfect_question',
                                 'future_simple_question'],
    'how_question': [   'open_present_simple_how_question',
                        'past_perfect_how_question',
                        'present_perfect_how_question',
                        'future_simple_how_question',
                        'past_simple_how_question',
                        'past_perfect_continuous_how_question'],
    'inference': ['deductive_inference'],
    'open_present_simple_question': [   'open_present_simple_who_question',
                                        'open_present_simple_what_question'],
    'perfect_continuous_question': [   'past_perfect_continuous_question',
                                       'present_continuous_question'],
    'perfect_tense_question': ['past_perfect_question'],
    'present_continuous_question': ['present_perfect_continuous_question'],
    'present_simple_question': [   'open_present_simple_question',
                                   'present_simple_what_question'],
    'present_tense_question': ['present_perfect_question'],
    'probing': [   'clarifying',
                   'redirection',
                   'prompting',
                   'refocusing',
                   'critical_awareness'],
    'pronoun': [   'third_person_pronoun',
                   'second_person_pronoun',
                   'first_person_pronoun'],
    'question_component': ['what_is'],
    'second_person_pronoun': ['you', 'your', 'yourself'],
    'simple_tense_question': [   'present_simple_question',
                                 'past_simple_question'],
    'third_person_pronoun': ['he', 'she', 'they', 'her', 'it', 'him', 'them'],
    'wh_question': [   'why_question',
                       'do_question',
                       'when_question',
                       'how_question',
                       'who_question',
                       'what_question',
                       'where_question'],
    'what_question': [   'past_continuous_what_question',
                         'past_perfect_continuous_what_question',
                         'present_continuous_what_question',
                         'what_is_your_question'],
    'when_question': [   'past_simple_when_question',
                         'past_perfect_when_question',
                         'open_present_simple_when_question',
                         'future_simple_when_question'],
    'where_question': [   'present_simple_where_question',
                          'future_simple_where_question',
                          'past_continuous_where_question',
                          'present_perfect_continuous_where_question',
                          'open_present_simple_where_question'],
    'who_question': [   'past_simple_who_question',
                        'present_continuous_who_question'],
    'why_question': [   'future_pefect_why_question',
                        'past_perfect_why_question',
                        'past_simple_why_question',
                        'past_perfect_continuous_why_question',
                        'present_perfect_why_question',
                        'open_present_simple_why_question',
                        'present_continuous_why_question',
                        'past_continuous_why_question',
                        'present_perfect_continuous_why_question']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
