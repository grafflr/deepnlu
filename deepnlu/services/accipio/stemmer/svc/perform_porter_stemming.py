# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Facade to find Dictionaries on Disk """


from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

from baseblock import BaseObject
from datablock import FindDictionaries

class PerformPorterStemming(BaseObject):

    """ Facade to find Dictionaries on Disk """

    def __init__(self):
        """
        Created:
            30-Sept-2021
            craig@grafflr.ai
        """
        BaseObject.__init__(self, __name__)
        self._ps = PorterStemmer()

    def process(self,
                input_text: str) -> str:
        return self._ps.stem(input_text)
