#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Find Entity Names capable of triggering an Inference Action """


from collections import defaultdict

from baseblock import BaseObject


class FindEntityTriggers(BaseObject):
    """ Find Entity Names capable of triggering an Inference Action """

    def __init__(self,
                 d_entities: dict):
        """ Change Log

        Created:
            13-Jul-2022
            craig@graffl.ai
                https://github.com/grafflr/deepnlu/issues/48
        """
        BaseObject.__init__(self, __name__)
        self._d_entities = d_entities

    def process(self,
                input_tokens: list) -> list or None:
        """ Find Entity Triggers

        Args:
            entity_names (list): a list of entity names to infer
        """
        triggers = set()
        for key in self._d_entities:
            if key in input_tokens:
                triggers.add(key)

        if len(triggers):
            return sorted(triggers, key=len, reverse=True)

        return None
