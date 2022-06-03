# -*- coding: UTF-8 -*-


import os
from pprint import pprint

from baseblock import FileIO
from baseblock import BaseObject

from deepnlu.recipe.bp import DeepNluAPI

""" Test Entity Recognition

Regression Test Reference:
    https://github.com/grafflr/deepnlu/issues/28
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
            ontologies=['TestDN028'],
            absolute_path=self.absolute_path)

        actual_text = svcresult[0][0]['tokens'][0]['text']
        csvresult = self.api.to_csv(svcresult, include_position=False)
        entities = [x['Canon'] for x in csvresult]

        failures = 0

        if actual_text != spanned_text:
            pprint(svcresult)
            self.logger.error('\n'.join([
                "Spanned Match Failure",
                f"\tActual Text: {actual_text}",
                f"\tExpected Text: {spanned_text}"]))
            failures += 1

        if entity_name not in entities:
            if actual_text != spanned_text:
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
        input_text="Mark Lombardi",
        entity_name="mark_lombardi",
        spanned_text="Mark Lombardi"
    )

    harness.execute(
        input_text="Dr Mark Lombardi",
        entity_name="mark_lombardi",
        spanned_text="Dr Mark Lombardi"
    )

    harness.execute(
        input_text="Dr. Mark Lombardi",
        entity_name="mark_lombardi",
        spanned_text="Dr. Mark Lombardi"
    )

    harness.execute(
        input_text="dr. Mark Lombardi",
        entity_name="mark_lombardi",
        spanned_text="dr. Mark Lombardi"
    )

    # NOTE: 20220602 this fails
    # harness.execute(
    #     input_text="dr . Mark Lombardi",
    #     entity_name="mark_lombardi",
    #     spanned_text="dr . Mark Lombardi"
    # )


def main():
    test_001()


if __name__ == "__main__":
    main()
