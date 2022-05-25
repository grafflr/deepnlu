#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Portendo performs Predictive Classification of deepNLU parsed ASTs """


from pprint import pformat
from pprint import pprint

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer

from datablock import FindClassifications

from portendo.svc import PredictMapping
from portendo.svc import SelectMapping
from portendo.dmo import InputTokensTransform


class Portendo(BaseObject):
    """ Portendo performs Predictive Classification of deepNLU parsed ASTs """

    __slots__ = (
        '_input_tokens',
        '_ontology_name',
    )

    def __init__(self,
                 ontology_name: str):
        """Initialize Portendo API

        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169

        Args:
            ontology_name (str): the Ontology provenance
        """
        BaseObject.__init__(self, __name__)
        Enforcer.is_str(ontology_name)

        self._ontology_name = ontology_name
        self._indices = FindClassifications(ontology_name)

        if self.isEnabledForDebug:
            self._indices.print()

    def _run(self,
             input_tokens: list) -> tuple:

        d_tokens = InputTokensTransform(input_tokens).process()
        input_tokens = [x for x in d_tokens]

        svcresult = {
            'transform': d_tokens,
            'input': input_tokens
        }

        mapping = PredictMapping(
            indices=self._indices,
            ontology_name=self._ontology_name).process(svcresult)

        mapping = SelectMapping(
            results=mapping,
            scoring=self._indices.score).process()

        self.logger.debug('\n'.join([
            "Mapping Completed",
            f"\tInput:\n{pformat(input_tokens)}",
            f"\tOutput:\n{pformat(mapping)}"]))

        if not len(mapping):
            return {
                'result': None,
                'tokens': d_tokens
            }

        return {
            'result': mapping,
            'tokens': d_tokens
        }

    def run(self,
            input_tokens: list) -> tuple:

        sw = Stopwatch()

        svcresult = self._run(input_tokens)

        self.logger.info('\n'.join([
            "Portendo Service Completed",
            f"\tTotal Time: {str(sw)}",
            f"\tResult:\n{pformat(svcresult)}"]))

        return svcresult
