#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Exclude Candidates that contain pre-swapped tokens """


import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject


class SlidingWindowExcludeSwaps(BaseObject):
    """ Exclude Candidates that contain pre-swapped tokens """

    def __init__(self,
                 candidates: list):
        """
        Created:
            8-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/15#issuecomment-939224476
        """
        BaseObject.__init__(self, __name__)
        self._candidates = candidates

    def _process(self) -> list:
        results = []

        for candididate in self._candidates:

            def has_swap() -> bool:
                for token in candididate:
                    if 'swaps' in token:
                        return True
                return False

            if not has_swap():
                results.append(candididate)

        return results

    def process(self) -> list:
        sw = Stopwatch()

        results = self._process()

        if self.isEnabledForDebug:

            self.logger.debug('\n'.join([
                "Sliding Window Swap Exclusion Completed",
                f"\tTotal Tokens: {len(results)}",
                f"\tTotal Time: {str(sw)}"]))

            if self._candidates != results:
                self.logger.debug('\n'.join([
                    "Sliding Window Swap Exclusion",
                    f"\tTokens: {pprint.pformat(results, indent=4)}"]))

        return results
