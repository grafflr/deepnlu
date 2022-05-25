#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Score Candidate Mapping Results """


from pprint import pprint
from collections import defaultdict

from baseblock import Stopwatch
from baseblock import BaseObject


class MappingScoreCandidates(BaseObject):
    """ Score Candidate Mapping Results """

    __slots__ = (
        '_results',
    )

    def __init__(self,
                 results: dict,
                 scoring: object):
        """
        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        Created:
            10-Feb-2022
            craig@grafflr.ai
            *   integrate scoring dictionary
                https://github.com/grafflr/graffl-core/issues/176
        """
        BaseObject.__init__(self, __name__)
        self._results = results
        self._scoring = scoring

    def _score(self,
               category: str,
               d_result: dict) -> int:

        def compute() -> float:
            confidence = 100.0

            # Deductions for Low Coverage
            # confidence -= (1 - d_result['coverage'])

            # Deductions for Recursion
            if d_result['recursion'] == 1:
                confidence -= 12
            elif d_result['recursion'] == 2:
                confidence -= 25
            elif d_result['recursion'] >= 3:
                confidence -= 50

            confidence += self._scoring(category)

            # Deductions (or Increases) for Weight (weighted coverage)
            if d_result['weight'] > 3:
                confidence += (d_result['weight'] - 3) * 1.1
            elif d_result['weight'] < 3:
                confidence -= (3 - d_result['weight']) * 1.2

            return round(confidence)

        def bound(confidence: float) -> int:
            if confidence > 100:
                return 100
            if confidence < 0:
                return 0
            return int(confidence)

        return bound(compute())

    def process(self,
                d_results: dict) -> int:
        for k in d_results:
            d_results[k]["score"] = self._score(k,
                                                d_results[k])

        return d_results
