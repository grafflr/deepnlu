#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pformat
from collections import Counter

from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.services.portendo.dto import Markers


class ComputerIncludeOneOf(BaseObject):

    def __init__(self,
                 d_mapping: dict,
                 d_include_oneof: dict):
        """
        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        :param d_include_oneof:
            relevant section of mapping ruleset
        """
        BaseObject.__init__(self, __name__)
        self._mapping = d_mapping
        self._d_include_oneof = d_include_oneof

    def _coverage(self,
                  weight: int,
                  mapping_name: str) -> float:
        """ Determine the Coverage """
        d_mapping = self._mapping[mapping_name][0]['include_one_of']
        total_markers = len(d_mapping)
        return round(weight / total_markers, 2)

    def _weight(self,
                common: set) -> dict:
        c = Counter()
        for marker in common:
            mapping = self._d_include_oneof[marker]
            [c.update({x: 1}) for x in mapping]

        return dict(c)

    def _find_input_tokens(self,
                           d_input_tokens: dict) -> dict:
        s_mapping = set(self._d_include_oneof.keys())
        return s_mapping.intersection(set(d_input_tokens.keys()))

    def process(self,
                d_input_tokens: dict) -> set:

        sw = Stopwatch()
        d_results = {}

        common = self._find_input_tokens(d_input_tokens)

        d_weights = self._weight(common)

        for mapping_name in d_weights:
            weight = d_weights[mapping_name]

            coverage = self._coverage(weight=weight,
                                      mapping_name=mapping_name)

            d_results[mapping_name] = {"weight": weight,
                                       "coverage": coverage}

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Computation Complete: Include One Of",
                f"\tTotal Input Tokens: {len(d_input_tokens)}",
                f"\tTotal Results: {len(d_results)}",
                f"\tTotal Time: {str(sw)}"]))

        if self.isEnabledForDebug and len(d_results):
            self.logger.debug('\n'.join([
                "INCLUDE_ONE_OF Results:",
                f"{pformat(d_results)}"]))

        return d_results
