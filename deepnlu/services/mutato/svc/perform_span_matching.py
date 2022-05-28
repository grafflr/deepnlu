#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Span Matching """


from gettext import find
from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer

from deepnlu.datablock.svc import FindNER
from deepnlu.datablock.svc import FindSpans

from deepnlu.owlblock.bp import FindOntologyData

from deepnlu.services.mutato.dmo import SpanMatchFinder
from deepnlu.services.mutato.dmo import SpanMatchSwapper


class PerformSpanMatching(BaseObject):
    """Perform Span Matching

    Sample Input:
        the history of nursing

    Sample Rule:
        nursing_history ~ nurse+history

    Sample Match:
        "history of nursing" == nursing_history

    Sample Output:
        the nursing_history
    """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History

        Created:
            20-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/77
        Updated:
            26-May-2022
            craig@grafflr.ai
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7
        Updated:
            27-May-2022
            craig@grafflr.ai
            *   remove 'ontologies' and integrate 'find-ontology-data'
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            find_ontology_data (FindOntologyData): an instantiation of this object
        """
        BaseObject.__init__(self, __name__)
        self._span_match_finder = SpanMatchFinder(
            d_spans=find_ontology_data.spans(),
            span_keys=find_ontology_data.span_keys()).process

        print (">>>>>>>>>> ", type(find_ontology_data))
        self._span_match_swapper = SpanMatchSwapper(find_ontology_data)

    def _process(self,
                 tokens: list) -> list:

        matching_rules = self._span_match_finder(tokens)
        if not matching_rules or not len(matching_rules):
            return tokens

        tokens = self._span_match_swapper.process(
            tokens=tokens,
            matching_rules=matching_rules)

        return tokens

    def process(self,
                tokens: list) -> list:

        if self.isEnabledForInfo:
            sw = Stopwatch()
            Enforcer.is_list(tokens)

        swaps = self._process(tokens)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Span Swapping Completed",
                f"\tTotal Time: {str(sw)}"]))

        return swaps
