

import os
from pprint import pprint

from baseblock import Stopwatch


from deepnlu.datablock.svc import FindTypes
from deepnlu.datablock.svc import FindSynonyms


def test_descendants():
    finder = FindTypes(['chitchat'])
    assert finder

    assert finder.descendants('greeting')
