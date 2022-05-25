#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Choose the Best Mapping """


from baseblock import Enforcer
from baseblock import BaseObject

from portendo.dmo import MappingFindCandidates
from portendo.dmo import MappingRemoveDuplicates
from portendo.dmo import MappingScoreCandidates
from portendo.dmo import MappingSelectCandidates

from portendo.dto import MappingResult


class SelectMapping(BaseObject):
    """ Choose the Best Mapping """

    def __init__(self,
                 results: dict,
                 scoring: object):
        """
        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        :param results:
            relevant section of mapping ruleset
        :param scoring:
            callback to scoring method
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_dict(results)

            self.logger.debug('\n'.join([
                "Initialized Service",
                f"\tTotal Results: {len(results)}"]))

        self._results = results
        self._scoring = scoring

    def process(self) -> MappingResult:

        find_candidates = MappingFindCandidates(self._results).process

        score_candidates = MappingScoreCandidates(
            results=self._results,
            scoring=self._scoring).process

        dedupe_candidates = MappingRemoveDuplicates(self._results).process

        select_candidates = MappingSelectCandidates(self._results).process

        d_candidates = find_candidates()  # Find Candidates
        d_candidates = score_candidates(d_candidates)  # Score Candidates
        d_candidates = dedupe_candidates(d_candidates)  # Remove Duplicates
        d_results = select_candidates(d_candidates)  # Select Results

        return d_results
