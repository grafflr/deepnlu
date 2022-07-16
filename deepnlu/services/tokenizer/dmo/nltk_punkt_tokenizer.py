#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""  Perform NTLK Punkt Tokenization  """


import logging


class NLTKPunktTokenizer(object):
    """  Perform NTLK Punkt Tokenization
    Reference:
        https://www.nltk.org/api/nltk.tokenize.html """

    def __init__(self,
                 input_text: str):
        """
        Created:
            29-Sept-2021
            craig@graffl.ai
        :param input_text:
        """
        self._input_text = input_text

    def process(self) -> list:
        # TODO: this is sentence segmentation; not tokenization
        pass
