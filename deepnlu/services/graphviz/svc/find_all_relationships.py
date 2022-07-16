# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to Find Data """


from typing import Callable
from functools import lru_cache
from baseblock import BaseObject


from deepnlu.owlblock.bp import FindOntologyData


class FindAllRelationships(BaseObject):
    """ Generic Facade to Find Data """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change History

        Created:
            2-Feb-2022
            craig@graffl.ai
        Updated:
            18-May-2022
            craig@graffl.ai
            *   refactor in pursuit of
                https://github.com/grafflr/graffl-core/issues/384
        Updated:
            31-May-2022
            craig@graffl.ai
            *   migrated from graffl-core and renamed from 'find-data'
                https://github.com/grafflr/graffl-core/issues/418

        """
        BaseObject.__init__(self, __name__)
        self._find_ontology_data = find_ontology_data

    def _recursion(self,
                   entity_name: str,
                   predicate: str,
                   update: Callable,
                   search_function: Callable):

        def inner_loop(
                source: str,
                target: str,
                inner_depth: int):

            update(subject=source,
                   search_results=[target],
                   predicate=predicate,
                   depth=inner_depth)

            search_results = search_function(target)
            if search_results and len(search_results):
                [inner_loop(source=target,
                            target=x,
                            inner_depth=inner_depth+1) for x in search_results]

        search_results = search_function(entity_name)
        if search_results and len(search_results):
            [inner_loop(source=entity_name,
                        target=x,
                        inner_depth=1) for x in search_results]

    @lru_cache(maxsize=2048)
    def find(self,
             entity_name: str,
             find_requires: bool = True,
             find_implies: bool = True,
             find_similar: bool = True,
             find_ancestors: bool = True,
             find_descendants: bool = True) -> list:
        """ Find Data Relationships

        Args:
            entity_name (str): the entity to start searching with
            find_requires (bool, optional): use "Requires" relationships. Defaults to True.
            find_implies (bool, optional): use "Implies" relationships. Defaults to True.
            find_similar (bool, optional): use "Similar" relationships. Defaults to True.
            find_ancestors (bool, optional): find ancestor entities. Defaults to True.
            find_descendants (bool, optional): find descendant entities. Defaults to True.

        Returns:
            list: a list of results
        """
        results = []

        # Function Registration is not strictly required by Python
        # but it does help keep the code clean
        requires = self._find_ontology_data.requires_by_entity
        required_by = self._find_ontology_data.required_by_entity
        implies = self._find_ontology_data.implies_by_entity
        implied_by = self._find_ontology_data.implied_by_entity
        similar = self._find_ontology_data.similar_by_entity
        parents = self._find_ontology_data.parents
        descendants = self._find_ontology_data.descendants

        def update(subject: str,
                   search_results: list or None,
                   predicate: str,
                   depth: int = 1) -> None:

            if search_results and len(search_results):
                [results.append({
                    "Subject": subject,
                    "Predicate": predicate,
                    "Object": x,
                    "Ontology": self._find_ontology_data.ontologies()[0],
                    "Depth": depth,
                }) for x in search_results]

        if find_requires:
            self._recursion(entity_name=entity_name,
                            predicate="requires",
                            update=update,
                            search_function=requires)

            self._recursion(entity_name=entity_name,
                            predicate="requiredBy",
                            update=update,
                            search_function=required_by)

        if find_implies:
            self._recursion(entity_name=entity_name,
                            predicate="implies",
                            update=update,
                            search_function=implies)

            self._recursion(entity_name=entity_name,
                            predicate="impliedBy",
                            update=update,
                            search_function=implied_by)

        if find_similar:
            self._recursion(entity_name=entity_name,
                            predicate="similar",
                            update=update,
                            search_function=similar)

        if find_ancestors:
            self._recursion(entity_name=entity_name,
                            predicate="parent",
                            update=update,
                            search_function=parents)

        if find_descendants:
            self._recursion(entity_name=entity_name,
                            predicate="has_child",
                            update=update,
                            search_function=descendants)

        s = set()
        normalized = []
        for result in results:
            key = f"{result['Subject']}-{result['Predicate']}-{result['Object']}".lower()
            if key not in s:
                normalized.append(result)
                s.add(key)

        return normalized
