#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" deepNLU Regression API """


from baseblock import BaseObject


class RegressionAPI(BaseObject):
    """ deepNLU Regression API """

    def __init__(self):
        """ Change History

        Created:
            6-Jun-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/22
        """
        BaseObject.__init__(self, __name__)

    def process(self) -> None:
        pass
