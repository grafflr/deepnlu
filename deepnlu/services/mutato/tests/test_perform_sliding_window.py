import os

from deepnlu.datablock.svc import FindLookup
from deepnlu.services.mutato.dmo import ExactMatchFinder

lookup_data = FindLookup(['nursing']).data()


def test_gram_size_1():

    tokens = [
        {
            "normal": "americans",
        }
    ]

    svc = ExactMatchFinder(gram_size=1,
                           d_lookup=lookup_data)
    assert svc

    result = svc.process(tokens)
    assert result
    assert type(result) == list

    actual_result = [x['normal'] for x in result[0]]
    assert actual_result == ['americans']


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

    result = svc.process(tokens)
    assert result
    assert type(result) == list

    actual_result = [x['normal'] for x in result[0]]
    assert actual_result == ['registered', 'nurse']


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

    result = svc.process(tokens)
    assert result
    assert type(result) == list

    actual_result = [x['normal'] for x in result[0]]
    assert actual_result == ['american', 'nurses', 'association']


def main():
    test_gram_size_1()
    test_gram_size_2()
    test_gram_size_3()


if __name__ == "__main__":
    main()
