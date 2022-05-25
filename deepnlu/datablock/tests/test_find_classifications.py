import os

from datablock.svc import FindClassifications


def test_load() -> None:
    svc = FindClassifications('chitchat')
    assert svc

    assert svc.include_one_of is not None
    assert svc.include_all_of is not None
    assert svc.exclude_one_of is not None
    assert svc.exclude_all_of is not None

    # assert svc.score('RANDOM_CATEGORIES#3')


def main():
    test_load()


if __name__ == "__main__":
    main()
