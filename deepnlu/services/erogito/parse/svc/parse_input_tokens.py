#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Use spaCy to Parse Input Tokens """


import pprint


from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject


from deepnlu.services.erogito.parse.dmo import GrafflParserSpacy
from deepnlu.services.erogito.parse.dmo import GrafflParserWordnet
from deepnlu.services.erogito.parse.dmo import GrafflParserNormalize
from deepnlu.services.erogito.parse.dmo import GrafflParserPunctuation
from deepnlu.services.erogito.parse.dmo import GrafflParserCoordinates
from deepnlu.services.erogito.parse.dmo import GrafflParserSquots
from deepnlu.services.erogito.parse.dmo import GrafflParserResultSet


class ParseInputTokens(BaseObject):
    """ Use spaCy to Parse Input Tokens """

    def __init__(self):
        """
        Created:
            1-Oct-2021
            craig@grafflr.ai
        Updated:
            13-Oct-2021
            craig@grafflr.ai
            *   refactored into component parts in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                tokens: list) -> list:

        sw = Stopwatch()

        tokens = GrafflParserSquots().process(tokens)
        doc = GrafflParserSpacy().process(' '.join(tokens))

        results = GrafflParserResultSet().process(doc)
        results = GrafflParserPunctuation().process(results)
        results = GrafflParserNormalize().process(results)
        results = GrafflParserCoordinates().process(results)
        results = GrafflParserWordnet().process(results)

        self.logger.info('\n'.join([
            "Input Token Parsing Completed",
            f"\tTotal Tokens: {len(results)}",
            f"\tTotal Time: {str(sw)}"]))

        return results
