# -*- coding: UTF-8 -*-


import os
from pprint import pprint

from baseblock import FileIO

from deepnlu.recipe.bp import DeepNluAPI

""" Test Entity Recognition

Regression Test Reference:
    https://github.com/grafflr/deepnlu/issues/22
"""

api = DeepNluAPI()
assert api

absolute_path = os.path.normpath(
    os.path.join(os.getcwd(), 'resources/testing'))
FileIO.exists_or_error(absolute_path)


def test_001():
    """ Baseline Test Case: This works """

    svcresult = api.handle_text(
        input_text="student-athlete graduation rate",
        ontologies=['TestDN022'],
        absolute_path=absolute_path)

    csvresult = api.to_csv(svcresult, include_position=False)
    entities = [x['Canon'] for x in csvresult]

    assert 'student_athlete_graduation_rate' in entities


def test_002():
    """ Defective Test Case: Ensure this works """

    svcresult = api.handle_text(
        input_text="Maryville has also been honored with the NCAA Division II Presidents’ Award for Academic Excellence for the 4 out of the last 5 years—including one year in which Maryville was the only school in the U.S. with a 100 percent student-athlete graduation rate. ",
        ontologies=['TestDN022'],
        absolute_path=absolute_path)

    csvresult = api.to_csv(svcresult, include_position=False)
    entities = [x['Canon'] for x in csvresult]

    assert 'student_athlete_graduation_rate' in entities


def main():
    # test_001()
    test_002()


if __name__ == "__main__":
    main()
