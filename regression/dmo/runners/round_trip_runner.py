# -*- coding: UTF-8 -*-
""" Execute the Recipe for the "Round-Trip" Engine """

import os
from pprint import pprint

from baseblock import FileIO
from baseblock import BaseObject

from deepnlu.recipe.bp import DeepNluAPI


class RoundTripRunner(BaseObject):
    """ Execute the Recipe for the "Round-Trip" Engine """

    def __init__(self):
        BaseObject.__init__(self, __name__)
        self._absolute_path = self._get_absolute_path()

    def _get_absolute_path(self) -> str:
        absolute_path = os.path.normpath(
            os.path.join(os.getcwd(), 'resources/testing'))
        FileIO.exists_or_error(absolute_path)

        return absolute_path

    def process(self,
                d_test_case: dict) -> None:

        api = DeepNluAPI()

        pprint(d_test_case)

        svcresult = api.handle_text(
            input_text=d_test_case['input'],
            ontologies=d_test_case['ontologies'],
            absolute_path=self._absolute_path)

        actual_texts = [x['text'].strip() for x in svcresult[0][0]['tokens']]

        csvresult = api.to_csv(svcresult, include_position=False)
        entities = [x['Canon'] for x in csvresult]

        return {
            'canon': entities,
            'text': actual_texts
        }
