#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Mutato API """


from baseblock import Stopwatch
from baseblock import BaseObject
from deepnlu.datablock.dto import get_ontology_name

from deepnlu.datablock.svc import FindNER
from deepnlu.datablock.svc import FindTypes
from deepnlu.datablock.svc import FindLookup
from deepnlu.datablock.svc import FindSynonyms

from deepnlu.services.mutato.svc import PerformExactMatching
from deepnlu.services.mutato.svc import PerformSpanMatching
from deepnlu.services.mutato.svc import PerformSpacyMatching
from deepnlu.services.mutato.svc import PerformHierarchyMatching
from deepnlu.services.mutato.svc import AugmentTokenHierarchy


class MutatoAPI(BaseObject):
    """ Mutato API """

    def __init__(self,
                 ontology_name: object = None):
        """ Change History

        Created:
            6-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/5
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785
        Args:
            ontology_name (object, optional): the OWL model to use. Defaults to None.
                if not provided as a param, must exist in the environment
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)

        ner_finder = FindNER(ontologies)

        type_finder = FindTypes(ontologies)
        syn_finder = FindSynonyms(ontologies)

        d_lookup_data = FindLookup(ontologies).data()

        self._perform_exact_matching = PerformExactMatching(
            ner_finder=ner_finder,
            syn_finder=syn_finder,
            d_lookup_data=d_lookup_data,
            ontology_name=ontologies).process

        self._perform_span_matching = PerformSpanMatching(
            ner_finder=ner_finder,
            ontology_name=ontologies).process

        self._perform_hierarchal_matching = PerformHierarchyMatching(
            ontology_name=ontologies,
            find_types_cb=type_finder).process

        self._perform_spacy_matching = PerformSpacyMatching(
            ontology_name=ontologies).process

        self._augment_hierarchy = AugmentTokenHierarchy(
            ontology_name=ontologies,
            find_types_cb=type_finder).process

    def swap(self,
             tokens: list) -> list:

        sw = Stopwatch()

        ## ---------------------------------------------------------- ##
        # Document:   Tokens vs Swaps
        # Reference:  https://github.com/grafflr/graffl-core/issues/74#issuecomment-947903611
        ## ---------------------------------------------------------- ##

        swaps = self._augment_hierarchy(tokens)
        swaps = self._perform_exact_matching(tokens)
        swaps = self._perform_span_matching(swaps)
        swaps = self._perform_hierarchal_matching(swaps)

        # Change Log:
        # 20220214  Disable Environment Check
        # 20220228  GRAFFL-205-1055059118   Disable Entire Service
        # if EnvIO.exists_as_true('ENABLE_SPACY_SPANNING'):
        #   swaps = self._perform_spacy_matching(swaps)

        self.logger.info('\n'.join([
            "Synonym Swap Completed",
            f"\tTotal Time: {str(sw)}"]))

        return swaps
