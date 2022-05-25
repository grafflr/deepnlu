#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Convenience Recipe for Jupyter Displacy Notebooks """


import os
import pprint
import logging

import spacy

from baseblock import BaseObject
from datablock.svc import FindNER

from erogito import ErogitoAPI

from deepnlu.svc import ParseTextOneShot


class RunJupyterDisplacy(BaseObject):
    """ Convenience Recipe for Jupyter Displacy Notebooks """

    def __init__(self,
                 ontology_name: str = "nursing"):
        """
        Created:
            13-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/26
        """
        BaseObject.__init__(self, __name__)
        os.environ['GRAFFL_ONTOLOGIES'] = ontology_name

        for microservice in ['datablock', 'accipio', 'erogito', 'mutato', 'deepnlu']:
            logging.getLogger(microservice).setLevel(logging.ERROR)

        self._ner_finder = FindNER()
        self._erogito_api = ErogitoAPI()
        self._deepnlu = ParseTextOneShot()

    def _options(self) -> dict:
        return {
            'colors': self._ner_finder.colors(),
            'ents': list(self._ner_finder.colors().keys())}

        # return {
        #     'colors': {
        #         'NER': '#9DAAB6',
        #         'ACTIVITY': '#106b5f',
        #         'AGENT': '#77aaff',
        #         'ARTIFACT': '#bf7979',
        #         'ASSOC': '#5588ff',
        #         'CARDINAL': '#6e4433',
        #         'CARE': '#f6b26b',
        #         'DATE': '#0031f7',
        #         'DIPLOMA': '#f6e5b3',
        #         'EDU': '#8296e4',
        #         'EVAL': '#fff2cc',
        #         'EVENT': '#e69138',
        #         'FAC': '#eac32a',
        #         'GEO': '#e8702a',
        #         'GROUP': '#99ccff',
        #         'LANGUAGE': '#940f0f',
        #         'LOC': '#ffa700',
        #         'MEASURE': '#e3c7ff',
        #         'MONEY': '#d07129',
        #         'NORP': '#3366ff',
        #         'ORDINAL': '#0031f7',
        #         'ORG': '#e8702a',
        #         'PERCENT': '#ff24ab',
        #         'PERSON': '#bbeeff',
        #         'PRODUCT': '#d07129',
        #         'PROFESSION': '#38761d',
        #         'QUALITY': '#ffd966',
        #         'QUANTITY': '#ffc0f9',
        #         'REG': '#fdeded',
        #         'RULE': '#9b794f',
        #         'TIME': '#f7c665',
        #         'WORK_OF_ART': '#311b29'},
        #     'ents': [
        #         'NER',
        #         'AGENT',
        #         'GROUP',
        #         'PERSON',
        #         'ASSOC',
        #         'NORP',
        #         'ARTIFACT',
        #         'DIPLOMA',
        #         'REG',
        #         'RULE',
        #         'EVENT',
        #         'CARE',
        #         'EVAL',
        #         'QUALITY',
        #         'QUANTITY',
        #         'MEASURE',
        #         'ACTIVITY',
        #         'FAC',
        #         'CARDINAL',
        #         'DATE',
        #         'EDU',
        #         'GEO',
        #         'LANGUAGE',
        #         'LOC',
        #         'MONEY',
        #         'ORDINAL',
        #         'ORG',
        #         'PERCENT',
        #         'PRODUCT',
        #         'PROFESSION',
        #         'TIME',
        #         'WORK_OF_ART']}

    def process(self,
                input_text: str) -> tuple:
        result = self._deepnlu.process(input_text)

        displacy = self._erogito_api.displacy(result)

        if type(displacy) == dict:
            displacy = [displacy]

        return result, displacy, self._options()
