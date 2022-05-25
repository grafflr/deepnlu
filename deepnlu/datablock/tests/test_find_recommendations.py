

import os
from pprint import pprint
from baseblock import Enforcer
from baseblock import Stopwatch

from deepnlu.datablock.svc import FindRecommendations


def test_exists():

    svc = FindRecommendations()
    assert svc

    Enforcer.is_dict(svc.fwd())
    Enforcer.is_dict(svc.rev())

    Enforcer.is_list(svc.random_comments(5))
    Enforcer.is_str(svc.random_comment())

    Enforcer.is_list(svc.implies_by_comment(
        'it was a pleasure working with you'))
    Enforcer.is_none(svc.implies_by_comment(
        'blah blah blah'))

    Enforcer.is_list(svc.comments_by_implies(
        ['colleague', 'great']))
    Enforcer.is_none(svc.comments_by_implies(
        ['alpha', 'beta']))


def main():
    test_exists()


if __name__ == "__main__":
    main()
