# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find the Depth of a NER entity within a Taxonomy """


import os
import pprint
import logging
import importlib.util

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject

from datablock.dmo import GenericClassLoader


class NerDepthFinder(BaseObject):
    """ Find the Depth of a NER entity within a Taxonomy """

    __d_merge_depth = None

    def __init__(self,
                 ontologies: list):
        """
        Created:
            27-Oct-2021
            craig@grafflr.ai
            *   refactored out of find-ner in pursuit of 
                https://github.com/grafflr/graffl-core/issues/94
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   enforce ontologies as a list param in domain components
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370
        """
        BaseObject.__init__(self, __name__)
        if type(ontologies) != list:
            raise ValueError('Incorrect DataType')

        load = GenericClassLoader().load

        self.__depth = {
            x: load(package_name=x,
                    class_suffix="NerDepth",
                    module_suffix="ner_depth") for x in ontologies}

    def process(self,
                ner: str) -> int or None:
        """Return NER Depth

        Implementation:
            If the class is instantiated with multiple Ontology Names,
            this data routine will merge all the span sets into a single structure
            unless the consumer calls this method with a specific Ontology name

        Args:
            name (str, optional): Ontology Name. Defaults to None.

        Returns:
            dict: Span set
        """

        def merge() -> dict:
            d = {}
            for name in self.__depth:
                d_finder = self.__depth[name].data()
                for k in d_finder:
                    if k not in d:
                        d[k] = d_finder[k]
                    else:
                        [d[k].append(x) for x in d_finder[k]]
            return d

        def get_dict() -> dict:
            if not self.__d_merge_depth:
                self.__d_merge_depth = merge()

            return self.__d_merge_depth

        d = get_dict()
        if ner not in d:
            return None

        return d[ner][0]
