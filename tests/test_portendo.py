from baseblock import Enforcer

from portendo import __version__
from portendo.bp import Portendo


def test_version():
    assert __version__ == '0.1.0'


def test_portendo():
    input_tokens = [
        {
            "normal": "my",
        },
        {
            "normal": "late_transport",
            "swaps": {
                "canon": "late_transport",
                "type": "chitchat"
            }
        },
    ]

    api = Portendo('chitchat')
    assert api

    svcresult = api.run(input_tokens)
    assert type(svcresult) == dict

    keys = sorted(svcresult.keys())
    assert keys == ['result', 'tokens']

    assert type(svcresult['tokens']) == dict


def main():
    test_portendo()


if __name__ == "__main__":
    main()
