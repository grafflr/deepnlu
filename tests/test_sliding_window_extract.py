from deepnlu.services.mutato import __version__

from deepnlu.services.mutato.dmo import SlidingWindowExtract


def test_component():
    tokens = ['Most', 'people', 'think', 'of', 'the', 'nursing', 'profession',
              'as', 'beginning', 'with', 'the', 'work', 'of', 'Florence', 'Nightingale']

    dmo = SlidingWindowExtract(tokens=tokens, gram_size=3)
    assert dmo

    result = dmo.process()
    assert result
    assert type(result) == list

    assert result == [
        ['Most', 'people', 'think'],
        ['people', 'think', 'of'],
        ['think', 'of', 'the'],
        ['of', 'the', 'nursing'],
        ['the', 'nursing', 'profession'],
        ['nursing', 'profession', 'as'],
        ['profession', 'as', 'beginning'],
        ['as', 'beginning', 'with'],
        ['beginning', 'with', 'the'],
        ['with', 'the', 'work'],
        ['the', 'work', 'of'],
        ['work', 'of', 'Florence'],
        ['of', 'Florence', 'Nightingale']
    ]


def main():
    test_component()


if __name__ == "__main__":
    main()
