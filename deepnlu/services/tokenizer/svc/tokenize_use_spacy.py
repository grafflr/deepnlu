#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""  Perform Tokenization with spaCy  """


from spacy.lang.en import English
from spacy.tokenizer import Tokenizer


class TokenizeUseSpacy(object):
    """  Perform Tokenization with spaCy  
    Reference:
        https://spacy.io/api/tokenizer """

    __tokenizer = None

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
        if not self.__tokenizer:
            nlp = English()
            self.__tokenizer = Tokenizer(nlp.vocab)

        return self.__tokenizer(self._input_text)
