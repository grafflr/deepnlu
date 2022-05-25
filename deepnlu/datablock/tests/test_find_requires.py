

from deepnlu.datablock.bp import FindData
from deepnlu.datablock.svc import FindRequires
from baseblock import Stopwatch


import os


def test_skills():

    finder = FindRequires('skills')
    assert finder

    assert finder.requires('lecturer')
    assert finder.required_by('communication')


def test_by_ancestor():
    api = FindData()
    assert api

    result = api.find_requires(entity_name='late_train',
                               ontology_name='chitchat')
    print(result)
    # assert result


def test_chitchat_adorkable():
    api = FindData()
    assert api

    result = api.find_requires(entity_name='adorkable',
                               ontology_name='chitchat')
    print(result)
    assert result


def main():
    test_skills()
    test_by_ancestor()
    test_chitchat_adorkable()


if __name__ == "__main__":
    main()
