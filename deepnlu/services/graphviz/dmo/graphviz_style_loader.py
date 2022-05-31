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
                 stylesheet_name: str):
        """ Change History

        Created:
            9-Nov-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/101

        Args:
            stylesheet_name (str): name of the stylesheet that will be used
        """
        BaseObject.__init__(self, __name__)
        self._style = self._load(stylesheet_name)

    def _load(self,
              stylesheet_name: str) -> dict:

        path = os.path.normpath(os.path.join(
            EnvIO.str_or_exception('GRAFFLR_HOME'),
            'apps/services/imaginor/resources'))

        files = FileIO.load_files(directory=path,
                                  extension="yaml")

        if not len(files):
            self.logger.error('\n'.join([
                "No Stylesheets Found",
                f"\tPath: {path}"]))
            raise FileNotFoundError

        files = [x for x in files if stylesheet_name in x]

        if not len(files):
            self.logger.error('\n'.join([
                "No Stylesheets Found By Name",
                f"\tName: {stylesheet_name}",
                f"\tPath: {path}",
                f"\tFiles: {files}"]))
            raise FileNotFoundError

        return FileIO.read_yaml(files[0])

    def style(self) -> dict:
        return self._style
