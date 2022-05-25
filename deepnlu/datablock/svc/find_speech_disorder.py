# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Speech Disorder Data """


from random import sample

from baseblock import BaseObject

from deepnlu.datablock.os.speech_disorder import speech_disorder_questions


class FindSpeechDisorder(BaseObject):
    """ Generic Facade to interact with Speech Disorder Data """

    def __init__(self):
        """
        Created:
            25-Apr-2022
            craig@grafflr.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/298
        """
        BaseObject.__init__(self, __name__)
        self._speech_disorder_questions = speech_disorder_questions

    def random(self) -> str:
        return sample(self._speech_disorder_questions, 1)[0]
