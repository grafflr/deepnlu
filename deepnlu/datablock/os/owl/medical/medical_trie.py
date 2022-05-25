
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

class MedicalTrie(object):

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
 'config': {'classname': 'MedicalTrie',
            'filename': 'medical_trie',
            'queries': ['trie.sparql'],
            'transformers': ['lowercase', 'trie']},
 'source': 'medical.owl',
 'time': '2022-04-27 21:15:55.983355'}

    __data = {
    1: [   'cytomegalovirus',
           'transfusion',
           'transplant',
           'intestines',
           'infection',
           'discharge',
           'esophagus',
           'symptom',
           'hearing',
           'healthy',
           'illness',
           'toddler',
           'stomach',
           'tongue',
           'spleen',
           'infect',
           'severe',
           'person',
           'breast',
           'saliva',
           'muscle',
           'artery',
           'urine',
           'semen',
           'happy',
           'brain',
           'taste',
           'organ',
           'touch',
           'liver',
           'gland',
           'birth',
           'blood',
           'smell',
           'child',
           'tears',
           'sight',
           'lung',
           'mild',
           'nose',
           'baby',
           'ear',
           'eye'],
    2: [   'quantifiable',
           'qualifiable',
           'parathyroid',
           'congenital',
           'emotional',
           'pituitary',
           'physical',
           'skeletal',
           'hearing',
           'medical',
           'mammary',
           'adrenal',
           'healthy',
           'health',
           'breast',
           'vision',
           'mental',
           'immune',
           'bodily',
           'short',
           'taste',
           'blood',
           'fluid',
           'organ',
           'young',
           'weak',
           'long'],
    3: ['quantified', 'qualified', 'state'],
    4: [],
    5: [],
    6: []}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
