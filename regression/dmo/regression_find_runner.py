#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find the Runner for a given Regression Test """


from typing import Callable

from baseblock import BaseObject

from regression.dmo.runners import RoundTripRunner
from regression.dmo.runners import FindOntologyDataRunner


class RegressionFindRunner(BaseObject):
    """ Find the Runner for a given Regression Test """

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
        runner_name = d_test_case['engine']['runner']

        if runner_name == "round_trip":
            return RoundTripRunner().process

        if runner_name == "find_ontology_data":
            return FindOntologyDataRunner().process

        raise NotImplementedError(runner_name)
