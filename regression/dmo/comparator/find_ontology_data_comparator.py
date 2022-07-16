# -*- coding: UTF-8 -*-
""" Comparator of Actual vs Expected Values for the "Find-Ontology-Data" Engine """


from pprint import pprint
from pprint import pformat
from collections import defaultdict

from baseblock import BaseObject


class FindOntologyDataComparator(BaseObject):
    """ Comparator of Actual vs Expected Values for the "Find-Ontology-Data" Engine """

    def __init__(self):
        """ Change History

        Created:
            6-Jun-2022
            craig@graffl.ai
            *   https://github.com/grafflr/deepnlu/issues/38
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                actual_results: dict,
                expected_results: list) -> bool:
        """ Compare Actual Results to Expected Resuilts

        Args:
            actual_results (object): a dictionary that contains two keys:
                'canon':    [ ...list of entity names... ],
                'text':     [ ...list of extracted text spans... ]
            expected_results (object): a list of expected values
                each list contains a dictionary that is optionally keyed by either 'canon' or 'text'
        """

        def is_empty_actual() -> bool:
            return actual_results is None or not len(actual_results)

        def is_empty_expected() -> bool:
            return expected_results is None or not len(expected_results)

        has_empty_actual = is_empty_actual()

        has_empty_expected = is_empty_expected()

        # if the test case doesn't define expected output, then pass the test automatically ...
        if has_empty_expected:
            return True

        # output was expected, but none was provided ...
        if not has_empty_expected and has_empty_actual:
            return False

        d_fail = defaultdict(list)

        for k in expected_results:

            expected_value = expected_results[k]

            if k == 'is_canon' and expected_value != actual_results['is_canon']:
                d_fail['is_canon'].append(expected_value)

            if k == 'is_variant' and expected_value != actual_results['is_variant']:
                d_fail['is_variant'].append(expected_value)

            if k == 'canon' and expected_value != actual_results['canon']:
                d_fail['canon'].append(expected_value)

            if k == 'variants' and expected_value != actual_results['variants']:
                d_fail['variants'].append(expected_value)

        if len(d_fail):
            self.logger.error('\n'.join([
                "Test Case Failure",
                f"\t{pformat(dict(d_fail))}"]))
            return False

        return True
