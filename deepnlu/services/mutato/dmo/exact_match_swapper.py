#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Synonym Swapping with Exact Matches """


from pprint import pprint

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer

from deepnlu.datablock import FindNER
from deepnlu.datablock import FindSynonyms

from deepnlu.services.mutato.dmo.core import SwapTokenGenerator


class ExactMatchSwapper(BaseObject):
    """ Perform Synonym Swapping with Exact Matches """

    __slots__ = (
        '_syn_finder',
        '_ner_finder',
        '_create_swap',
    )

    def __init__(self,
                 ner_finder: FindNER,
                 syn_finder: FindSynonyms,
                 ontologies: list):
        """
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
        """
        BaseObject.__init__(self, __name__)
        self._find_ner = ner_finder.find_ner
        self._find_canon = syn_finder.find_canon
        self._create_swap = SwapTokenGenerator(ontologies).process

    def process(self,
                candidate_tokens: list) -> list:

        sw = Stopwatch()

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
                return self._find_ner(canon)

            return self._create_swap(canon=canon,
                                     normal=normal(),
                                     ner=ner(),
                                     tokens=tokens,
                                     swap_type='exact')