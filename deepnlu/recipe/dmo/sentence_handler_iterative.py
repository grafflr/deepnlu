#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute the deepNLU stack on a single sentence """


import logging
from pprint import pprint
from functools import lru_cache

from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.tokenizer import Tokenizer
from deepnlu.services.stemmer import Stemmer
from deepnlu.services.normalize import Normalizer
from deepnlu.services.mutato import MutatoAPI
from deepnlu.services.spacyparse.svc import ParseInputTokens


class SentenceHandlerIterative(BaseObject):
    """ Execute the deepNLU stack on a single sentence using Individual Ontology Calls 

    Sample Call and Output:
        https://github.com/grafflr/graffl-core/issues/193#issuecomment-1047320212
    """

    def __init__(self,
                 ontologies: list,
                 absolute_path: str):
        """ Change History

        Created:
            21-Feb-2022
            craig@grafflr.ai
            *   refactored out of 'deep-sentence-handler' 
                with the additional of a tokenization cache for optimization and
                a modification to the output structure to preserve ontological identity
                https://github.com/grafflr/graffl-core/issues/193#issuecomment-1047303350
        Updated:
            28-Feb-2022
            craig@grafflr.ai
            *   update summary output in response to defect with spaCy types found in
                https://github.com/grafflr/graffl-core/issues/205

        Args:
            ontologies (list): one-or-more Ontology models to use in processing
            absolute_path (str): absolute path to Ontology models
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(ontologies)

        self._ontologies = ontologies
        self._absolute_path = absolute_path

        self._stem = Stemmer().input_text
        self._normalize = Normalizer().input_text
        self._string_tokenize = Tokenizer().input_text
        self._parse = ParseInputTokens().process

    @lru_cache(maxsize=5196, typed=True)
    def _tokenize(self,
                  input_text: str) -> list:
        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)

        tokens = self._string_tokenize(input_text)
        tokens, _ = self._parse(tokens)

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

        return tokens

    def process(self,
                input_text: str,
                summary_only: bool = True) -> dict:
        """Run deepNLU on a single sentence

        Args:
            input_text (str): An input string assumed to be a single sentence
                no sentence segmentation will be performed on this input
            summary_only (bool): if False, append the entire AST to each result structure
                note that the summary is generally sufficient

        Returns:
            dict: the processed result
        """

        sw = Stopwatch()
        svcresult = []

        tokens = self._tokenize(input_text)

        for ontology in self._ontologies:

            finder = FindOntologyData(
                ontologies=[ontology],
                absolute_path=self._absolute_path)

            result = MutatoAPI(finder).swap(tokens)

            def summary() -> list:
                def is_valid(d_token: dict) -> bool:
                    if 'swaps' not in d_token:
                        return False
                    return d_token['swaps']['type'] == 'exact'  # GRAFFLR-205

                results = [token['normal'] for token in result
                           if is_valid(token)]
                return sorted(set(results), key=len)

            d_sentence = {
                "type": "sentence",
                "text": input_text,
                "ontologies": [ontology],
                "result": result,  # GRAFFLR-205; need for debug ...
                "summary": summary()}

            if not summary_only:
                d_sentence['tokens'] = result

            svcresult.append(d_sentence)

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Sentence Analysis Completed",
                f"\tTotal Tokens: {len(tokens)}",
                f"\tTotal Ontologies: {len(self._ontologies)}",
                f"\tTotal Time: {str(sw)}"]))

        return svcresult
