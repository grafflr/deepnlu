#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Filter Candidate Span Matches by Context """


import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject


class SpanContextCheck(BaseObject):
    """Filter Candidate Span Matches by Context

    Phase 3 in
        https://github.com/grafflr/graffl-core/issues/77#issuecomment-947342784

    Notes:
    -   Each candidate may optionally have a context that is required for the match.

    -   For example, this rule
            alpha+beta!gamma

        implies that alpha and beta can form a long-distance match, 
            but for this match to be valid, 
                'gamma' is a token that must be found in the context
    """

    def __init__(self,
                 d_rules: dict):
        """
        Created:
            20-Oct-2021
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/70
        """
        BaseObject.__init__(self, __name__)
        self._d_rules = d_rules

    def _process(self,
                 tokens: list) -> list:

        normal = None

        matching_rules = []
        for d_rule in self._d_rules:

            def has_context_requirement() -> bool:
                if 'context' not in d_rule:
                    return False
                if not len(d_rule['context']):
                    return False
                return True

            if not has_context_requirement():
                matching_rules.append(d_rule)
                continue

            if not normal:
                normal = [x['normal'] for x in tokens]

            def has_context_match() -> bool:
                for token in d_rule['context']:
                    if token not in normal:
                        return False

                return True

            if has_context_match():
                matching_rules.append(d_rule)

        return matching_rules

    def process(self,
                tokens: list) -> list:

        sw = Stopwatch()

        matching_rules = self._process(tokens)

        if self.isEnabledForDebug:

            self.logger.debug('\n'.join([
                "Span Context Check Complete",
                f"\tTotal Rules: {len(matching_rules)}",
                f"\tTotal Time: {str(sw)}"]))

            self.logger.debug('\n'.join([
                "Span Context Rules",
                pprint.pformat(matching_rules, indent=4)]))

        return matching_rules
