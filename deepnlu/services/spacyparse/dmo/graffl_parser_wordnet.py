#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Add Wordnet Flag to Token """


from baseblock import BaseObject
from deepnlu.datablock import FindWordnet


class GrafflParserWordnet(BaseObject):
    """ Add Wordnet Flag to Token """

    def __init__(self):
        """
        Created:
            13-Oct-2021
            craig@graffl.ai
            *   refactored out of 'parse-input-tokens' in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        """
        BaseObject.__init__(self, __name__)
        self._is_wordnet = FindWordnet().exists

    def process(self,
                tokens: list) -> list:
        """Add Wordnet Flag to tokens that are found in Wordnet
            these tokens are considered 'lexical'; that is,
            they are commonly known words in the english language
            as opposed to industry jargon

        Args:
            tokens (list): list of tokens

        Returns:
            list: list of tokens
        """
        results = []

        for token in tokens:

            def is_wordnet() -> bool:
                if token['is_punct']:
                    return False

                return self._is_wordnet(token['text'])

            token['is_wordnet'] = is_wordnet()
            results.append(token)

        return results
