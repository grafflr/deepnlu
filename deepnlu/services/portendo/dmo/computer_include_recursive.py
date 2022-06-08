#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from collections import Counter

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer


class ComputerIncludeRecursive(BaseObject):
    """ Establish Recursive Mappings """

    def __init__(self,
                 d_index: dict,
                 recursion_level: int):
        """ Change History

        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        Updated:
            8-Jun-2022
            craig@grafflr.ai
            *   read schema in-memory 
                https://github.com/grafflr/deepnlu/issues/45

        Args:
            d_index (dict): the in-memory schema
        """
        BaseObject.__init__(self, __name__)
        self._mapping = d_index['mapping']
        self._recursion_level = recursion_level
        self._d_exclude_allof = d_index['include_one_of']

    def _taxonomy_lookup(self,
                         token_name: str,
                         token_type: str) -> tuple or None:

        if token_type == "owl_local":
            token_name = f"local_{token_name}"

        if token_name in self._d_server['marker_types_rev']:
            parent_name = self._d_server['marker_types_rev'][token_name]

            if parent_name.startswith("local_"):
                parent_name = parent_name[6:]

            return parent_name, "owl_local"

        return None, None

    def _find_parent(self,
                     results: list,
                     token_name: str,
                     token_type: str,
                     max_parent_level: int,
                     cur_parent_level: int) -> None:
        """ Purpose:
            Find Parent name for a given Token name
        Sample Input:
            { disk_drive: owl_local }
        Sample Output:
            { computer_storage: owl_local }
        """

        parent_name, parent_type = self._taxonomy_lookup(token_name=token_name,
                                                         token_type=token_type)

        if parent_name and parent_type:
            results.append((parent_name, parent_type))

            if cur_parent_level + 1 < max_parent_level:
                self._find_parent(results=results,
                                  token_name=parent_name,
                                  token_type=parent_type,
                                  max_parent_level=max_parent_level,
                                  cur_parent_level=cur_parent_level+1)

    def _to_parents(self,
                    d_input_tokens: dict) -> dict:
        """ Purpose:
            Given Input Tokens find Parents Tokens
        Sample Input:
            [   {'disk_drive': 'owl_local'} ]
        Sample Results (Intermediate Stage):
            [   ('computer_storage', 'owl_local'), 
                ('computer_hardware', 'owl_local') ]
        Sample Output:
            {   'computer_hardware': 'owl_local', 
                'computer_storage': 'owl_local' }
        """
        results = []
        for input_token in d_input_tokens:
            self._find_parent(results=results,
                              token_name=input_token,
                              token_type=d_input_tokens[input_token],
                              max_parent_level=self._recursion_level,
                              cur_parent_level=0)

        return {x[0]: x[1] for x in results}

    def _coverage(self,
                  weight: int,
                  mapping_name: str) -> float:
        """ Determine the Coverage """
        d_mapping = self._mapping[mapping_name][0]['include_one_of']
        total_markers = len(d_mapping)
        return round(weight / total_markers, 2)

    def _weight(self,
                common: set) -> dict:
        c = Counter()  # NLP-886-12297; this gives weights
        for marker in common:
            mapping = self._d_include_oneof[marker]
            [c.update({x: 1}) for x in mapping]

        return dict(c)

    def process(self,
                d_input_tokens: dict) -> set:
        # sw = Stopwatch()

        # s_mapping = set(self._d_include_oneof.keys())
        # d_parents = self._to_parents(input_tokens)

        # s_markers = set(d_parents.keys())
        # common = s_mapping.intersection(s_markers)

        # d_results = {}

        # d_weights = self._weight(common)
        # for mapping_name in d_weights:
        #     weight = d_weights[mapping_name]
        #     coverage = self._coverage(weight=weight,
        #                               mapping_name=mapping_name)
        #     d_results[mapping_name] = {"weight": weight,
        #                                "coverage": coverage}

        # self.logger.debug('\n'.join([
        #     "Computation Complete: Include Recursive",
        #     f"\tTotal Markers: {len(markers)}",
        #     f"\tTotal Results: {len(d_results)}",
        #     f"\tTotal Time: {str(sw)}"]))

        # return d_results
        raise NotImplementedError
