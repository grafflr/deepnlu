#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Choose the Best Mapping """


from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.services.portendo.schema.dmo import MappingFindCandidates
from deepnlu.services.portendo.schema.dmo import MappingRemoveDuplicates
from deepnlu.services.portendo.schema.dmo import MappingScoreCandidates
from deepnlu.services.portendo.schema.dmo import MappingSelectCandidates

from deepnlu.services.portendo.schema.dto import MappingResult


class SelectMapping(BaseObject):
    """ Choose the Best Mapping """

    def __init__(self,
                 results: dict,
                 d_index: dict):
        """ Change History

        Created:
            7-Feb-2022
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        Updated:
            8-Jun-2022
            craig@graffl.ai
            *   eliminate callback and pass d-index in pursuit of
                https://github.com/grafflr/deepnlu/issues/45

        :param results:
            relevant section of mapping ruleset
        :param scoring:
            callback to scoring method
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_dict(results)
            Enforcer.is_dict(d_index)
            self.logger.debug('\n'.join([
                "Initialized Service",
                f"\tTotal Results: {len(results)}"]))

        self._results = results
        self._d_index = d_index

    def process(self) -> MappingResult:

        find_candidates = MappingFindCandidates(self._results).process

        score_candidates = MappingScoreCandidates(
            results=self._results,
            d_index=self._d_index).process

        dedupe_candidates = MappingRemoveDuplicates(self._results).process

        select_candidates = MappingSelectCandidates(self._results).process

        d_candidates = find_candidates()  # Find Candidates
        d_candidates = score_candidates(d_candidates)  # Score Candidates
        d_candidates = dedupe_candidates(d_candidates)  # Remove Duplicates
        d_results = select_candidates(d_candidates)  # Select Results

        return d_results
