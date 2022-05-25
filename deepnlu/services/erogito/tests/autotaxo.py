import os

from baseblock import FileIO
from baseblock import Enforcer

from erogito import ErogitoAPI


def driver(input_text: str):
    api = ErogitoAPI()
    assert api

    result = api.taxonomy(input_text)
    Enforcer.is_optional_list(result)

    [print(x) for x in result]


def main(input_text):
    driver(input_text)


if __name__ == '__main__':
    import plac

    plac.call(main)
