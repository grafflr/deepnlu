

import os

from baseblock import FileIO

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.mutato.dmo import ExactMatchSwapper


def test_component():

    ont14n = 'chitchat'

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/data/owl'))
    FileIO.exists_or_error(absolute_path)

    finder = FindOntologyData(
        ontologies=[ont14n],
        absolute_path=absolute_path)

    dmo = ExactMatchSwapper(finder)
    assert dmo


def main():
    test_component()


if __name__ == "__main__":
    main()
