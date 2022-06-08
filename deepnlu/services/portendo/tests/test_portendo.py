import os

from baseblock import FileIO


from deepnlu.services.portendo.bp import Portendo


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

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/testing'))
    FileIO.exists_or_error(absolute_path)

    api = Portendo(schema_name='test_intents',
                   absolute_path=absolute_path)
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
