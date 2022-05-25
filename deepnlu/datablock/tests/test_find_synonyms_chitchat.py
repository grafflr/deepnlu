import os


from baseblock import Stopwatch

from deepnlu.datablock.svc import FindSynonyms


def test_finder():

    finder = FindSynonyms('chitchat')

    assert finder.find_variants('hi')


def main():
    test_finder()


if __name__ == "__main__":
    main()
