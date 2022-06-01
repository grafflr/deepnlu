#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" An API for generating Graphviz dot structures """


from graphviz import Digraph

from baseblock import BaseObject

from deepnlu.owlblock.bp import FindOntologyData
from deepnlu.services.graphviz.svc import FindAllRelationships
from deepnlu.services.graphviz.svc import GenerateEntityStructure
from deepnlu.services.graphviz.svc import GenerateEntityGraph


class GraphvizAPI(BaseObject):
    """ An API for generating Graphviz dot structures """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History

        Created:
            5-Nov-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/102
        """
        BaseObject.__init__(self, __name__)
        self._find_ontology_data = find_ontology_data

    def generate(self,
                 entity_names: list) -> Digraph:

        find_all_relationships = FindAllRelationships(
            self._find_ontology_data).find

        generate_structure = GenerateEntityStructure(
            find_ontology_data=self._find_ontology_data,
            find_all_relationships=find_all_relationships,
        ).process

        generate_graph = GenerateEntityGraph().process

        d_result = generate_structure(entity_names)

        return generate_graph(d_result)
