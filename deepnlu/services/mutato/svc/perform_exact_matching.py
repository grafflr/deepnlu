#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Exact Matching """


from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer


from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.mutato.dmo import ExactMatchFinder
from deepnlu.services.mutato.dmo import ExactMatchSwapper


class PerformExactMatching(BaseObject):
    """ Perform Exact Matching """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History

        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   refactored out of 'mutato-api'
                https://github.com/grafflr/graffl-core/issues/77
        Updated:
            26-May-2022
            craig@grafflr.ai
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7
        Updated:
            27-May-2022
            craig@grafflr.ai
            *   remove all params in place of 'find-ontology-data'
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            find_ontology_data (FindOntologyData): an instantiation of this object
        """
        BaseObject.__init__(self, __name__)
        self._d_lookup = find_ontology_data.lookup()
        self._exact_match_swapper = ExactMatchSwapper(
            find_ontology_data).process

    def _process(self,
                 tokens: list) -> list:

        gram_size = 5
        while gram_size > 0:

            exact_match_finder = ExactMatchFinder(
                gram_size=gram_size,
                d_lookup=self._d_lookup).process

            results = exact_match_finder(tokens)

            if not results:
                gram_size -= 1
                continue

            d_swap = self._exact_match_swapper(results)

            ids = [x['id'] for x in d_swap['swaps']['tokens']]

            merged = []
            for token in tokens:
                if token['id'] not in ids:
                    merged.append(token)
                elif token['id'] == ids[0]:
                    merged.append(d_swap)

            tokens = self._process(merged)

        return tokens

    def process(self,
                tokens: list) -> list:

        if self.isEnabledForDebug:
            Enforcer.is_list(tokens)

        sw = Stopwatch()

        swaps = self._process(tokens)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Exact Swapping Completed",
                f"\tTotal Time: {str(sw)}"]))

        return swaps
