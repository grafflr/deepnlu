#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find Candidate Span Matches """


import logging

from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.services.mutato.dmo.spans import SpanContentCheck
from deepnlu.services.mutato.dmo.spans import SpanDistanceCheck
from deepnlu.services.mutato.dmo.spans import SpanContextCheck


class SpanMatchFinder(BaseObject):
    """ Find Candidate Span Matches 

    The Span Match Pipeline is documented here
        https://github.com/grafflr/graffl-core/issues/77#issuecomment-947342784 """

    def __init__(self,
                 d_spans: dict,
                 span_keys: list):
        """_summary_

        Created:
            20-Oct-2021
            craig@graffl.ai
            *   renamed from 'perform-sliding-window'
                https://github.com/grafflr/graffl-core/issues/77
        Updated:
            27-May-2022
            craig@graffl.ai
            *   pass in-memory dictionaries in pursuit of
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            d_spans (dict): full dictionary of span data
            span_keys (list): span dictionary keys sorted by length
        """
        BaseObject.__init__(self, __name__)
        self._d_spans = d_spans
        self._span_keys = span_keys

    def _process(self,
                 tokens: list) -> list:

        ## ---------------------------------------------------------- ##
        # Find Candidate Spans via Content Matching
        ## ---------------------------------------------------------- ##
        matching_rules = SpanContentCheck(
            d_rules=self._d_spans,
            rule_keys=self._span_keys).process(tokens)

        if not matching_rules or not len(matching_rules):
            return None

        ## ---------------------------------------------------------- ##
        # Filter Candidate Spans via Distance Analysis
        ## ---------------------------------------------------------- ##
        matching_rules = SpanDistanceCheck(
            d_rules=matching_rules).process(tokens)

        if not matching_rules or not len(matching_rules):
            return None

        ## ---------------------------------------------------------- ##
        # Filter Candidate Spans via Context Analysis
        ## ---------------------------------------------------------- ##
        matching_rules = SpanContextCheck(
            d_rules=matching_rules).process(tokens)

        if not matching_rules or not len(matching_rules):
            return None

        return matching_rules

    def process(self,
                tokens: list) -> list:
        sw = Stopwatch()

        results = self._process(tokens)

        if self.isEnabledForInfo:

            def total_results() -> int:
                if results:
                    return len(results)
                return 0

            self.logger.info('\n'.join([
                "Span Match Finder Completed",
                f"\tTotal Results: {total_results()}",
                f"\tTotal Time: {str(sw)}"]))

        return results
