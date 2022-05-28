#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute the deepNLU stack on a single sentence """


import logging
from pprint import pprint

from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.accipio import Tokenizer
from deepnlu.services.accipio import Stemmer
from deepnlu.services.accipio import Normalizer
from deepnlu.services.erogito import ErogitoAPI
from deepnlu.services.mutato import MutatoAPI


class SentenceHandlerOneShot(BaseObject):
    """ Execute the deepNLU stack on a single sentence using a single Ontology Call

    This implies that the caller has passed one-or-more Ontologies into the component

    In the event of multiple Ontologies, 
    -   the underlying data dictionaries are automatically merged
    -   and collisions are resolved on a first-come-first-serve basis

    This is suitable when it's suitable

    Reference:
        https://github.com/grafflr/graffl-core/issues/193#issue-1146312499
    """
#

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History

        Created:
            1-Oct-2021
            craig@grafflr.ai
        Updated:
            14-Oct-2021
            craig@grafflr.ai
            *   do not use lemma as basis for 'normal' form
                https://github.com/grafflr/graffl-core/issues/46#issuecomment-943708492
        Updated:
            29-Oct-2021
            craig@grafflr.ai
            *   integrate intelligo-api
                https://github.com/grafflr/graffl-core/issues/97
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   enforce ontologies as a list parameter
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370
        Updated:
            21-Feb-2022
            craig@grafflr.ai
            *   renamed from 'deep-sentence-handler' for consistency with 'sentence-handler-oneshot'
                https://github.com/grafflr/graffl-core/issues/193#issuecomment-1047303350
        Updated:
            27-May-2022
            craig@grafflr.ai
            *   remove all params in place of 'find-ontology-data'
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            find_ontology_data (FindOntologyData): an instantiation of this object
        """
        BaseObject.__init__(self, __name__)
        self._ontologies = find_ontology_data.ontologies()
        self._stemmer = Stemmer()
        self._tokenizer = Tokenizer()
        self._normalizer = Normalizer()
        self._erogito_api = ErogitoAPI()
        self._swap_synonyms = MutatoAPI(find_ontology_data).swap

    def _tokenize(self,
                  input_text: str) -> list:

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

    def process(self,
                input_text: str) -> dict:
        """Run deepNLU on a single sentence

        Args:
            input_text (str): An input string assumed to be a single sentence
                no sentence segmentation will be performed on this inpu

        Returns:
            dict: the processed result
        """

        sw = Stopwatch()

        tokens = self._tokenize(input_text)

        tokens = self._swap_synonyms(tokens)

        d_sentence = {
            "type": "sentence",
            "text": input_text,
            "ontologies": self._ontologies,
            "tokens": tokens}

        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug('\n'.join([
                "Sentence Analysis Completed",
                f"\tTotal Tokens: {len(tokens)}",
                f"\tTotal Time: {str(sw)}"]))

        return d_sentence
