# -*- coding: UTF-8 -*-


import pprint


from deepnlu.services.erogito.parse.svc import ParseInputTokens


def execute(tokens: list):
    parser = ParseInputTokens()
    assert parser

    svcresult = parser.process(tokens)

    txtresult = [x['text'] for x in svcresult]

    # normalize for the purpose of testing only
    tokens = [x.replace("'", '"').strip() for x in tokens]
    txtresult = [x.replace("'", '"').strip() for x in txtresult]

    if tokens != txtresult:
        print(tokens)
        print(txtresult)

    assert tokens == txtresult


def test_parse_input_tokens():

    execute(["alpha", "alpha"])
    execute(["health's ", 'management', ', ', 'NPs ', 'bring'])
    execute(["'", "every", "'", "time",
             '(', "'", "Test's", "'", ')', 'for', 'now', '!'])


def main():
    test_parse_input_tokens()


if __name__ == "__main__":
    main()
