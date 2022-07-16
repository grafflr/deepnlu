#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Synonym Swapping with Spacy Entities """


from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData


from deepnlu.services.mutato.dmo.core import SwapTokenGenerator


class SpacyMatchSwapper(BaseObject):
    """ Perform Synonym Swapping with Spacy Entities """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History

        Created:
            20-Oct-2021
            craig@graffl.ai
            *   renamed from 'perform-sliding-window'
                https://github.com/grafflr/graffl-core/issues/77
        Updated:
            1-Feb-2022
            craig@graffl.ai
            *   pass 'ontologies' as list param
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370
        Updated:
            27-May-2022
            craig@graffl.ai
            *   remove 'ontologies' and integrate 'find-ontology-data'
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            find_ontology_data (FindOntologyData): an instantiation of this object
        """
        BaseObject.__init__(self, __name__)
        self._create_swap = SwapTokenGenerator(
            find_ontology_data.ontologies()).process

    def process(self,
                tokens: list,
                matching_rules: list) -> list:

        for d_match in matching_rules:

            positions = list(d_match.keys())

            x = positions[0]
            y = positions[-1] + 1
            subset = tokens[x:y]

            canon = '_'.join([x['normal'] for x in subset]).lower().strip()

            def normal() -> str:
                ## ---------------------------------------------------------- ##
                # Purpose:    The 'canonical' form is the appropriate normal form
                # Reference:  https://github.com/grafflr/graffl-core/issues/20#issuecomment-940678237
                ## ---------------------------------------------------------- ##
                return canon

            ## ---------------------------------------------------------- ##
            # Purpose:    Construct the NER tag
            # Reference:  https://github.com/grafflr/graffl-core/issues/35#issuecomment-949988463
            ## ---------------------------------------------------------- ##
            ner = f"{subset[0]['ent']}"

            d_swap = self._create_swap(normal=normal(),
                                       canon=canon,
                                       ner=ner,
                                       tokens=subset,
                                       swap_type='spacy')

            normalized = tokens[:x]
            normalized.append(d_swap)
            [normalized.append(x) for x in tokens[y:]]

            return normalized

        return tokens
