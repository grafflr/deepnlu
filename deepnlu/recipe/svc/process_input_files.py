#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Orchestrator the deepNLU Processing of an Input File """


import os
import pprint

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject


class ProcessInputFiles(BaseObject):
    """ Orchestrator the deepNLU Processing of an Input File """

    __slots__ = (
        '_input_files',
        '_output_dir',
        '_ontologies'
    )

    def __init__(self,
                 input_files: list,
                 output_dir: str,
                 ontologies: list):
        """Process Input Files and Write Output to Disk

        Created:
            10-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/5

        Args:
            input_files (list): a list of one or more paths
            output_dir (str): the output directory
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(input_files)
            Enforcer.is_str(output_dir)
            Enforcer.is_list(ontologies)

            self.logger.debug('\n'.join([
                "Initialized Service",
                f"\tTotal Input Files: {len(input_files)}",
                f"\tOutput Dir: {output_dir}",
                f"\tOntologies: {ontologies}"]))

        self._input_files = input_files
        self._output_dir = output_dir
        self._ontologies = ontologies

    def _write_output(self,
                      data: object,
                      file_name: str):
        def path() -> str:
            if os.path.isdir(self._output_dir):
                return os.path.normpath(os.path.join(
                    self._output_dir, f"{file_name}.json"))
            return self._output_dir

        output_path = path()
        FileIO.write_json(data=data,
                          file_path=output_path)

        self.logger.debug('\n'.join([
            "Wrote Result to File",
            f"\tOutput Path: {output_path}"]))

    def process(self) -> list:
        from deepnlu.recipe.svc import ParseTextOneShot

        sw = Stopwatch()

        results = []
        parse = ParseTextOneShot(self._ontologies).process

        for input_file in self._input_files:

            result = parse(FileIO.read_string(input_file))
            self._write_output(data=result,
                               file_name=FileIO.get_file_name(input_file))

            results.append(result)

        self.logger.info('\n'.join([
            "Deep NLU Processing Completed",
            f"\tTotal Files: {len(self._input_files)}",
            f"\tTotal Time: {str(sw)}"]))

        return results
