# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with span dictionaries on disk """


import os
import logging
import importlib.util

from baseblock import EnvIO
from baseblock import BaseObject
from baseblock import get_ontology_name

from deepnlu.datablock.dmo import GenericClassLoader


class FindSpans(BaseObject):
    """ Generic Facade to interact with span dictionaries on disk """

    def __init__(self,
                 ontology_name: object = None):
        """
        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/74
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   pass ontology-name as optional param
                https://github.com/grafflr/graffl-core/issues/135
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)

        load = GenericClassLoader().load

        self._d_merge_data = None
        self._finders = {x: load(package_name=x,
                                 class_suffix="Spans",
                                 module_suffix="spans") for x in ontologies}

    def data(self) -> dict:
        """Return Span Dictionary

        Implementation:
            If the class is instantiated with multiple Ontology Names,
            this data routine will merge all the span dictionaries into a single structure
            unless the consumer calls this method with a specific Ontology name

        Args:
            name (str, optional): Ontology Name. Defaults to None.

        Returns:
            dict: Span Dictionary
        """

        def merge() -> dict:
            d = {}
            for name in self._finders:
                d_finder = self._finders[name].data()
                for k in d_finder:
                    if k not in d:
                        d[k] = d_finder[k]
                    else:
                        [d[k].append(x) for x in d_finder[k]]
            return d

        if not self._d_merge_data:
            self._d_merge_data = merge()

        return self._d_merge_data

    def keys(self) -> list:
        """Return Span Keys

        Implementation:
            If the class is instantiated with multiple Ontology Names,
            this data routine will merge all the span sets into a single structure
            unless the consumer calls this method with a specific Ontology name

        Returns:
            dict: Span set
        """
        return sorted(self.data().keys(), key=len)
