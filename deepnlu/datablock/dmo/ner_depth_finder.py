# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find the Depth of a NER entity within a Taxonomy """


from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.datablock.dmo import GenericClassLoader


class NerDepthFinder(BaseObject):
    """ Find the Depth of a NER entity within a Taxonomy """

    __d_merge_depth = None

    def __init__(self,
                 ontologies: list):
        """ Change History

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
