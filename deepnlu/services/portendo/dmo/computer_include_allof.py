#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Compute INCLUDE_ALL_OF Rulesets """


from pprint import pformat


from baseblock import Stopwatch
from baseblock import BaseObject


class ComputerIncludeAllOf(BaseObject):
    """ Compute INCLUDE_ALL_OF Rulesets """

    def __init__(self,
                 d_mapping: dict,
                 d_include_allof: dict):
        """ Initialize Component

        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169

        Args:
            indices (dict): the indexed rule set
        """

        BaseObject.__init__(self, __name__)
        self._mapping = d_mapping
        self._d_include_allof = d_include_allof

    def _find_candidates(self,
                         d_input_tokens: dict) -> list:
        """ Find Candidate Mappings

        Args:
            d_input_tokens (dict): the user input tokens

        Returns:
            list: Candidate matches
        """
        candidates = []
        for marker_name in d_input_tokens.keys():
            if marker_name in self._d_include_allof:
                [candidates.append(x)
                 for x in self._d_include_allof[marker_name]]

        return candidates

    def _filter_candidates(self,
                           candidates: list,
                           d_input_tokens: dict) -> list:
        """ Filter Candidate to find Matches

        Args:
            candidates (list): candidate rule matches
            d_input_tokens (dict): the user input tokens

        Returns:
            list: actual rule matches
        """
        token_names = sorted(set(d_input_tokens.keys()))

        results = []
        for candidate in candidates:

            matches = []
            for term in candidate['terms']:
                matches.append(term in token_names)

            if sum(matches) == len(candidate['terms']):
                results.append(candidate)

        return results

    def _to_final_result(self,
                         candidates: list) -> dict:
        """ Create a Compatible Result Structure

        Args:
            candidates (list): candidate rule matches

        Returns:
            dict: a final data structure
        """

        d = {}
        for candidate in candidates:
            for mapping in candidate['mappings']:
                weight = 1 + len(candidate['terms'])
                coverage = 100.0  # coverage is always 100% for include-all-of by design
                d[mapping] = {"weight": weight, "coverage": coverage}

        return d

    def process(self,
                d_input_tokens: dict) -> dict:
        sw = Stopwatch()

        candidates = self._find_candidates(d_input_tokens)
        candidates = self._filter_candidates(candidates=candidates,
                                             d_input_tokens=d_input_tokens)

        d_results = self._to_final_result(candidates)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Computation Complete: Include All Of",
                f"\tTotal Input Tokens: {len(d_input_tokens)}",
                f"\tTotal Results: {len(d_results)}",
                f"\tTotal Time: {str(sw)}"]))

        if self.isEnabledForDebug and len(d_results):
            self.logger.debug('\n'.join([
                "INCLUDE_ALL_OF Results:",
                f"{pformat(d_results)}"]))

        return d_results
