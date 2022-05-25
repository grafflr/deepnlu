#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""  Perform NTLK MWET Tokenization  """


from nltk.tokenize import MWETokenizer


class NLTKMwetTokenizer(object):
    """  Perform NTLK MWET Tokenization
    Reference:
        https://www.nltk.org/api/nltk.tokenize.html """

    def __init__(self,
                 input_text: str):
        """
        Created:
            29-Sept-2021
            craig@grafflr.ai
        :param input_text:
        """
        self._input_text = input_text

    def process(self) -> list:
        tokenizer = MWETokenizer(
            [('a', 'little'), ('a', 'little', 'bit'), ('a', 'lot')])
        tokenizer.add_mwe(('paid', 'in', 'full'))

        return tokenizer.tokenize(self._input_text.split())
