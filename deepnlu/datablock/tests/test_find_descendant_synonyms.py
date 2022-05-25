

import os
from pprint import pprint

from baseblock import Stopwatch


from deepnlu.datablock.bp import FindData


def test_recipe_1():

    # input
    ONTi14N = 'chitchat'
    entity = 'greeting_response'

    api = FindData()

    result = api.find_descendant_synonyms(entity_name=entity,
                                          ontology_name=ONTi14N)
    print(result)

    assert result
    assert type(result) == list
    assert len(result)


def test_recipe_2():

    # input
    ONTi14N = 'chitchat'
    entity = 'hello_response'

    api = FindData()

    result = api.find_descendant_synonyms(entity_name=entity,
                                          ontology_name=ONTi14N)
    print(result)

    assert result
    assert type(result) == list
    assert len(result)


def test_recipe_3():

    # input
    ONTi14N = 'chitchat'
    entity = 'adorkable_response'

    api = FindData()

    result = api.find_descendant_synonyms(entity_name=entity,
                                          ontology_name=ONTi14N)
    print(result)

    assert result
    assert type(result) == list
    assert len(result)


def main():
    test_recipe_3()


if __name__ == "__main__":
    main()
