#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Analyze Incoming Entity Names for Downstream Predictive Classification """


from collections import defaultdict

from baseblock import BaseObject


class AnalyzeEntityNames(BaseObject):
    """ Analyze Incoming Entity Names for Downstream Predictive Classification """

    def __init__(self):
        """ Change Log

        Created:
            13-Jul-2022
            craig@graffl.ai
                https://github.com/grafflr/deepnlu/issues/48
        """
        BaseObject.__init__(self, __name__)

    def _filter(self,
                entity_names: list) -> list:
        def normalize(input_text: str) -> str:
            if '_' in input_text:
                input_text = input_text.replace('_', ' ')
            return input_text.strip().lower()

        entity_names = [x for x in entity_names if x and len(x)]
        entity_names = [normalize(x) for x in entity_names]
        entity_names = [x for x in entity_names if x and len(x)]
        entity_names = [x for x in entity_names if ' ' in x]
        entity_names = sorted(set(entity_names), key=len, reverse=True)

        return entity_names

    def process(self,
                entity_names: list) -> dict:
        """ Analyze Entity Names

        Args:
            entity_names (list): a list of entity names to infer
        """
        d_entities = defaultdict(list)

        entity_names = self._filter(entity_names)
        for entity_name in entity_names:
            tokens = entity_name.split()
            d_entities[tokens[0]].append(tokens[1:])

        return dict(d_entities)
