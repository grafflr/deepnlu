# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to Find Data in 1..* Ontology Models """


from functools import lru_cache

from baseblock import Enforcer
from baseblock import BaseObject

from askowl.bp import AskOwlAPI
from askowl.dto import QueryResultType
from deepnlu.datablock.dmo import ner_pallete_lookup

from deepnlu.owlblock.svc import QueryNerLabel
from deepnlu.owlblock.svc import QueryNerDepth
from deepnlu.owlblock.svc import QueryNerTaxo
from deepnlu.owlblock.svc import FindNER

from deepnlu.owlblock.dmo import ModelResultMerge
from deepnlu.owlblock.dmo import NerPalleteLookup


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

        self._ontologies = ontologies
        self._d_ontologies = self._load(
            ontologies=ontologies,
            absolute_path=absolute_path)

        self._merge = ModelResultMerge().process
        self._query_ner_label = QueryNerLabel(self._d_ontologies).process
        self._query_ner_depth = QueryNerDepth(self._d_ontologies).process
        self._query_ner_taxo = QueryNerTaxo(self._d_ontologies).process

    def ontologies(self) -> list:
        return self._ontologies

    def _load(self,
              ontologies: list,
              absolute_path: str) -> dict:
        d = {}
        for ontology_name in ontologies:
            d[ontology_name] = AskOwlAPI(
                ontology_name=ontology_name,
                absolute_path=absolute_path)
        return d

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
    def find_ner(self,
                 input_text: str) -> str or None:

        svc = FindNER(
            d_ner_depth=self.ner_depth(),
            d_ner_taxo=self.ner_taxonomy(),
            d_graffl_ner=self.graffl_ner(),
            d_spacy_ner=self.spacy_ner())

        return svc.find_ner(input_text)

    @lru_cache
    def graffl_ner(self) -> dict:
        return self._query_ner_label('grafflNER')

    @lru_cache
    def graffl_ner_rev(self) -> dict:
        return self._query_ner_label('grafflNER', reverse=True)

    @lru_cache
    def spacy_ner(self) -> dict:
        return self._query_ner_label('spacyNER')

    @lru_cache
    def spacy_ner_rev(self) -> dict:
        return self._query_ner_label('spacyNER', reverse=True)

    @lru_cache
    def ner_depth(self) -> dict:
        return self._query_ner_depth(reverse=False)

    @lru_cache
    def ner_depth_rev(self) -> dict:
        return self._query_ner_depth(reverse=True)

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
    def ner_taxonomy(self) -> dict:
        return self._query_ner_taxo(reverse=False)

    @lru_cache
    def ner_taxonomy_rev(self) -> dict:
        return self._query_ner_taxo(reverse=True)

    @lru_cache
    def ner_pallete_lookup(self,
                           input_text: str) -> dict:
        return NerPalleteLookup(self.ner_taxonomy_rev()).lookup(input_text)

    @lru_cache
    def ner_pallete_colors(self) -> dict:
        return NerPalleteLookup(self.ner_taxonomy_rev()).colors()

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
