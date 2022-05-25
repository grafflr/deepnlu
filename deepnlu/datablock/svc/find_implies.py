# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Implies relationships """


from pprint import pprint

from baseblock import BaseObject
from baseblock import get_ontology_name

from deepnlu.datablock.dmo import GenericDataFinder


class FindImplies(BaseObject):
    """ Generic Facade to interact with Implies relationships """

    __slots__ = (
        '_finders_fwd',
        '_finders_rev',
    )

    def __init__(self,
                 ontology_name: object = None):
        """
        Created:
            2-Feb-2022
            craig@grafflr.ai
            *   copied from 'find-requires' in pursuit of
                https://github.com/grafflr/graffl-core/issues/156
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)

        self._finders_fwd = GenericDataFinder(class_suffix='Implies',
                                              module_suffix='implies',
                                              ontologies=ontologies)

        self._finders_rev = GenericDataFinder(class_suffix='ImpliesRev',
                                              module_suffix='implies_rev',
                                              ontologies=ontologies)

    def fwd_data(self):
        return self._finders_fwd.data()

    def rev_data(self):
        return self._finders_rev.data()

    def _lookup(self,
                input_text: str,
                d_implies: dict) -> str or None:

        if not input_text:
            return None

        input_text = input_text.lower().strip()
        if not len(input_text):
            return None

        if input_text in d_implies:
            results = d_implies[input_text]
            if results and len(results):
                return results[0]

        if ' ' in input_text:
            input_text = input_text.replace(' ', '_').strip()
            return self._lookup(input_text, d_implies)

        if not input_text.islower():
            return self._lookup(input_text.lower(), d_implies)

    def implies(self,
                input_text: str) -> str:
        return self._lookup(input_text, self.fwd_data())

    def implied_by(self,
                   input_text: str) -> str:
        return self._lookup(input_text, self.rev_data())
