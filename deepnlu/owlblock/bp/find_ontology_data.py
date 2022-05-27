# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to Find Data in 1..* Ontology Models """


from baseblock import Enforcer
from baseblock import BaseObject

from askowl.bp import AskOwlAPI


class FindOntologyData(BaseObject):
    """ Generic Facade to Find Data in 1..* Ontology Models """

    def __init__(self,
                 ontologies: list):
        """ Change History

        Created:
            26-May-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/2

        Args:
            ontologies (list): one-or-more Ontology models to use in processing
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(ontologies)

        self._ontologies = ontologies

    def _load(self,
              ontologies: list) -> dict:
        d = {}
        for ontology_name in self._ontologies:
            pass
