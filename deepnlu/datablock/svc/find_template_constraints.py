# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find Constraints for NLG Templates """


import os
import pprint
import logging
import importlib.util

from baseblock import EnvIO
from baseblock import BaseObject
from baseblock import Enforcer
from baseblock import get_ontology_name

from datablock.dmo import GenericClassLoader


class FindTemplateConstraints(BaseObject):
    """ Find Constraints for NLG Templates """

    def __init__(self,
                 ontology_name: str = None):
        """
        Created:
            13-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/182
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)

        load = GenericClassLoader().load

        self._finders_fwd = {x: load(package_name=x,
                                     class_suffix="TemplateConstraints",
                                     module_suffix="template_constraints") for x in ontologies}

    def _merge(self,
               d_finder: dict) -> dict:
        d = {}
        for name in d_finder:
            data = d_finder[name].data()
            for k in data:
                if k not in d:
                    d[k] = data[k]
                else:
                    [d[k].append(x) for x in data[k]]
        return d

    def data(self):
        if not self.__d_merge_fwd:
            self.__d_merge_fwd = self._merge(self._finders_fwd)

        return self.__d_merge_fwd

    def has_constraint(self,
                       input_text) -> bool:
        pass
