# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Facade to find Wordnet Data on Disk """


from string import ascii_lowercase

from baseblock import BaseObject

from datablock.os import stopwords


class FindStopWords(BaseObject):
    """ Facade to find Wordnet Data on Disk """

    __slots__ = (
    )

    def __init__(self):
        """
        Created:
            12-Jan-2022
            craig@grafflr.ai
            *   in pursuit of 
                https://github.com/grafflr/graffl-core/issues/120
        """
        BaseObject.__init__(self, __name__)

    def exists(self,
               input_text: str) -> bool:
        input_text = input_text.lower().strip()
        return input_text in stopwords
