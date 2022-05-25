# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Requires relationships """


from pprint import pprint

from baseblock import BaseObject
from baseblock import get_ontology_name

from deepnlu.datablock.dmo import GenericDataFinder


class FindRequires(BaseObject):
    """ Generic Facade to interact with Requires relationships """

    __slots__ = (
        '_finders_fwd',
        '_finders_rev',
    )

    def __init__(self,
                 ontology_name: object = None):
        """
        Created:
            8-Nov-2021
            craig@grafflr.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/108
        Updated:
            25-Jan-2022
            craig@grafflr.ai
            *   pass ontology-name as optional param
            *   add 'rev' function and refactor logic into '_lookup'
                https://github.com/grafflr/graffl-core/issues/135
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   make ontology param consistent; permit multiple values
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027468040
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)

        self._finders_fwd = GenericDataFinder(class_suffix='Requires',
                                              module_suffix='requires',
                                              ontologies=ontologies)

        self._finders_rev = GenericDataFinder(class_suffix='RequiresRev',
                                              module_suffix='requires_rev',
                                              ontologies=ontologies)

    def _merge(self,
               d_finder: dict) -> dict:
        d = {}
        for name in d_finder:
            data = d_finder[name].data()
            for k in data:
                if k not in d:
                    d[k] = data[k]
                else:
                    [d[k].append(x) for x in data[k]]
        return d

    def fwd_data(self):
        # if not self.__d_merge_fwd:
        #     self.__d_merge_fwd = self._merge(self._finders_fwd)

        # return self.__d_merge_fwd
        return self._finders_fwd.data()

    def rev_data(self):
        # if not self.__d_merge_rev:
        #     self.__d_merge_rev = self._merge(self._finders_rev)

        # return self.__d_merge_rev
        return self._finders_rev.data()

    def _lookup(self,
                input_text: str,
                d_requires: dict) -> list or None:

        if input_text in d_requires:
            results = d_requires[input_text]
            if results and len(results):
                return results

        if ' ' in input_text:
            input_text = input_text.replace(' ', '_').strip()
            return self._lookup(input_text, d_requires)

        if not input_text.islower():
            return self._lookup(input_text.lower(), d_requires)

    def requires(self,
                 input_text: str) -> list or None:
        return self._lookup(input_text, self.fwd_data())

    def required_by(self,
                    input_text: str) -> list or None:
        return self._lookup(input_text, self.rev_data())
