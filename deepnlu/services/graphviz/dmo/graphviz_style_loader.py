#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generates a GraphViz Node """


import os

from pprint import pprint
from graphviz import Digraph


from baseblock import EnvIO
from baseblock import FileIO
from baseblock import BaseObject


class GraphvizStyleLoader(BaseObject):
    """ Generates a GraphViz Node """

    def __init__(self,
                 stylesheet_name: str,
                 absolute_path: str):
        """ Change History

        Created:
            9-Nov-2021
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/101
        Updated:
            31-May-2022
            craig@graffl.ai
            *   migrate to deepnlu and update absolute path
                https://github.com/grafflr/graffl-core/issues/418

        Args:
            stylesheet_name (str): name of the stylesheet that will be used
            absolute_path (str): the absolute path to the location of the stylesheet resource
        """
        BaseObject.__init__(self, __name__)
        self._style = self._load(
            absolute_path=absolute_path,
            stylesheet_name=stylesheet_name)

    def _load(self,
              absolute_path: str,
              stylesheet_name: str) -> dict:

        files = FileIO.load_files(extension="yaml",
                                  directory=absolute_path)

        if not len(files):
            self.logger.error('\n'.join([
                "No Stylesheets Found",
                f"\tPath: {absolute_path}"]))
            raise FileNotFoundError

        files = [x for x in files if stylesheet_name in x]

        if not len(files):
            self.logger.error('\n'.join([
                "No Stylesheets Found By Name",
                f"\tName: {stylesheet_name}",
                f"\tPath: {absolute_path}",
                f"\tFiles: {files}"]))
            raise FileNotFoundError

        return FileIO.read_yaml(files[0])

    def style(self) -> dict:
        return self._style
