# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find a NER within either the Graffl or spaCy Taxonomy """


from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.datablock.dmo import GenericClassLoader


class NerTypeFinder(BaseObject):
    """ Find a NER within either the Graffl or spaCy Taxonomy """

    __d_merge_graffl = None
    __d_merge_spacy = None

    def __init__(self,
                 ontologies: list):
        """ Change History

        Created:
            27-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/94
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   enforce ontologies as a list param in domain components
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370

        Args:
            ontologies (list): one-or-more Ontology models to use in processing
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(ontologies)

        load = GenericClassLoader().load

        self._graffl_finders = {x: load(package_name=x,
                                        class_suffix="GrafflNER",
                                        module_suffix="graffl_ner") for x in ontologies}

        self._spacy_finders = {x: load(package_name=x,
                                       class_suffix="SpacyNER",
                                       module_suffix="spacy_ner") for x in ontologies}

    @staticmethod
    def _merge(finders: list) -> dict:
        d = {}
        for name in finders:
            d_finder = finders[name].data()
            for k in d_finder:
                if k not in d:
                    d[k] = d_finder[k]
                else:
                    [d[k].append(x) for x in d_finder[k]]
        return d

    def spacy(self,
              name: str) -> list or None:

        if '_' in name:
            name = name.replace('_', ' ')

        for ontology in self._spacy_finders:
            d_spacy = self._spacy_finders[ontology].data()

            if len(d_spacy) and name in d_spacy:
                return sorted(d_spacy[name])

    def graffl(self,
               name: str) -> list or None:

        def graffl_data():
            if not self.__d_merge_graffl:
                self.__d_merge_graffl = self._merge(self._graffl_finders)
            return self.__d_merge_graffl

        if '_' in name:
            name = name.replace('_', ' ')

        if len(graffl_data()) and name in graffl_data():
            return sorted(graffl_data()[name])
