#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Text Tokenization API """


from functools import lru_cache


class Tokenizer(object):
    """ Text Tokenization API """

    def __init__(self):
        self._spacy = None
        self._graffl = None
        self._whitespace = None

    @lru_cache
    def spacy(self,
              input_text: str) -> list:
        """Tokenize with spaCy 

        Args:
            input_text (str): input text of any length

        Returns:
            list: list of tokens
        """
        if not self._spacy:
            from deepnlu.services.tokenizer.svc import TokenizeUseSpacy
            self._spacy = TokenizeUseSpacy().process

        return self._spacy(input_text)

    @lru_cache
    def whitespace(self,
                   input_text: str) -> list:
        """Tokenize using Whitespace 

        Args:
            input_text (str): input text of any length

        Returns:
            list: list of tokens
        """
        if not self._whitespace:
            from deepnlu.services.tokenizer.svc import TokenizeUseWhitespace
            self._whitespace = TokenizeUseWhitespace().process

        return self._whitespace(input_text)

    @lru_cache
    def input_text(self,
                   input_text: str) -> list:
        """Tokenize with Graffl Custom Tokenizer 

        Args:
            input_text (str): input text of any length

        Returns:
            list: list of tokens
        """
        if not self._graffl:
            from deepnlu.services.tokenizer.svc import TokenizeUseGraffl
            self._graffl = TokenizeUseGraffl().process

        return self._graffl(input_text)
