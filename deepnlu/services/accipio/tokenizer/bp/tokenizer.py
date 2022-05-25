#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Text Tokenization API """

import functools


class Tokenizer(object):
    """ Text Tokenization API """

    __slots__ = (
        '_spacy',
        '_whitespace',
        '_graffl',
    )

    def __init__(self):
        self._spacy = None
        self._graffl = None
        self._whitespace = None

    @functools.lru_cache
    def spacy(self,
              input_text: str) -> list:
        """Tokenize with spaCy 

        Args:
            input_text (str): input text of any length

        Returns:
            list: list of tokens
        """
        if not self._spacy:
            from accipio.tokenizer.svc import TokenizeUseSpacy
            self._spacy = TokenizeUseSpacy().process

        return self._spacy(input_text)

    @functools.lru_cache
    def whitespace(self,
                   input_text: str) -> list:
        """Tokenize using Whitespace 

        Args:
            input_text (str): input text of any length

        Returns:
            list: list of tokens
        """
        if not self._whitespace:
            from accipio.tokenizer.svc import TokenizeUseWhitespace
            self._whitespace = TokenizeUseWhitespace().process

        return self._whitespace(input_text)

    @functools.lru_cache
    def input_text(self,
                   input_text: str) -> list:
        """Tokenize with Graffl Custom Tokenizer 

        Args:
            input_text (str): input text of any length

        Returns:
            list: list of tokens
        """
        if not self._graffl:
            from accipio.tokenizer.svc import TokenizeUseGraffl
            self._graffl = TokenizeUseGraffl().process

        return self._graffl(input_text)
