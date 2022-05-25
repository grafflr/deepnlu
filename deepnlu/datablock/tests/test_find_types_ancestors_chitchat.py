

import os
from pprint import pprint


from datablock.svc import FindTypes
from baseblock import Stopwatch


def test_ancestors():

    finder = FindTypes('chitchat')
    assert finder
    assert finder.fwd_data()

    def _ancestors(term: str) -> None:
        ancestors = finder.ancestors(term)
        assert ancestors
        assert len(ancestors) > 0
        print(f"Ancestors of {term}: {ancestors}")

    _ancestors('bus')


def main():
    test_ancestors()


if __name__ == "__main__":
    main()
