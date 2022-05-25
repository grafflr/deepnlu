import os

from deepnlu.datablock.bp import FindData


def test_find_data() -> None:

    bp = FindData()
    assert bp

    results = bp.find_implies(
        entity_name='nursing_school', ontology_name='nursing')
    assert results


def main():
    test_find_data()


if __name__ == "__main__":
    main()
