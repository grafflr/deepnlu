#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform spaCy parse and retokenization """


import spacy
from spacy.tokens import Doc
from spacy.lang.en import English


from baseblock import BaseObject
from deepnlu.datablock import FindWordnet


class GrafflParserSpacy(BaseObject):
    """ Perform spaCy parse and retokenization """

    __slots__ = (
        '_nlp',
    )

    def __init__(self):
        """
        Created:
            13-Oct-2021
            craig@grafflr.ai
            *   refactored out of 'parse-input-tokens' in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        """
        BaseObject.__init__(self, __name__)
        self._nlp = spacy.load("en_core_web_sm")

    def process(self,
                input_text: str) -> Doc:
        """Perform actual spaCy parse and retokenize input

        Args:
            tokens (list): list of tokens

        Returns:
            Doc: spacy doc
        """
        doc = self._nlp(input_text)

        ## ---------------------------------------------------------- ##
        # Purpose:    Perform Retokenization
        # Reference:  https://github.com/grafflr/graffl-core/issues/1#issuecomment-935048135
        ## ---------------------------------------------------------- ##
        position = [token.i for token in doc if token.i !=
                    0 and "'" in token.text]
        with doc.retokenize() as retokenizer:
            for pos in position:
                retokenizer.merge(doc[pos-1:pos+1])

        return doc
