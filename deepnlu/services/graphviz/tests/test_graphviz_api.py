import os

from baseblock import FileIO

from deepnlu.owlblock.bp import FindOntologyData
from deepnlu.services.graphviz.bp import GraphvizAPI


def test_process():

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/testing'))
    FileIO.exists(absolute_path)

    find_ontology_data = FindOntologyData(
        ontologies=['unitest'],
        absolute_path=absolute_path)
    assert find_ontology_data

    generate_graph = GraphvizAPI(find_ontology_data).generate
    assert generate_graph

    generate_graph(entity_names=['nursing_school'])


def main():
    test_process()


if __name__ == "__main__":
    main()
