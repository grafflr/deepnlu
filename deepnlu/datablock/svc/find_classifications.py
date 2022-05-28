# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Classification Rules """


import os

from pprint import pprint

from baseblock import BaseObject

from deepnlu.datablock.dmo import GenericFunctionLoader


class FindClassifications(BaseObject):
    """ Generic Facade to interact with Classification Rules """

    __ndx_all_models = []

    def __init__(self,
                 schema_name: str,
                 absolute_path: str):
        """ Change History:

        Created:
            10-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/172
        Updated:
            5-Apr-2022
            craig@grafflr.ai
            *   include 'startswith'
                https://github.com/grafflr/graffl-core/issues/264

        Args:
            schema_name (str): name of the schema containing classification rules
            absolute_path (str): absolute path to the directory containing these files
        """
        BaseObject.__init__(self, __name__)
        self._schema_name = schema_name

        loader = GenericFunctionLoader(absolute_path).load

        self.include_one_of = loader('include_one_of')
        self.include_all_of = loader('include_all_of')
        self.exclude_one_of = loader('exclude_one_of')
        self.exclude_all_of = loader('exclude_all_of')
        self.startswith = loader('startswith')
        self.mapping = loader('mapping')
        self._d_scores = loader('scoring')

    def models(self) -> list:
        return sorted(self.mapping.keys())

    def is_known_model(self,
                       input_text: str) -> bool:
        """ Check if Input Text is a known model

        Args:
            input_text (str): any input text of any length

        Returns:
            bool: True if this is a model that exists in the underlying mapping.py file
        """
        if not self.__ndx_all_models:
            self.__ndx_all_models = [x.lower().strip() for x in self.models()]
        return input_text.lower().strip() in self.__ndx_all_models

    def score(self,
              category: str) -> float:
        if category in self._d_scores:
            return self._d_scores[category]
        raise NotImplementedError(category)

    def print(self) -> None:

        def inner(d: dict,
                  name: str) -> None:
            if len(d):
                print(f"{name}: {len(d)}")
                pprint(d)
            else:
                print(f"{name}: EMPTY")

        inner(self.include_one_of, "include-one-of")
        inner(self.include_all_of, "include-all-of")
        inner(self.exclude_one_of, "exclude_one_of")
        inner(self.exclude_all_of, "exclude_all_of")
        inner(self.startswith, "startswith")
