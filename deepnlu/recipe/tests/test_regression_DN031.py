# -*- coding: UTF-8 -*-


import os
from pprint import pprint

from baseblock import FileIO
from baseblock import BaseObject

from deepnlu.recipe.bp import DeepNluAPI
from deepnlu.owlblock.bp import FindOntologyData

""" Key Lookup Error

Regression Test Reference:
    https://github.com/grafflr/deepnlu/issues/31
"""


ONTOLOGIES = ['TestDN031a', 'TestDN031b']


class TestHarness(BaseObject):

    def __init__(self):
        BaseObject.__init__(self, __name__)

        self.absolute_path = os.path.normpath(
            os.path.join(os.getcwd(), 'resources/testing'))
        FileIO.exists_or_error(self.absolute_path)

        self.api = DeepNluAPI()

        self.finder = FindOntologyData(
            ontologies=ONTOLOGIES,
            absolute_path=self.absolute_path)

    def parse(self,
              input_text: str) -> list:
        svcresult = self.api.handle_text(
            input_text=input_text,
            ontologies=ONTOLOGIES,
            absolute_path=self.absolute_path)

        to_csv = self.api.to_csv(svcresult)
        print (to_csv)

    def execute(self,
                input_text: str,
                entity_name: str,
                spanned_text: str) -> None:

        self.parse(input_text)


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
