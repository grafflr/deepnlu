# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Pronouns """


from baseblock import BaseObject


from deepnlu.datablock.os import first_person_pronouns
from deepnlu.datablock.os import second_person_pronouns
from deepnlu.datablock.os import third_person_pronouns


class FindPronouns(BaseObject):
    """ Generic Facade to interact with Pronouns """

    __all = None
    __alphabet = [(chr(ord('a') + i)) for i in range(26)]

    def __init__(self):
        """ Change History:

        Created:
            3-May-2022
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/345
        """
        BaseObject.__init__(self, __name__)

    def all(self) -> list:
        if not self.__all:
            s = set()
            [s.add(x) for x in first_person_pronouns]
            [s.add(x) for x in second_person_pronouns]
            [s.add(x) for x in third_person_pronouns]
            self.__all = sorted(s)
        return self.__all

    def has_pronoun(self,
                    input_text: str) -> bool:

        input_text = [ch for ch in input_text.lower()
                      if ch in self.__alphabet or ch == ' ']
        tokens = ''.join(input_text).split()
        tokens = [x.strip().lower() for x in tokens if x.isalpha()]
        tokens = [x for x in tokens if x in self.all()]
        return len(tokens)
