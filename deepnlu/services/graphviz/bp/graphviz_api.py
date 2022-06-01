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
                 center_node_name: str = None) -> Digraph:
        """ Visualize Extracted Entities in a Graph

        Args:
            entity_names (list): the entity names to visualize in the graph
            center_node_name (str, optional): the center node of the graph. Defaults to None.
                Reference: https://github.com/grafflr/deepnlu/issues/25

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

        if center_node_name and center_node_name in entity_names:
            entity_names = [x for x in entity_names if x != center_node_name]

        d_result = generate_structure(
            entity_names=entity_names,
            center_node_name=center_node_name)

        return generate_graph(d_result)
