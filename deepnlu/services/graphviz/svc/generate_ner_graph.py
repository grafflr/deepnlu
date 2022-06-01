#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Structure NER Graph """


from graphviz import Digraph


from baseblock import BaseObject


from deepnlu.services.graphviz.dmo import GraphvizStyleLoader
from deepnlu.services.graphviz.dmo import GraphvizEdgeGenerator
from deepnlu.services.graphviz.dmo import GraphvizNodeGenerator


class GenerateNerGraph(BaseObject):
    """ Structure NER Graph """

    def __init__(self,
                 absolute_path: str):
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

        Args:
            absolute_path (str): the absolute path to the location of the stylesheet resource
        """
        BaseObject.__init__(self, __name__)
        self._d_style = GraphvizStyleLoader(
            stylesheet_name='nlu',
            absolute_path=absolute_path).style()

    def process(self,
                svcresult: dict) -> dict:

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
            d_style=self._d_style)

        edgegen = GraphvizEdgeGenerator(
            graph=graph,
            d_style=self._d_style)

        nodegen.process(svcresult['nodes'])
        edgegen.process(svcresult['edges'])

        graph.render("c:/Users/Craig/Desktop/graphviz")
