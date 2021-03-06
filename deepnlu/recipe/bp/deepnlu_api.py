#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" deepNLU Orchestrator """


import os

from baseblock import FileIO
from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.recipe.svc import ProcessInputFiles
from deepnlu.recipe.svc import ParseTextOneShot
from deepnlu.recipe.svc import ResultsAsDataFrame
from deepnlu.recipe.dmo import InputPathReader
from deepnlu.owlblock.bp import FindOntologyData


class DeepNluAPI(BaseObject):
    """ deepNLU Orchestrator """

    def __init__(self):
        """ Change History

        Created:
            1-Oct-2021
            craig@graffl.ai
        Updated:
            26-May-2022
            craig@graffl.ai
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7
        """
        BaseObject.__init__(self, __name__)
        self._to_dataframe = ResultsAsDataFrame().process

    def to_csv(self,
               results: list,
               include_position: bool = True) -> list:
        """ Transform deepNLU results to a pandas-compatible input format

        Args:
            results (list): the deepNLU results
            include_position (bool): include positionary elements

        Returns:
            list: a flat list
        """
        if self.isEnabledForDebug:
            Enforcer.is_list(results)

        return self._to_dataframe(results, include_position)

    def handle_directory(self,
                         input_dir: str,
                         output_dir: str,
                         ontologies: list) -> list:
        """ DeepNLU on an input directory of files

        Args:
            input_dir (str): input directory of text files
            output_dir (str): output directory of JSON results
            ontologies (list): one-or-more Ontology models to use in processing

        Returns:
            list: the JSON results
        """
        if self.isEnabledForDebug:
            Enforcer.is_str(input_dir)
            Enforcer.is_str(output_dir)
            Enforcer.is_list(ontologies)

        def load_files() -> list:
            return InputPathReader().process(input_dir)

        svcresult = ProcessInputFiles(input_files=load_files(),
                                      output_dir=output_dir).process()

        return svcresult

    def handle_text(self,
                    input_text: str,
                    ontologies: list,
                    absolute_path: str) -> tuple:
        """ DeepNLU on single line of input text

        Args:
            input_text (str): input text of any length
            ontologies (list): one-or-more Ontology models to use in processing
            absolute_path (str): absolute path to OWL models

        Returns:
            tuple: the deepNLU result and tokens
        """
        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)
            Enforcer.is_list(ontologies)

        finder = FindOntologyData(
            ontologies=ontologies,
            absolute_path=absolute_path)

        svc = ParseTextOneShot(finder)
        svcresult = svc.process(input_text)

        tokens = [x['Canon'] for x in self.to_csv(svcresult)]
        # tokens = [x['normal'] for x in
        #           svcresult[0][0]['tokens'] if 'swaps' in x]
        # [tokens.append(x) for x in svcresult[0][0]['inferred']]
        tokens = sorted(set(tokens), key=len, reverse=True)

        return svcresult, tokens
