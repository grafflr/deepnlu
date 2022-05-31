# -*- coding: UTF-8 -*-


import os
from pprint import pprint

from baseblock import FileIO

from deepnlu.recipe.bp import DeepNluAPI

api = DeepNluAPI()
assert api


def test_process():
    """ Test Entity Spans

    Regression Test Reference:
        https://github.com/grafflr/graffl-core/issues/77
    """

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/testing'))
    FileIO.exists_or_error(absolute_path)

    svcresult = api.handle_text(
        input_text="the president of Maryville university said this!",
        ontologies=['TestGC077'],
        absolute_path=absolute_path)

    csvresult = api.to_csv(svcresult, include_position=False)
    entities = [x['Canon'] for x in csvresult]

    assert 'university_president' in entities


def main():
    test_process()


if __name__ == "__main__":
    main()
