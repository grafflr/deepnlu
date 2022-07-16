#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" API for Erogito Services """


import os
from pprint import pprint

from baseblock import FileIO
from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.autotaxo.bp import AutoTaxoOrchestrator
from deepnlu.services.autotaxo.svc import ExtractTextacyNgrams
from deepnlu.services.autotaxo.svc import ExtractTextacyKeyterms

from deepnlu.services.spacyparse.svc import ParseInputTokens
from deepnlu.services.spacyparse.svc import GenerateDisplacyOutput

from deepnlu.services.mutato.bp import MutatoAPI
from deepnlu.services.normalize.bp import Normalizer
from deepnlu.services.portendo.bp import Portendo
from deepnlu.services.segmenter.bp import Segmenter
from deepnlu.services.spacyparse.svc import ParseInputTokens
from deepnlu.services.stemmer import Stemmer
from deepnlu.services.tokenizer import Tokenizer


class ServicesAPI(BaseObject):
    """ API for all DeepNLU Services """

    def __init__(self):
        """ Change History

        Created:
            16-Apr-2022
            craig@graffl.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/286
        Updated:
            2-May-2022
            craig@graffl.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/328
        Updated:
            27-May-2022
            craig@graffl.ai
            *   refactored into general purpose services-API
                https://github.com/grafflr/deepnlu/issues/15

        """
        BaseObject.__init__(self, __name__)

    def spacy_parse_tokens(self,
                           tokens: list) -> list:
        return ParseInputTokens().process(tokens)

    def classify(self,
                 tokens: list,
                 ontology_name: str) -> str:
        return Portendo(ontology_name).run(tokens)

    def stem(self,
             input_text: str) -> str:
        return Stemmer().input_text(input_text)

    def tokenize(self,
                 input_text: str) -> str:
        return Tokenizer().input_text(input_text)

    def normalize_text(self,
                       input_text: str) -> str:
        return Normalizer().input_text(input_text)

    def segment_text(self,
                     input_text: str) -> str:
        return Segmenter().input_text(input_text)

    def swap_synonyms(self,
                      tokens: list,
                      ontologies: list,
                      absolute_path: str) -> list:
        """ Swap Synonyms 

        Args:
            tokens (list): _description_
            ontologies (list): list of OWL models
            absolute_path (str): absolute path to the OWL models

        Returns:
            list: tokens with swapped synonyms
        """

        absolute_path = os.path.normpath(
            os.path.join(os.getcwd(), 'resources/data/owl'))
        FileIO.exists_or_error(absolute_path)

        finder = FindOntologyData(
            ontologies=ontologies,
            absolute_path=absolute_path)

        MutatoAPI(finder).swap(tokens)

    def ngrams(self,
               input_text: str,
               ngram_level: int = 3,
               filter_stops: bool = True,
               filter_punct: bool = True,
               filter_nums: bool = True,
               term_frequency: int = 2,
               case_sensitive: bool = False) -> list:
        """ Extract n-Grams from Input Text

        Args:
            input_text (str): input text of any length
            ngram_level (int, optional): n-Gram level to extract. Defaults to 3.
            filter_stops (bool, optional): Filter Stopwords. Defaults to True.
            filter_punct (bool, optional): Filter Punctuation. Defaults to True.
            filter_nums (bool, optional): Filter Numbers. Defaults to True.
            term_frequency (int, optional): Number of times a term must repeat. Defaults to 2.
            case_sensitive (bool, optional): Determine if input text case should be maintained.  Defaults to False

        Returns:
            list: n-Gram results
        """

        return ExtractTextacyNgrams().process(input_text=input_text,
                                              ngram_level=ngram_level,
                                              filter_stops=filter_stops,
                                              filter_punct=filter_punct,
                                              filter_nums=filter_nums,
                                              term_frequency=term_frequency,
                                              case_sensitive=case_sensitive)

    def keyterms(self,
                 input_text: str,
                 top_n: int = 50,
                 decompose: bool = True) -> list:
        """ Generate a list of Keyterms with Confidence Levels

        Args:
            input_text (str): Input Text of any length
            top_n (int, optional): the total terms to return. Defaults to 50.
            decompose (bool, optional): if True, decompose an n-gram into a hierarchy. Defaults to True
                Sample Input:   Alpha Beta Gamma
                Sample Output:  [ Alpha Beta Gamma, Alpha Beta, Alpha ]

        Returns:
            list: a list of tuples representing the extracted keyterm and a confidence level
        """

        return ExtractTextacyKeyterms().process(
            top_n=top_n,
            decompose=decompose,
            input_text=input_text)

    def taxonomy(self,
                 input_text: str,
                 top_n: int = 250) -> str:
        """ Essentially identical under the covers to the 'keyterms' function
        except each token is decomposed and then converted to TTL format

        For example:
            "Alpha Beta Gamma" becomes part of the taxonomy "Beta Gamma" and "Gamma"

        Args:
            input_text (str): Input Text of any length
            top_n (int, optional): the total terms to return. Defaults to 50.

        Returns:
            str: TTL entities suitable for an OWL file
        """

        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)

        results = AutoTaxoOrchestrator().process(input_text=input_text,
                                                 top_n=top_n)

        if self.isEnabledForDebug:
            Enforcer.is_optional_list(results)

        return results

    def parse(self,
              tokens: list) -> list:
        """Perform spaCy Parse of Tokens
            and augment with related metadata

        Sample Input:
            "American "

        Sample Output:
            {
                "dep":"compound",
                "head":"6447259181653080421",
                "id":"8947108287989031391",
                "is_alpha":true,
                "is_punct":false,
                "is_stop":false,
                "is_wordnet":true,
                "normal":"american",
                "pos":"PROPN",
                "shape":"Xxxxx",
                "stem":"american",
                "tag":"NNP",
                "text":"American ",
                "x":0,
                "y":8
            }

        Args:
            tokens (list): a list of plain-text token strings

        Returns:
            list: a list of token dictionaries
        """
        return ParseInputTokens().process(tokens)

    def displacy(self,
                 tokens: list) -> list:
        """Create displaCy Output for Visualizations

        Reference:
            https://github.com/grafflr/graffl-core/issues/26#issuecomment-941524282

        Args:
            tokens (list): List of Tokens

        Returns:
            list: displaCy compatible output
        """
        return GenerateDisplacyOutput().process(tokens)
