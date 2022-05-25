#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Text Tokenization API """


import functools

from deepnlu.services.accipio.stemmer.svc import PerformPorterStemming


class Stemmer(object):
    """ Text Stemming API """

    def __init__(self):
        self._stem = PerformPorterStemming().process

    @functools.lru_cache(maxsize=1024)
    def input_text(self,
                   input_text: str) -> list:
        return self._stem(input_text)
