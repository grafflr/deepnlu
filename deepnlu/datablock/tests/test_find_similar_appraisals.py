import os


from deepnlu.datablock.svc import FindSimilar


def test_load() -> None:

    svc = FindSimilar('appraisal')
    assert svc

    results = svc.is_similar_to('prt_7433166876723966947')
    assert results
    assert type(results) == list

    results = svc.is_similar_to_random_n('prt_7433166876723966947', 5)
    print(results)


def main():
    test_load()


if __name__ == "__main__":
    main()
