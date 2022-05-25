#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate a Swapped Token """


import os

import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer


class SwapTokenGenerator(BaseObject):
    """ Generate a Swapped Token """

    __slots__ = (
        '_ontologies'
    )

    def __init__(self,
                 ontologies: list):
        """
        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   refactored out of 'exact-match-swapper'
                https://github.com/grafflr/graffl-core/issues/77
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   pass 'ontologies' as list param
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370
        """
        BaseObject.__init__(self, __name__)
        Enforcer.is_list(ontologies)
        self._ontologies = ', '.join(ontologies).strip()

    def process(self,
                normal: str,
                canon: str,
                ner: str,
                tokens: list,
                swap_type: str,
                confidence: float = 100.0) -> dict:

        Enforcer.is_str(normal)
        Enforcer.is_str(canon)
        Enforcer.is_str(ner)
        Enforcer.is_list(tokens)
        Enforcer.is_optional_str(normal)

        return {
            'id': tokens[0]['id'],
            'x': tokens[0]['x'],
            'y': tokens[-1]['y'],
            'ner': ner.upper(),
            'text': ''.join([x['text'] for x in tokens]),
            'normal': normal,
            'swaps': {
                "tokens": tokens,
                "canon": canon,
                "type": swap_type,
                "ontologies": [self._ontologies],
                "confidence": confidence
            }
        }
