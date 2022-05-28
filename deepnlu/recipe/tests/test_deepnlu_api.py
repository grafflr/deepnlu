# -*- coding: UTF-8 -*-
import pprint


from deepnlu.recipe.bp import DeepNluAPI
from deepnlu.owlblock.bp import FindOntologyData


def test_service():

    api = DeepNluAPI()
    assert api


def main():
    test_service()


if __name__ == "__main__":
    main()
