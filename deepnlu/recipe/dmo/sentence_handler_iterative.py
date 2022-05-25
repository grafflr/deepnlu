#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute the deepNLU stack on a single sentence """


import logging
from pprint import pprint

from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.services.accipio import Tokenizer
from deepnlu.services.accipio import Stemmer
from deepnlu.services.accipio import Normalizer
from deepnlu.services.erogito import ErogitoAPI
from deepnlu.services.mutato import MutatoAPI


class SentenceHandlerIterative(BaseObject):
    """ Execute the deepNLU stack on a single sentence using Individual Ontology Calls 

    Sample Call and Output:
        https://github.com/grafflr/graffl-core/issues/193#issuecomment-1047320212
    """

    __tokcache = {}

    def __init__(self,
                 ontologies: list):
        """
        Created:
            21-Feb-2022
            craig@grafflr.ai
            *   refactored out of 'deep-sentence-handler' 
                with the additional of a tokenization cache for optimization and
                a modification to the output structure to preserve ontological identity
                https://github.com/grafflr/graffl-core/issues/193#issuecomment-1047303350
            28-Feb-2022
            craig@grafflr.ai
            *   update summary output in response to defect with spaCy types found in
                https://github.com/grafflr/graffl-core/issues/205
        """
        BaseObject.__init__(self, __name__)
        Enforcer.is_list(ontologies)

        self._ontologies = ontologies
        self._stemmer = Stemmer()
        self._tokenizer = Tokenizer()
        self._normalizer = Normalizer()
        self._erogito_api = ErogitoAPI()

    def _tokenize(self,
                  input_text: str) -> list:

        if input_text in self.__tokcache:
            return self.__tokcache[input_text]

        def inner() -> list:

            tokens = self._tokenizer.input_text(input_text)
            tokens = self._erogito_api.parse(tokens)

            for token in tokens:
                ## ---------------------------------------------------------- ##
                # Update:     DO NOT use lemma as basis for 'normal' form
                # Reference:  https://github.com/grafflr/graffl-core/issues/46#issuecomment-943708492
                # Old Code:   self._normalizer.input_text(token['lemma'])
                ## ---------------------------------------------------------- ##
                token['normal'] = self._normalizer.input_text(token['text'])

                if token['is_punct']:
                    token['stem'] = token['normal']
                else:
                    token['stem'] = str(
                        self._stemmer.input_text(token['normal']))
                del token['lemma']

            return tokens

        self.__tokcache[input_text] = inner()

        return self.__tokcache[input_text]

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
            result = MutatoAPI(ontology).swap(tokens)

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

        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug('\n'.join([
                "Sentence Analysis Completed",
                f"\tTotal Tokens: {len(tokens)}",
                f"\tTotal Ontologies: {len(self._ontologies)}",
                f"\tTotal Time: {str(sw)}"]))

        return svcresult
