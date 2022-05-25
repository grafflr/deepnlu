
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

class DefiNerTaxonomyRev(object):

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
 'config': {'classname': 'DefiNerTaxonomy',
            'filename': 'defi_ner_taxonomy',
            'queries': ['ner-taxonomy.sparql % $PREFIX=defi $NER_1=spacyNER '
                        '$NER_2=grafflNER'],
            'reverse': True,
            'transformers': ['ner_taxonomy']},
 'source': 'defi.owl',
 'time': '2022-04-27 21:15:54.784857'}

    __data = {
 }

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
