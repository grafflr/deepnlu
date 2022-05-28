#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""  Perform NTLK Regular Expression Tokenization  """


from nltk.tokenize import RegexpTokenizer


class NLTKRegexpTokenizer(object):
    """  Perform NTLK Regular Expression Tokenization

    Specific Variations of the Regex Tokenizer can be imported:
        1.  from nltk.tokenize import regexp_tokenize
        2.  from nltk.tokenize import wordpunct_tokenize
        3.  from nltk.tokenize import blankline_tokenize

    and custom regex patterns can be created

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
        tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
        return tokenizer.tokenize(self._input_text)
