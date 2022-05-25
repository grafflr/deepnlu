

import os
from pprint import pprint


from deepnlu.datablock.svc import FindTypes
from baseblock import Stopwatch


def test_ancestors():

    finder = FindTypes('chitchat')
    assert finder

    # testing case sensitivity ...
    assert finder.has_ancestor('favorite_animal_response', 'response')
    assert finder.has_ancestor('Favorite_Animal_Response', 'response')
    assert finder.has_ancestor('FAVORITE_ANIMAL_RESPONSE', 'response')


def main():
    test_ancestors()


if __name__ == "__main__":
    main()
