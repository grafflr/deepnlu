# -*- coding: UTF-8 -*-


import os
import pprint

from baseblock import FileIO

from deepnlu.recipe.svc import ParseTextOneShot
from deepnlu.owlblock.bp import FindOntologyData


def test_service():

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/testing'))
    FileIO.exists_or_error(absolute_path)

    finder = FindOntologyData(
        ontologies=['unitest'],
        absolute_path=absolute_path)

    svc = ParseTextOneShot(finder)
    assert svc

    svcresult = svc.process("registered nurse")
    assert svcresult


def main():
    test_service()


if __name__ == "__main__":
    main()
