# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to Find Data in 1..* Ontology Models """


from audioop import reverse
from functools import lru_cache

from baseblock import Enforcer
from baseblock import BaseObject

from askowl.bp import AskOwlAPI
from askowl.dto import QueryResultType


class FindOntologyData(BaseObject):
    """ Generic Facade to Find Data in 1..* Ontology Models """

    def __init__(self,
                 ontologies: list,
                 absolute_path: str):
        """ Change History

        Created:
            26-May-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/2

        Args:
            ontologies (list): one-or-more Ontology models to use in processing
            absolute_path (str): an absolute path that applies to all the OWL models
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(ontologies)

        self._d_ontologies = self._load(
            ontologies=ontologies,
            absolute_path=absolute_path)

    def _load(self,
              ontologies: list,
              absolute_path: str) -> dict:
        d = {}
        for ontology_name in ontologies:
            d[ontology_name] = AskOwlAPI(
                ontology_name=ontology_name,
                absolute_path=absolute_path)
        return d

    def _merge(results: list,
               result_type: QueryResultType) -> list:

        if result_type == QueryResultType.DICT_OF_STR2LIST:
            d_merge = {}
            for d_result in results:
                for k in d_result:
                    if k not in d_merge:
                        d_merge[k] = []

                    for value in d_result[k]:
                        if value not in d_merge[k]:
                            d_merge[k].append(value)
            return d_merge

        elif result_type == QueryResultType.DICT_OF_STR2DICT:
            d_merge = {}
            for d_result in results:
                for k in d_result:
                    for value in d_result[k]:
                        d_merge[k].append(value)

            return d_merge

        else:
            raise NotImplementedError

    @lru_cache
    def _by_predicate(self,
                      predicate_name: str) -> dict:
        results = []
        for ontology_name in self._d_ontologies:
            results.append(
                self._d_ontologies[ontology_name].by_predicate(predicate_name))

        if not results:
            return None
        elif len(results) == 1:
            return results[0]
        return self._merge(results, QueryResultType.DICT_OF_STR2LIST)

    @lru_cache
    def _by_predicate_rev(self,
                          predicate_name: str) -> dict:
        results = []
        for ontology_name in self._d_ontologies:
            results.append(
                self._d_ontologies[ontology_name].by_predicate(predicate_name, reverse=True))

        if not results:
            return None
        elif len(results) == 1:
            return results[0]
        return self._merge(results, QueryResultType.DICT_OF_STR2LIST)

    @lru_cache
    def comments(self) -> dict:
        results = []
        for ontology_name in self._d_ontologies:
            results.append(self._d_ontologies[ontology_name].comments())

        if not results:
            return None
        elif len(results) == 1:
            return results[0]
        return self._merge(results, QueryResultType.DICT_OF_STR2LIST)

    def effects(self) -> dict:
        return self._by_predicate('effects')

    @lru_cache
    def effects_rev(self) -> dict:
        return self._by_predicate_rev('effects')

    @lru_cache
    def requires(self) -> dict:
        return self._by_predicate('requires')

    @lru_cache
    def requires_rev(self) -> dict:
        return self._by_predicate_rev('requires')

    @lru_cache
    def similar(self) -> dict:
        return self._by_predicate('similar')

    @lru_cache
    def similar_rev(self) -> dict:
        return self._by_predicate_rev('similar')

    @lru_cache
    def implies(self) -> dict:
        return self._by_predicate('implies')

    @lru_cache
    def implies_rev(self) -> dict:
        return self._by_predicate_rev('implies')

    @lru_cache
    def graffl_ner(self) -> dict:
        raise NotImplementedError

    @lru_cache
    def graffl_ner_rev(self) -> dict:
        raise NotImplementedError

    @lru_cache
    def infer_by_requires(self) -> dict:
        raise NotImplementedError

    @lru_cache
    def labels(self) -> dict:
        return self._by_predicate('rdfs:label')

    @lru_cache
    def labels_rev(self) -> dict:
        return self._by_predicate_rev('rdfs:label')

    @lru_cache
    def lookup(self) -> dict:
        results = []
        for ontology_name in self._d_ontologies:
            results.append(self._d_ontologies[ontology_name].lookup())

        if not results:
            return None
        elif len(results) == 1:
            return results[0]
        return self._merge(results, QueryResultType.DICT_OF_STR2LIST)

    @lru_cache
    def ner_depth(self) -> dict:
        raise NotImplementedError

    @lru_cache
    def ner_depth_rev(self) -> dict:
        raise NotImplementedError

    @lru_cache
    def ner_taxonomy(self) -> dict:
        raise NotImplementedError

    @lru_cache
    def ner_taxonomy_rev(self) -> dict:
        raise NotImplementedError

    @lru_cache
    def ner_spacy(self) -> dict:
        raise NotImplementedError

    @lru_cache
    def ner_spacy_rev(self) -> dict:
        raise NotImplementedError

    @lru_cache
    def spans(self) -> dict:
        results = []
        for ontology_name in self._d_ontologies:
            results.append(self._d_ontologies[ontology_name].spans())

        if not results:
            return None
        elif len(results) == 1:
            return results[0]
        return self._merge(results, QueryResultType.DICT_OF_STR2DICT)

    @lru_cache
    def synonyms(self) -> dict:
        results = []
        for ontology_name in self._d_ontologies:
            results.append(self._d_ontologies[ontology_name].synonyms())

        if not results:
            return None
        elif len(results) == 1:
            return results[0]
        return self._merge(results, QueryResultType.DICT_OF_STR2LIST)

    @lru_cache
    def synonyms_rev(self) -> dict:
        results = []
        for ontology_name in self._d_ontologies:
            results.append(self._d_ontologies[ontology_name].synonyms_rev())

        if not results:
            return None
        elif len(results) == 1:
            return results[0]
        return self._merge(results, QueryResultType.DICT_OF_STR2LIST)

    @lru_cache
    def trie(self) -> dict:
        results = []
        for ontology_name in self._d_ontologies:
            results.append(self._d_ontologies[ontology_name].trie())

        if not results:
            return None
        elif len(results) == 1:
            return results[0]
        return self._merge(results, QueryResultType.DICT_OF_STR2LIST)

    @lru_cache
    def types(self) -> dict:
        return self._by_predicate('rdfs:subClassOf')

    @lru_cache
    def types_rev(self) -> dict:
        return self._by_predicate_rev('rdfs:subClassOf')

    @lru_cache
    def uses(self) -> dict:
        return self._by_predicate('uses')

    @lru_cache
    def uses_rev(self) -> dict:
        return self._by_predicate_rev('uses')
