# -*- coding: UTF-8 -*-


import os


from baseblock import FileIO
from baseblock import EnvIO


from deepnlu.services.erogito import ErogitoAPI


def test_api_parse():
    assert ErogitoAPI().parse(['great', 'people', ',', 'said', 'John', 'Doe'])


def test_api_displacy():
    relative_path = 'apps/recipes/deepnlu/regression/output/Grafflr-Core-0020-003.json'

    file_path = os.path.normpath(os.path.join(
        EnvIO.str_or_exception('GRAFFLR_HOME'),
        relative_path))

    FileIO.exists_or_error(file_path)

    tokens = FileIO.read_json(file_path)

    assert ErogitoAPI().displacy(tokens)


def main():
    test_api_parse()


if __name__ == "__main__":
    main()
