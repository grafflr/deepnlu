from pprint import pprint

from deepnlu.services.portendo.entity.svc import AnalyzeEntityNames


def test_portendo_1():

    entity_names = ['network_topology', 'network_architecture']

    svc = AnalyzeEntityNames()
    assert svc

    svcresult = svc.process(entity_names)
    assert type(svcresult) == dict

    assert svcresult == {'network': [['architecture'], ['topology']]}


def test_portendo_2():

    entity_names = ['network_topology', 'network_architecture_design']

    svc = AnalyzeEntityNames()
    assert svc

    svcresult = svc.process(entity_names)
    assert type(svcresult) == dict

    assert svcresult == {'network': [['architecture', 'design'], ['topology']]}


def main():
    test_portendo_1()
    test_portendo_2()


if __name__ == "__main__":
    main()
