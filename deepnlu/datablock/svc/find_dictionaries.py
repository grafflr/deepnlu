# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Facade to find Dictionaries on Disk """


from baseblock import BaseObject


class FindDictionaries(BaseObject):
    """ Facade to find Dictionaries on Disk """

    __slots__ = (
    )

    def __init__(self):
        """
        Created:
            30-Sept-2021
            craig@grafflr.ai
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def hyphens() -> dict:
        from deepnlu.datablock.os import d_hyphens
        return d_hyphens

    @staticmethod
    def currency() -> dict:
        from deepnlu.datablock.os import d_currency
        return d_currency

    @staticmethod
    def squotes() -> dict:
        from deepnlu.datablock.os import d_squotes
        return d_squotes

    @staticmethod
    def dquotes() -> dict:
        from deepnlu.datablock.os import d_dquotes
        return d_dquotes

    @staticmethod
    def enclitics() -> dict:
        from deepnlu.datablock.os import d_enclitics
        return d_enclitics

    @staticmethod
    def abbreviations() -> dict:
        from deepnlu.datablock.os import d_abbreviations
        return d_abbreviations
