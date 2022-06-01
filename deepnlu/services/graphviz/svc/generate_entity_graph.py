#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Structure NER Graph """


from graphviz import Digraph


from baseblock import BaseObject


from deepnlu.services.graphviz.dmo import GraphvizStyleLoader
from deepnlu.services.graphviz.dmo import GraphvizEdgeGenerator
from deepnlu.services.graphviz.dmo import GraphvizNodeGenerator


class GenerateEntityGraph(BaseObject):
    """ Structure NER Graph """

    def __init__(self,
                 absolute_path: str):
        """ Change History

        Created:
            18-May-2022
            craig@grafflr.ai
            *   cloned from 'generate-ner-graph'
                https://github.com/grafflr/graffl-core/issues/384
        Updated:
            31-May-2022
            craig@grafflr.ai
            *   migrate to deepnlu and update absolute path
                https://github.com/grafflr/graffl-core/issues/418

        Args:
            absolute_path (str): the absolute path to the location of the stylesheet resource
        """
        BaseObject.__init__(self, __name__)
        self._d_style = GraphvizStyleLoader(
            stylesheet_name='nlu',
            absolute_path=absolute_path).style()

    def process(self,
                entities: list) -> Digraph:
        """ Generate a directed Graphviz Graph

        Args:
            entities (list): output from 'generate-entity-structure' service
        """

        graph = Digraph(engine="dot",
                        comment='Graffl',
                        format="png",
                        name="Graffl")

        graph.attr('graph',
                   compound='True',
                   ranksep='1.2 equally',
                   ratio='fill',
                   rotate='0',
                   splines='spline',
                   rankdir='LR')

        nodegen = GraphvizNodeGenerator(
            graph=graph,
            d_style=self._d_style['nodes'])
        nodegen.process(entities['nodes'])

        edgegen = GraphvizEdgeGenerator(
            graph=graph,
            d_style=self._d_style['edges'])
        edgegen.process(entities['rels'])

        # graph.render("c:/Users/Craig/Desktop/graphviz")
        return graph
