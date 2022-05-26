#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Span Matching """


from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer

from deepnlu.datablock.svc import FindNER
from deepnlu.datablock.svc import FindSpans

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

    def __init__(self,
                 ner_finder: FindNER,
                 ontologies: list):
        """ Change History

        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/77
        Updated:
            26-May-2022
            craig@grafflr.ai
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7

        Args:
            ner_finder (FindNER): instantiation of NER finder
            ontologies (list): one-or-more Ontology models to use in processing
        """
        BaseObject.__init__(self, __name__)
        span_finder = FindSpans(ontologies)

        self._span_match_finder = SpanMatchFinder(
            finder=span_finder).process

        self._span_match_swapper = SpanMatchSwapper(
            ner_finder=ner_finder,
            ontologies=ontologies)

    def _process(self,
                 tokens: list) -> list:

        print("TOKENS: ", tokens)

        matching_rules = self._span_match_finder(tokens)
        print("MATCHING RULES: ", matching_rules)
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
