#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Use Token Hierarchies to perform Inferred Matching """


from typing import Callable

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.mutato.dmo import HierarchyMatchFinder
from deepnlu.services.mutato.dmo import HierarchyMatchSwapper


class PerformHierarchyMatching(BaseObject):
    """ Use Token Hierarchies to perform Inferred Matching """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History

        Created:
            14-Feb-2022
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/188
        Updated:
            26-May-2022
            craig@graffl.ai
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7
        Updated:
            27-May-2022
            craig@graffl.ai
            *   remove 'ontologies' and integrate 'find-ontology-data'
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            find_ontology_data (FindOntologyData): an instantiation of this object
        """
        BaseObject.__init__(self, __name__)
        self._finder = HierarchyMatchFinder().process
        self._swapper = HierarchyMatchSwapper(find_ontology_data).process

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

        if self.isEnabledForDebug:
            Enforcer.is_list(tokens)

        sw = Stopwatch()

        recurse = True
        while recurse:
            tokens, recurse = self._process(tokens)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Exact Swapping Completed",
                f"\tTotal Time: {str(sw)}"]))

        return tokens
