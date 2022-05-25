#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Transform deepNLU results to a pandas DataFrame """


from baseblock import BaseObject
from datablock.svc import FindLabels


class ResultsAsDataFrame(BaseObject):
    """ Transform deepNLU results to a pandas DataFrame """

    __d_finders = {}

    def __init__(self):
        """ Change History

        Created:
            13-May-2022
            craig@grafflr.ai
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
        ontologies = [x.strip() for x in
                      swap['swaps']['ontologies'][0].split(',')]
        if len(ontologies) == 1:
            return ontologies[0]

        for ontology in ontologies:
            if ontology not in self.__d_finders:
                self.__d_finders[ontology] = FindLabels(ontology)
            if self.__d_finders[ontology].exists(swap['swaps']['canon']):
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
