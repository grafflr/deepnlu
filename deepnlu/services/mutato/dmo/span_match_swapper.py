#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Synonym Swapping with Spanned Matches """


import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.datablock.svc import FindNER
from deepnlu.datablock.svc import FindSynonyms

from deepnlu.services.mutato.dmo.core import SwapTokenGenerator


class SpanMatchSwapper(BaseObject):
    """ Perform Synonym Swapping with Spanned Matches """

    __slots__ = (
        '_ner_finder',
        '_create_swap',
    )

    def __init__(self,
                 ner_finder: FindNER,
                 ontologies: list):
        """
        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   renamed from 'perform-sliding-window'
                https://github.com/grafflr/graffl-core/issues/77
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   pass 'ontologies' as list param
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370
        """
        BaseObject.__init__(self, __name__)
        self._find_ner = ner_finder.find_ner
        self._create_swap = SwapTokenGenerator(ontologies).process

    def process(self,
                tokens: list,
                matching_rules: list) -> list:

        for matching_rule in matching_rules:

            x = matching_rule['positions'][0]
            y = matching_rule['positions'][-1] + 1

            subset = tokens[x:y]

            canon = matching_rule['canon']

            def normal() -> str:
                ## ---------------------------------------------------------- ##
                # Purpose:    The 'canonical' form is the appropriate normal form
                # Reference:  https://github.com/grafflr/graffl-core/issues/20#issuecomment-940678237
                ## ---------------------------------------------------------- ##
                return canon

            def ner() -> str:
                ## ---------------------------------------------------------- ##
                # Purpose:
                # Reference:  https://github.com/grafflr/graffl-core/issues/35#issuecomment-949986993
                ## ---------------------------------------------------------- ##
                return self._find_ner(canon)

            d_swap = self._create_swap(normal=normal(),
                                       canon=canon,
                                       ner=ner(),
                                       tokens=subset,
                                       swap_type='spans')

            normalized = tokens[:x]
            normalized.append(d_swap)
            [normalized.append(x) for x in tokens[y:]]

            return normalized
