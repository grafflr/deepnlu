# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Facade to find Dictionaries on Disk """


from baseblock import BaseObject
from datablock import FindDictionaries


class NormalizeText(BaseObject):
    """ Facade to find Dictionaries on Disk """

    def __init__(self):
        """
        Created:
            30-Sept-2021
            craig@grafflr.ai
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_text: str) -> str:
        if type(input_text) != str:
            raise ValueError

        hyphens = [x for x in FindDictionaries.hyphens() if x in input_text]
        for hyphen in hyphens:
            input_text = input_text.replace(hyphen, '-')

        dquotes = [x for x in FindDictionaries.dquotes() if x in input_text]
        for dquote in dquotes:
            input_text = input_text.replace(dquote, '"')

        squotes = [x for x in FindDictionaries.squotes() if x in input_text]
        for squote in squotes:
            input_text = input_text.replace(squote, "'")

        return input_text.strip().lower()
