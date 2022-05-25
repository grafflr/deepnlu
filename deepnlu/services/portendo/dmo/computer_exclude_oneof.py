#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pformat

from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.services.portendo.dto import Markers


class ComputerExcludeOneOf(BaseObject):

    def __init__(self,
                 d_mapping: dict,
                 d_exclude_oneof: dict):
        """
        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        :param indices:
        """
        BaseObject.__init__(self, __name__)
        self._mapping = d_mapping
        self._d_exclude_oneof = d_exclude_oneof

    def process(self,
                d_input_tokens: dict) -> set:
        sw = Stopwatch()

        s_mapping = set(self._d_exclude_oneof.keys())
        s_input_tokens = set(d_input_tokens.keys())
        common = s_mapping.intersection(s_input_tokens)

        mapping = set()
        [[mapping.add(y) for y in self._d_exclude_oneof[x]] for x in common]

        d_results = {}
        for k in mapping:
            d_results[k] = {}

        if self.isEnabledForInfo:
            self.logger.debug('\n'.join([
                "Computation Complete: Exclude One Of",
                f"\tTotal Mapping: {len(s_mapping)}",
                f"\tTotal Input Tokens: {len(s_input_tokens)}",
                f"\tTotal Candidates: {len(mapping)}",
                f"\tTotal Time: {str(sw)}"]))

        if self.isEnabledForDebug and len(d_results):
            self.logger.debug('\n'.join([
                "EXCLUDE_ONE_OF Results:",
                f"{pformat(d_results)}"]))

        return d_results
