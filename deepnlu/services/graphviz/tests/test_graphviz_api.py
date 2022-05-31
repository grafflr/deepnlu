

from baseblock import Enforcer


from imaginor.graphviz.bp import GraphvizAPI


def test_process():

    generate_graph = GraphvizAPI().generate
    assert generate_graph

    generate_graph(entity_names=['nursing_school'],
                   ontologies=['nursing'])


def main():
    test_process()


if __name__ == "__main__":
    main()
