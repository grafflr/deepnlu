#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute a specified Comparator on a Regression Case """


import os
from typing import Callable

from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject
from numpy import exp


class RegressionExecuteComparator(BaseObject):
    """ Execute a specified Comparator on a Regression Case """

    def __init__(self):
        """ Change History

        Created:
            6-Jun-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/22
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                actual_results: object,
                expected_results: object,
                comparator: Callable) -> bool:

        return comparator(
            actual_results=actual_results,
            expected_results=expected_results)
