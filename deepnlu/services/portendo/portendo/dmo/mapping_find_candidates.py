#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find Candidate Mapping Results """


import pprint
from collections import defaultdict

from baseblock import Stopwatch
from baseblock import BaseObject


class MappingFindCandidates(BaseObject):
    """ Find Candidate Mapping Results """

    __include_keys = [
        'include_one_of',
        'include_all_of',
        'startswith',
        # 'include_r1',
        # 'include_r2'
    ]

    __exclude_keys = [
        'exclude_one_of',
        'exclude_all_of'
    ]

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

    def _consolidate(self,
                     diff: set) -> dict:
        """ Create a Consolidated Dictionary
        Sample Input ('diff'):
            [   "GICS_CODE_50101020_3", "GICS_CODE_25401030_1"]
        Sample Output:
            {   'GICS_CODE_25401030_1': {'coverage': 0.17, 'weight': 1, 'recursion': 0},
                'GICS_CODE_50101020_3': {'coverage': 100.0, 'weight': 2, 'recursion': 0} }
        """
        d_result = {}

        def update(d_map: dict) -> None:
            for k in d_map:
                if k in diff:

                    def recursion_level() -> int:
                        """ Level of Recursion for Mapping
                            more recursion == less confidence """
                        # if k in self._results['include_r1']:
                        #     return 1
                        # if k in self._results['include_r2']:
                        #     return 2
                        return 0

                    inner_map = d_map[k]

                    # Add Recursion Level
                    inner_map["recursion"] = recursion_level()

                    d_result[k] = inner_map

        update(self._results['include_one_of'])
        update(self._results['include_all_of'])
        update(self._results['startswith'])
        # update(self._results['include_r1'])
        # update(self._results['include_r2'])

        return d_result

    def process(self) -> dict:
        """ Join Include and Exclude results to find Candidate Mappings """

        include = set()
        for include_key in self.__include_keys:
            [include.add(x) for x in self._results[include_key]]

        exclude = set()
        for exclude_key in self.__exclude_keys:
            [exclude.add(x) for x in self._results[exclude_key]]

        diff = include.difference(exclude)

        d_consolidated = self._consolidate(diff)

        self.logger.debug('\n'.join([
            "Located Candidate Mappings",
            f"\tInclude: {include}",
            f"\tExclude: {exclude}",
            f"\tDifference: {diff}"]))

        return d_consolidated
