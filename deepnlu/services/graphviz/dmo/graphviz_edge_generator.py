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

        Args:
            graph (Digraph): the instantiated graph model
            d_style (dict): the in-memory stylesheet
        """
        BaseObject.__init__(self, __name__)
        self._graph = graph
        self._d_style = d_style

    def _validate_styles(self,
                         edges: List[dict]) -> None:
        """ Validate that incoming Edges have corresponding Stylesheet definitions

        Args:
            edges (List[dict]): the incoming edges

        Raises:
            ValueError: the Stylesheet is missing an edge type
        """

        for edge in edges:

            if 'style' not in edge:
                self.logger.error('\n'.join([
                    "Edge Style Not Defined",
                    f"\tEdge: {edge}"]))
                raise ValueError('Edge Style Exception')

            if edge['style'] not in self._d_style:
                self.logger.error('\n'.join([
                    "Edge Style Not Found",
                    f"\tEdge Style: {edge['style']}",
                    f"\tKnown Styles: {sorted(self._d_style.keys())}"]))
                raise ValueError('Edge Style Exception')

    def process(self,
                edges: list) -> Digraph:

        self._validate_styles(edges)

        for edge in edges:

            def get_style() -> dict:
                return deepcopy(self._d_style[edge['Predicate'].lower()])

            d_style = get_style()

            def label() -> bool:

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

                return edge['label']

            edge_label = label()

            def get_tail_head() -> tuple:
                # if edge['Predicate'].lower() == 'ancestor':
                #     return edge['Object'], edge['Subject']
                return edge['Subject'], edge['Object']

            tail_name, head_name = get_tail_head()

            self._graph.edge(tail_name=tail_name,
                             head_name=head_name,
                             label=edge_label,
                             **d_style)

        return self._graph
