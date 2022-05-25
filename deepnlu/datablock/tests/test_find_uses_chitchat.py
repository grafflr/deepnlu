

from datablock.svc import FindUses
from baseblock import Stopwatch


import os


def test_uses_1():

    finder = FindUses('chitchat')
    assert finder

    result = finder.uses('monday')
    print(result)


def main():
    test_uses_1()


if __name__ == "__main__":
    main()
