#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Simplify the Complex Input AST """


from pprint import pprint


from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject


class InputTokensTransform(BaseObject):
    """ Transform Complex Input AST into a list-of-dictionaries 
        containing a simplified form of the AST suitable for the Portendo API 

    Sample Output:
       {
            "5":"number",
            "category":"appraisal",
            "give":"appraisal",
            "me":"",
            "random":""
        }
    """

    def __init__(self,
                 input_tokens: list):
        """
        Created:
            8-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/170
        :param input_tokens:
            the input AST
        """
        BaseObject.__init__(self, __name__)
        Enforcer.is_list(input_tokens)

        self._input_tokens = input_tokens
        self._ent_mapper = {
            'CARDINAL': 'number',
            'DATE': 'date',
        }

    @staticmethod
    def _name(token: dict or str) -> str:

        if type(token) == str:
            return token

        if 'swaps' in token:
            return token['swaps']['canon']

        return token['normal']

    def _type(self,
              token: dict or str) -> str:

        if type(token) == str:
            return token

        if self.isEnabledForDebug:
            Enforcer.is_dict(token)

        if 'swaps' in token:
            return token['swaps']['type']

        if 'ent' in token:
            if token['ent'] in self._ent_mapper:
                return self._ent_mapper[token['ent']]
            if self.isEnabledForWarning and len(token['ent']):
                self.logger.warning('\n'.join([
                    'spaCy ENT type not mappped',
                    f"\tENT: {token['ent']}"]))

        return ""

    def _process(self) -> list:
        results = []

        for d_token in self._input_tokens:
            results.append({
                "name": self._name(d_token),
                "type": self._type(d_token),
            })

        # GRAFFL-170-1032853911; ultra simplified output
        return {x['name']: x['type'] for x in results}

    def process(self) -> list:
        sw = Stopwatch()

        results = self._process()

        self.logger.debug('\n'.join([
            "Input Token Transformation Completed",
            f"\tTotal Tokens: {len(results)}",
            f"\tTotal Time: {str(sw)}"]))

        return results
