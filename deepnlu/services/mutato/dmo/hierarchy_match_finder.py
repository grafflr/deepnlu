#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Use Token Hierarchies to Find Matches """


from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer

from deepnlu.services.mutato.dmo import SlidingWindowExtract


class HierarchyMatchFinder(BaseObject):
    """ Use Token Hierarchies to Find Matches """

    def __init__(self):
        """
        Created:
            14-Feb-2022
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/188
        """
        BaseObject.__init__(self, __name__)

    def _filter(self,
                window: list) -> list:
        results = []

        for candidates in window:

            def is_valid(d_token: dict) -> bool:

                if 'ancestors' in d_token and len(d_token['ancestors']):
                    return True

                if 'descendants' in d_token and len(d_token['descendants']):
                    return True

                if 'swaps' in d_token:

                    if self.isEnabledForDebug:
                        Enforcer.is_str(d_token['swaps']['type'])

                    if d_token['swaps']['type'] == 'hierarchy':
                        return False

                    for child in d_token['swaps']['tokens']:

                        if self.isEnabledForDebug:
                            Enforcer.is_dict(child)

                        if 'ancestors' in child and len(child['ancestors']):
                            return True

                        if 'descendants' in child and len(child['descendants']):
                            return True

                return False

            has_valid_tokens = len([token for token
                                    in candidates if is_valid(token)])

            if has_valid_tokens:
                results.append(candidates)

        return results

    def _process(self,
                 tokens: list,
                 gram_size: int) -> list:

        window = SlidingWindowExtract(
            tokens=tokens,
            gram_size=gram_size).process()

        return self._filter(window)

    def process(self,
                tokens: list,
                gram_size: int) -> list:
        Enforcer.is_list(tokens)

        sw = Stopwatch()

        swaps = self._process(tokens=tokens,
                              gram_size=gram_size)

        self.logger.info('\n'.join([
            "Hierarchy Match Finding Completed",
            f"\tTotal Time: {str(sw)}"]))

        return swaps
