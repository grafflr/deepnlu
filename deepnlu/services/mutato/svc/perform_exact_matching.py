#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Exact Matching """


import logging
from pprint import pprint

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer
from deepnlu.datablock.dto import get_ontology_name

from deepnlu.datablock import FindNER
from deepnlu.datablock import FindSynonyms

from deepnlu.services.mutato.dmo import ExactMatchFinder
from deepnlu.services.mutato.dmo import ExactMatchSwapper


class PerformExactMatching(BaseObject):
    """ Perform Exact Matching """

    def __init__(self,
                 ner_finder: FindNER,
                 syn_finder: FindSynonyms,
                 d_lookup_data: dict,
                 ontology_name: object = None):
        """
        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   refactored out of 'mutato-api'
                https://github.com/grafflr/graffl-core/issues/77
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)
        self._d_lookup_data = d_lookup_data

        self._exact_match_swapper = ExactMatchSwapper(
            syn_finder=syn_finder,
            ner_finder=ner_finder,
            ontologies=ontologies).process

    def _process(self,
                 tokens: list) -> list:

        gram_size = 5
        while gram_size > 0:

            exact_match_finder = ExactMatchFinder(
                gram_size=gram_size,
                d_lookup=self._d_lookup_data).process

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
        Enforcer.is_list(tokens)

        sw = Stopwatch()

        swaps = self._process(tokens)

        self.logger.info('\n'.join([
            "Exact Swapping Completed",
            f"\tTotal Time: {str(sw)}"]))

        return swaps
