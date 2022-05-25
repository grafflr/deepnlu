#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Use Token Hierarchies to perform Inferred Matching """


import logging
import itertools
from pprint import pprint

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer
from baseblock import get_ontology_name

from mutato.dmo import SlidingWindowExtract
from mutato.dmo import SwapTokenGenerator
from mutato.dmo import HierarchyMatchFinder
from mutato.dmo import HierarchyMatchSwapper


class PerformHierarchyMatching(BaseObject):
    """ Use Token Hierarchies to perform Inferred Matching """

    __slots__ = (
        '_find_types',
        '_swap_token',
    )

    def __init__(self,
                 find_types_cb: object,
                 ontology_name: object = None):
        """
        Created:
            14-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/188
        """
        BaseObject.__init__(self, __name__)
        self._finder = HierarchyMatchFinder().process
        self._swapper = HierarchyMatchSwapper(
            find_types_cb=find_types_cb,
            ontology_name=ontology_name).process

    def _process(self,
                 tokens: list) -> tuple:

        gram_size = 9
        while gram_size > 1:  # GRAFFLR-188-1039702022; No Unigrams!

            list_of_candidates = self._finder(
                tokens=tokens,
                gram_size=gram_size)

            if len(list_of_candidates):

                results = self._swapper(
                    tokens=tokens,
                    gram_size=gram_size,
                    list_of_candidates=list_of_candidates)

                if results is not None:
                    return results, True

            gram_size -= 1

        return tokens, False

    def process(self,
                tokens: list) -> list:
        Enforcer.is_list(tokens)

        sw = Stopwatch()

        recurse = True
        while recurse:
            tokens, recurse = self._process(tokens)

        self.logger.info('\n'.join([
            "Exact Swapping Completed",
            f"\tTotal Time: {str(sw)}"]))

        return tokens
