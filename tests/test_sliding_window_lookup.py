from deepnlu.services.mutato import __version__


import os
from deepnlu.services.mutato.dmo import SlidingWindowLookup


def test_component():
    from datablock.svc import FindLookup

    os.environ['GRAFFL_ONTOLOGIES'] = 'nursing'
    lookup_data = FindLookup().data()

    candidates = [
        [
            {
                "normal": "think",
            },
            {
                "normal": "of",
            },
            {
                "normal": "american",
            }
        ],
        [
            {
                "normal": "of",
            },
            {
                "normal": "american",
            },
            {
                "normal": "nurses",
            },
        ],
        [
            {
                "normal": "american",
            },
            {
                "normal": "nurses",
            },
            {
                "normal": "association",
            },
        ]
    ]

    dmo = SlidingWindowLookup(gram_size=3,
                              candidates=candidates,
                              d_runtime_kb=lookup_data)
    assert dmo

    result = dmo.process()
    assert result
    assert type(result) == list

    actual_output = [x['normal'] for x in result[0]]
    assert actual_output == ['american', 'nurses', 'association']


def main():
    test_component()


if __name__ == "__main__":
    main()
