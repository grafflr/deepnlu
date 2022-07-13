#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute the deepNLU stack on a single sentence """


from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.stemmer import Stemmer
from deepnlu.services.mutato import MutatoAPI
from deepnlu.services.portendo import Portendo
from deepnlu.services.tokenizer import Tokenizer
from deepnlu.services.normalize import Normalizer
from deepnlu.services.spacyparse.svc import ParseInputTokens


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
        self._entity_names = [x.lower() for x in
                              find_ontology_data.labels() if '_' in x]

        self._ontologies = find_ontology_data.ontologies()
        self._swap_synonyms = MutatoAPI(find_ontology_data).swap

        self._stem = Stemmer().input_text
        self._normalize = Normalizer().input_text
        self._string_tokenize = Tokenizer().input_text
        self._parse = ParseInputTokens().process

        self._infer_tokens = Portendo().entity

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

    def _infer_entities(self,
                        svcresult: list) -> list:
        """ Use Schema-less Inference via Portendo

        Args:
            svcresult (list): the deepNLU service result

        Returns:
            list: the list of inferred entities
                cardinality of return list is 0..*
        """
        input_tokens = [x['normal'] for x in svcresult if 'swaps' in x]

        inferred_results = self._infer_tokens(
            input_tokens=input_tokens,
            entity_names=self._entity_names)

        if not inferred_results:
            return []

        if not inferred_results['result']:
            return []

        return inferred_results['result']

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
        svcresult = self._swap_synonyms(tokens)
        inferred = self._infer_entities(svcresult)

        d_sentence = {
            "type": "sentence",
            "text": input_text,
            "ontologies": self._ontologies,
            "tokens": svcresult,
            "inferred": inferred
        }

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Sentence Analysis Completed",
                f"\tTotal Tokens: {len(tokens)}",
                f"\tTotal Time: {str(sw)}"]))

        return d_sentence
