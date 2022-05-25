#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Filter Extracted Candidate Sequences """


import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject


class SlidingWindowBlacklist(BaseObject):
    """ Filter Extracted Candidate Sequences """

    def __init__(self,
                 candidates: list,
                 gram_size: int,
                 blacklist: list):
        """
        Created:
            8-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/14#issuecomment-939029052
        """
        BaseObject.__init__(self, __name__)
        self._gram_size = gram_size
        self._blacklist = blacklist
        self._candidates = candidates

    def _process(self) -> list:
        filtered = []

        for candidate in self._candidates:

            normalized_text = ' '.join([x['normal']
                                        for x in candidate]).strip().lower()
            if normalized_text not in self._blacklist:
                filtered.append(candidate)

        return filtered

    def process(self) -> list:
        sw = Stopwatch()

        results = self._process()

        if self.logger.isEnabledFor(logging.DEBUG):

            self.logger.debug('\n'.join([
                "Sliding Window Blacklist Completed",
                f"\tGram Size: {self._gram_size}",
                f"\tTotal Time: {str(sw)}"]))

            if self._candidates != results:
                self.logger.debug('\n'.join([
                    "Sliding Window Blacklist Results",
                    f"\tTokens: {pprint.pformat(results, indent=4)}"]))

        return results
