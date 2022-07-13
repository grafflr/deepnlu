
from deepnlu.services.portendo.entity.bp import EntityOrchestrator


def test_portendo_1():

    entity_names = ['network_topology']
    input_tokens = ['network', 'topology']

    api = EntityOrchestrator(entity_names)
    assert api

    svcresult = api.run(input_tokens)
    assert type(svcresult) == dict

    assert svcresult == {
        'result': ['network_topology'],
        'tokens': ['network', 'topology']
    }


def test_portendo_2():

    entity_names = ['network_topology',
                    'network_architecture_design', 'network_architecture_testing']
    input_tokens = ['network', 'topology', 'architecture', 'testing']

    api = EntityOrchestrator(entity_names)
    assert api

    svcresult = api.run(input_tokens)
    assert type(svcresult) == dict

    assert svcresult == {

        'result': [
            'network_architecture_testing',
            'network_topology'
        ],

        'tokens': [
            'network',
            'topology',
            'architecture',
            'testing'
        ]
    }


def main():
    test_portendo_1()
    test_portendo_2()


if __name__ == "__main__":
    main()
