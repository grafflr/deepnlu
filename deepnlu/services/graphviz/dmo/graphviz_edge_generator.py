#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generates a GraphViz Edge """

from typing import List, Dict, Tuple, Union

from copy import deepcopy
from pprint import pformat
from graphviz import Digraph

from baseblock import BaseObject


class GraphvizEdgeGenerator(BaseObject):
    """ Generates a GraphViz Edge """

    def __init__(self,
                 graph: Digraph,
                 d_style: dict):
        """ Change History

        Created:
            8-Nov-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/102
        Created:
            31-May-2022
            craig@grafflr.ai
            *   refactored to return 'default' if no style found in pursuit of
                https://github.com/grafflr/deepnlu/issues/23

        Args:
            graph (Digraph): the instantiated graph model
            d_style (dict): the in-memory stylesheet
        """
        BaseObject.__init__(self, __name__)
        self._graph = graph
        self._d_style = d_style

    def _get_edge_style(self,
                        d_edge: dict) -> str:
        if d_edge['Predicate'].lower() in self._d_style:
            return deepcopy(self._d_style[d_edge['Predicate'].lower()])

        if 'default' in self._d_style:
            return deepcopy(self._d_style['default'])

        self.logger.error('\n'.join([
            "Node Style Not Found",
            f"\tNode Style: {d_edge['style']}",
            f"\tNo Default Style Defined",
            f"\tKnown Styles: {sorted(self._d_style.keys())}"]))

        raise ValueError('Edge Style Exception')

    def _get_edge_label(self,
                        d_edge: dict,
                        d_style: dict) -> str:

        # should the label be displayed along the edge?
        if 'display_label' in d_style:
            result = d_style['display_label']
            del d_style['display_label']
            if not result:
                return ""

        # the preferred display label in the stylesheet
        if 'label' in d_style:
            result = d_style['label']
            del d_style['label']
            return result

        return d_edge['label']

    def process(self,
                edges: list) -> Digraph:

        for d_edge in edges:

            d_style = self._get_edge_style(d_edge)

            edge_label = self._get_edge_label(
                d_edge=d_edge,
                d_style=d_style)

            def get_tail_head() -> tuple:
                return d_edge['Subject'], d_edge['Object']

            tail_name, head_name = get_tail_head()

            self._graph.edge(tail_name=tail_name,
                             head_name=head_name,
                             label=edge_label,
                             **d_style)

        return self._graph
