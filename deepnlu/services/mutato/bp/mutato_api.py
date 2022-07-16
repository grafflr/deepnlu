#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Mutato API """


from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData
from deepnlu.services.mutato.svc import PerformExactMatching

from deepnlu.services.mutato.svc import PerformSpanMatching
from deepnlu.services.mutato.svc import PerformSpacyMatching
from deepnlu.services.mutato.svc import PerformHierarchyMatching
from deepnlu.services.mutato.svc import AugmentTokenHierarchy


class MutatoAPI(BaseObject):
    """ Mutato API """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History

        Created:
            6-Oct-2021
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/5
        Updated:
            1-Feb-2022
            craig@graffl.ai
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785
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

        self._perform_exact_matching = PerformExactMatching(
            find_ontology_data).process

        self._perform_span_matching = PerformSpanMatching(
            find_ontology_data).process

        self._perform_hierarchal_matching = PerformHierarchyMatching(
            find_ontology_data).process

        self._augment_hierarchy = AugmentTokenHierarchy(
            find_ontology_data).process

        # Change Log:
        # 20220214  Disable Environment Check
        # 20220228  GRAFFL-205-1055059118   Disable Entire Service
        # self._perform_spacy_matching = PerformSpacyMatching(
        #     find_ontology_data).process

    def swap(self,
             tokens: list,
             ctr: int = 0) -> list:

        sw = Stopwatch()

        ## ---------------------------------------------------------- ##
        # Document:   Tokens vs Swaps
        # Reference:  https://github.com/grafflr/graffl-core/issues/74#issuecomment-947903611
        ## ---------------------------------------------------------- ##

        swaps = self._augment_hierarchy(tokens)
        swaps = self._perform_exact_matching(tokens)
        swaps = self._perform_span_matching(swaps)
        swaps = self._perform_hierarchal_matching(swaps)

        if ctr < 2:
            swaps = self.swap(swaps, ctr + 1)

        # Change Log:
        # 20220214  Disable Environment Check
        # 20220228  GRAFFL-205-1055059118   Disable Entire Service
        # if EnvIO.exists_as_true('ENABLE_SPACY_SPANNING'):
        #   swaps = self._perform_spacy_matching(swaps)

        self.logger.info('\n'.join([
            "Synonym Swap Completed",
            f"\tTotal Time: {str(sw)}"]))

        return swaps
