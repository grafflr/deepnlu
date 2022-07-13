#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Remove Duplicate Mappings """


import pprint
from collections import defaultdict

from baseblock import Stopwatch
from baseblock import BaseObject


class MappingRemoveDuplicates(BaseObject):
    """ Find and Remove Duplicate Mappings

    Sample Input:
        {   'GICS_CODE_40102010#2': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
            'GICS_CODE_4020': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
            'GICS_CODE_40301010#2': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
            'GICS_CODE_40301040#2': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
            'GICS_CODE_40301040#3': {'coverage': 0.5, 'recursion': 0, 'weight': 1}}

    Duplicates Detected:
        {   'GICS_CODE_40301040': ['GICS_CODE_40301040#2', 'GICS_CODE_40301040#3']}

    Sample Output:
        {   'GICS_CODE_40102010_2': {'coverage': 0.5, 'weight': 1},
            'GICS_CODE_4020': {'coverage': 0.5, 'weight': 1},
            'GICS_CODE_40301010_2': {'coverage': 0.5, 'weight': 1},
            'GICS_CODE_40301040_2': {'coverage': 0.5, 'weight': 1}}
    """

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
    def _normalize(name: str) -> str:
        """ Normalize Mapping
        Sample Input:
            GICS_CODE_35102015#2
        Sample Output:
            GICS_CODE_35102015
        """
        if '#' in name:
            return name.split('#')[0].strip()
        return name

    def _index_by_name(self,
                       d_results: dict) -> dict:
        """ Index Mapping by (logical) Name to find Duplicates

        Sample Input:
            {   'GICS_CODE_40102010#2': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
                'GICS_CODE_4020': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
                'GICS_CODE_40301010#2': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
                'GICS_CODE_40301040#2': {'coverage': 0.5, 'recursion': 0, 'weight': 1},
                'GICS_CODE_40301040#3': {'coverage': 0.5, 'recursion': 0, 'weight': 1}}

        Sample Output:
            {   'GICS_CODE_40301040': ['GICS_CODE_40301040#2', 'GICS_CODE_40301040#3']}
        """

        d_idx = defaultdict(list)
        for k in d_results:
            d_idx[self._normalize(k)].append(k)

        d_idx = {k: sorted(d_idx[k]) for k in d_idx
                 if len(d_idx[k]) > 1}

        return d_idx

    def _find_discards(self,
                       d_results: dict,
                       d_idx_by_name: dict) -> dict:
        """ Find Lowest Scored Mappings (discards)

        Sample Input:
            {   'GICS_CODE_40301040': ['GICS_CODE_40301040#2', 'GICS_CODE_40301040#3']}

        d_idx_by_score:
            {   62: 'GICS_CODE_40301040#3' }

        Sample Output ('keep'):
            [  GICS_CODE_40301040#3 ]
        """
        results = set()

        for name in d_idx_by_name:

            # Index Duplicates by Score (map to int:str)
            d_idx_by_score = {d_results[k]['score']: k
                              for k in d_idx_by_name[name]}

            # Highest Scored Mapping
            max_mapping = d_idx_by_score[max(d_idx_by_score)]

            # Discard all other Mappings
            discards = [x for x in d_idx_by_name[name] if x != max_mapping]

            # Add to result set
            [results.add(x) for x in discards]

        return results

    def process(self,
                d_results: dict):

        # No Duplicates Possible
        if len(d_results) == 1:
            return d_results

        d_idx_by_name = self._index_by_name(d_results)

        # No Duplicates Detected
        if not len(d_idx_by_name):
            return d_results

        # Identify Discards
        discards = self._find_discards(d_results=d_results,
                                       d_idx_by_name=d_idx_by_name)

        # Minimize Scoring on Discards
        for k in d_results:
            if k in discards:
                d_results[k]["score"] = 0

        return d_results
