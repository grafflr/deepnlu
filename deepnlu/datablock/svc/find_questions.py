# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Question Lists """


import os

from pprint import pprint
from random import sample

from baseblock import BaseObject

from deepnlu.datablock.dmo import GenericFunctionLoader
from deepnlu.datablock.os.qlists import list_of_questions


class FindQuestions(BaseObject):
    """ Generic Facade to interact with Question Lists """

    def __init__(self):
        """
        Created:
            6-Apr-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/274
        """
        BaseObject.__init__(self, __name__)

    def random(self) -> str:

        return sample(list_of_questions[0], 1)[0]
