#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Leverage spaCy NERs """


from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer

from deepnlu.services.mutato.dmo import SpacyMatchFinder
from deepnlu.services.mutato.dmo import SpacyMatchSwapper


class PerformSpacyMatching(BaseObject):
    """Collapse Contiguous spaCy NERs into a single entity

    Sample Input:
        and/CONJ John/PERSON Doe/PERSON said/DECL

    Sample Match:
        "John Doe" == PERSON PERSON

    Sample Output:
        and john_doe said
    """

    def __init__(self,
                 ontologies: list):
        """ Change History

        Created:
            22-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/35
        Updated:
            29-Oct-2021
            craig@grafflr.ai
            *   Update for Recursive Processing
                https://github.com/grafflr/graffl-core/issues/96
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   pass 'ontology-name' as a param
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027468040
        Updated:
            26-May-2022
            craig@grafflr.ai
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7

        Args:
            ontologies (list): one-or-more Ontology models to use in processing
        """
        BaseObject.__init__(self, __name__)
        self._spacy_match_swapper = SpacyMatchSwapper(ontologies).process

    def _process(self,
                 tokens: list) -> list:

        matching_rules = SpacyMatchFinder().process(tokens)
        if not matching_rules or not len(matching_rules):
            return tokens

        tokens = self._spacy_match_swapper(tokens=tokens,
                                           matching_rules=matching_rules)

        return self._process(tokens)  # graffl-core-96-954953141

    def process(self,
                tokens: list) -> list:
        Enforcer.is_list(tokens)

        sw = Stopwatch()

        swaps = self._process(tokens)

        self.logger.info('\n'.join([
            "spaCy Matching Completed",
            f"\tTotal Time: {str(sw)}"]))

        return swaps
