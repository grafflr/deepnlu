# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Similarity relationships """


from random import sample
from pprint import pprint

from baseblock import BaseObject
from baseblock import get_ontology_name

from datablock.dmo import GenericDataFinder


class FindSimilar(BaseObject):
    """ Generic Facade to interact with Similarity relationships """

    __slots__ = (
        '_fwd',
        '_rev',
    )

    def __init__(self,
                 ontology_name: object = None):
        """
        Created:
            25-Feb-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/199
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)

        self._fwd = GenericDataFinder(class_suffix='Similar',
                                      module_suffix='similar',
                                      ontologies=ontologies)

        self._rev = GenericDataFinder(class_suffix='SimilarRev',
                                      module_suffix='similar_rev',
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
        return self._fwd.data()

    def rev_data(self):
        return self._rev.data()

    def _lookup(self,
                input_text: str,
                d: dict) -> list or None:

        if input_text in d:
            results = d[input_text]
            if results and len(results):
                return results

        if ' ' in input_text:
            input_text = input_text.replace(' ', '_').strip()
            return self._lookup(input_text, d)

        if not input_text.islower():
            return self._lookup(input_text.lower(), d)

    def similar(self,
                input_text: str) -> list or None:
        return self._lookup(input_text, self.fwd_data())

    def is_similar_to(self,
                      rdf_id: str) -> list or None:
        results = self._lookup(rdf_id, self.fwd_data())
        if results and len(results):
            return results

        return self._lookup(rdf_id, self.rev_data())

    def is_similar_to_random_n(self,
                               rdf_id: str,
                               n: int) -> list or None:
        results = self.is_similar_to(rdf_id)
        if not results or len(results) <= n:
            return results

        return sample(results, n)
