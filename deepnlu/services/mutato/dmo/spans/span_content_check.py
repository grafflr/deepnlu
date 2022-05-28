#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find Candidate Span Matches """


import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject


class SpanContentCheck(BaseObject):
    """ Find Candidate Span Matches

    Phase 1 in
        https://github.com/grafflr/graffl-core/issues/77#issuecomment-947342784
    """

    def __init__(self,
                 d_rules: dict,
                 rule_keys: set):
        """
        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/70
        Updated:
            25-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/75
        """
        BaseObject.__init__(self, __name__)
        self._d_rules = d_rules
        self._rule_keys = rule_keys

    def _process(self,
                 tokens: list) -> list:
        token_keys = {x['normal'] for x in tokens}
        common = token_keys.intersection(self._rule_keys)

        if not len(common):
            return []

        matching_rules = []

        for key in common:
            for d_rule in self._d_rules[key]:

                content = set(d_rule['content']).intersection(token_keys)
                if len(content) == len(d_rule['content']):
                    d_rule['content'] = [key] + list(d_rule['content'])
                    matching_rules.append(d_rule)

        return matching_rules

    def process(self,
                tokens: list) -> list:

        sw = Stopwatch()

        matching_rules = self._process(tokens)

        if self.isEnabledForDebug:

            self.logger.debug('\n'.join([
                "Span Content Check Complete",
                f"\tTotal Rules: {len(matching_rules)}",
                f"\tTotal Time: {str(sw)}"]))

            self.logger.debug('\n'.join([
                "Span Content Rules",
                pprint.pformat(matching_rules, indent=4)]))

        return matching_rules
