# -*- coding: UTF-8 -*-
from deepnlu.services.accipio.tokenizer import Tokenizer


## ---------------------------------------------------------- ##
# Purpose:    Test Basic I/O
#             for complex and complete tokenization tests, use the regression suite
## ---------------------------------------------------------- ##


def test_graffl_1():
    tokenizer = Tokenizer()
    assert tokenizer

    # https://github.com/grafflr/graffl-core/issues/48
    assert tokenizer.input_text("health's management, NPs") == [
        "health's ", 'management', ', ', 'NPs']

    # https://github.com/grafflr/graffl-core/issues/41
    assert tokenizer.input_text("(RN)") == ['(', 'RN', ')']


def test_graffl_2():
    tokenizer = Tokenizer()
    assert tokenizer

    input_text = "please generate something similar to 'consistently achieves timely delivery'"
    assert type(input_text) == str

    tokenizer.input_text(input_text)


def main():
    test_graffl_2()


if __name__ == "__main__":
    main()
