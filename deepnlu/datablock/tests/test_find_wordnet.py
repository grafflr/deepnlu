
from baseblock import Stopwatch

from deepnlu.datablock.svc import FindWordnet

finder = FindWordnet()
assert finder


def test_exists():

    sw = Stopwatch()
    assert finder.exists('waddling')
    print(str(sw))

    sw = Stopwatch()
    assert not finder.exists('waddling22')
    print(str(sw))

    sw = Stopwatch()
    assert finder.exists('myxovirus')
    print(str(sw))

    sw = Stopwatch()
    assert finder.exists('according')
    print(str(sw))

    sw = Stopwatch()
    assert finder.exists('acetabulars')
    print(str(sw))


def main():
    test_exists()


if __name__ == "__main__":
    main()
