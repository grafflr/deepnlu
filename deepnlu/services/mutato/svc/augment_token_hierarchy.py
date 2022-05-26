#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Augment Tokens with Descendant and Ancestory Hierarchy for Inference Purposes """


from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer
from deepnlu.datablock.dto import get_ontology_name


class AugmentTokenHierarchy(BaseObject):
    """ Augment Tokens with Descendant and Ancestory Hierarchy for Inference Purposes """

    def __init__(self,
                 find_types_cb: object,
                 ontology_name: object = None):
        """
        Created:
            14-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/188
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)
        self._find_types = find_types_cb

    def _process(self,
                 tokens: list) -> list:
        for token in tokens:
            token['ancestors'] = self._find_types.ancestors(token['normal'])
            token['descendants'] = self._find_types.descendants(
                token['normal'])

        return tokens

    def process(self,
                tokens: list) -> list:
        Enforcer.is_list(tokens)

        sw = Stopwatch()

        tokens = self._process(tokens)

        self.logger.info('\n'.join([
            "Hierarchy Augmentation Completed",
            f"\tTotal Time: {str(sw)}"]))

        return tokens
