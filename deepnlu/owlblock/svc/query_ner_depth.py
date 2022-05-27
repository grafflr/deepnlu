# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to Find Data in 1..* Ontology Models """


from baseblock import BaseObject

from askowl.dto import QueryResultType

from deepnlu.owlblock.dmo import ModelResultMerge
from deepnlu.owlblock.dmo import ViewGeneratorNerDepth


class QueryNerDepth(BaseObject):
    """ Generic Facade to Find Data in 1..* Ontology Models """

    __SPARQL_QUERY = """
            select ?ner (count(?mid)-1 as ?depth) {
            #-- Select root classes (classes that have no
            #-- superclasses other than themselves).
            {
                select ?root {
                ?root a owl:Class
                filter not exists {
                    ?root rdfs:subClassOf ?superroot 
                    filter ( ?root != ?superroot )
                }
                }
            }

            ?class owl:backwardCompatibleWith ?ner .
            ?class rdfs:subClassOf* ?mid .
            ?mid rdfs:subClassOf* ?root .
            }
            group by ?ner
            order by ?depth
    """

    def __init__(self,
                 d_ontologies: list):
        """ Change History

        Created:
            27-May-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/deepnlu/issues/13

        Args:
            d_ontologies (list): in-memory graph model keyed by name
        """
        BaseObject.__init__(self, __name__)
        self._merge = ModelResultMerge().process
        self._d_ontologies = d_ontologies
        self._generate_view = ViewGeneratorNerDepth().process

    def _get_results(self,
                     sparql_query: str) -> list:
        results = []
        for ontology_name in self._d_ontologies:
            ask_owl_api = self._d_ontologies[ontology_name]

            results.append(ask_owl_api.adhoc(
                to_lowercase=False,
                sparql_query=sparql_query,
                result_type=QueryResultType.DICT_OF_STR2LIST))

        if not results:
            return None

        elif len(results) == 1:
            return results[0]

        return self._merge(results, QueryResultType.DICT_OF_STR2LIST)

    def process(self,
                ner_type: str,
                reverse: bool = False) -> dict:

        d_results = self._get_results(
            ner_type=ner_type,
            sparql_query=self.__SPARQL_QUERY)

        return self._generate_view(
            reverse=reverse,
            d_results=d_results)
