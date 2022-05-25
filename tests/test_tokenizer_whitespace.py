# -*- coding: UTF-8 -*-
from accipio.tokenizer import Tokenizer


## ---------------------------------------------------------- ##
# Purpose:    Test Basic I/O
#             for complex and complete tokenization tests, use the regression suite
## ---------------------------------------------------------- ##


def test_whitespace():
    input_text = '"The $4.50 is paid in full tomorrow!" said Mr. Berluski'

    actual_output = Tokenizer().whitespace(input_text)
    print(actual_output)

    expected_output = [
        '"The', '$4.50', 'is', 'paid', 'in',
        'full', 'tomorrow!"', 'said', 'Mr.', 'Berluski'
    ]

    assert actual_output == expected_output


def main():
    test_whitespace()


if __name__ == "__main__":
    main()
