#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Load and Validate Regression Files """


import os

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject


class LoadRegressionTests(BaseObject):
    """ Load and Validate Regression Files """

    def __init__(self):
        """ Change History

        Created:
            6-Jun-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/22
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def _absolute_path() -> str:
        absolute_path = os.path.normpath(os.path.join(
            os.getcwd(),
            EnvIO.str_or_exception('TEST_CASE_LOCATION')))
        FileIO.exists_or_error(absolute_path)

        return absolute_path

    @staticmethod
    def _load(absolute_path: str) -> list:
        d = {}

        for file_name in FileIO.load_files(absolute_path, "yaml"):
            d[file_name] = FileIO.read_yaml(file_name)

        return d

    @staticmethod
    def _validate(test_cases: list) -> None:
        # pass through for now
        # throw exception if failure
        pass

    def process(self) -> list:
        sw = Stopwatch()

        absolute_path = self._absolute_path()
        test_cases = self._load(absolute_path)
        self._validate(test_cases)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Loaded Test Cases",
                f"\tAbsolute Path: {absolute_path}",
                f"\tTotal Time: {str(sw)}",
                f"\tTotal Files: {len(test_cases)}"]))

        return test_cases
