#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from baseblock import Stopwatch
from baseblock import BaseObject

from portendo.dto import Markers
from portendo.dto import ExplainResult
from portendo.dto import MappingResult


class ConfidenceExcludeAllOf(BaseObject):
    """ Determine Confidence Level for Selected Mapping """

    def __init__(self,
                 mapping: dict,
                 markers: Markers,
                 result: MappingResult):
        """
        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        :param d_include_oneof:
            relevant section of mapping ruleset
        """
        BaseObject.__init__(self, __name__)
        self._result = result
        self._mapping = mapping
        self._markers = markers

    def _excludeall(self,
                    confidence: float,
                    mapping: dict) -> float:
        # but do any of these exclusions exist in the mapping?
        exclusions = set(mapping['exclude_all_of'])
        markers = set(self._markers.keys())

        # let's multiply each exclusion by N and deduct from the confidence
        total_matches = len(exclusions.intersection(markers))

        ratio = round((total_matches / len(markers)) * 100, 0)
        if ratio > 80:
            confidence -= 8
        elif ratio > 60:
            confidence -= 16
        elif ratio > 40:
            confidence -= 32
        elif ratio > 20:
            confidence -= 64
        elif ratio > 0:
            confidence -= 90
        else:
            confidence -= 99

        self.logger.debug('\n'.join([
            "Exclude All Of Confidence",
            f"\tExclusions ({len(exclusions)}): {exclusions}",
            f"\tMarkers ({len(markers)}): {markers}",
            f"\tMatches: {total_matches}",
            f"\tRatio: {ratio}"]))

        return confidence

    def process(self) -> float:
        confidence = self._result['confidence']

        mappings = self._mapping[self._result['classification']]

        # at this point, we know the exclusions rule did not apply
        for mapping in mappings:

            if 'exclude_all_of' in mapping:
                confidence = self._excludeall(mapping=mapping,
                                              confidence=confidence)

        return confidence
