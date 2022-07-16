#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute the deepNLU Recipe on Input Text of any Length or Type """


from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData
from deepnlu.recipe.dmo import SentenceHandlerOneShot
from deepnlu.services.segmenter import Segmenter


class ParseTextOneShot(BaseObject):
    """ Execute the deepNLU Recipe on Input Text of any Length or Type """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History

        Created:
            1-Oct-2021
            craig@graffl.ai
        Updated:
            24-May-2022
            craig@graffl.ai
            *   add conditional check on input-text
                https://github.com/grafflr/graffl-core/issues/395#issuecomment-1136369575
        Updated:
            27-May-2022
            craig@graffl.ai
            *   integrate 'find-ontology-data' and absolute path
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            find_ontology_data (FindOntologyData): an instantiation of this object
        """
        BaseObject.__init__(self, __name__)
        self._handle_sentence = SentenceHandlerOneShot(
            find_ontology_data).process

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
