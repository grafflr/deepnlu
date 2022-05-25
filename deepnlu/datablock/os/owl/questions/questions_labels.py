
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

class QuestionsLabels(object):

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
 'config': {'classname': 'QuestionsLabels',
            'filename': 'questions_labels',
            'queries': ['labels.sparql'],
            'reverse': True,
            'transformers': ['labels']},
 'source': 'questions.owl',
 'time': '2022-05-13 12:06:42.649842'}

    __data = {
    'affective': ['Affective'],
    'analysis': ['Analysis'],
    'application': ['Application'],
    'boolean': ['Boolean'],
    'choice': ['Choice'],
    'clarifying': ['Clarifying'],
    'close_ended': ['Close Ended'],
    'closed_present_simple_do_question': ['Closed Present Simple Do Question'],
    'closed_present_simple_question': ['Closed Present Simple Question'],
    'comparison': ['Comparison'],
    'comprehension': ['Comprehension'],
    'continuous_question': ['Continuous Question'],
    'convergent': ['Convergent'],
    'critical_awareness': ['Critical Awareness'],
    'disjunctive': ['Disjunctive'],
    'divergent': ['Divergent'],
    'do_question': ['Do Question'],
    'double_barreled': ['Double Barreled'],
    'evaluation': ['Evaluation'],
    'evaluative': ['Evaluative'],
    'factual': ['Factual'],
    'first_person_pronoun': ['First Person Pronoun'],
    'future_continuous_question': ['Future Continuous Question'],
    'future_continuous_where_question': ['Future Continuous Where Question'],
    'future_continuous_why_question': ['Future Continuous Why Question'],
    'future_pefect_why_question': ['Future Pefect Why Question'],
    'future_perfect_continuous_how_question': [   'Future Perfect Continuous '
                                                  'How Question'],
    'future_perfect_continuous_question': [   'Future Perfect Continuous '
                                              'Question'],
    'future_perfect_question': ['Future Perfect Question'],
    'future_perfect_statement': ['Future Perfect Statement'],
    'future_perfect_when_question': ['Future Perfect When Question'],
    'future_simple_how_question': ['Future Simple How Question'],
    'future_simple_question': ['Future Simple Question'],
    'future_simple_when_question': ['Future Simple When Question'],
    'future_simple_where_question': ['Future Simple Where Question'],
    'future_tense_question': ['Future Tense Question'],
    'he': ['He'],
    'her': ['Her'],
    'him': ['Him'],
    'how_question': ['How Question'],
    'hypothetical': ['Hypothetical'],
    'i': ['I'],
    'inference': ['Inference'],
    'it': ['It'],
    'leading': ['Leading'],
    'loaded': ['Loaded'],
    'me': ['Me'],
    'mine': ['Mine'],
    'my': ['My'],
    'myself': ['Myself'],
    'open_ended': ['Open Ended'],
    'open_present_simple_how_question': ['Open Present Simple How Question'],
    'open_present_simple_question': ['Open Present Simple Question'],
    'open_present_simple_what_question': ['Open Present Simple What Question'],
    'open_present_simple_when_question': ['Open Present Simple When Question'],
    'open_present_simple_where_question': [   'Open Present Simple Where '
                                              'Question'],
    'open_present_simple_who_question': ['Open Present Simple Who Question'],
    'open_present_simple_why_question': ['Open Present Simple Why Question'],
    'organization': ['Organization'],
    'our': ['Our'],
    'ourselves': ['Ourselves'],
    'past_continuous_question': ['Past Continuous Question'],
    'past_continuous_what_question': ['Past Continuous What Question'],
    'past_continuous_where_question': ['Past Continuous Where Question'],
    'past_continuous_why_question': ['Past Continuous Why Question'],
    'past_perfect_continuous_how_question': [   'Past Perfect Continuous How '
                                                'Question'],
    'past_perfect_continuous_question': ['Past Perfect Continuous Question'],
    'past_perfect_continuous_what_question': [   'Past Perfect Continuous What '
                                                 'Question'],
    'past_perfect_continuous_why_question': [   'Past Perfect Continuous Why '
                                                'Question'],
    'past_perfect_how_question': ['Past Perfect How Question'],
    'past_perfect_question': ['Past Perfect Question'],
    'past_perfect_statement': ['Past Perfect Statement'],
    'past_perfect_when_question': ['Past Perfect When Question'],
    'past_perfect_why_question': ['Past Perfect Why Question'],
    'past_simple_how_question': ['Past Simple How Question'],
    'past_simple_question': ['Past Simple Question'],
    'past_simple_when_question': ['Past Simple When Question'],
    'past_simple_who_question': ['Past Simple Who Question'],
    'past_simple_why_question': ['Past Simple Why Question'],
    'past_tense_question': ['Past Tense Question'],
    'perfect_continuous_question': ['Perfect Continuous Question'],
    'perfect_tense_question': ['Perfect Tense Question'],
    'present_continuous_question': ['Present Continuous Question'],
    'present_continuous_what_question': ['Present Continuous What Question'],
    'present_continuous_who_question': ['Present Continuous Who Question'],
    'present_continuous_why_question': ['Present Continuous Why Question'],
    'present_perfect_continuous_question': [   'Present Perfect Continuous '
                                               'Question'],
    'present_perfect_continuous_where_question': [   'Present Perfect '
                                                     'Continuous Where '
                                                     'Question'],
    'present_perfect_continuous_why_question': [   'Present Perfect Continuous '
                                                   'Why Question'],
    'present_perfect_how_question': ['Present Perfect How Question'],
    'present_perfect_question': ['Present Perfect Question'],
    'present_perfect_statement': ['Present Perfect Statement'],
    'present_perfect_why_question': ['Present Perfect Why Question'],
    'present_simple_do_question': ['Present Simple Do Question'],
    'present_simple_question': ['Present Simple Question'],
    'present_simple_what_question': ['Present Simple What Question'],
    'present_simple_where_question': ['Present Simple Where Question'],
    'present_tense_question': ['Present Tense Question'],
    'probing': ['Probing'],
    'problem_solving': ['Problem Solving'],
    'prompting': ['Prompting'],
    'pronoun': ['Pronoun'],
    'question_component': ['Question Component'],
    'redirection': ['Redirection'],
    'refocusing': ['Refocusing'],
    'rhetorical': ['Rhetorical'],
    'second_person_pronoun': ['Second Person Pronoun'],
    'she': ['She'],
    'simple_recall': ['Simple Recall'],
    'simple_tense_question': ['Simple Tense Question'],
    'structuring': ['Structuring'],
    'synthesis': ['Synthesis'],
    'tag': ['Tag'],
    'them': ['Them'],
    'they': ['They'],
    'third_person_pronoun': ['Third Person Pronoun'],
    'us': ['Us'],
    'we': ['We'],
    'wh_question': ['Knowledge'],
    'what_is': ['What Is'],
    'what_is_your_question': ['What Is Your Question'],
    'what_question': ['What Question'],
    'when_question': ['When Question'],
    'where_question': ['Where Question'],
    'who_question': ['Who Question'],
    'why_question': ['Why Question'],
    'you': ['You'],
    'your': ['Your'],
    'yourself': ['Yourself']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
