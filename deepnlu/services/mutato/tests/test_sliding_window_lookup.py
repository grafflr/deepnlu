import os

from baseblock import FileIO
from baseblock import Enforcer

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.mutato.dmo import SlidingWindowLookup


def test_component():
    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/testing'))
    FileIO.exists_or_error(absolute_path)

    finder = FindOntologyData(
        ontologies=['unitest'],
        absolute_path=absolute_path)

    candidates = [
        [
            {
                "normal": "think",
            },
            {
                "normal": "of",
            },
            {
                "normal": "american",
            }
        ],
        [
            {
                "normal": "of",
            },
            {
                "normal": "american",
            },
            {
                "normal": "nurses",
            },
        ],
        [
            {
                "normal": "american",
            },
            {
                "normal": "nurses",
            },
            {
                "normal": "association",
            },
        ]
    ]

    dmo = SlidingWindowLookup(gram_size=3,
                              candidates=candidates,
                              d_runtime_kb=finder.lookup())
    assert dmo

    result = dmo.process()
    Enforcer.is_optional_list(result)


def main():
    test_component()


if __name__ == "__main__":
    main()
