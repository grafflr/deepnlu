#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Portendo performs Predictive Classification of deepNLU parsed ASTs """


from pprint import pformat

from baseblock import FileIO
from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject


class EntityOrchestrator(BaseObject):
    """ Portendo performs Predictive Classification of deepNLU parsed ASTs 

    This Orchestration sequence requires a list of entity names
    This is a less nuanced form of classification than the schema orchestrator
    """

    def __init__(self,
                 entity_names: list):
        """Initialize Portendo API

        Created:
            13-Jul-2022
            craig@grafflr.ai
                https://github.com/grafflr/deepnlu/issues/48

        Args:
            entity_names (list): a list of entity names to infer
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(entity_names)

        self._entity_names = entity_names

    def _run(self,
             input_tokens: list) -> tuple:

        # d_tokens = InputTokensTransform(input_tokens).process()
        # input_tokens = [x for x in d_tokens]

        # svcresult = {
        #     'transform': d_tokens,
        #     'input': input_tokens
        # }

        # mapping = PredictMapping(
        #     d_index=self._d_index,
        #     ontology_name=self._schema_name).process(svcresult)

        # mapping = SelectMapping(
        #     results=mapping,
        #     d_index=self._d_index).process()

        # if self.isEnabledForDebug:
        #     self.logger.debug('\n'.join([
        #         "Mapping Completed",
        #         f"\tInput:\n{pformat(input_tokens)}",
        #         f"\tOutput:\n{pformat(mapping)}"]))

        # if not len(mapping):
        #     return {
        #         'result': None,
        #         'tokens': d_tokens
        #     }

        return {
            'result': None,
            'tokens': None
        }

    def run(self,
            input_tokens: list,
            deepnlu: dict = None) -> tuple:
        """ Run the Entity Orchestrator

        Args:
            input_tokens (list): a list of entity names extracted from text
            deepnlu (dict, optional): the deepNLU service result
                this data structure is used to provide confidence intervals for the token inference
                if not provided, token inference will be performed without confidence intervals

        Returns:
            tuple: the service result
        """

        sw = Stopwatch()

        svcresult = self._run(input_tokens)

        self.logger.info('\n'.join([
            "Portendo Entity Orchestrator Completed",
            f"\tTotal Time: {str(sw)}",
            f"\tResult:\n{pformat(svcresult)}"]))

        return svcresult
