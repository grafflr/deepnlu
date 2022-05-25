from mutato import __version__


import os
import logging
from pprint import pprint

from mutato.bp import MutatoAPI


def test_service():

    bp = MutatoAPI('chitchat')
    assert bp

    tokens = [
        {
            'ent': 'PERSON',
            'id': '7#23#11174346320140919546',
            'normal': 'john',
            'stem': 'john',
            'text': 'John ',
            'x': 19,
            'y': 23
        },
        {
            'ent': 'PERSON',
            'id': '9#29#1620733109687891090',
            'normal': 'doe',
            'stem': 'doe',
            'text': 'Doe',
            'x': 24,
            'y': 27
        },
        {
            'id': '0#0#7199752172782760331',
            'normal': 'late',
            'stem': 'late',
            'text': 'late ',
            'x': 0,
            'y': 4
        },
        {
            'id': '2#6#15155854979279043342',
            'normal': 'bus',
            'stem': 'bu',
            'text': 'bus',
            'x': 5,
            'y': 8
        },
        {
            'id': 1,
            'x': 10,
            'y': 1,
            'normal': 'gamma',
            'stem': 'gamma',
            'text': 'gamma ',
            'ent': '',
        },
        {
            'id': 2,
            'x': 12,
            'y': 2,
            'normal': 'delta',
            'stem': 'delta',
            'text': 'delta ',
            'ent': '',
        },
    ]

    swaps = bp.swap(tokens)
    pprint(swaps)


def main():
    test_service()


if __name__ == "__main__":
    main()
