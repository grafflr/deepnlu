# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Normalize Input Text """


import functools

from baseblock import BaseObject

from accipio.normalize.svc import NormalizeText


class Normalizer(BaseObject):
    """ Normalize Input Text """

    __slots__ = (
        '_svc',
    )

    def __init__(self):
        """
        Created:
            1-Oct-2021
            craig@grafflr.ai
        """
        BaseObject.__init__(self, __name__)
        self._svc = NormalizeText().process

    @functools.lru_cache
    def input_text(self,
                   input_text: str) -> str:
        return self._svc(input_text)
