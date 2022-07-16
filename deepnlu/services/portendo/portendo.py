#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Wrapper API over Portendo Orcheration """


from baseblock import BaseObject
from deepnlu.services.mutato import svc

from deepnlu.services.portendo.schema.bp import SchemaOrchestrator
from deepnlu.services.portendo.entity.bp import EntityOrchestrator


class Portendo(BaseObject):
    """ Wrapper API over Portendo Orcheration """

    def __init__(self):
        """Initialize Portendo API

        Created:
            13-Jul-2022
            craig@graffl.ai
                https://github.com/grafflr/deepnlu/issues/48
        """
        self._schema_inference = None
        self._entity_inference = None

    def schema(self,
               schema_name: str,
               absolute_path: str,
               input_tokens: list) -> dict:
        """ Run the Schema Orchestrator

        Args:
            schema_name (str): name of the schema containing classification rules
            absolute_path (str): absolute path to the location of the classification rules
            input_tokens (list): a flat list of tokens extracted from text
                Sample Input:
                    ['network_topology', 'user', 'customer']
        """
        if not self._schema_inference:
            self._schema_inference = SchemaOrchestrator(
                schema_name=schema_name,
                absolute_path=absolute_path).run

        svcresult = self._schema_inference(input_tokens)

        return svcresult

    def entity(self,
               entity_names: list,
               input_tokens: list,
               deepnlu: dict = None) -> dict:
        """ Run the Schema Orchestrator

        Args:
            entity_names (list): a list of entity names to infer
            input_tokens (list): a flat list of tokens extracted from text
                Sample Input:
                    ['network_topology', 'user', 'customer']
            deepnlu (dict, optional): the deepNLU service result
                this data structure is used to provide confidence intervals for the token inference
                if not provided, token inference will be performed without confidence intervals
        """
        if not self._entity_inference:
            self._entity_inference = EntityOrchestrator(
                entity_names=entity_names).run

        svcresult = self._entity_inference(
            input_tokens=input_tokens,
            deepnlu=deepnlu)

        return svcresult
