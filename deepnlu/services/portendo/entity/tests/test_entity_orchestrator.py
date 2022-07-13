
from deepnlu.services.portendo.entity.bp import EntityOrchestrator


def test_portendo():

    entity_names = ['network_topology']
    input_tokens = ['network', 'topology']

    api = EntityOrchestrator(entity_names)
    assert api

    svcresult = api.run(input_tokens)
    assert type(svcresult) == dict


def main():
    test_portendo()


if __name__ == "__main__":
    main()
