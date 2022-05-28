#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Synonym Swapping with Exact Matches """


from baseblock import BaseObject
from baseblock import Enforcer

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.mutato.dmo.core import SwapTokenGenerator


class ExactMatchSwapper(BaseObject):
    """ Perform Synonym Swapping with Exact Matches """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History
        Created:
            6-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/5
        Updated:
            20-Oct-2021
            craig@grafflr.ai
            *   renamed from 'perform-synonym-swapping'
                https://github.com/grafflr/graffl-core/issues/77
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   pass 'ontologies' as list param
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370
        Updated:
            27-May-2022
            craig@grafflr.ai
            *   remove all params in place of 'find-ontology-data'
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            find_ontology_data (FindOntologyData): an instantiation of this object
        """
        BaseObject.__init__(self, __name__)
        self._find_ner = find_ontology_data.find_ner
        self._find_canon = find_ontology_data.find_canon
        self._create_swap = SwapTokenGenerator(
            find_ontology_data.ontologies()).process

    def process(self,
                candidate_tokens: list) -> list:

        for tokens in candidate_tokens:

            normal = [x['normal'] for x in tokens]
            input_text = '_'.join(normal).strip().lower()

            canon = self._find_canon(input_text)
            if self.isEnabledForDebug:
                Enforcer.is_optional_str(canon)

            if not canon:
                self.logger.error('\n'.join([
                    "Canonical Form Not Found",
                    f"\tInput Tokens: {input_text}"]))
                raise ValueError

            def normal() -> str:
                ## ---------------------------------------------------------- ##
                # Purpose:    The 'canonical' form is the appropriate normal form
                # Reference:  https://github.com/grafflr/graffl-core/issues/20#issuecomment-940678237
                # Old Code:
                return canon

            def ner() -> str:
                ## ---------------------------------------------------------- ##
                # Purpose:    Construct the NER tag
                # Reference:  https://github.com/grafflr/graffl-core/issues/35#issuecomment-949988463
                ## ---------------------------------------------------------- ##
                # return self._find_ner(canon)
                return None

            return self._create_swap(canon=canon,
                                     normal=normal(),
                                     ner=ner(),
                                     tokens=tokens,
                                     swap_type='exact')
