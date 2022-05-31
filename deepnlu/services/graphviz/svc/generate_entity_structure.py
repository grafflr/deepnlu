#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate a Graph Input Structure based on a list of entity name inputs """


from uuid import uuid1
from pprint import pprint
from graphviz import Digraph


from baseblock import BaseObject
from datablock import FindData
from datablock import FindLabels


from imaginor.graphviz.dmo import GraphvizStyleLoader
from imaginor.graphviz.dmo import GraphvizEdgeGenerator
from imaginor.graphviz.dmo import GraphvizNodeGenerator


class GenerateEntityStructure(BaseObject):
    """ Generate a Graph Input Structure based on a list of entity name inputs """

    def __init__(self):
        """ Change History

        Created:
            18-May-2022
            craig@grafflr.ai
            *   cloned from 'generate-ner-graph'
                https://github.com/grafflr/graffl-core/issues/384
        """
        BaseObject.__init__(self, __name__)
        self._find_data = FindData().find

    def process(self,
                entity_names: list,
                ontologies: list) -> list:

        results = []
        for ontology_name in ontologies:
            for entity_name in entity_names:
                [results.append(x) for x in
                 self._find_data(entity_name=entity_name,
                                 ontology_name=ontology_name,
                                 find_requires=True,
                                 find_similar=True,
                                 find_implies=True,
                                 find_ancestors=True,
                                 find_siblings=True,
                                 find_descendants=True,
                                 find_descendant_synonyms=False)]

        # add labels
        for result in results:
            finder = FindLabels(result['Ontology'])
            result['ObjectLabel'] = finder.label_or_self(result['Object'])
            result['SubjectLabel'] = finder.label_or_self(result['Subject'])
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
