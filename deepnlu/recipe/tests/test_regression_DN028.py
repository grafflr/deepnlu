# -*- coding: UTF-8 -*-


import os
from pprint import pprint

from baseblock import FileIO

from deepnlu.recipe.bp import DeepNluAPI

""" Test Entity Recognition

Regression Test Reference:
    https://github.com/grafflr/deepnlu/issues/28
"""

api = DeepNluAPI()
assert api

absolute_path = os.path.normpath(
    os.path.join(os.getcwd(), 'resources/testing'))
FileIO.exists_or_error(absolute_path)


def execute(input_text: str) -> list:
    svcresult = api.handle_text(
        input_text=input_text,
        ontologies=['TestDN028'],
        absolute_path=absolute_path)

    pprint(svcresult)

    csvresult = api.to_csv(svcresult, include_position=False)
    entities = [x['Canon'] for x in csvresult]
    print(entities)

    return entities


def test_001():
    # assert 'mark_lombardi' in execute("Mark Lombardi")
    assert 'mark_lombardi' in execute("Dr. Mark Lombardi")
    # assert 'mark_lombardi' in execute("dr. Mark Lombardi")
    # assert 'mark_lombardi' in execute("dr . Mark Lombardi")


def main():
    test_001()


if __name__ == "__main__":
    main()
