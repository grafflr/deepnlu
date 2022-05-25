#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Span Matching """




import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer
from baseblock import get_ontology_name

from datablock.svc import FindNER
from datablock.svc import FindSpans
from datablock.svc import FindSynonyms

from deepnlu.services.mutato.dmo import SpanMatchFinder
from deepnlu.services.mutato.dmo import SpanMatchSwapper


class PerformSpanMatching(BaseObject):
    """Perform Span Matching

    Sample Input:
        the history of nursing

    Sample Rule:
        nursing_history ~ nurse+history

    Sample Match:
        "history of nursing" == nursing_history

    Sample Output:
        the nursing_history
    """

    __slots__ = (
        '_span_match_finder',
        '_span_match_swapper',
    )

    def __init__(self,
                 ner_finder: FindNER,
                 syn_finder: FindSynonyms,
                 ontology_name: object = None):
        """
        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/77
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)
        span_finder = FindSpans(ontologies)

        self._span_match_finder = SpanMatchFinder(
            finder=span_finder).process

        self._span_match_swapper = SpanMatchSwapper(
            ner_finder=ner_finder,
            ontologies=ontologies)

    def _process(self,
                 tokens: list) -> list:

        print ("TOKENS: ", tokens)

        matching_rules = self._span_match_finder(tokens)
        print ("MATCHING RULES: ", matching_rules)
        if not matching_rules or not len(matching_rules):
            return tokens

        tokens = self._span_match_swapper.process(
            tokens=tokens,
            matching_rules=matching_rules)

        return tokens

    def process(self,
                tokens: list) -> list:

        if self.isEnabledForInfo:
            sw = Stopwatch()
            Enforcer.is_list(tokens)

        swaps = self._process(tokens)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Span Swapping Completed",
                f"\tTotal Time: {str(sw)}"]))

        return swaps
