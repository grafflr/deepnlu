
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

class QuestionsSynonyms(object):

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
 'config': {'classname': 'QuestionsSynonyms',
            'filename': 'questions_synonyms',
            'files': ['questions.txt'],
            'queries': ['synonyms.sparql'],
            'reverse': True,
            'transformers': ['lowercase', 'synonyms']},
 'source': 'questions.owl',
 'time': '2022-05-13 12:06:42.616340'}

    __data = {
    'affective': ['affective'],
    'analysis': ['analysis'],
    'application': ['application'],
    'boolean': [   'general question',
                   'yes/no question',
                   'polar question',
                   'boolean'],
    'choice': ['choice'],
    'clarifying': ['clarifying'],
    'close_ended': ['close ended'],
    'closed_present_simple_do_question': ['closed present simple do question'],
    'closed_present_simple_question': ['closed present simple question'],
    'comparison': ['comparison'],
    'comprehension': ['comprehension'],
    'continuous_question': ['continuous question'],
    'convergent': ['convergent'],
    'critical_awareness': ['critical awareness'],
    'deductive_inference': ['deductive inference'],
    'disjunctive': ['tag question', 'disjunctive'],
    'divergent': ['divergent'],
    'do_question': ['do question'],
    'double_barreled': ['double barreled'],
    'evaluation': ['evaluation'],
    'evaluative': ['evaluative'],
    'factual': ['factual'],
    'first_person_pronoun': ['first person pronoun'],
    'future_continuous_question': ['future continuous question'],
    'future_continuous_where_question': ['future continuous where question'],
    'future_continuous_why_question': ['future continuous why question'],
    'future_pefect_why_question': ['future pefect why question'],
    'future_perfect_continuous_how_question': [   'future perfect continuous '
                                                  'how question'],
    'future_perfect_continuous_question': [   'future perfect continuous '
                                              'question'],
    'future_perfect_question': ['future perfect question'],
    'future_perfect_statement': ['future perfect statement'],
    'future_perfect_when_question': ['future perfect when question'],
    'future_simple_how_question': ['future simple how question'],
    'future_simple_question': ['future simple question'],
    'future_simple_when_question': ['future simple when question'],
    'future_simple_where_question': ['future simple where question'],
    'future_tense_question': ['future tense question'],
    'he': ['he'],
    'her': ['her'],
    'him': ['him'],
    'how_question': ['how question'],
    'hypothetical': ['hypothetical'],
    'i': ['i'],
    'inference': ['inference'],
    'it': ['it'],
    'leading': ['leading'],
    'loaded': ['loaded'],
    'me': ['me'],
    'mine': ['mine'],
    'my': ['my'],
    'myself': ['myself'],
    'open_ended': ['open question', 'open ended'],
    'open_present_simple_how_question': ['open present simple how question'],
    'open_present_simple_question': ['open present simple question'],
    'open_present_simple_what_question': ['open present simple what question'],
    'open_present_simple_when_question': ['open present simple when question'],
    'open_present_simple_where_question': [   'open present simple where '
                                              'question'],
    'open_present_simple_who_question': ['open present simple who question'],
    'open_present_simple_why_question': ['open present simple why question'],
    'organization': ['organization'],
    'our': ['our'],
    'ourselves': [   "one's self",
                     'ones self',
                     'ourselves',
                     'onesself',
                     'ourself'],
    'past_continuous_question': ['past continuous question'],
    'past_continuous_what_question': ['past continuous what question'],
    'past_continuous_where_question': ['past continuous where question'],
    'past_continuous_why_question': ['past continuous why question'],
    'past_perfect_continuous_how_question': [   'past perfect continuous how '
                                                'question'],
    'past_perfect_continuous_question': ['past perfect continuous question'],
    'past_perfect_continuous_what_question': [   'past perfect continuous what '
                                                 'question'],
    'past_perfect_continuous_why_question': [   'past perfect continuous why '
                                                'question'],
    'past_perfect_how_question': ['past perfect how question'],
    'past_perfect_question': ['past perfect question'],
    'past_perfect_statement': ['past perfect statement'],
    'past_perfect_when_question': ['past perfect when question'],
    'past_perfect_why_question': ['past perfect why question'],
    'past_simple_how_question': ['past simple how question'],
    'past_simple_question': ['past simple question'],
    'past_simple_when_question': ['past simple when question'],
    'past_simple_who_question': ['past simple who question'],
    'past_simple_why_question': ['past simple why question'],
    'past_tense_question': ['past tense question'],
    'perfect_continuous_question': ['perfect continuous question'],
    'perfect_tense_question': ['perfect tense question', 'complete tense'],
    'present_continuous_question': ['present continuous question'],
    'present_continuous_what_question': ['present continuous what question'],
    'present_continuous_who_question': ['present continuous who question'],
    'present_continuous_why_question': ['present continuous why question'],
    'present_perfect_continuous_question': [   'present perfect continuous '
                                               'question'],
    'present_perfect_continuous_where_question': [   'present perfect '
                                                     'continuous where '
                                                     'question'],
    'present_perfect_continuous_why_question': [   'present perfect continuous '
                                                   'why question'],
    'present_perfect_how_question': ['present perfect how question'],
    'present_perfect_question': ['present perfect question'],
    'present_perfect_statement': ['present perfect statement'],
    'present_perfect_why_question': ['present perfect why question'],
    'present_simple_do_question': ['present simple do question'],
    'present_simple_question': ['present simple question'],
    'present_simple_what_question': ['present simple what question'],
    'present_simple_where_question': ['present simple where question'],
    'present_tense_question': ['present tense question'],
    'probing': ['probing'],
    'problem_solving': ['problem-solving', 'problem solving'],
    'prompting': ['prompting'],
    'pronoun': ['pronoun'],
    'question_component': ['question component'],
    'redirection': ['redirection'],
    'refocusing': ['refocusing'],
    'rhetorical': ['rhetorical'],
    'second_person_pronoun': ['second person pronoun'],
    'she': ['she'],
    'simple_recall': ['recall question', 'simple recall'],
    'simple_tense_question': ['simple tense question'],
    'structuring': ['structuring'],
    'synthesis': ['synthesis'],
    'tag': ['tag'],
    'them': ['them'],
    'they': ['they'],
    'third_person_pronoun': ['third person pronoun'],
    'us': ['us'],
    'we': ['we'],
    'wh_question': ['special question', 'wh question', 'knowledge'],
    'what_is': ['what is', "what's"],
    'what_is_your_question': ['what is your question', 'what is your'],
    'what_question': ['what question'],
    'when_question': ['when question'],
    'where_question': ['where question'],
    'who_question': ['who question'],
    'why_question': ['why question'],
    'you': ['you'],
    'your': ['yours', 'your'],
    'yourself': ['yourself']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
