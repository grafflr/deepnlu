import os

from baseblock import FileIO
from baseblock import Enforcer

from deepnlu.owlblock.bp import FindOntologyData
from deepnlu.services.mutato.dmo import ExactMatchFinder


absolute_path = os.path.normpath(
    os.path.join(os.getcwd(), 'resources/testing'))
FileIO.exists_or_error(absolute_path)

finder = FindOntologyData(
    ontologies=['unitest'],
    absolute_path=absolute_path)

lookup_data = finder.lookup()
Enforcer.is_dict(lookup_data)


def test_gram_size_1():

    tokens = [
        {
            "normal": "americans",
        }
    ]

    svc = ExactMatchFinder(gram_size=1,
                           d_lookup=lookup_data)
    assert svc

    svc.process(tokens)


def test_gram_size_2():

    tokens = [
        {
            "normal": "registered",
        },
        {
            "normal": "nurse",
        }
    ]

    svc = ExactMatchFinder(gram_size=2,
                           d_lookup=lookup_data)
    assert svc

    svc.process(tokens)


def test_gram_size_3():

    tokens = [
        {
            "normal": "the",
        },
        {
            "normal": "american",
        },
        {
            "normal": "nurses",
        },
        {
            "normal": "association",
        },
        {
            "normal": "is",
        },
        {
            "normal": "here",
        },
    ]

    svc = ExactMatchFinder(gram_size=3,
                           d_lookup=lookup_data)
    assert svc

    svc.process(tokens)


def main():
    test_gram_size_1()
    test_gram_size_2()
    test_gram_size_3()


if __name__ == "__main__":
    main()
