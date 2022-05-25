
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

class QuestionsTypes(object):

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
 'time': '2022-05-13 12:06:42.628842'}

    __data = {
    'clarifying': ['probing'],
    'closed_present_simple_do_question': ['do_question'],
    'closed_present_simple_question': ['close_ended'],
    'critical_awareness': ['probing'],
    'deductive_inference': ['inference'],
    'do_question': ['wh_question'],
    'first_person_pronoun': ['pronoun'],
    'future_continuous_question': ['continuous_question'],
    'future_continuous_where_question': ['future_continuous_question'],
    'future_continuous_why_question': ['future_continuous_question'],
    'future_pefect_why_question': ['why_question'],
    'future_perfect_continuous_how_question': [   'future_perfect_continuous_question'],
    'future_perfect_continuous_question': ['future_tense_question'],
    'future_perfect_question': ['future_tense_question'],
    'future_perfect_when_question': ['future_perfect_question'],
    'future_simple_how_question': ['how_question'],
    'future_simple_question': ['future_tense_question'],
    'future_simple_when_question': ['when_question'],
    'future_simple_where_question': ['where_question'],
    'he': ['third_person_pronoun'],
    'her': ['third_person_pronoun'],
    'him': ['third_person_pronoun'],
    'how_question': ['wh_question'],
    'i': ['first_person_pronoun'],
    'it': ['third_person_pronoun'],
    'me': ['first_person_pronoun'],
    'mine': ['first_person_pronoun'],
    'my': ['first_person_pronoun'],
    'myself': ['first_person_pronoun'],
    'open_present_simple_how_question': ['how_question'],
    'open_present_simple_question': ['present_simple_question'],
    'open_present_simple_what_question': ['open_present_simple_question'],
    'open_present_simple_when_question': ['when_question'],
    'open_present_simple_where_question': ['where_question'],
    'open_present_simple_who_question': ['open_present_simple_question'],
    'open_present_simple_why_question': ['why_question'],
    'organization': ['factual'],
    'our': ['first_person_pronoun'],
    'ourselves': ['first_person_pronoun'],
    'past_continuous_question': ['continuous_question'],
    'past_continuous_what_question': ['what_question'],
    'past_continuous_where_question': ['where_question'],
    'past_continuous_why_question': ['why_question'],
    'past_perfect_continuous_how_question': ['how_question'],
    'past_perfect_continuous_question': ['perfect_continuous_question'],
    'past_perfect_continuous_what_question': ['what_question'],
    'past_perfect_continuous_why_question': ['why_question'],
    'past_perfect_how_question': ['how_question'],
    'past_perfect_question': ['perfect_tense_question'],
    'past_perfect_when_question': ['when_question'],
    'past_perfect_why_question': ['why_question'],
    'past_simple_how_question': ['how_question'],
    'past_simple_question': ['simple_tense_question'],
    'past_simple_when_question': ['when_question'],
    'past_simple_who_question': ['who_question'],
    'past_simple_why_question': ['why_question'],
    'perfect_continuous_question': ['continuous_question'],
    'present_continuous_question': ['perfect_continuous_question'],
    'present_continuous_what_question': ['what_question'],
    'present_continuous_who_question': ['who_question'],
    'present_continuous_why_question': ['why_question'],
    'present_perfect_continuous_question': ['present_continuous_question'],
    'present_perfect_continuous_where_question': ['where_question'],
    'present_perfect_continuous_why_question': ['why_question'],
    'present_perfect_how_question': ['how_question'],
    'present_perfect_question': ['present_tense_question'],
    'present_perfect_why_question': ['why_question'],
    'present_simple_do_question': ['do_question'],
    'present_simple_question': ['simple_tense_question'],
    'present_simple_what_question': ['present_simple_question'],
    'present_simple_where_question': ['where_question'],
    'prompting': ['probing'],
    'redirection': ['probing'],
    'refocusing': ['probing'],
    'second_person_pronoun': ['pronoun'],
    'she': ['third_person_pronoun'],
    'simple_recall': ['factual'],
    'them': ['third_person_pronoun'],
    'they': ['third_person_pronoun'],
    'third_person_pronoun': ['pronoun'],
    'us': ['first_person_pronoun'],
    'we': ['first_person_pronoun'],
    'what_is': ['question_component'],
    'what_is_your_question': ['what_question'],
    'what_question': ['wh_question'],
    'when_question': ['wh_question'],
    'where_question': ['wh_question'],
    'who_question': ['wh_question'],
    'why_question': ['wh_question'],
    'you': ['second_person_pronoun'],
    'your': ['second_person_pronoun'],
    'yourself': ['second_person_pronoun']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
