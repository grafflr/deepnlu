

import os
from baseblock import Stopwatch

from deepnlu.datablock.svc import FindLookup


def test_exists():

    sw = Stopwatch()

    svc = FindLookup(['nursing', 'skills'])

    assert svc.grams(1)
    assert len(svc.grams(1)) > 1

    print(str(sw))

    total_grams_skills = len(FindLookup(['skills']).grams(1))
    total_grams_nursing = len(FindLookup(['nursing']).grams(1))

    total_grams_all = len(svc.grams(1))

    assert total_grams_all == total_grams_nursing + total_grams_skills


def main():
    test_exists()


if __name__ == "__main__":
    main()
