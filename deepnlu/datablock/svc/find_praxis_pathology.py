# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Praxis Pathology Data """


from random import sample

from baseblock import BaseObject

from datablock.os.praxis_pathology import praxis_pathology_questions


class FindPraxisPathology(BaseObject):
    """ Generic Facade to interact with Praxis Pathology Data """

    def __init__(self):
        """
        Created:
            25-Apr-2022
            craig@grafflr.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/298
        """
        BaseObject.__init__(self, __name__)
        self._praxis_pathology_questions = praxis_pathology_questions

    def random(self) -> str:
        return sample(self._praxis_pathology_questions, 1)[0]
