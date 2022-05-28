

import os

from baseblock import FileIO

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.mutato.dmo import ExactMatchSwapper


def test_component():

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources'))
    FileIO.exists_or_error(absolute_path)

    finder = FindOntologyData(
        ontologies=['unitest'],
        absolute_path=absolute_path)

    dmo = ExactMatchSwapper(finder)
    assert dmo


def main():
    test_component()


if __name__ == "__main__":
    main()
