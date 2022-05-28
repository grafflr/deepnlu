# -*- coding: UTF-8 -*-
from deepnlu.services.normalize import Normalizer


## ---------------------------------------------------------- ##
# Purpose:    Test Basic I/O
#             for complex and complete tokenization tests, use the regression suite
## ---------------------------------------------------------- ##


norm = Normalizer()
assert norm


def test_normalize_text():
    actual_input = """
    ‐ ‒ ‑ – — ― ‛«“hello world”»’ can`t
    """.strip()

    expected_output = """
    - - - - - - '""hello world""' can't
    """.strip()

    print(norm.input_text(actual_input))
    assert norm.input_text(actual_input) == expected_output


def test_normalize_registered():
    # https://github.com/grafflr/graffl-core/issues/46#issuecomment-943703538
    actual_input = """
    registered
    """.strip()

    expected_output = """
    registered
    """.strip()

    print(norm.input_text(actual_input))
    assert norm.input_text(actual_input) == expected_output
