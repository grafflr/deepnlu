#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Whitespace Tokenizer """


from deepnlu.datablock.svc import FindDictionaries


class TokenizeUseWhitespace(object):
    """ Whitespace Tokenizer """

    def __init__(self):
        """
        Created:
            12-Oct-2021
            craig@grafflr.ai
        """
        pass

    def process(self,
                input_text: str) -> list:
        return input_text.split()
