#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generates a GraphViz Node """


from typing import List, Dict, Tuple, Union


from pprint import pprint
from pprint import pformat
from graphviz import Digraph
from copy import deepcopy

from baseblock import Enforcer
from baseblock import BaseObject
from baseblock import TextUtils


class GraphvizNodeGenerator(BaseObject):
    """ Generates a GraphViz Node """

    def __init__(self,
                 graph: Digraph,
                 d_style: dict):
        """ Change History

        Created:
            5-Nov-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/102
        Updated:
            9-Nov-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/101
        Updated:
            18-May-2022
            craig@grafflr.ai
            *   updated in pursuit of
                https://github.com/grafflr/graffl-core/issues/384

        Args:
            graph (Digraph): the instantiated graph model
            d_style (dict): the in-memory stylesheet
        """
        BaseObject.__init__(self, __name__)
        self._graph = graph
        self._d_style = d_style

    def _validate_styles(self,
                         entities: List[dict]) -> None:
        """ Validate that incoming Entities have corresponding Stylesheet definitions

        Args:
            entities (List[dict]): the incoming entities

        Raises:
            ValueError: the Stylesheet is missing an entity type
        """

        for entity in entities:

            if 'style' not in entity:
                self.logger.error('\n'.join([
                    "Entity Style Not Defined",
                    f"\tEntity: {entity}"]))
                raise ValueError('Node Style Exception')

            if entity['style'] not in self._d_style:
                self.logger.error('\n'.join([
                    "Entity Style Not Found",
                    f"\tEntity: {entity}",
                    f"\tStyle: {pformat(self._d_style)}"]))
                raise ValueError('Node Style Exception')

    def process(self,
                entities: List[dict]) -> Digraph:
        """ Generate Graphviz Node Definitions

        Args:
            entities (List[dict]): the incoming entities

        Returns:
            Digraph: the modified graph
        """

        if self.isEnabledForDebug:  # >DEV/INT
            Enforcer.is_list_of_dicts(entities)

        if self.isEnabledForInfo:  # <PROD
            self._validate_styles(entities)

        for entity in entities:

            d_node_style = self._d_style[entity['style']]
            entity_label = TextUtils.split_on_len(entity['label'])

            self._graph.node(entity['node_id'],
                             label=entity_label,
                             **d_node_style)

        return self._graph
