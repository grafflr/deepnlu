# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Interact with the NER Taxonomy """


from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.datablock.dmo import GenericDataFinder


class NerTaxonomyFinder(BaseObject):
    """ Interact with the NER Taxonomy """

    def __init__(self,
                 ontologies: list):
        """ Change History

        Created:
            8-Nov-2021
            craig@grafflr.ai
            *   in pursuit of 
                https://github.com/grafflr/graffl-core/issues/108
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

        self._fwd = GenericDataFinder(
            class_suffix='NerTaxonomy',
            module_suffix='ner_taxonomy',
            ontologies=ontologies)

    def data(self) -> dict:
        return self._fwd.data()

    def is_ner(self,
               input_text: str) -> bool:
        return input_text.upper().strip() in self.data()
