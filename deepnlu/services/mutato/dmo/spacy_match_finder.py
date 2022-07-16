#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find Contiguous Sequences of spaCy Entities """


import pprint
import logging

from baseblock import Stopwatch
from baseblock import BaseObject


class SpacyMatchFinder(BaseObject):
    """ Find Contiguous Sequences of spaCy Entities keyed by Token Position 

    Sample Input:
        [
            {    "ent": "",         "text": "blah " }
            {    "ent": "ALPHA",    "text": "blah "  }
            {    "ent": "GAMMA",    "text": "blah "  }
            {    "ent": "GAMMA",    "text": "blah "  }
            {    "ent": "",         "text": "blah "  }
            {    "ent": "PHI",      "text": "blah "  }
            {    "ent": "",         "text": "blah "  }
            {    "ent": "BETA",     "text": "blah "  }
            {    "ent": "BETA",     "text": "blah "  }
        ]

    Sample Output:
        [
            {   "2": {  "ent":"GAMMA", "text":"blah"  },
                "3": {  "ent":"GAMMA", "text":"blah"  }
            },
            {   "7":{   "ent":"BETA",  "text":"blah"  }
                "8":{   "ent":"BETA",  "text":"blah"  }
            }
        ]

    This algorithm demonstrates that two contiguous sequences of entities exist in the parsed text
    -   Tokens at position 2,3 can be collapsedd into a single GAMMA entity
    -   Tokens at position 7,8 can be collapsedd into a single BETA entity
    """

    def __init__(self):
        """
        Created:
            22-Oct-2021
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/35
        Updated:
            29-Oct-2021
            craig@graffl.ai
            *   Update for Recursive Processing
                https://github.com/grafflr/graffl-core/issues/96
        """
        BaseObject.__init__(self, __name__)

    def _process(self,
                 tokens: list) -> list:

        i = 0
        master = []

        max_len = len(tokens) - 1

        while i < max_len:

            token_curr = tokens[i]
            curr_i = i

            def curr_ent() -> bool:
                if 'ent' not in token_curr:
                    return False
                if not token_curr['ent']:
                    return False
                return True

            if not curr_ent():
                i += 1
                continue

            token_next = tokens[i + 1]
            next_i = i + 1

            def next_ent() -> bool:
                if 'ent' not in token_next:
                    return False
                if not token_next['ent']:
                    return False
                return token_next['ent'] == token_curr['ent']

            if not next_ent():
                i += 1
                continue

            i += 2

            buffer = {
                curr_i: token_curr,
                next_i: token_next
            }

            while i < len(tokens):

                def is_match():
                    if 'ent' not in tokens[i]:
                        return False
                    if not tokens[i]['ent']:
                        return False
                    return tokens[i]['ent'] == tokens[i-1]['ent']

                if is_match():
                    buffer[i] = tokens[i]
                    i += 1
                else:
                    break

            if len(buffer) > 1:
                master.append(buffer)
                ## ---------------------------------------------------------- ##
                # Purpose:    Return First Match for Recursive Processing
                # Reference:  https://github.com/grafflr/graffl-core/issues/96#issuecomment-954957907
                ## ---------------------------------------------------------- ##
                return master

            buffer = []

        return master

    def process(self,
                tokens: list) -> list:

        sw = Stopwatch()

        matching_rules = self._process(tokens)

        self.logger.info('\n'.join([
            "Sequence Matching Completed",
            f"\tTotal Matches: {len(matching_rules)}",
            f"\tTotal Time: {str(sw)}"]))

        return matching_rules
