#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Classify Input using the Portendo Microservice """


from pprint import pprint
from pprint import pformat


from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import Enforcer


from deepnlu.services.portendo import Portendo


class ClassifyInput(BaseObject):
    """ Classify Input using the Portendo Microservice """

    __slots__ = (
        '_d_parse_ast',
        '_portendo',
    )

    def __init__(self,
                 d_parse_ast: dict,
                 ontology_name: str,
                 d_classification_rules: dict):
        """ Initialize the Service

        Created:
            7-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/167

        Args:
            d_parse_ast (dict): a deepNLU AST outcome
            ontology_name (str): an Ontology to classify against
            d_classification_rules (dict): a set of classification rules loaded from a manifest file
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_dict(d_parse_ast)
            Enforcer.is_str(ontology_name)
            Enforcer.is_dict(d_classification_rules)

            self.logger.debug('\n'.join([
                "Initialized Service",
                f"\tTotal Classification Rules: {len(d_classification_rules)}",
                f"\tOntology Name: {ontology_name}"]))

        self._d_parse_ast = d_parse_ast

        self._portendo = Portendo(
            ontology_name=ontology_name,
            d_classification_rules=d_classification_rules).run

    def _process(self) -> list:

        d_classifications, d_user_tokens = self._portendo(
            self._d_parse_ast['tokens'])

        if not d_classifications or not len(d_classifications):
            return {
                'target': None,
                'rule': None,
                'tokens': d_user_tokens
            }

        results = []
        for d_classification in d_classifications:

            def target() -> str:
                target = d_classification['classification']
                if '#' in target:
                    return target.split('#')[0].strip()
                return target

            results.append({
                'target': target(),
                'rule': d_classification,
                'tokens': d_user_tokens
            })

        return results

    def process(self) -> list:

        sw = Stopwatch()

        results = self._process()

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Input Classification Successful",
                f"\tTotal Time: {str(sw)}",
                f"{pformat(results)}"]))

        return results
