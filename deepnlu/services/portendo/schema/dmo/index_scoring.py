#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate an Index of 'score' Mappings """


from collections import defaultdict

from baseblock import Stopwatch
from baseblock import BaseObject


class IndexScoring(BaseObject):
    """ Generate an Index of 'score' Mappings """

    def __init__(self,
                 mapping: dict):
        """ Change History

        Created:
            10-Feb-2022
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/176
        Updated:
            8-Jun-2022
            craig@graffl.ai
            *   https://github.com/grafflr/deepnlu/issues/45

        :param mapping:
        """
        BaseObject.__init__(self, __name__)
        self._mapping = mapping

    def process(self) -> dict:
        sw = Stopwatch()
        d = defaultdict(list)

        for k in self._mapping:
            for mapping in self._mapping[k]:

                def score() -> float:
                    if 'score' in mapping:
                        return float(mapping['score'])
                    return 0.0

                d[k] = score()

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Generated Index: Scoring",
                f"\tTotal Rows: {len(d)}",
                f"\tTotal Time: {str(sw)}"]))

        return dict(d)
