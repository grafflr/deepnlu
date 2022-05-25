from deepnlu.datablock.dmo import NerTypeFinder


def test_version():
    svc = NerTypeFinder(['nursing'])
    assert svc

    assert svc.spacy('nationality') == ['NORP']


def main():
    test_version()


if __name__ == "__main__":
    main()
