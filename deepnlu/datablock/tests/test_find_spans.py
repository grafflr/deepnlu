

import os
import pprint


from datablock.svc import FindSpans
from baseblock import Stopwatch


def test_ner():

    os.environ['GRAFFL_ONTOLOGIES'] = "medical, nursing"

    finder = FindSpans()
    assert finder

    # Prove the 'keys' functionality across both dictionaries
    assert finder.keys()
    assert len(finder.keys())
    print('\n'*2)
    print("First 3 Keys: ")
    print(list(finder.keys())[:3])


def main():
    test_ner()


if __name__ == "__main__":
    main()
