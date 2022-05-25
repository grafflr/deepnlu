# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Inferrable entities """


import os
import logging
import importlib.util

from baseblock import EnvIO
from baseblock import BaseObject
from baseblock import get_ontology_name

from deepnlu.datablock.dmo import GenericDataFinder


class FindInference(BaseObject):
    """ Generic Facade to interact with Inferrable entities """

    __requires = None
    __effects = None

    def __init__(self,
                 ontology_name: object = None):
        """
        Created:
            29-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/97
        Updated:
            3-Nov-2021
            craig@grafflr.ai
            *   add 'effects' dictionary and refactor 
                https://github.com/grafflr/graffl-core/issues/71
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   use baseblock ontology name loader
                https://github.com/grafflr/graffl-core/issues/135
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785
        """
        BaseObject.__init__(self, __name__)
        self._ontologies = get_ontology_name(ontology_name)

    def effects(self):
        """Dataset for 'Effects' Inferences

        Returns:
            Facade: a Facade that gives access to data and triggers
        """

        class Facade(object):

            __effects_fwd = None
            __effects_rev = None

            @classmethod
            def fwd(cls) -> dict:
                """Dataset Dictionary; either by Ontology Name or across all Ontologies

                Args:
                    ontology_name (str, optional): Ontology Name. Defaults to None.

                Returns:
                    dict: dataset for the forward relations
                """
                if not cls.__effects_fwd:
                    cls.__effects_fwd = GenericDataFinder(
                        class_suffix='Effects',
                        module_suffix='effects',
                        ontologies=self._ontologies)

                return cls.__effects_fwd.data()

            @classmethod
            def rev(cls) -> dict:
                """Dataset Dictionary; either by Ontology Name or across all Ontologies

                Args:
                    ontology_name (str, optional): Ontology Name. Defaults to None.

                Returns:
                    dict: dataset for the reverse relations
                """
                if not cls.__effects_rev:
                    cls.__effects_rev = GenericDataFinder(
                        class_suffix='EffectsRev',
                        module_suffix='effects_rev',
                        ontologies=self._ontologies)

                return cls.__effects_rev.data()

        if not self.__effects:
            self.__effects = Facade()

        return self.__effects

    def requires(self):
        """Dataset for 'Requires' Inferences

        Returns:
            Facade: a Facade that gives access to data and triggers
        """

        class Facade(object):
            __triggers = None
            __requires = None

            @classmethod
            def data(cls) -> dict:
                """Dataset Dictionary; either by Ontology Name or across all Ontologies

                Args:
                    ontology_name (str, optional): Ontology Name. Defaults to None.

                Returns:
                    dict: dataset for the entire dictionary
                """
                if not cls.__requires:
                    cls.__requires = GenericDataFinder(
                        class_suffix='InferByRequires',
                        module_suffix='infer_by_requires',
                        ontologies=self._ontologies)

                return cls.__requires.data()

            @classmethod
            def triggers(cls) -> set:
                """Triggering Tokens

                Returns:
                    set: tokens that are capable of triggering inference capability
                """
                if not cls.__triggers:
                    cls.__triggers = set(cls.data().keys())

                return cls.__triggers

        if not self.__requires:
            self.__requires = Facade()

        return self.__requires
