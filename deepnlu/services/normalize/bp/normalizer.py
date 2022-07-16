# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Normalize Input Text """


from functools import lru_cache

from baseblock import BaseObject

from deepnlu.services.normalize.svc import NormalizeText


class Normalizer(BaseObject):
    """ Normalize Input Text """

    def __init__(self):
        """
        Created:
            1-Oct-2021
            craig@graffl.ai
        """
        BaseObject.__init__(self, __name__)
        self._svc = NormalizeText().process

    @lru_cache(maxsize=1024, typed=True)
    def input_text(self,
                   input_text: str) -> str:
        return self._svc(input_text)
