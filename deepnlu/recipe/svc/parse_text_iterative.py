#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute the deepNLU Recipe on Input Text of any Length or Type """


from baseblock import Enforcer
from baseblock import BaseObject
from baseblock import get_ontology_name

from deepnlu.services.accipio import Segmenter
from deepnlu.recipe.dmo import SentenceHandlerIterative


class ParseTextIterative(BaseObject):
    """ Execute the deepNLU Recipe on Input Text of any Length or Type 

    In the even of multiple Ontologies, parse operations will be invoked 
        separately on the input text and individual result structures preserved
        within the final input.

    This service is optimized for repeated parse operations and is recommended
        over repeated 'ParseTextOneShot().process(...)' calls
    """

    def __init__(self,
                 ontologies: list):
        """
        Created:
            1-Oct-2021
            craig@grafflr.ai
        Updated:
            21-Feb-2022
            craig@grafflr.ai
            *   refactored out of 'process-input-text' in pursuit of
                https://github.com/grafflr/graffl-core/issues/193
        Updated:
            2-Mar-2022
            craig@grafflr.ai
            *   add total-sentences parameter in pursuit of
                https://github.com/grafflr/graffl-core/issues/208
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(ontologies)

            self.logger.debug('\n'.join([
                "Initialized Service",
                f"\tOntologies: {ontologies}"]))

        self._handle_sentence = SentenceHandlerIterative(ontologies).process

    def process(self,
                input_text: str,
                total_sentences: int = None) -> list:
        """ Process Input Text

            Steps:

                1.  Segmentation 
                    Paragraphs and Sentences

                2.  Tokenization
                    Each sentence into a list of tokens (original words)

                3.  Normalization
                    Normalize each list of tokens
                        Normal Form     (e.g., lowercased and trimmed)
                        Stemmed Form    (e.g., more aggresive stemming and chopping)

                4.  Parsing

        Args:
            input_text (str): an input text of any length
            total_sentences (int): total sentences to parse
                if this value is None, parse all sentences
                if this value is greater than the number of all sentences, just parse all sentences

        Returns:
            list:   the output is a list of lists
                    [   # paragraph level
                        [   # sentence level
                            {   
                                text:   <the sentence>,
                                tokens: <the ast>,
                            },
                            ... next sentence ...
                        ],
                        ... next paragraph ...
                    ]
        """

        ctr = 0
        paragraphs = []

        for input_paragraph in Segmenter().input_text(input_text):

            sentences = []
            for input_sentence in input_paragraph:
                sentences.append(self._handle_sentence(input_sentence))

                if total_sentences is not None:
                    ctr += 1
                    if ctr >= total_sentences:
                        paragraphs.append(sentences)
                        return paragraphs

            paragraphs.append(sentences)

        return paragraphs
