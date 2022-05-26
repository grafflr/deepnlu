# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with lookup dictionaries on disk """


from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.datablock.dmo import GenericClassLoader


class FindLookup(BaseObject):
    """ Generic Facade to interact with lookup dictionaries on disk """

    __d_merge = None

    def __init__(self,
                 ontologies: list):
        """ Change History

        Created:
            9-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/17#issue-1021788619
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
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785
        Updated:
            26-May-2022
            craig@grafflr.ai
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7

        Args:
            ontologies (list): one-or-more Ontology models to use in processing
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(ontologies)
        
        load = GenericClassLoader().load
        self._finders = {x: load(package_name=x,
                                 class_suffix="Lookup",
                                 module_suffix="lookup") for x in ontologies}

    def _merge(self) -> dict:
        d = {}
        for name in self._finders:
            d_finder = self._finders[name].data()
            for k in d_finder:
                if k not in d:
                    d[k] = d_finder[k]
                else:
                    [d[k].append(x) for x in d_finder[k]]
        return d

    def data(self):
        if not self.__d_merge:
            self.__d_merge = self._merge()
        return self.__d_merge

    def grams(self,
              gram_level: int) -> list:
        if gram_level in self.data():
            return self.data()[gram_level]
