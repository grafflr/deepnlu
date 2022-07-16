#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Build an in-memory Index over a Dictionary of Classifications """


import os

from baseblock import FileIO
from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.services.portendo.schema.dmo import IndexScoring
from deepnlu.services.portendo.schema.dmo import IndexExcludeAllOf
from deepnlu.services.portendo.schema.dmo import IndexExcludeOneOf
from deepnlu.services.portendo.schema.dmo import IndexIncludeAllOf
from deepnlu.services.portendo.schema.dmo import IndexIncludeOneOf
from deepnlu.services.portendo.schema.dmo import IndexStartsWith


class ReadMapping(BaseObject):
    """ Build an in-memory Index over a Dictionary of Classifications """

    def __init__(self,
                 schema_name: str,
                 absolute_path: str):
        """ Initialize Manifest Indicer

        Created:
            7-Feb-2022
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/167
        Updated:
            8-Jun-2022
            craig@graffl.ai
            *   read schema in-memory 
                https://github.com/grafflr/deepnlu/issues/45

        Args:
            schema_name (str): name of the schema containing classification rules
            absolute_path (str): absolute path to the location of the classification rules
        """
        BaseObject.__init__(self, __name__)
        d_schema = self._read_file(schema_name, absolute_path)
        self._d_index = self._create_index(d_schema)

    def _read_file(self,
                   schema_name: str,
                   absolute_path: str) -> dict:

        def get_file_name() -> str:
            if "yml" not in schema_name:
                return f"{schema_name}.yml"
            return schema_name

        input_file = os.path.normpath(os.path.join(
            absolute_path, get_file_name()))

        FileIO.exists_or_error(input_file)
        return FileIO.read_yaml(input_file)

    def _create_index(self,
                      d_schema: dict):

        return {
            'scoring': IndexScoring(d_schema).process(),
            'include_one_of': IndexIncludeOneOf(d_schema).process(),
            'include_all_of': IndexIncludeAllOf(d_schema).process(),
            'exclude_one_of': IndexExcludeOneOf(d_schema).process(),
            'exclude_all_of': IndexExcludeAllOf(d_schema).process(),
            'startswith': IndexStartsWith(d_schema).process(),
            'mapping': d_schema,
        }

    def index(self) -> dict:
        return self._d_index
