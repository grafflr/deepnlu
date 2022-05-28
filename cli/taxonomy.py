

from baseblock import Enforcer

from deepnlu.services import AutoTaxoOrchestrator


def driver(input_text: str):
    api = AutoTaxoOrchestrator()
    assert api

    result = api.process(input_text)
    Enforcer.is_optional_list(result)

    [print(x) for x in result]


def main(input_text):
    driver(input_text)


if __name__ == '__main__':
    import plac

    plac.call(main)
