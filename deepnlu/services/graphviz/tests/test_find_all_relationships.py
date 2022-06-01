import os

from baseblock import FileIO

from deepnlu.owlblock.bp import FindOntologyData
from deepnlu.services.graphviz.svc import FindAllRelationships


def test_process():

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/testing'))

    find_ontology_data = FindOntologyData(ontologies=['unitest'],
                                          absolute_path=absolute_path)
    assert find_ontology_data

    find_all_relationships = FindAllRelationships(find_ontology_data)
    assert find_all_relationships

    entity_name = "Activity"

    results = find_all_relationships.find(
        entity_name=entity_name,
        find_requires=True,
        find_similar=True,
        find_implies=True,
        find_ancestors=True,
        find_descendants=True)

    [print(x) for x in results]


def main():
    test_process()


if __name__ == "__main__":
    main()
