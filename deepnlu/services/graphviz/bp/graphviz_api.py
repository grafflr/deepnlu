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
        Updated:
            31-May-2022
            craig@grafflr.ai
            *   migrate to deepnlu and update absolute path
                https://github.com/grafflr/graffl-core/issues/418
        Updated:
            1-Jun-2022
            craig@grafflr.ai
            *   add 'center-node-name' param
                https://github.com/grafflr/deepnlu/issues/25

        Args:
            find_ontology_data (FindOntologyData): an instantiation of the class
        """
        BaseObject.__init__(self, __name__)
        self._find_ontology_data = find_ontology_data

    def generate(self,
                 entity_names: list,
                 enforced_triples: str = None) -> Digraph:
        """ Visualize Extracted Entities in a Graph

        Args:
            entity_names (list): the entity names to visualize in the graph
            enforced_triples (list, optional): a set of enforced relationships that aren't found in the data. Defaults to None.
                each item in the list is a tuple of (S,P,O)
                Reference: https://github.com/grafflr/deepnlu/issues/25#issuecomment-1144190779

        Returns:
            Digraph: the Graphviz graph
        """

        find_all_relationships = FindAllRelationships(
            self._find_ontology_data).find

        generate_structure = GenerateEntityStructure(
            find_ontology_data=self._find_ontology_data,
            find_all_relationships=find_all_relationships,
        ).process

        generate_graph = GenerateEntityGraph(
            absolute_path=self._find_ontology_data.absolute_path()).process

        d_result = generate_structure(
            entity_names=entity_names,
            enforced_triples=enforced_triples)

        return generate_graph(d_result)
