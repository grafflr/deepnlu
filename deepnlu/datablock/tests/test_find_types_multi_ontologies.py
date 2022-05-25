

import os
from pprint import pprint


from datablock.svc import FindSynonyms
from baseblock import Stopwatch


def test_fwd_data_single():

    finder = FindSynonyms(['ontologica'])
    assert finder

    d_fwd = finder.fwd_data()
    assert d_fwd

    pprint(d_fwd)
    assert 'similar' in d_fwd


def test_fwd_data_multi_1():

    finder = FindSynonyms(['ontologica', 'appraisal'])
    assert finder

    d_fwd = finder.fwd_data()
    assert d_fwd

    pprint(d_fwd)
    assert 'similar' in d_fwd


def test_fwd_data_multi_2():

    finder = FindSynonyms(['appraisal', 'ontologica'])
    assert finder

    d_fwd = finder.fwd_data()
    assert d_fwd

    pprint(d_fwd)
    assert 'similar' in d_fwd


def main():
    test_fwd_data_single()
    test_fwd_data_multi_1()
    test_fwd_data_multi_2()


if __name__ == "__main__":
    main()
