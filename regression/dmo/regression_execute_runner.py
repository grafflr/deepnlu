#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute a specified Runner on a Regression Case """


import os
from typing import Callable

from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject


class RegressionExecuteRunner(BaseObject):
    """ Execute a specified Runner on a Regression Case """

    def __init__(self):
        """ Change History

        Created:
            6-Jun-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/22
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                d_test_case: dict,
                runner: Callable) -> object:
        return runner(d_test_case)
