

from pprint import pprint


from baseblock import Enforcer


from imaginor.graphviz.svc import GenerateEntityStructure


def test_service():
    svc = GenerateEntityStructure()
    assert svc

    result = svc.process(entity_names=['weather'],
                         ontologies=['chitchat'])

    pprint(result)


def main():
    test_service()


if __name__ == "__main__":
    main()
