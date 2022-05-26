

import os
from pprint import pprint


from deepnlu.datablock.svc import FindLabels
from baseblock import Stopwatch


def test_label():

    finder = FindLabels(['appraisal'])
    result = finder.label('Ethics')

    result = finder.label('Is Sincere')
    print(finder.rdf_id('Is Sincere'))
    print(finder.rdf_id('takes decisive action based on well documented facts'))

    # no assertion necessary ; just make sure the system doesn't blow up


def main():
    test_label()


if __name__ == "__main__":
    main()
