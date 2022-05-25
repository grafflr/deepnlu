#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pformat


from baseblock import Stopwatch
from baseblock import BaseObject


class ComputerExcludeAllOf(BaseObject):

    def __init__(self,
                 d_mapping: dict,
                 d_exclude_allof: dict):
        """
        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        :param indices:
        """
        BaseObject.__init__(self, __name__)
        self._mapping = d_mapping
        self._d_exclude_allof = d_exclude_allof

    def process(self,
                d_input_tokens: dict) -> set:
        sw = Stopwatch()

        def input_tokens_to_set() -> set:
            s = set()
            s.add('-'.join(set(d_input_tokens.keys())))
            return s

        def mapping_to_set() -> set:
            return set(self._d_exclude_allof.keys())

        s_input_tokens = input_tokens_to_set()
        s_mapping = mapping_to_set()
        common = s_input_tokens.intersection(s_mapping)

        mapping = [self._d_exclude_allof[x] for x in common]

        d_results = {}
        for k in mapping:
            d_results[k] = {}

        if self.isEnabledForInfo:
            self.logger.debug('\n'.join([
                "Computation Complete: Exclude All Of",
                f"\tTotal Mapping: {len(s_mapping)}",
                f"\tTotal Input Tokens: {len(s_input_tokens)}",
                f"\tTotal Candidates: {len(mapping)}",
                f"\tTotal Time: {str(sw)}"]))

        if self.isEnabledForDebug and len(d_results):
            self.logger.debug('\n'.join([
                "EXCLUDE_ALL_OF Results:",
                f"{pformat(d_results)}"]))

        return d_results
