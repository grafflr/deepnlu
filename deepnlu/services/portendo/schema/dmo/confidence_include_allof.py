#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pprint

from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.services.portendo.schema.dto import Markers
from deepnlu.services.portendo.schema.dto import ExplainResult
from deepnlu.services.portendo.schema.dto import MappingResult


class ConfidenceIncludeAllOf(BaseObject):
    """ Determine Confidence Level for Selected Mapping """

    def __init__(self,
                 mapping: dict,
                 markers: Markers):
        """
        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        :param d_include_oneof:
            relevant section of mapping ruleset
        """
        BaseObject.__init__(self, __name__)
        self._mapping = mapping
        self._markers = markers

    @staticmethod
    def _max_confidence(d: dict) -> dict:
        """
        Sample Input
            {   23.0: { 'classification': 'GICS_CODE_50102010_2',
                        'confidence': 23.0,
                        'explain': <ExplainResult.INCLUDE_NEAR_MATCH_1: 30>},
                35.0: { 'classification': 'GICS_CODE_25302020_2',
                        'confidence': 35.0,
                        'explain': <ExplainResult.INCLUDE_NEAR_MATCH_1: 30>},
                85.0: { 'classification': 'GICS_CODE_50101020_3',
                        'confidence': 85.0,
                        'explain': <ExplainResult.INCLUDE_NEAR_MATCH_1: 30>}}
        Sample Output:
            {   'classification': 'GICS_CODE_50101020_3',
                'confidence': 85.0,
                'explain': <ExplainResult.INCLUDE_NEAR_MATCH_1: 30>}
        """
        return d[max(d)]

    def process(self) -> MappingResult or None:
        confidence = 100.0

        d = {}

        for k in self._mapping:
            for mapping in self._mapping[k]:
                if 'include_all_of' in mapping:

                    # mapping-supplied
                    map_tags = set(mapping['include_all_of'])
                    usr_tags = set(self._markers.keys())  # user supplied

                    matches = map_tags.intersection(usr_tags)

                    total_matches = len(matches)
                    if total_matches == 0:
                        continue

                    total_map_tags = len(map_tags)
                    total_usr_tags = len(usr_tags)

                    def compute() -> float:
                        base = 5.00
                        boost = ((base - total_map_tags) * base) / 100
                        confidence = (total_matches / total_map_tags) - boost
                        confidence = round(confidence * 100, 0)

                        if confidence > 100:
                            return 99
                        if confidence < 1:
                            return 0

                        return confidence

                    confidence = compute()
                    self.logger.debug('\n'.join([
                        "Include All Confidence Computation",
                        f"\tClassification: {k}",
                        f"\tUser Tags ({total_usr_tags}): {usr_tags}",
                        f"\tMapping Tags ({total_map_tags}): {map_tags}",
                        f"\tMatches ({total_matches}): {matches}",
                        f"\tConfidence: {confidence}"]))

                    if confidence == 0:
                        continue

                    d[confidence] = MappingResult(confidence=confidence,
                                                  classification=k,
                                                  explain=ExplainResult.INCLUDE_NEAR_MATCH_1)

        pprint.pprint(d)
        raise ValueError()

        if not len(d):
            return None

        return self._max_confidence(d)
        # return d[max(d, key=d.get)]
