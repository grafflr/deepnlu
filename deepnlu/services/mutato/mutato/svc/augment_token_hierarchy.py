#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Augment Tokens with Descendant and Ancestory Hierarchy for Inference Purposes """


import logging
from pprint import pprint

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer
from baseblock import get_ontology_name

from datablock import FindNER
from datablock import FindSynonyms

from mutato.dmo import ExactMatchFinder
from mutato.dmo import ExactMatchSwapper


class AugmentTokenHierarchy(BaseObject):
    """ Augment Tokens with Descendant and Ancestory Hierarchy for Inference Purposes """

    __slots__ = (
        '_d_lookup_data',
        '_exact_match_swapper',
    )

    def __init__(self,
                 find_types_cb: object,
                 ontology_name: object = None):
        """
        Created:
            14-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/188
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)
        self._find_types = find_types_cb

    def _process(self,
                 tokens: list) -> list:
        for token in tokens:
            token['ancestors'] = self._find_types.ancestors(token['normal'])
            token['descendants'] = self._find_types.descendants(
                token['normal'])

        return tokens

    def process(self,
                tokens: list) -> list:
        Enforcer.is_list(tokens)

        sw = Stopwatch()

        tokens = self._process(tokens)

        self.logger.info('\n'.join([
            "Hierarchy Augmentation Completed",
            f"\tTotal Time: {str(sw)}"]))

        return tokens
