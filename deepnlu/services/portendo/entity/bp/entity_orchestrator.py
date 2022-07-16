#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Portendo performs Predictive Classification of deepNLU parsed ASTs """


from pprint import pformat

from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.services.portendo.entity.svc import AnalyzeEntityNames
from deepnlu.services.portendo.entity.svc import FindEntityTriggers
from deepnlu.services.portendo.entity.svc import FormEntityInference


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
            craig@graffl.ai
                https://github.com/grafflr/deepnlu/issues/48

        Args:
            entity_names (list): a list of entity names to infer
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list_of_str(entity_names)

        self._d_entities = AnalyzeEntityNames().process(entity_names)
        self._find_triggers = FindEntityTriggers(self._d_entities).process
        self._form_inference = FormEntityInference().process

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Initialized Orchestrator",
                f"\tTotal Entity Names: {len(entity_names)}",
                f"\tAnalyzed Entities: {self._d_entities}"]))

    def _run(self,
             input_tokens: list) -> tuple or None:

        triggers = self._find_triggers(input_tokens)
        if not triggers:
            return None

        d_candidates = {k: self._d_entities[k] for k in triggers}

        result = self._form_inference(
            d_candidates=d_candidates,
            input_tokens=input_tokens)

        return {
            'result': result,
            'tokens': input_tokens
        }

    def run(self,
            input_tokens: list,
            deepnlu: dict = None) -> tuple or None:
        """ Run the Entity Orchestrator

        Args:
            input_tokens (list): a list of entity names extracted from text
            deepnlu (dict, optional): the deepNLU service result
                this data structure is used to provide confidence intervals for the token inference
                if not provided, token inference will be performed without confidence intervals

        Returns:
            tuple or None: the service result (if any)
        """

        if self.isEnabledForDebug:
            Enforcer.is_list_of_str(input_tokens)

        sw = Stopwatch()

        svcresult = self._run(input_tokens)

        if self.isEnabledForInfo:
            if svcresult:
                self.logger.info('\n'.join([
                    "Portendo Entity Orchestrator Completed",
                    f"\tTotal Time: {str(sw)}",
                    f"\tResult:\n{pformat(svcresult)}"]))
            else:
                self.logger.info('\n'.join([
                    "Portendo Entity Orchestrator Completed",
                    f"\tTotal Time: {str(sw)}",
                    f"\tNo Entity Inference Performed"]))

        return svcresult
