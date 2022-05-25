

import os
from pprint import pprint

from baseblock import Stopwatch


from datablock.svc import FindTypes
from datablock.svc import FindSynonyms


def test_descendants():
    finder = FindTypes('chitchat')
    assert finder

    assert finder.descendants('greeting')
