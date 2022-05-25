
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

class DefiEffectsRev(object):

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
 'config': {'classname': 'DefiEffects',
            'filename': 'defi_effects',
            'queries': ['effects.sparql % $PREFIX=defi'],
            'reverse': True,
            'transformers': ['effects']},
 'source': 'defi.owl',
 'time': '2022-04-27 21:15:54.599355'}

    __data = {
    'blockchain': ['proof_of_work'],
    'electronic_payment': ['electronic_payment_system'],
    'exchange': ['exchange_platform'],
    'hash': ['hashing'],
    'malicious_action': ['attacker_node'],
    'payment': ['payment_system'],
    'slashing_condition': ['malicious_action'],
    'smart_contract': ['ethereum'],
    'timestamp': ['timestamp_server']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
