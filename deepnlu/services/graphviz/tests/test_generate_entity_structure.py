
import os
from pprint import pprint

from deepnlu.owlblock.bp import FindOntologyData
from deepnlu.services.graphviz.svc import FindAllRelationships

from deepnlu.services.graphviz.svc import GenerateEntityStructure


def test_service():

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/testing'))

    find_ontology_data = FindOntologyData(ontologies=['unitest'],
                                          absolute_path=absolute_path)
    assert find_ontology_data

    find_all_relationships = FindAllRelationships(find_ontology_data).find
    assert find_all_relationships

    svc = GenerateEntityStructure(
        find_ontology_data=find_ontology_data,
        find_all_relationships=find_all_relationships)
    assert svc

    result = svc.process(entity_names=['weather'])

    pprint(result)


def main():
    test_service()


if __name__ == "__main__":
    main()
