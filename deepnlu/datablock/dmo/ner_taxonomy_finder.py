# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Interact with the NER Taxonomy """


import os
import pprint
import logging
import importlib.util

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject

from datablock.dmo import GenericDataFinder


class NerTaxonomyFinder(BaseObject):
    """ Interact with the NER Taxonomy """

    def __init__(self,
                 ontologies: list):
        """
        Created:
            8-Nov-2021
            craig@grafflr.ai
            *   in pursuit of 
                https://github.com/grafflr/graffl-core/issues/108
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   enforce ontologies as a list param in domain components
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370
        """
        BaseObject.__init__(self, __name__)
        if type(ontologies) != list:
            raise ValueError('Incorrect DataType')

        self._fwd = GenericDataFinder(
            class_suffix='NerTaxonomy',
            module_suffix='ner_taxonomy',
            ontologies=ontologies)

    def data(self) -> dict:
        return self._fwd.data()

    def is_ner(self,
               input_text: str) -> bool:
        return input_text.upper().strip() in self.data()
