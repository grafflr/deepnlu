# -*- coding: UTF-8 -*-
""" Execute the Recipe for the "Round-Trip" Engine """

import os
from pprint import pprint

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData


class FindOntologyDataRunner(BaseObject):
    """ Execute the Recipe for the "Find-Ontology-Data" Engine """

    def __init__(self):
        """ Change History

        Created:
            6-Jun-2022
            craig@graffl.ai
            *   https://github.com/grafflr/deepnlu/issues/38
        """
        BaseObject.__init__(self, __name__)
        self._absolute_path = self._get_absolute_path()

    def _get_absolute_path(self) -> str:
        absolute_path = os.path.normpath(os.path.join(
            os.getcwd(), EnvIO.str_or_exception('TEST_ONTO_LOCATION')))
        FileIO.exists_or_error(absolute_path)

        return absolute_path

    def process(self,
                ontologies: list,
                input_text: str) -> dict:
        """ Execute the "Find-Ontology-Data" Recipe on the Input Text

        Args:
            ontologies (list): a list of 1..* ontologies to test with
            input_text (str): input text of any size or content

        Returns:
            dict: the finder results
        """

        absolute_path = self._get_absolute_path()

        finder = FindOntologyData(
            ontologies=ontologies,
            absolute_path=absolute_path)

        canon = finder.find_canon(input_text)
        variants = finder.find_variants(input_text)
        is_canon = finder.is_canon(input_text)
        is_variant = finder.is_variant(input_text)

        return {
            'is_canon': is_canon,
            'is_variant': is_variant,
            'canon': canon,
            'variants': variants,
        }
