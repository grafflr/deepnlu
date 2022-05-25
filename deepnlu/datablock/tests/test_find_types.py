

import os
from pprint import pprint


from deepnlu.datablock.svc import FindTypes
from baseblock import Stopwatch


os.environ['GRAFFL_ONTOLOGIES'] = "nursing"

finder = FindTypes()
assert finder
assert finder.fwd_data()
assert finder.exists('nursing')


def test_ancestors():

    def _ancestors(term: str) -> None:
        ancestors = finder.ancestors(term)
        assert ancestors
        assert len(ancestors) > 0
        print(f"Ancestors of {term}: {ancestors}")

    _ancestors('nursing')
    _ancestors('urgent_care')
    _ancestors('psychiatric_mental_health_nurse_practitioner')


def test_children():

    def _children(term: str) -> None:
        children = finder.children(term)
        assert children
        assert len(children) > 0
        print(f"Children of {term}: {children}")

    _children('diploma')
    _children('nursing')


def test_descendants():

    def _descendants(term: str) -> None:
        descendants = finder.descendants(term)
        assert descendants
        assert len(descendants) > 0
        print(f"Descendants of {term}: {descendants}")

    _descendants('nurse')
    _descendants('health')


def test_parents():

    def _parents(term: str) -> None:
        parents = finder.parents(term)
        assert parents
        assert len(parents) > 0
        print(f"Parents of {term}: {parents}")

    _parents('patient')


def main():
    test_ancestors()
    test_children()
    test_descendants()
    test_parents()


if __name__ == "__main__":
    main()
