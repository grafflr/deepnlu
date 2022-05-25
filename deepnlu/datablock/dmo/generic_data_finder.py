# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Load Inference Data Dictionaries """


from baseblock import EnvIO
from baseblock import BaseObject

from deepnlu.datablock.dmo import GenericClassLoader


class GenericDataFinder(BaseObject):
    """ Load Inference Data Dictionaries """

    __d_merge_data = None

    def __init__(self,
                 class_suffix: str,
                 module_suffix: str,
                 ontologies: list):
        """
        Created:
            29-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/97
        Updated:
            25-Jan-2022
            craig@grafflr.ai
            *   pass ontology-name as optional param
                https://github.com/grafflr/graffl-core/issues/135
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   enforce division of responsibility between DMOs and SVCs
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370
        """
        BaseObject.__init__(self, __name__)
        if type(ontologies) != list:
            raise ValueError('Incorrect DataType')

        load = GenericClassLoader().load

        self._finders = {x: load(package_name=x,
                                 class_suffix=class_suffix,
                                 module_suffix=module_suffix) for x in ontologies}

    def data(self) -> dict:
        """Return Data Dictionary

        Implementation:
            If the class is instantiated with multiple Ontology Names,
            this data routine will merge all the span dictionaries into a single structure
            unless the consumer calls this method with a specific Ontology name

        Args:
            ontology_name (str, optional): Ontology Name. Defaults to None.

        Returns:
            dict: Data Dictionary
        """

        def merge() -> dict:
            d = {}
            for ontology_name in self._finders:
                d_finder = self._finders[ontology_name].data()
                for k in d_finder:
                    if k not in d:
                        d[k] = d_finder[k]
                    else:
                        [d[k].append(x) for x in d_finder[k]]
            return d

        if not self.__d_merge_data:
            self.__d_merge_data = merge()

        return self.__d_merge_data
