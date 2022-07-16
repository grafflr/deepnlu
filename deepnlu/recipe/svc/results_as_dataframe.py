#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Transform deepNLU results to a pandas DataFrame """


import os

from baseblock import FileIO
from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData


class ResultsAsDataFrame(BaseObject):
    """ Transform deepNLU results to a pandas DataFrame """

    def __init__(self):
        """ Change History

        Created:
            13-May-2022
            craig@graffl.ai
        """
        BaseObject.__init__(self, __name__)

    def _find_ontology_name(self,
                            swap: dict) -> str:
        """ Find the Ontology this Swap came from

        Args:
            swap (dict): the incoming dictionary swap

        Raises:
            ValueError: Unable to find the source of this swap

        Returns:
            str: The Ontology that triggered this swap
        """

        def entity_exists(ontology: str,
                          input_text: str) -> bool:

            absolute_path = os.path.normpath(
                os.path.join(os.getcwd(), 'resources/data/owl'))
            FileIO.exists_or_error(absolute_path)

            finder = FindOntologyData(
                ontologies=[ontology],
                absolute_path=absolute_path)

            return finder.entity_exists(input_text)

        ontologies = [x.strip() for x in
                      swap['swaps']['ontologies'][0].split(',')]
        if len(ontologies) == 1:
            return ontologies[0]

        for ontology in ontologies:
            if entity_exists(swap['swaps']['canon']):
                return ontology

        raise ValueError(swap['swaps']['canon'])

    def process(self,
                results: list,
                include_position: bool = True) -> list:
        """ Transform deepNLU results to a pandas-compatible input format

        Args:
            results (list): the deepNLU results
            include_position (bool): include positionary elements

        Returns:
            list: a flat list
        """

        summary = []

        for i in range(len(results)):
            paragraph = results[i]

            for j in range(len(paragraph)):
                sentence = paragraph[j]

                if type(sentence) == dict:
                    sentence = [sentence]

                for k in range(len(sentence)):
                    token = sentence[k]

                    for inferred in token['inferred']:  # deepnlu-48
                        summary.append({
                            "Canon": inferred,
                            "Text": inferred,
                            "Ontology": 'inference',
                            "Sentence": sentence[0]['text']})

                    swaps = [x for x in token['tokens']
                             if 'swaps' in x]

                    for swap in swaps:
                        canon = swap['swaps']['canon']
                        d_result = {
                            "Canon": canon,
                            "Text": swap['text'],
                            "Ontology": self._find_ontology_name(swap),
                            "Sentence": sentence[0]['text']}

                        if include_position:
                            d_result["Type"] = swap['swaps']['type']
                            d_result["Pos-X"] = swap['x']
                            d_result["Pos-Y"] = swap['y']
                            d_result["Pos-ID"] = f"{i}-{j}-{k}"

                        summary.append(d_result)

        return summary
