#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Tokenize the Input Text and Parse with spaCy """


from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.services.tokenizer import Tokenizer
from deepnlu.services.stemmer import Stemmer
from deepnlu.services.normalize import Normalizer
from deepnlu.services.spacyparse.svc import ParseInputTokens


class InputTextParser(BaseObject):
    """ Tokenize the Input Text and Parse with spaCy """

    def __init__(self):
        """ Change History

        Created:
            8-Jun-2022
            craig@graffl.ai
            *   refactored out of 'sentence-handler-oneshot'
        """
        BaseObject.__init__(self, __name__)
        self._stem = Stemmer().input_text
        self._normalize = Normalizer().input_text
        self._string_tokenize = Tokenizer().input_text
        self._parse = ParseInputTokens().process

    def _tokenize(self,
                  input_text: str,
                  strip_tokens: bool) -> list:

        tokens = self._string_tokenize(input_text)
        if strip_tokens:
            tokens = [x.strip() for x in tokens]
        tokens, doc = self._parse(tokens)

        for token in tokens:
            ## ---------------------------------------------------------- ##
            # Update:     DO NOT use lemma as basis for 'normal' form
            # Reference:  https://github.com/grafflr/graffl-core/issues/46#issuecomment-943708492
            # Old Code:   self._normalizer.input_text(token['lemma'])
            ## ---------------------------------------------------------- ##
            token['normal'] = self._normalize(token['text'])

            if token['is_punct']:
                token['stem'] = token['normal']
            else:
                token['stem'] = str(
                    self._stem(token['normal']))
            del token['lemma']

        return tokens, doc

    def process(self,
                input_text: str,
                strip_tokens: bool = True) -> dict:
        """ Run deepNLU on a single sentence

        Args:
            input_text (str): An input string assumed to be a single sentence
                no sentence segmentation will be performed on this inpu
            strip_tokens (bool, optional): trim (strip) tokens to remove whitespace. Defaults to True.
                set this to False to preserve original whitespace
                set this to True to simplify spaCy dependency parsing

        Returns:
            dict: the processed result
        """

        sw = Stopwatch()

        tokens, doc = self._tokenize(input_text, strip_tokens)

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Text Tokenization Completed",
                f"\tTotal Time: {str(sw)}",
                f"\tTotal Tokens: {len(tokens)}"]))

        return tokens, doc
