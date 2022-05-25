
from pprint import pprint

from datablock.svc import FindReviews

finder = FindReviews()
assert finder


# def test_find_comments_by_implies() -> None:

#     # test an input string
#     results = finder.find_comments_by_implies('learning_curve')
#     print(results)
#     assert results
#     assert type(results) == list

#     # test an input list with one value
#     results = finder.find_comments_by_implies(['learning_curve'])
#     print(results)
#     assert results
#     assert type(results) == list
#     assert len(results)
#     assert type(results[0]) == list  # assert a list of lists

#     # test an input list with multiple values
#     results = finder.find_comments_by_implies([
#         'accelerate_change', 'learning_curve'])
#     print(results)
#     assert results
#     assert type(results) == list


# def test_find_common_comments() -> None:

#     tokens = ['goal_seeker']

#     results = finder.find_common_comments(tokens)
#     print(results)
#     assert (results)
#     assert type(results) == list
#     assert len(results)
#     assert type(results[0]) == str  # list of strings


def test_is_implies() -> None:
    # assert finder.is_implies('effect')
    assert not finder.is_implies('blah')


def test_group_comments_by_category() -> None:
    results = finder.group_comments_by_category([
        'displays strong analytical qualities',
        'places high priority projects on a special assignment basis',
        'makes a strong effort to keep expenditures within budget',
        'assists employees in career assessment',
    ])

    pprint(results)
    assert results
    assert type(results) == dict

    for k in results:

        # the dictionary keys must be strings
        assert type(k) == str

        # the value for each key must be a list
        assert type(results[k]) == list

        # and the value in each list
        for value in results[k]:

            # must be a string
            assert type(value) == str


def main():
    test_is_implies()
    # test_find_common_comments()
    test_group_comments_by_category()


if __name__ == "__main__":
    import plac

    plac.call(main)
