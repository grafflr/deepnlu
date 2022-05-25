

import os
from pprint import pprint


from deepnlu.datablock.svc import FindInference
from baseblock import Stopwatch


def test_requires():

    os.environ['GRAFFL_ONTOLOGIES'] = "nursing"

    finder = FindInference()
    assert finder

    sw = Stopwatch()
    assert finder.requires().data()
    assert finder.requires().data()
    assert finder.requires().data()
    assert finder.requires().data()
    assert finder.requires().data()
    assert finder.requires().data()
    assert finder.requires().triggers()
    assert finder.requires().triggers()
    assert finder.requires().triggers()
    print(str(sw))

    pprint(finder.requires().data())
    pprint(finder.requires().triggers())


def test_effects():

    os.environ['GRAFFL_ONTOLOGIES'] = "nursing"

    finder = FindInference()
    assert finder

    sw = Stopwatch()
    assert finder.effects().fwd()
    assert finder.effects().rev()
    assert finder.effects().fwd()
    assert finder.effects().rev()
    assert finder.effects().fwd()
    assert finder.effects().rev()
    assert finder.effects().fwd()
    assert finder.effects().rev()
    print(str(sw))

    pprint(finder.effects().fwd())
    pprint(finder.effects().rev())


def main():
    test_requires()
    test_effects()


if __name__ == "__main__":
    main()
