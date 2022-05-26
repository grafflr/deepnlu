# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to find Synonym Data on Disk """


import os
import pprint
import logging
import importlib.util

from baseblock import EnvIO
from baseblock import BaseObject
from baseblock import Enforcer
from deepnlu.datablock.dto import get_ontology_name

from deepnlu.datablock.dmo import GenericClassLoader


class FindSynonyms(BaseObject):
    """ Generic Facade to find Synonym Data on Disk """

    __d_merge_fwd = None
    __d_merge_rev = None

    def __init__(self,
                 ontology_name: str = None):
        """
        Created:
            7-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/8
        Updated:
            11-Oct-2021
            craig@grafflr.ai
            *   support args for 1..* names in param
                https://github.com/grafflr/graffl-core/issues/30#issuecomment-940252993
        Updated:
            25-Jan-2022
            craig@grafflr.ai
            *   pass ontology-name as optional param
                https://github.com/grafflr/graffl-core/issues/135
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   use baseblock ontology name loader
                https://github.com/grafflr/graffl-core/issues/135
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)

        load = GenericClassLoader().load

        self._finders_fwd = {x: load(package_name=x,
                                     class_suffix="Synonyms",
                                     module_suffix="synonyms") for x in ontologies}

        self._finders_rev = {x: load(package_name=x,
                                     class_suffix="SynonymsRev",
                                     module_suffix="synonyms_rev") for x in ontologies}

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

    def fwd_data(self):
        if not self.__d_merge_fwd:
            self.__d_merge_fwd = self._merge(self._finders_fwd)

        return self.__d_merge_fwd

    def rev_data(self):
        if not self.__d_merge_rev:
            self.__d_merge_rev = self._merge(self._finders_rev)

        return self.__d_merge_rev

    def _cleanse(self,
                 input_text: str) -> str:
        input_text = input_text.lower()
        if ' ' in input_text:
            input_text = input_text.replace(' ', '_')
        return input_text

    def is_canon(self,
                 input_text: str) -> bool:
        """Check if Input Text is Canonical Entity

        Args:
            input_text (str): any input string

        Returns:
            bool: True if the input string is a Nursing Entity
        """
        return self._cleanse(input_text) in self.fwd_data()

    def is_variant(self,
                   input_text: str) -> bool:
        """Check if Input Text is known variant for at least one Canonical Entry

        Args:
            input_text (str): any input string

        Returns:
            bool: True if the input string is a known synonym to a Nursing Entity
        """
        return self._cleanse(input_text) in self.rev_data()

    def find_canon(self,
                   input_text: str) -> str or None:
        """Find the Canonical Representation of the Input String

        Args:
            input_text (str): any input string

        Returns:
            str or None: The Canonical Entity
        """
        input_text = self._cleanse(input_text)

        def find() -> str or None:

            # is canon
            if input_text in self.fwd_data():
                return input_text

            # is variant
            if input_text in self.rev_data():
                return self.rev_data()[input_text]

            if '_' in input_text:
                temp = input_text.replace('_', ' ')
                if temp in self.rev_data():
                    return self.rev_data()[temp]

        result = find()

        if not result:
            return None  # no canonical form exists

        def get_result() -> str:
            if type(result) == list:
                if len(result) > 1:
                    self.logger.warning('\n'.join([
                        f"Multi Typed Result (total={len(result)})",
                        f"\tInput: {input_text}",
                        f"\tTypes: {result}"]))
                return result[0]
            return result

        result = get_result()
        if self.isEnabledForDebug:
            Enforcer.is_str(result)

        return result

    def find_variants(self,
                      input_text: str) -> list:
        """Find the Synonyms for a known Entity

        Args:
            input_text (str): any input string

        Returns:
            list or None: a list of synonyms for the input entity
        """
        input_text = self._cleanse(input_text)

        def get_values() -> list:

            # is canon
            if input_text in self.fwd_data():
                return self.fwd_data()[input_text]

            # is variant
            if input_text in self.rev_data():
                s = set()
                for canon in self.rev_data()[input_text]:
                    [s.add(x) for x in self.fwd_data()[canon]]
                return sorted(s, key=len)

            return []

        values = [x for x in get_values() if x and len(x)]

        return values
