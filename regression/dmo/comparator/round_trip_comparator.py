# -*- coding: UTF-8 -*-
""" Comparator of Actual vs Expected Values for the "Round-Trip" Engine """


from pprint import pprint

from baseblock import BaseObject


class RoundTripComparator(BaseObject):
    """ Comparator of Actual vs Expected Values for the "Round-Trip" Engine """

    def __init__(self):
        BaseObject.__init__(self, __name__)

    def process(self,
                actual_results: object,
                expected_results: object) -> None:

        pprint(actual_results)
        print('-'*100)
        pprint(expected_results)
