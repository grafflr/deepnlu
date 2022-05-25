#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Predict a Mapping"""


from pprint import pformat

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer

from deepnlu.datablock import FindClassifications

from deepnlu.services.portendo.dto import ExplainResult
from deepnlu.services.portendo.dto import MappingResult
from deepnlu.services.portendo.dto import MappingResults
from deepnlu.services.portendo.dmo import ComputerIncludeOneOf
from deepnlu.services.portendo.dmo import ComputerIncludeRecursive
from deepnlu.services.portendo.dmo import ComputerIncludeAllOf
from deepnlu.services.portendo.dmo import ComputerExcludeOneOf
from deepnlu.services.portendo.dmo import ComputerExcludeAllOf
from deepnlu.services.portendo.dmo import ConfidenceExcludeAllOf
from deepnlu.services.portendo.dmo import ConfidenceIncludeAllOf
from deepnlu.services.portendo.dmo import ComputerStartsWith


class PredictMapping(BaseObject):
    """Predict a Mapping"""

    def __init__(self,
                 ontology_name: str,
                 indices: FindClassifications):
        """ Initialize Service

        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/169

        Args:
            ontology_name (str):
            d_classifications (dict): [description]
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_str(ontology_name)

            self.logger.debug('\n'.join([
                "Initialized Service",
                f"\tOntology Name: {ontology_name}"]))

        self._include_one_of = ComputerIncludeOneOf(
            d_mapping=indices.mapping,
            d_include_oneof=indices.include_one_of).process

        self._include_all_of = ComputerIncludeAllOf(
            d_mapping=indices.mapping,
            d_include_allof=indices.include_all_of).process

        self._exclude_one_of = ComputerExcludeOneOf(
            d_mapping=indices.mapping,
            d_exclude_oneof=indices.exclude_one_of).process

        self._exclude_all_of = ComputerExcludeAllOf(
            d_mapping=indices.mapping,
            d_exclude_allof=indices.exclude_all_of).process

        self._startswith = ComputerStartsWith(
            d_mapping=indices.mapping,
            d_startswith=indices.startswith).process

        # TODO: include inference via taxonomical relationships
        # self._include_r1 = ComputerIncludeRecursive(
        #     indices=indices,
        #     recursion_level=1,
        #     ontology_name=ontology_name).process

        # self._include_r2 = ComputerIncludeRecursive(
        #     indices=indices,
        #     recursion_level=2,
        #     ontology_name=ontology_name).process

    def _process(self,
                 d_tokens: dict) -> MappingResults:
        mapping_results = []

        sw = Stopwatch()

        d_transform = d_tokens['transform']  # has token:canon mapping
        d_input = d_tokens['input']  # just text tokens

        m_include_oneof = self._include_one_of(d_transform)
        m_include_allof = self._include_all_of(d_transform)
        m_exclude_oneof = self._exclude_one_of(d_transform)
        m_exclude_allof = self._exclude_all_of(d_transform)
        m_startswith = self._startswith(d_input)

        # m_include_r1 = self._include_r1(d_input_tokens)
        # m_include_r2 = self._include_r2(d_input_tokens)
        # m_include_r2 = {k: m_include_r2[k] for k in m_include_r2
        #                 if k not in m_include_r1}

        if self.isEnabledForDebug:
            Enforcer.is_dict(m_include_oneof)
            Enforcer.is_dict(m_include_allof)
            Enforcer.is_dict(m_exclude_oneof)
            Enforcer.is_dict(m_exclude_allof)
            Enforcer.is_dict(m_startswith)

        return {
            'include_one_of': m_include_oneof,
            # 'include_r1': m_include_r1,
            # 'include_r2': m_include_r2,
            'include_all_of': m_include_allof,
            'exclude_one_of': m_exclude_oneof,
            'exclude_all_of': m_exclude_allof,
            'startswith': m_startswith,
        }

    def process(self,
                d_tokens: dict) -> MappingResults:
        sw = Stopwatch()

        results = self._process(d_tokens)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Mapping Prediction Completed",
                f"\tTotal Time: {str(sw)}",
                f"\tTotal Results: {len(results)}"]))

        if self.isEnabledForDebug and len(results):
            self.logger.debug('\n'.join([
                "Mapping Prediction Results",
                f"{pformat(results)}"]))

        return results
