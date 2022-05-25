

import os
from baseblock import Stopwatch

from datablock.svc import FindLookup


def test_exists():

    sw = Stopwatch()

    os.environ['GRAFFL_ONTOLOGIES'] = "nursing, skills"
    svc = FindLookup()

    assert svc.grams(1)
    assert len(svc.grams(1)) > 1

    print(str(sw))

    os.environ['GRAFFL_ONTOLOGIES'] = "skills"
    total_grams_skills = len(FindLookup().grams(1))

    os.environ['GRAFFL_ONTOLOGIES'] = "nursing"
    total_grams_nursing = len(FindLookup().grams(1))

    total_grams_all = len(svc.grams(1))

    assert total_grams_all == total_grams_nursing + total_grams_skills


def main():
    test_exists()


if __name__ == "__main__":
    main()
