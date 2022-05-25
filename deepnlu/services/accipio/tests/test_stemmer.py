# -*- coding: UTF-8 -*-
from accipio.stemmer.bp import Stemmer


## ---------------------------------------------------------- ##
# Purpose:    Test Basic I/O
#             for complex and complete tokenization tests, use the regression suite
## ---------------------------------------------------------- ##


def test_stemmer():

    assert Stemmer().input_text('irons')
