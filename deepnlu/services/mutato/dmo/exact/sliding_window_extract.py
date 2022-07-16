#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract Tokens using a Sliding Window Algorithm """


import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject


class SlidingWindowExtract(BaseObject):
    """ Extract Tokens using a Sliding Window Algorithm """

    def __init__(self,
                 tokens: list,
                 gram_size: int):
        """
        Created:
            6-Oct-2021
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/5
        """
        BaseObject.__init__(self, __name__)
        self._tokens = tokens
        self._gram_size = gram_size

    def _process(self) -> list:
        results = []
        tokens = self._tokens

        if self._gram_size == len(tokens):
            return [tokens]

        if self._gram_size == 1:
            return [[x] for x in tokens]

        x = 0
        y = x + self._gram_size

        while y <= len(tokens):
            results.append(tokens[x: y])

            x += 1
            y = x + self._gram_size

        return results

    def process(self) -> list:
        sw = Stopwatch()

        results = self._process()

        if self.isEnabledForDebug:

            self.logger.debug('\n'.join([
                "Sliding Window Extract Completed",
                f"\tGram Size: {self._gram_size}",
                f"\tTotal Tokens: {len(results)}",
                f"\tTotal Time: {str(sw)}"]))

            if self._tokens != results:
                self.logger.debug('\n'.join([
                    "Sliding Window Extract Results",
                    f"\tTokens: {pprint.pformat(results, indent=4)}"]))

        return results
