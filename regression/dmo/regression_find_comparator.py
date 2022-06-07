#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find the Comparator for a given Regression Test """


import os
from typing import Callable

from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject


from regression.dmo.comparator import RoundTripComparator


class RegressionFindComparator(BaseObject):
    """ Find the Comparator for a given Regression Test """

    def __init__(self):
        """ Change History

        Created:
            6-Jun-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/22
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                d_test_case: dict) -> Callable:
        runner_name = d_test_case['engine']['comparator']

        if runner_name == "round_trip":
            return RoundTripComparator().process

        raise NotImplementedError(runner_name)
