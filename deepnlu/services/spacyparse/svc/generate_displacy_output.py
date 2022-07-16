#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate Output for Displacy Visualizations in Jupyter """


import pprint


from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject


class GenerateDisplacyOutput(BaseObject):
    """ Generate Output for Displacy Visualizations in Jupyter """

    def __init__(self):
        """
        Created:
            12-Oct-2021
            craig@graffl.ai
            *   https://github.com/grafflr/graffl-core/issues/26#issuecomment-941524282
        Updated:
            14-Oct-2021
            craig@graffl.ai
            *   remove recursive navigational call for finding tokens to display
                https://github.com/grafflr/graffl-core/issues/52#issuecomment-943847367
        """
        BaseObject.__init__(self, __name__)
        self._master = []
        self._d_buffer = {}

    def _navigation(self,
                    data):
        if type(data) == list:
            [self._navigation(x) for x in data]

        elif type(data) == dict:

            if 'type' in data and data['type'] == 'sentence':  # this is a sentence

                if len(self._d_buffer):
                    self._master.append(self._d_buffer)

                self._d_buffer = {
                    "text": data["text"],
                    "ents": [],
                    "title": None}

                self._navigation(data['tokens'])

            elif 'swaps' in data:  # this is a token
                term = data['normal']
                self._d_buffer["ents"].append({
                    "term": term,
                    "start": data['x'],
                    "end": data['y'],
                    "label": data['ner']})

                ## ---------------------------------------------------------- ##
                # Purpose:    Remove Recursive Call
                # Reference:  https://github.com/grafflr/graffl-core/issues/52#issuecomment-943847367
                # Old Code:   self._navigation(data['swaps']['tokens'])
                ## ---------------------------------------------------------- ##

    def process(self,
                tokens: list):
        self._navigation(tokens)
        if len(self._d_buffer):
            self._master.append(self._d_buffer)

        return self._master
