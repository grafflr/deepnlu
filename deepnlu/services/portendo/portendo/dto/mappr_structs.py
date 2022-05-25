#!/usr/bin/env python
# -*- coding: utf-8 -*-


from enum import Enum
from typing import TypedDict


class ExplainResult(Enum):
    NO_MAPPING_FOUND = 0

    FOUND_NONAMBIGUOUS_TYPE_1 = 10
    FOUND_NONAMBIGUOUS_TYPE_2 = 11

    FILTERED_RESULT_TYPE_1 = 20

    INCLUDE_NEAR_MATCH_1 = 30

    ONLY_ONE_MATCH = 50
    FILTER_BY_WEIGHT = 51
    FILTER_BY_COVERAGE = 52
    DUPLICATE_MAPPINGS_FOUND = 53


class MappingResult(TypedDict):
    confidence: float
    explain: ExplainResult
    classification: str


class MappingResults(TypedDict):
    results: list


class Markers(TypedDict):
    marker_name: str
    marker_type: str
