#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate a Graph Input Structure based on a list of entity name inputs """


from uuid import uuid1
from pprint import pprint
from typing import Callable
from graphviz import Digraph


from baseblock import BaseObject
# from datablock import FindData
# from datablock import FindLabels


from deepnlu.owlblock.bp import FindOntologyData
from deepnlu.services.graphviz.dmo import GraphvizStyleLoader
from deepnlu.services.graphviz.dmo import GraphvizEdgeGenerator
from deepnlu.services.graphviz.dmo import GraphvizNodeGenerator


class GenerateEntityStructure(BaseObject):
    """ Generate a Graph Input Structure based on a list of entity name inputs """

    def __init__(self,
                 find_ontology_data: FindOntologyData,
                 find_all_relationships: Callable):
        """ Change History

        Created:
            18-May-2022
            craig@grafflr.ai
            *   cloned from 'generate-ner-graph'
                https://github.com/grafflr/graffl-core/issues/384
        Updated:
            31-May-2022
            craig@grafflr.ai
            *   migrated from graffl-core
                https://github.com/grafflr/graffl-core/issues/418
        Updated:
            1-Jun-2022
            craig@grafflr.ai
            *   add 'center-node-name' param
                https://github.com/grafflr/deepnlu/issues/25

        Args:
            find_ontology_data (FindOntologyData): _description_
            find_all_relationships (Callable): _description_
        """
        BaseObject.__init__(self, __name__)
        self._find_ontology_data = find_ontology_data
        self._find_all_relationships = find_all_relationships

    def process(self,
                entity_names: list,
                enforced_triples: list = None) -> list:
        """ Visualize Extracted Entities in a Graph

        Args:
            entity_names (list): the entity names to visualize in the graph
            enforced_triples (list, optional): a set of enforced relationships that aren't found in the data. Defaults to None.
                each item in the list is a tuple of (S,P,O)
                Reference: https://github.com/grafflr/deepnlu/issues/25#issuecomment-1144190779

        Returns:
            Digraph: the Graphviz graph
        """

        results = []

        # if center_node_name:  # DEEPNLU-25
        #     for entity_name in entity_names:
        #         results.append({
        #             "Subject": center_node_name,
        #             "Predicate": 'attains',
        #             "Object": entity_name,
        #             "Ontology": self._find_ontology_data.ontologies()[0],
        #             "Depth": 1,
        #         })

        if enforced_triples:
            for enforced_triple in enforced_triples:
                results.append({
                    "Subject": enforced_triple[0],
                    "Predicate": enforced_triple[1],
                    "Object": enforced_triple[2],
                    "Ontology": "enforced-triple",
                    "Depth": 1,
                })

        for entity_name in entity_names:
            [results.append(x) for x in
                self._find_all_relationships(entity_name=entity_name,
                                             find_requires=True,
                                             find_similar=True,
                                             find_implies=True,
                                             find_ancestors=True,
                                             find_descendants=True)]

        # add labels
        for result in results:
            result['ObjectLabel'] = self._find_ontology_data.label_by_entity(
                result['Object'])
            result['SubjectLabel'] = self._find_ontology_data.label_by_entity(
                result['Subject'])
            result['style'] = result['Predicate'].lower().strip()

        # now we need to index this into
        # 1. unique node names
        # 2. unique edge names
        # 3. which edges link which nodes

        # it's important to focus on #1 and #2 first because
        # we have to define these nodes and edges in Graphviz
        # prior to defining the actual graph shape in #3

        # index the structure
        d_nodes = {}
        for result in results:

            d_nodes[result['Subject']] = {
                "label": result['SubjectLabel'],
                "entity": result['Object'],
                "node_id": result['Subject'],
                "style": "default",
            }

            d_nodes[result['Object']] = {
                "label": result['ObjectLabel'],
                "entity": result['Object'],
                "node_id": result['Object'],
                "style": "default",
            }

        # d_predicates = {}
        # for result in results:
        #     predicate_id = result['Predicate'].lower()
        #     d_predicates[predicate_id] = {
        #         "label": result['Predicate'],
        #         "node_id": predicate_id,
        #         "style": result['Predicate'].lower(),
        #     }

        d_rels = {}
        for result in results:
            key = f"{result['Subject']}-{result['Predicate']}-{result['Object']}".lower()
            d_rels[key] = result

        svcresult = {
            'nodes': list(d_nodes.values()),
            # 'edges': list(d_predicates.values()),
            'rels': list(d_rels.values()),
        }

        return svcresult
