# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Jokes Data """

from random import sample

from baseblock import BaseObject

from deepnlu.datablock.os.jokes import dad_jokes


class FindJokes(BaseObject):
    """ Generic Facade to interact with Jokes Data """

    def __init__(self):
        """
        Created:
            26-Apr-2022
            craig@grafflr.ai
        """
        BaseObject.__init__(self, __name__)
        self._dad_jokes = dad_jokes

    def random(self) -> str:
        return sample(self._dad_jokes, 1)[0]
