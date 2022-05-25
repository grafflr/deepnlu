# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Facade to find Recommendations """


from random import sample
from pprint import pprint

from itertools import product
from functools import lru_cache

from collections import Counter
from collections import defaultdict

from baseblock import Enforcer
from baseblock import BaseObject
from baseblock import get_ontology_name

from deepnlu.datablock.dmo import GenericDataFinder


class FindRecommendations(BaseObject):
    """ Facade to find Recommendations """

    __slots__ = (
        '_fwd',
        '_rev',
    )

    def __init__(self):
        """
        Created:
            1-Mar-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/204#issuecomment-1055724474
        """
        BaseObject.__init__(self, __name__)
        ontologies = ['appraisal']  # restricted facade

        self._fwd = GenericDataFinder(
            class_suffix='Recommendations',
            module_suffix='recommendations',
            ontologies=ontologies).data()

        self._rev = GenericDataFinder(
            class_suffix='RecommendationsRev',
            module_suffix='recommendations_rev',
            ontologies=ontologies).data()

    def fwd(self) -> dict:
        return self._fwd

    def rev(self) -> dict:
        return self._rev

    @lru_cache
    def comments(self) -> list:
        return sorted(self.fwd().keys())

    def random_comments(self,
                        n: int = 1) -> list:
        if n > len(self.comments()):
            return self.comments()

        return sample(self.comments(), n)

    def random_comment(self) -> str:
        return self.random_comments(1)[0]

    @lru_cache
    def implies_by_comment(self,
                           comment: str) -> list or None:
        comment = comment.lower().strip()
        if comment in self._fwd:
            return self._fwd[comment]

    def comments_by_implies(self,
                            implies: list) -> list or None:
        implies = [x.lower().strip() for x in implies]
        implies = [x for x in implies if x in self.rev()]

        if not len(implies):
            return None

        results = set()
        for imply in implies:
            [results.add(x) for x in self.rev()[imply]]

        return sorted(results, key=len)
