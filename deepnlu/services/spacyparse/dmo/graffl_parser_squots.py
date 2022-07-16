#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Transform unigram squots into unigram dquots """


from baseblock import BaseObject


class GrafflParserSquots(BaseObject):
    """ Transform unigram squots into unigram dquots """

    def __init__(self):
        """
        Created:
            13-Oct-2021
            craig@graffl.ai
            *   refactored out of 'parse-input-tokens' in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                tokens: list) -> list:
        """Transform unigram squots into unigram dquots

        Reference:
             https://github.com/grafflr/graffl-core/issues/1#issuecomment-934967879

        Args:
            tokens (list): list of tokens

        Returns:
            list: list of token results
        """
        results = []

        for token in tokens:
            if token == "'":
                token = '"'
            results.append(token)

        return results
