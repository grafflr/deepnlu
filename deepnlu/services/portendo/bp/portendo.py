#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Portendo performs Predictive Classification of deepNLU parsed ASTs """


from pprint import pformat

from baseblock import FileIO
from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject


from deepnlu.services.portendo.svc import ReadMapping
from deepnlu.services.portendo.svc import PredictMapping
from deepnlu.services.portendo.svc import SelectMapping
from deepnlu.services.portendo.dmo import InputTokensTransform


class Portendo(BaseObject):
    """ Portendo performs Predictive Classification of deepNLU parsed ASTs """

    def __init__(self,
                 schema_name: str,
                 absolute_path: str):
        """Initialize Portendo API

        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169
        Updated:
            8-Jun-2022
            craig@grafflr.ai
            *   make absolute_path a required parameter in pursuit of
                https://github.com/grafflr/deepnlu/issues/44
            *   read classifications from memory (not python files)
                https://github.com/grafflr/deepnlu/issues/45

        Args:
            schema_name (str): name of the schema containing classification rules
            absolute_path (str): absolute path to the location of the classification rules
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_str(schema_name)
            Enforcer.is_str(absolute_path)
            FileIO.exists_or_error(absolute_path)

        self._schema_name = schema_name

        self._d_index = ReadMapping(
            schema_name=schema_name,
            absolute_path=absolute_path).index()

    def _run(self,
             input_tokens: list) -> tuple:

        d_tokens = InputTokensTransform(input_tokens).process()
        input_tokens = [x for x in d_tokens]

        svcresult = {
            'transform': d_tokens,
            'input': input_tokens
        }

        mapping = PredictMapping(
            d_index=self._d_index,
            ontology_name=self._schema_name).process(svcresult)

        mapping = SelectMapping(
            results=mapping,
            d_index=self._d_index).process()

        if self.isEnabledForDebug:
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
