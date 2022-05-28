#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Filter Candidate Span Matches by Distance """


import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject


class SpanDistanceCheck(BaseObject):
    """Filter Candidate Span Matches by Distance

    Phase 2 in
        https://github.com/grafflr/graffl-core/issues/77#issuecomment-947342784

    Steps:
    1.  This component will take a list of candidate rules and consider the distance between tokens for each candidate.
    2.  If the distance exceeds the defined width or the preset default, discard this candidate.
        All long-distance matches that remain are considered candidates.

    The Input Structure looks like this:
        [
            {
                'canon': 'nurse_history',
                'distance': 3,
                'forward': True,
                'reverse': True,
                'content': [
                    'nursing',
                    'history'
                ]
            }
        ]

    -   There will be 1..* rules
    -   Each rule will have a 'content' attribute that lists the required tokens
        in natural order of occurence
    -   If the reverse attribute is set to True, the natural order can be disregarded
    """

    def __init__(self,
                 d_rules: dict):
        """
        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/70
        """
        BaseObject.__init__(self, __name__)
        self._d_rules = d_rules

    def _process(self,
                 tokens: list) -> list:

        d_token_pos = {}
        for i in range(len(tokens)):
            d_token_pos[tokens[i]['normal']] = i

        matching_rules = []
        for d_rule in self._d_rules:

            positions = [d_token_pos[x] for x in d_rule['content']]
            delta = positions[0] - positions[-1]

            if abs(delta) > d_rule['distance']:
                continue

            if delta < 0 and not d_rule['reverse']:
                continue

            if delta > 0 and not d_rule['forward']:
                continue

            # for debug only, but could be used in confidence levels downstream
            d_rule['delta'] = delta

            # used in the synonym swapping stage ...
            d_rule['positions'] = sorted(positions)

            matching_rules.append(d_rule)

        return matching_rules

    def process(self,
                tokens: list) -> list:

        sw = Stopwatch()

        matching_rules = self._process(tokens)

        if self.isEnabledForDebug:

            self.logger.debug('\n'.join([
                "Span Distance Check Complete",
                f"\tTotal Rules: {len(matching_rules)}",
                f"\tTotal Time: {str(sw)}"]))

            self.logger.debug('\n'.join([
                "Span Distance Rules",
                pprint.pformat(matching_rules, indent=4)]))

        return matching_rules
