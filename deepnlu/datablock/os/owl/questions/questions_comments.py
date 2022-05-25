
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

class QuestionsComments(object):

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
 'config': {'classname': 'QuestionsComments',
            'filename': 'questions_comments',
            'queries': ['comments.sparql'],
            'transformers': ['comments']},
 'source': 'questions.owl',
 'time': '2022-05-13 12:06:42.665344'}

    __data = {
    'affective': [   'Affective questions seek to learn how others feel about '
                     "the information they're learning."],
    'analysis': ['Separation of a whole into component parts'],
    'application': [   'Use of facts',
                       'Rules and principles',
                       'Application questions are designed for students to '
                       'apply an idea or principle in a new context to '
                       'demonstrate higher-level learning.'],
    'boolean': [   'Common questions that can be answered with a simple “yes” '
                   'or “no” are logically called yes/no questions. the answer '
                   'can be a brief “yes” or “no.” or',
                   'A longer answer can be given: “yes',
                   'I do.” “no',
                   'I don’t like this country.” the response to a question '
                   'depends on the verb used. try to remember this formula: '
                   'answer the question the way it was asked. if the question '
                   'begins with a form of the verb “to be” – am',
                   'Is',
                   'Are – then answer “yes',
                   'I am/he is/they are',
                   '” or “no',
                   'I am not/he isn’t/they aren’t.”'],
    'choice': [   'Choice questions are questions that offer a choice of '
                  'several options as an answer (you might recognize them from '
                  'your exams as multiple-choice questions). they are made up '
                  'of two parts',
                  'Which are connected by the conjunction or.\n'
                  '\n'
                  'choice questions can be either general',
                  'Open-Ended questions or more specific ones. if the question '
                  'does not center on the subject of the sentence',
                  'A complete answer is needed.\n'
                  '\n'
                  'for example:\n'
                  '1. does she like ice cream or sweets? – she likes ice '
                  'cream.\n'
                  '2. where would you go',
                  'To the cinema or the theatre? – i would go to the cinema.\n'
                  '3. is he a teacher or a student? – he is a student.\n'
                  '\n'
                  'however',
                  'When the question concerns the subject',
                  'The auxiliary verb comes before the second option. the '
                  'answer is short:\n'
                  '1. does she make it or do you? – she does.\n'
                  '2. did they buy that house or did she? – they did.'],
    'clarifying': [   'Clarifying questions help teachers or leaders ensure '
                      'group members understand the current material. they '
                      'also help teachers understand what a student is trying '
                      'to convey through a statement or question.'],
    'close_ended': [   'A question that attempts to limit your answer to a '
                       'choice or confirmation'],
    'comparison': [   'Comparison questions are higher-order questions that '
                      'ask learners to compare two things',
                      'Such as objects',
                      'People',
                      'Ideas',
                      'Stories or theories. they require a thorough '
                      'understanding of the material and the ability to '
                      'identify and describe similarities and differences.'],
    'comprehension': ['Organization and selection of facts and ideas'],
    'convergent': [   'Answers to these types of questions are usually within '
                      'a very finite range of acceptable accuracy. these may '
                      'be at several different levels of cognition — '
                      'comprehension',
                      'Application',
                      'Analysis',
                      'Or ones where the answerer makes inferences or '
                      'conjectures based on personal awareness',
                      'Or on material read',
                      'Presented or known. while these types of questions are '
                      'valuable in exercising mid-level cognitive thinking '
                      'skills',
                      'It is quite easy to expand students’ cognitive '
                      'processes even higher by adding another layer to these '
                      'questions whereby teachers ask students to justify '
                      'their answers in light of the evidence offered or the '
                      'inferences made.',
                      'Convergent questions test knowledge retention by '
                      'requiring a single correct answer or a narrow range of '
                      'acceptable answers. they often start with who',
                      'What',
                      'Where and when.'],
    'critical_awareness': [   'Critical awareness questions: critical '
                              'awareness questions require learners to '
                              'understand and apply information analytically '
                              'to reach a conclusion.'],
    'deductive_inference': [   'Deductive reasoning occurs when you make '
                               'predictions based on generalizations assumed '
                               'to be true. for instance',
                               'If all managers are good leaders',
                               'And all good leaders have strong communication '
                               'skills',
                               'Deductive reasoning tells you that all '
                               'managers have strong communication skills.'],
    'disjunctive': [   'This type of question is also made up of two parts',
                       'Where the first part is a positive statement',
                       'And the second part is negative',
                       'Or vice-versa.\n'
                       '\n'
                       'the first part of the sentence defines the expected '
                       'answer. if the statement is positive',
                       'A positive answer is expected; if the statement is '
                       'negative',
                       'A negative answer is expected.\n'
                       '\n'
                       'for example:\n'
                       '1. she sent him an invitation',
                       'Didn’T she? – yes',
                       'She did.\n2. you aren’t getting married',
                       'Are you? – no',
                       'I am not.\n3. jane isn’t in france',
                       'Is she? – no',
                       'She isn’t.\n4. our dad will come soon',
                       'Won’T he? – yes',
                       'He will.\n'
                       '\n'
                       'there are also exceptions:\n'
                       '1. i am going with you',
                       'Aren’T i? – yes',
                       'You are.\n\nyou can’t say',
                       '“I am a great person',
                       'Am i not?” that would be incorrect. just remember that '
                       'when the pronoun “i” is used',
                       'The tag is are/aren’t.\n'
                       '\n'
                       'tag questions are only used in conversational speech '
                       'to clarify information or to confirm or refute '
                       'something if there are doubts.'],
    'divergent': [   'Divergent questions have no right or wrong answers but '
                     'rather encourage open discussion. they are designed for '
                     'learners to evaluate and analyze information in order to '
                     'formulate their opinion.',
                     'These questions allow students to explore different '
                     'avenues and create many different variations and '
                     'alternative answers or scenarios. correctness may be '
                     'based on logical projections',
                     'May be contextual',
                     'Or arrived at through basic knowledge',
                     'Conjecture',
                     'Inference',
                     'Projection',
                     'Creation',
                     'Intuition',
                     'Or imagination. these types of questions often require '
                     'students to analyze',
                     'Evaluate',
                     'Or synthesize a knowledge base and then project or '
                     'predict different outcomes. answering these types of '
                     'questions may be aided by higher levels of affective '
                     'thinking as well — such as valuing',
                     'Organization',
                     'Or characterization. responses to these types of '
                     'questions generally fall into a wide array of '
                     'acceptability. often correctness is determined '
                     'subjectively based on the possibility or probability of '
                     'the proposed answer. the intent of these types of '
                     'questions is to stimulate imaginative',
                     'Creative',
                     'Or inventive thought',
                     'Or investigate “cause and effect” relationships.'],
    'double_barreled': [   'A question that unfairly assumes two things are '
                           'related'],
    'evaluation': [   'Development of opinions',
                      'Judgments',
                      'Or decisions',
                      'Evaluation questions require students to use their '
                      'knowledge to make value judgments—like ranking or '
                      'ordering—or anticipate future events or outcomes when '
                      'leaders do not provide this information. they require '
                      'information organization and analysis.'],
    'evaluative': [   'These types of questions usually require sophisticated '
                      'levels of cognitive and/or emotional (affective) '
                      'judgment. in attempting to answer these types of '
                      'questions',
                      'Students may be combining multiple cognitive and/or '
                      'affective processes or levels',
                      'Frequently in comparative frameworks. often an answer '
                      'is analyzed at multiple levels and from different '
                      'perspectives before the answerer arrives at newly '
                      'synthesized information or conclusions.'],
    'factual': [   'Soliciting reasonably simple',
                   'Straight forward answers based on obvious facts or '
                   'awareness. these are usually at the lowest level of '
                   'cognitive (thinking) or affective (feeling) processes and '
                   'answers are frequently either right or wrong.'],
    'hypothetical': [   'A question that acknowledges it contains unproven or '
                        'imaginary facts'],
    'inference': [   'Inference questions require learners to use inductive or '
                     'deductive reasoning to eliminate responses or critically '
                     'assess a statement. inductive reasoning is the process '
                     'by which you arrive at a generalization using specific',
                     'Known facts. for instance',
                     'You may decide that',
                     "Because all the people you've hired who live within five "
                     'miles of the company have been successful',
                     'Every person you hire that lives within this boundary '
                     'will be successful. you use what you know to make a '
                     'broader statement that could be true based on the '
                     'facts.'],
    'leading': [   'A question that provides the answer and seeks the '
                   'confirmation'],
    'loaded': [   'A question that contains unjustified assumptions that may '
                  'be used to influence or challenge'],
    'open_ended': [   'A question that seeks an answer with a wide scope.  '
                      'open ended questions encourage a creative response.'],
    'open_present_simple_question': [   'Questions with am - is - are - can - '
                                        'must - have got\n'
                                        '\n'
                                        'are they happy?\n'
                                        'is she a nice girl?\n'
                                        'can you swim?\n'
                                        'have you got a dog?\n'
                                        'where are the children?\n'
                                        'what is the time?\n'
                                        'what can you draw?\n'
                                        'how many stickers have you got?'],
    'organization': [   'Organizational questions ask the student or group '
                        'member to put answer elements in a logical order',
                        'Such as chronologically or greatest to least'],
    'perfect_tense_question': [   'Perfect tense is a category of verb tense '
                                  'used to describe completed actions.'],
    'present_perfect_question': [   'This tense is more common with yes/no '
                                    'questions',
                                    'But there are some times when you can '
                                    'make this tense into “wh-” questions.'],
    'probing': [   "Probing questions are follow-up responses to a student's "
                   'answer. this is another general question type that '
                   'encompasses more specific categories. probing questions '
                   "help leaders understand a student's perspective",
                   'Decipher their meaning and encourage more in-depth '
                   'reasoning.'],
    'problem_solving': [   'Problem-Solving questions present students with a '
                           'scenario or problem and require them to develop a '
                           'solution.'],
    'prompting': [   'Prompting refers to helping learners reach the right '
                     'answer with additional clues or context. for instance',
                     'If a group member cannot answer your question about how '
                     'many product lines your snack company produces',
                     'You might interject by asking how many pantry items you '
                     'sell',
                     'Followed by how many refrigerated items. these probing '
                     'questions can help learners compile fragmented '
                     'information into a single answer.'],
    'redirection': [   'Teachers can involve more participants and help others '
                       'think critically about information by allowing other '
                       'group members to add to',
                       "Object to or clarify another member's answer. for "
                       'instance',
                       "If sharon only remembers two of your company's five "
                       'core values',
                       'You could redirect the discussion by saying something '
                       'like',
                       '"Andrew',
                       'Can you add to sharon\'s answer?"'],
    'refocusing': [   'Group leaders or managers may use refocusing questions '
                      'to help members return to the point of the discussion '
                      'if answers are becoming unrelated or incorrect.'],
    'rhetorical': [   'Rhetorical questions are used to illustrate a point or '
                      'focus attention on an idea or principle and do not '
                      'require a response.'],
    'simple_recall': [   'Factual questions are closed questions that check a '
                         "learner's ability to recite facts."],
    'structuring': [   'Structuring questions are designed to ensure group '
                       'members understand the information being presented. '
                       'they allow learners an opportunity to clarify material '
                       'or ask follow-up questions.'],
    'synthesis': ['Combination of ideas to form a new whole'],
    'tag': [   'Normally you use tag questions to confirm information that you '
               'think is correct. they come at the end of a statement.'],
    'wh_question': [   'Identification and recall of information',
                       '“Who',
                       'What',
                       'When',
                       'Where',
                       'How …?”\n“describe …”',
                       'When you want to get a detailed answer',
                       'Not just yes or no',
                       'You must use a wh- question (or ‘non-polar’ question)',
                       'Which allows for many possible answers. the words who',
                       'Whom',
                       'Whose',
                       'Which',
                       'Why',
                       'And how are used to form this sort of question. these '
                       'words are referred to as wh- words.',
                       'A special question',
                       'As you can guess',
                       'Uses a certain word at the beginning of the sentence '
                       'to ask a specific question. the questions words who',
                       'How',
                       'How many',
                       'Etc.',
                       'Are used to begin the question:']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
