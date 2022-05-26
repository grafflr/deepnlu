

import os
from pprint import pprint


from deepnlu.datablock.svc import FindLabels
from baseblock import Stopwatch


def test_via_params_as_list():

    finder = FindLabels(['nursing'])
    assert finder
    assert finder.data()

    print(finder.label('urgent_care'))
    assert finder.label('urgent_care')


def test_find_age():
    finder = FindLabels(['demographics'])
    assert finder.exists('age')


def main():
    test_find_age()
    test_via_params_as_list()


if __name__ == "__main__":
    main()
