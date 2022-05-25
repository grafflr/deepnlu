

from deepnlu.datablock.svc import FindReviews


def test_dict() -> None:

    finder = FindReviews()
    assert finder

    d_comments_fwd = finder.comments_fwd()
    assert d_comments_fwd
    assert type(d_comments_fwd) == dict
    assert len(d_comments_fwd)

    d_comments_rev = finder.comments_rev()
    assert d_comments_rev
    assert type(d_comments_rev) == dict
    assert len(d_comments_rev)

    d_categories_fwd = finder.categories_fwd()
    assert d_categories_fwd
    assert type(d_categories_fwd) == dict
    assert len(d_categories_fwd)

    d_categories_rev = finder.categories_rev()
    assert d_categories_rev
    assert type(d_categories_rev) == dict
    assert len(d_categories_rev)

    d_knockouts_fwd = finder.knockouts_fwd()
    assert d_knockouts_fwd
    assert type(d_knockouts_fwd) == dict
    assert len(d_knockouts_fwd)

    d_knockouts_rev = finder.knockouts_rev()
    assert d_knockouts_rev
    assert type(d_knockouts_rev) == dict
    assert len(d_knockouts_rev)

    results = finder.knockouts_by_gram_level(1)
    assert results
    assert type(results) == list
    assert len(results)

    results = finder.knockouts_by_gram_level(2)
    assert results
    assert type(results) == list
    assert len(results)


def main():
    test_dict()


if __name__ == "__main__":
    import plac

    plac.call(main)
