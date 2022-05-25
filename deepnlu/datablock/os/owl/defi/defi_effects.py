
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

class DefiEffects(object):

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
 'time': '2022-04-27 21:15:54.597855'}

    __data = {
    'attacker_node': ['malicious_action'],
    'electronic_payment_system': ['electronic_payment'],
    'ethereum': ['smart_contract'],
    'exchange_platform': ['exchange'],
    'hashing': ['hash'],
    'malicious_action': ['slashing_condition'],
    'payment_system': ['payment'],
    'proof_of_work': ['blockchain'],
    'timestamp_server': ['timestamp']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
