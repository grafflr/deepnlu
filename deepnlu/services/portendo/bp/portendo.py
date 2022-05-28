#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Portendo performs Predictive Classification of deepNLU parsed ASTs """


import os
from pprint import pformat
from pprint import pprint

from baseblock import EnvIO
from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject

from deepnlu.datablock import FindClassifications

from deepnlu.services.portendo.svc import PredictMapping
from deepnlu.services.portendo.svc import SelectMapping
from deepnlu.services.portendo.dmo import InputTokensTransform


class Portendo(BaseObject):
    """ Portendo performs Predictive Classification of deepNLU parsed ASTs """

    def __init__(self,
                 schema_name: str,
                 absolute_path: str = None):
        """Initialize Portendo API

        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169

        Args:
            schema_name (str): name of the schema containing classification rules
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_str(schema_name)

        self._schema_name = schema_name

        if not absolute_path or not len(absolute_path):
            absolute_path = os.path.normpath(
                os.path.join(
                    EnvIO.str_or_exception('GRAFFLR_HOME'),
                    'apps/blocks/datablock/datablock/os/manifest',
                    schema_name))

        self._indices = FindClassifications(
            schema_name=schema_name,
            absolute_path=absolute_path)

        if self.isEnabledForDebug:
            self._indices.print()

    def is_known_model(self,
                       input_text: str) -> FindClassifications:
        """ Check if Input Text is a known model

        Args:
            input_text (str): any input text of any length

        Returns:
            bool: True if this is a model that exists in the underlying mapping.py file
        """
        return self._indices.is_known_model(input_text)

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
            ontology_name=self._schema_name).process(svcresult)

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
