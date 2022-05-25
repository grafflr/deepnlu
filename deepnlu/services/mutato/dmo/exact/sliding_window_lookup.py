#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Filter Extracted Candidate against known KBs """


import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject


class SlidingWindowLookup(BaseObject):
    """ Filter Extracted Candidate against known KBs """

    def __init__(self,
                 candidates: list,
                 gram_size: int,
                 d_runtime_kb: dict):
        """
        Created:
            8-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/14#issuecomment-939029052
        """
        BaseObject.__init__(self, __name__)
        self._gram_size = gram_size
        self._candidates = candidates
        self._d_runtime_kb = d_runtime_kb[self._gram_size]

    def _process(self) -> list:
        filtered = []
        for token in self._candidates:
            normal = ' '.join([x['normal'] for x in token]).lower()

            if normal in self._d_runtime_kb:
                filtered.append(token)

        return filtered

    def process(self) -> list:
        sw = Stopwatch()

        results = self._process()

        if self.logger.isEnabledFor(logging.DEBUG):

            self.logger.debug('\n'.join([
                "Sliding Window Lookup Completed",
                f"\tGram Size: {self._gram_size}",
                f"\tTotal Tokens: {len(results)}",
                f"\tTotal Time: {str(sw)}"]))

            if self._candidates != results:
                self.logger.debug('\n'.join([
                    "Sliding Window Lookup Results",
                    f"\tTokens: {pprint.pformat(results, indent=4)}"]))

        return results
