# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Comment Lookups """


from random import sample
from pprint import pprint

from baseblock import BaseObject
from baseblock import get_ontology_name

from deepnlu.datablock.dmo import GenericDataFinder


class FindComments(BaseObject):
    """ Generic Facade to interact with Comment Lookups """

    __slots__ = (
        '_fwd',
    )

    def __init__(self,
                 ontology_name: object = None):
        """
        Created:
            25-Jan-2022
            craig@grafflr.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/133
        Updated:
            25-Jan-2022
            craig@grafflr.ai
            *   pass ontology-name as optional param
                https://github.com/grafflr/graffl-core/issues/135
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)

        self._fwd = GenericDataFinder(class_suffix='Comments',
                                      module_suffix='comments',
                                      ontologies=ontologies).data()

    def data(self) -> dict:
        return self._fwd

    def comments(self,
                 input_text: str) -> list:
        """ Return 0..* Comments """
        if input_text in self.data():
            return self.data()[input_text]

        if ' ' in input_text:
            return self.label(input_text.replace(' ', '_')).strip()

        if not input_text.islower():
            return self.label(input_text.lower()).strip()

    def random_comment(self,
                       input_text: str) -> str or None:
        """ in the event of multiple comments,
            return one comment from the list at random """
        comments = self.comments(input_text)

        if not len(comments):
            return None

        if len(comments) == 1:
            return comments[0]

        return sample(comments, 1)[0]
