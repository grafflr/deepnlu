#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Perform Entity Inference Action where a match is found """


from baseblock import BaseObject


class FormEntityInference(BaseObject):
    """ Perform Entity Inference Action where a match is found """

    def __init__(self):
        """ Change Log

        Created:
            13-Jul-2022
            craig@grafflr.ai
                https://github.com/grafflr/deepnlu/issues/48
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                d_candidates: dict,
                input_tokens: list) -> list or None:
        """ Find Entity Triggers

        Args:
            d_candidates (dict): this is a list of entity names that are potentially applicable to the input tokens
            input_tokens (list): a list of input tokens extracted from text
        """

        def exists(candidate_values: list) -> bool:
            for candidate_value in candidate_values:
                if candidate_value not in input_tokens:
                    return False
            return True

        def generate(entity_key: str,
                     entity_values: list) -> str:
            return f"{entity_key}_{'_'.join(entity_values)}".strip()

        results = set()
        for key in d_candidates:
            for value_set in d_candidates[key]:
                if exists(value_set):
                    results.add(generate(key, value_set))

        if not len(results):
            return None

        return sorted(results, key=len, reverse=True)
