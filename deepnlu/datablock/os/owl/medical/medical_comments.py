
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

class MedicalComments(object):

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
 'config': {'classname': 'MedicalComments',
            'filename': 'medical_comments',
            'queries': ['comments.sparql'],
            'transformers': ['comments']},
 'source': 'medical.owl',
 'time': '2022-04-27 21:15:55.999355'}

    __data = {
    'affect': [   'Describes an impactful relationship\n'
                  '\n'
                  'a impacts b\n'
                  'a affects b'],
    'congenital_cytomegalovirus': [   'When a baby is born with '
                                      'cytomegalovirus (cmv) infection',
                                      'It is called congenital cmv. about one '
                                      'out of every 200 babies is born with '
                                      'congenital cmv infection.  about one in '
                                      'five babies with congenital cmv '
                                      'infection will have long-term health '
                                      'problems.'],
    'cytomegalovirus': [   'Cytomegalovirus (pronounced '
                           'sy-toe-meg-a-low-vy-rus)',
                           'Or cmv',
                           'Is a common virus that infects people of all ages. '
                           'over half of adults have been infected with cmv by '
                           'age 40. most people infected with cmv show no '
                           'signs or symptoms.'],
    'effect': [   'Use for causation\n'
                  '\n'
                  'until further decomposition proves necessary',
                  'The causation may be indisputable',
                  'Possible or probable']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
