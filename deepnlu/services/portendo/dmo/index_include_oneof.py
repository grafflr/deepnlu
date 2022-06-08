#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate an Index of 'include-all-of' Mappings"""


from collections import defaultdict

from baseblock import Stopwatch
from baseblock import BaseObject


class IndexIncludeOneOf(BaseObject):
    """ Generate an Index of 'include-all-of' Mappings"""

    def __init__(self,
                 mapping: dict):
        """ Change History

        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        Updated:
            8-Jun-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/45

        :param mapping
        """
        BaseObject.__init__(self, __name__)
        self._mapping = mapping

    def process(self) -> dict:
        sw = Stopwatch()
        d = defaultdict(list)

        for k in self._mapping:
            for mapping in self._mapping[k]:
                if 'include_one_of' in mapping:
                    for marker_name in mapping['include_one_of']:
                        d[marker_name].append(k)

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Generated Index: Include One Of",
                f"\tTotal Rows: {len(d)}",
                f"\tTotal Time: {str(sw)}"]))

        return dict(d)
