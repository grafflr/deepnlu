#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Text Tokenization API """


from functools import lru_cache

from deepnlu.services.stemmer.svc import PerformPorterStemming


class Stemmer(object):
    """ Text Stemming API """

    def __init__(self):
        self._stem = PerformPorterStemming().process

    @lru_cache(maxsize=1024, typed=True)
    def input_text(self,
                   input_text: str) -> list:
        return self._stem(input_text)
