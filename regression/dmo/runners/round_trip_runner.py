# -*- coding: UTF-8 -*-
""" Execute the Recipe for the "Round-Trip" Engine """

import os
from pprint import pprint

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import BaseObject

from deepnlu.recipe.bp import DeepNluAPI


class RoundTripRunner(BaseObject):
    """ Execute the Recipe for the "Round-Trip" Engine """

    def __init__(self):
        """ Change History

        Created:
            6-Jun-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/34
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
        """ Execute the "Round-Trip" Recipe on the Input Text

        Args:
            ontologies (list): a list of 1..* ontologies to test with
            input_text (str): input text of any size or content

        Returns:
            _type_: the receipe result
        """

        api = DeepNluAPI()

        svcresult, tokens = api.handle_text(
            input_text=input_text,
            ontologies=ontologies,
            absolute_path=self._absolute_path)

        actual_texts = [x['text'].strip() for x in svcresult[0][0]['tokens']]

        return {
            'canon': tokens,
            'text': actual_texts
        }
