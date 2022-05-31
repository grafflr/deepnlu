#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" An API for generating Graphviz dot structures """


from graphviz import Digraph

from baseblock import BaseObject

from imaginor.graphviz.svc import GenerateEntityStructure
from imaginor.graphviz.svc import GenerateEntityGraph


class GraphvizAPI(BaseObject):
    """ An API for generating Graphviz dot structures """

    def __init__(self):
        """ Change History

        Created:
            5-Nov-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/102
        """
        BaseObject.__init__(self, __name__)

    def generate(self,
                 entity_names: list,
                 ontologies: list) -> Digraph:

        generate_structure = GenerateEntityStructure().process
        generate_graph = GenerateEntityGraph().process

        d_result = generate_structure(
            ontologies=ontologies,
            entity_names=entity_names)

        return generate_graph(d_result)


if __name__ == "__main__":

    entity_names = ['weather']
    ontologies = ['chitchat']
    GraphvizAPI().generate(entity_names, ontologies)
