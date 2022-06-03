# -*- coding: UTF-8 -*-


import os
from pprint import pprint

from baseblock import FileIO
from baseblock import BaseObject

from deepnlu.recipe.bp import DeepNluAPI

""" Key Lookup Error

Regression Test Reference:
    https://github.com/grafflr/deepnlu/issues/31
"""


class TestHarness(BaseObject):

    def __init__(self):
        BaseObject.__init__(self, __name__)
        self.api = DeepNluAPI()
        assert self.api
        self.absolute_path = os.path.normpath(
            os.path.join(os.getcwd(), 'resources/testing'))
        FileIO.exists_or_error(self.absolute_path)

    def execute(self,
                input_text: str,
                entity_name: str,
                spanned_text: str) -> None:

        svcresult = self.api.handle_text(
            input_text=input_text,
            ontologies=['TestDN031'],
            absolute_path=self.absolute_path)

        actual_texts = [x['text'] for x in svcresult[0][0]['tokens']]

        csvresult = self.api.to_csv(svcresult, include_position=False)
        entities = [x['Canon'] for x in csvresult]

        failures = 0

        if spanned_text not in actual_texts:
            self.logger.error('\n'.join([
                "Spanned Match Failure",
                f"\tActual Texts: {actual_texts}",
                f"\tExpected Text: {spanned_text}"]))
            failures += 1

        if entity_name not in entities:
            self.logger.error('\n'.join([
                "Entity Match Failure",
                f"\tActual Entities: {entities}",
                f"\tExpected Entity: {entity_name}"]))
            failures += 1

        if failures > 0:
            raise ValueError(f"Total Failures: {failures}")


def test_001():

    harness = TestHarness()

    harness.execute(
        input_text="Associate VP for Academic Affairs",
        entity_name="academic_affairs",
        spanned_text="Academic Affairs"
    )


def main():
    test_001()


if __name__ == "__main__":
    main()
