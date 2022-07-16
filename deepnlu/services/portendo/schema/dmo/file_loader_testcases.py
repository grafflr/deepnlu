#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Load Test Files"""


import os

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import BaseObject
from baseblock import Stopwatch


class FileLoaderTestCases(BaseObject):
    """Load Test Files"""

    def __init__(self):
        """
        Created:
            7-Feb-2022
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        """
        BaseObject.__init__(self, __name__)

    def process(self) -> list:
        sw = Stopwatch()

        path = os.path.join(os.environ["PROJECT_BASE"],
                            "resources/regression")

        files = FileIO.load_files(path, 'yml')

        self.logger.debug('\n'.join([
            "Loaded Test Files",
            f"\tTotal Files: {len(files)}",
            f"\tTotal Time: {str(sw)}"]))

        if EnvIO.exists('FILE_NAME'):
            file_name = EnvIO.as_str('FILE_NAME')
            files = [x for x in files if file_name.lower() in x.lower()]

        if EnvIO.exists('LINE_NUMBER'):
            line_number = EnvIO.as_int('LINE_NUMBER') - 1
            if line_number < len(files):
                return [files[line_number]]

            self.logger.error('\n'.join([
                "Test Case Not Found",
                f"\tLine Number: {line_number}"]))
            raise NotImplementedError(f"Test Case Not Found: #{line_number}")

        return files
