#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate an Index of 'exclude-all-of' Mappings"""


from collections import defaultdict

from baseblock import Stopwatch
from baseblock import BaseObject


class IndexExcludeAllOf(BaseObject):
    """ Generate an Index of 'exclude-all-of' Mappings"""

    def __init__(self,
                 mapping: dict):
        """ Change History

        Created:
            7-Feb-2022
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/169
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
                if 'exclude_all_of' in mapping:
                    values = '-'.join(set(mapping['exclude_all_of']))
                    d[values] = k

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Generated Index: Exclude All Of",
                f"\tTotal Rows: {len(d)}",
                f"\tTotal Time: {str(sw)}"]))

        return dict(d)
