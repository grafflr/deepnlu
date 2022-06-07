#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Filter Selected Regression Tests based on User-Supplied Criteria """


from baseblock import EnvIO
from baseblock import Stopwatch
from baseblock import BaseObject


class FilterRegressionTests(BaseObject):
    """ Filter Selected Regression Tests based on User-Supplied Criteria """

    def __init__(self):
        """ Change History

        Created:
            6-Jun-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/22
        """
        BaseObject.__init__(self, __name__)

    def _process(self,
                 test_cases: list) -> list:

        filter_on = EnvIO.str_or_default('REGRESSION_FILENAME', '*')
        if filter_on == "*":
            return test_cases

        return [x for x in test_cases if filter_on in x]

    def process(self,
                test_cases: list) -> list:

        sw = Stopwatch()

        test_cases = self._process(test_cases)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Filtered Test Cases",
                f"\tTotal Time: {str(sw)}",
                f"\tTotal Files: {len(test_cases)}"]))

        return test_cases
