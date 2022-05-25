from mutato import __version__

from mutato.dmo import SlidingWindowBlacklist
from datablock.os import d_candidate_synonym_blacklist


def test_component():

    candidates = [
        [
            {
                "normal": "at",
            },
            {
                "normal": "this",
            },
            {
                "normal": "time",
            }
        ],
        [
            {
                "normal": "alpha",
            },
            {
                "normal": "beta",
            },
            {
                "normal": "gamma",
            }
        ]
    ]

    dmo = SlidingWindowBlacklist(gram_size=3,
                                 candidates=candidates,
                                 blacklist=d_candidate_synonym_blacklist[3])
    assert dmo

    results = dmo.process()
    assert results
    assert type(results) == list

    assert results == [
        [
            {'normal': 'alpha'},
            {'normal': 'beta'},
            {'normal': 'gamma'}
        ]
    ]


def main():
    test_component()


if __name__ == "__main__":
    main()
