#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Select Best Candidates """


import pprint
from collections import defaultdict

from baseblock import Stopwatch
from baseblock import BaseObject


class MappingSelectCandidates(BaseObject):
    """ Select 1..* Best Candidates as the Final Result """

    def __init__(self,
                 results: dict):
        """
        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        """
        BaseObject.__init__(self, __name__)
        self._results = results

    @staticmethod
    def _max_results(d_results: dict) -> list:
        """
        Sample Input:
            {   'GICS_CODE_40102010#2': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
                'GICS_CODE_4020': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
                'GICS_CODE_40301010#2': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
                'GICS_CODE_40301040#2': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
                'GICS_CODE_40301040#3': {'coverage': 0.5, 'recursion': 0, 'weight': 1}}
        Sample Output:
            [   ('GICS_CODE_4020', {'coverage': 0.5, 'recursion': 0, 'score': 62, 'weight': 1}),
                ('GICS_CODE_40102010#2', {'coverage': 0.5, 'recursion': 0, 'score': 62, 'weight': 1}),
                ('GICS_CODE_40301010#2', {'coverage': 0.5, 'recursion': 0, 'score': 62, 'weight': 1}),
                ('GICS_CODE_40301040#3', {'coverage': 0.5, 'recursion': 0, 'score': 62, 'weight': 1}) ]
        """
        d_idx = defaultdict(list)

        for k in d_results:
            d_idx[d_results[k]['score']].append((k, d_results[k]))

        if not len(d_idx):
            return []

        return d_idx[max(d_idx)]

    def process(self,
                d_results: dict) -> int:

        max_results = self._max_results(d_results)

        final_results = []
        for result in max_results:
            final_results.append({"classification": result[0],
                                  "confidence": result[1]['score']})

        return final_results
