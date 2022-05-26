# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to Find Data """


from typing import Callable


from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject


from deepnlu.datablock.svc import FindTypes
from deepnlu.datablock.svc import FindImplies
from deepnlu.datablock.svc import FindSimilar
from deepnlu.datablock.svc import FindRequires
from deepnlu.datablock.svc import FindSynonyms


class FindData(BaseObject):
    """ Generic Facade to Find Data """

    __cache = {}

    def __init__(self):
        """ Change History

        Created:
            2-Feb-2022
            craig@grafflr.ai
        Updated:
            18-May-2022
            craig@grafflr.ai
            *   refactor in pursuit of
                https://github.com/grafflr/graffl-core/issues/384

        """
        BaseObject.__init__(self, __name__)

    def find(self,
             entity_name: str,
             ontology_name: str,
             find_requires: bool = True,
             find_similar: bool = True,
             find_implies: bool = True,
             find_ancestors: bool = True,
             find_siblings: bool = True,
             find_descendants: bool = True,
             find_descendant_synonyms=False) -> list:
        """ Find Data Relationships

        Args:
            entity_name (str): the entity to start searching with
            ontology_name (str): the Ontology model to use
            find_requires (bool, optional): use "Requires" relationships. Defaults to True.
            find_similar (bool, optional): use "Similar" relationships. Defaults to True.
            find_implies (bool, optional): use "Implies" relationships. Defaults to True.
            find_descendant_synonyms (bool, optional): include descendant synonyms. Defaults to False.

        Returns:
            list: a list of results
        """
        results = []

        if find_requires:
            [results.append(x) for x in
             self.find_requires(entity_name, ontology_name)]

        if find_implies:
            [results.append(x) for x in
             self.find_implies(entity_name, ontology_name)]

        if find_similar:
            [results.append(x) for x in
             self.find_similar(entity_name, ontology_name)]

        if find_ancestors:
            [results.append(x) for x in
             self.find_ancestors(entity_name, ontology_name)]

        if find_descendants:
            [results.append(x) for x in
             self.find_descendants(entity_name, ontology_name)]

        if find_descendant_synonyms:
            for result in self.find_descendant_synonyms(entity_name, ontology_name):
                results.append({
                    "Entity": entity_name,
                    "DescendantSynonym": result,
                    "Ontology": ontology_name
                })

        # filter
        s = set()
        normalized = []
        for result in results:
            key = f"{result['Subject']}-{result['Predicate']}-{result['Object']}"
            if key not in s:
                normalized.append(result)
                s.add(key)

        return normalized

    def find_ancestors(self,
                       entity_name: str,
                       ontologies: list) -> list or None:
        """ Find 'Ancestor' Relationships

        Args:
            entity_name (str): the entity to start searching with
            ontologies (list): one-or-more Ontology models to use in processing

        Returns:
            list or None: a list of results (if any)
        """
        if self.isEnabledForDebug:
            Enforcer.is_str(entity_name)
            Enforcer.is_list(ontologies)

        finder = FindTypes(ontologies).ancestors
        return self._find_relationship(finder=finder,
                                       entity_name=entity_name,
                                       ontologies=ontologies,
                                       relationship_name="Ancestor")

    def find_descendants(self,
                         entity_name: str,
                         ontologies: list) -> list or None:
        """ Find 'Desecendant' Relationships

        Args:
            entity_name (str): the entity to start searching with
            ontologies (list): one-or-more Ontology models to use in processing

        Returns:
            list or None: a list of results (if any)
        """
        if self.isEnabledForDebug:
            Enforcer.is_str(entity_name)
            Enforcer.is_list(ontologies)

        finder = FindTypes(ontologies).children
        return self._find_relationship(finder=finder,
                                       entity_name=entity_name,
                                       ontologies=ontologies,
                                       relationship_name="Descendant")

    def find_similar(self,
                     entity_name: str,
                     ontologies: list) -> list or None:
        """ Find 'Similarity' Relationships

        Args:
            entity_name (str): the entity to start searching with
            ontologies (list): one-or-more Ontology models to use in processing

        Returns:
            list or None: a list of results (if any)
        """
        if self.isEnabledForDebug:
            Enforcer.is_str(entity_name)
            Enforcer.is_list(ontologies)

        finder = FindSimilar(ontologies).similar
        return self._find_relationship(finder=finder,
                                       entity_name=entity_name,
                                       ontologies=ontologies,
                                       relationship_name="Similar")

    def find_requires(self,
                      entity_name: str,
                      ontologies: list) -> list or None:
        """ Find 'Requires' Relationships

        Args:
            entity_name (str): the entity to start searching with
            ontologies (list): one-or-more Ontology models to use in processing

        Returns:
            list or None: a list of results (if any)
        """
        if self.isEnabledForDebug:
            Enforcer.is_str(entity_name)
            Enforcer.is_list(ontologies)

        finder = FindRequires(ontologies).requires
        return self._find_relationship(finder=finder,
                                       entity_name=entity_name,
                                       ontologies=ontologies,
                                       relationship_name="Requires")

    def find_implies(self,
                     entity_name: str,
                     ontologies: list) -> list or None:
        """ Find 'Implies' Relationships

        Args:
            entity_name (str): the entity to start searching with
            ontologies (list): one-or-more Ontology models to use in processing

        Returns:
            list or None: a list of results (if any)
        """
        if self.isEnabledForDebug:
            Enforcer.is_str(entity_name)
            Enforcer.is_list(ontologies)

        results = []

        finder = FindImplies(ontologies)

        [results.append(x) for x in self._find_relationship(
            finder=finder.implies,
            entity_name=entity_name,
            ontologies=ontologies,
            relationship_name="Implies")]

        [results.append(x) for x in self._find_relationship(
            finder=finder.implied_by,
            entity_name=entity_name,
            ontologies=ontologies,
            relationship_name="Implies")]

        return results

    def _find_relationship(self,
                           entity_name: str,
                           finder: Callable,
                           ontologies: list,
                           relationship_name: str,
                           total_recursion: int = 3) -> list or None:

        results = []

        def call_finder(a_value: str) -> list or None:
            result = finder(a_value)
            if result:
                return result

            requires = []

            type_finder = FindTypes(ontologies)
            for parent in type_finder.ancestors(a_value):
                result = finder(parent)
                if result:
                    requires.append(result)

            return requires

        def inner_method(a_value: str,
                         recursion_ctr: int) -> None:

            call_finder_results = call_finder(a_value)
            if type(call_finder_results) == str:
                call_finder_results = [call_finder_results]
            if type(call_finder_results) != list:
                raise ValueError('Unexpected Type')

            for result in call_finder_results:
                if type(result) == list:
                    result = result[0]

                if a_value != result:
                    results.append({
                        "Subject": a_value,
                        "Predicate": relationship_name,
                        "Object": result,
                        "Ontology": ','.join(ontologies),
                        "Depth": recursion_ctr,
                    })

                    if recursion_ctr < total_recursion:
                        inner_method(result, recursion_ctr + 1)

        inner_method(entity_name, 1)

        return results

    def find_descendant_synonyms(self,
                                 entity_name: str,
                                 ontologies: list) -> list:
        """ Find Descendant Synonyms

        Args:
            entity_name (str): the entity to start searching with
            ontologies (list): one-or-more Ontology models to use in processing

        Returns:
            list: the results
        """

        def key() -> str:
            return f"{','.join(ontologies)}-{entity_name}"

        if key() in self.__cache:
            return self.__cache[key()]

        s = set()
        type_finder = FindTypes(ontologies)
        synonym_finder = FindSynonyms(ontologies)

        [s.add(x) for x in synonym_finder.find_variants(entity_name)]
        for descendant in type_finder.descendants(entity_name):
            [s.add(x) for x in synonym_finder.find_variants(descendant)]

        def is_type(value: str):
            if type_finder.exists(value):
                return True
            if ' ' in value and type_finder.exists(value.replace(' ', '_')):
                return True
            return False

        s = sorted([x for x in s if not is_type(x)], key=len)

        self.__cache[key()] = s
        return s
