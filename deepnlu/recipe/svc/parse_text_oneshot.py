#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute the deepNLU Recipe on Input Text of any Length or Type """


from baseblock import Enforcer
from baseblock import BaseObject


from deepnlu.services.accipio import Segmenter
from deepnlu.recipe.dmo import SentenceHandlerOneShot


class ParseTextOneShot(BaseObject):
    """ Execute the deepNLU Recipe on Input Text of any Length or Type """

    def __init__(self,
                 ontologies: list):
        """ Change History

        Created:
            1-Oct-2021
            craig@grafflr.ai
        Updated:
            24-May-2022
            craig@grafflr.ai
            *   add conditional check on input-text
                https://github.com/grafflr/graffl-core/issues/395#issuecomment-1136369575

        Args:
            ontologies (list): list of ontologies to use for parsing
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(ontologies)

            self.logger.debug('\n'.join([
                "Initialized Service",
                f"\tOntologies: {ontologies}"]))

        self._handle_sentence = SentenceHandlerOneShot(ontologies).process

    def process(self,
                input_text: str) -> list or None:
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

        if not input_text or not len(input_text):
            return None

        paragraphs = []

        for input_sentence in Segmenter().input_text(input_text):
            paragraphs.append([self._handle_sentence(x)
                               for x in input_sentence])

        return paragraphs
