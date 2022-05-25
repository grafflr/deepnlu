#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Read Files from the Input Path """


import os
import pprint
import logging

from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject


class InputPathReader(BaseObject):
    """ Read Files from the Input Path """

    def __init__(self):
        """
        Created:
            10-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/28
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_dir: str) -> list or None:
        """Read an Input Directory or Input File

        Args:
            input_dir (str): the input path

        Returns:
            list or None: the output file or files
        """

        # may be a directory or single file
        FileIO.exists_or_error(input_dir)

        if os.path.isdir(input_dir):
            files = FileIO.load_files(directory=input_dir,
                                      extension="txt")
            if len(files):
                return files

            self.logger.error('\n'.join([
                "No Input Files Found",
                f"\tInput Directory: {input_dir}",
                f"\tInput Extension: txt"]))

            return None

        if os.path.splitext(input_dir)[1] == ".txt":
            return [input_dir]

        self.logger.error('\n'.join([
            "Input File Not Text",
            f"\tInput File: {input_dir}"]))

        return None
