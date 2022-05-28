# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Entity Taxonomies """


from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.datablock.dmo import GenericDataFinder


class FindTypes(BaseObject):
    """ Generic Facade to interact with Entity Taxonomies """

    def __init__(self,
                 d_types_fwd: dict,
                 d_types_rev: dict):
        """ Change History

        Created:
            29-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/97
        Updated:
            24-Oct-2022
            craig@grafflr.ai
            *   Update Finder Methods to Replace Spaces with Underscores 
                when no other results are found
                https://github.com/grafflr/graffl-core/issues/129
        Updated:
            25-Jan-2022
            craig@grafflr.ai
            *   pass ontology-name as optional param
                https://github.com/grafflr/graffl-core/issues/135
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   make ontology param consistent; permit multiple values
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027468040
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785
        Updated:
            26-May-2022
            craig@grafflr.ai
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7
        Updated:
            27-May-2022
            craig@grafflr.ai
            *   migrated to 'owlblock' in pursuit of
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            ontologies (list): one-or-more Ontology models to use in processing
        """
        BaseObject.__init__(self, __name__)
        self._d_types_fwd = d_types_fwd
        self._d_types_rev = d_types_rev
        # if self.isEnabledForDebug:
        #     Enforcer.is_list(ontologies)

        # self._finders_fwd = GenericDataFinder(class_suffix='Types',
        #                                       module_suffix='types',
        #                                       ontologies=ontologies)

        # self._finders_rev = GenericDataFinder(class_suffix='TypesRev',
        #                                       module_suffix='types_rev',
        #                                       ontologies=ontologies)

    # def fwd_data(self):
    #     return self._d_types_fwd.data()

    # def rev_data(self):
    #     return self._d_types_rev.data()

    def has_parent(self,
                   input_text: str,
                   parent: str) -> bool:
        input_text = input_text.lower().strip()
        return parent in self.parents(input_text)

    def has_ancestor(self,
                     input_text: str,
                     parent: str) -> bool:
        input_text = input_text.lower().strip()
        return parent in self.ancestors(input_text)

    def exists(self,
               input_text: str) -> bool:
        """ Simple Truth check
            Does this value exist anywhere in the Ontology?

        Args:
            input_text (str): a candidate concept

        Returns:
            bool: True if the concept exists in the Ontology
        """
        input_text = input_text.lower().strip()
        if ' ' in input_text:
            input_text = input_text.replace(' ', '_')

        if input_text in self._d_types_fwd():
            return True
        if input_text in self._d_types_rev():
            return True
        return bool(len(self.parents(input_text)))

    def children(self,
                 input_text: str) -> list:
        input_text = input_text.lower().strip()

        if input_text in self.rev_d_d_types_revata():
            return self._d_types_rev()[input_text]

        if ' ' in input_text:
            return self.children(input_text.replace(' ', '_'))

        return []

    def descendants(self,
                    input_text: str) -> list:
        results = []
        input_text = input_text.lower().strip()

        def _descendants(entity: str):
            if entity in self._d_types_rev():
                for child in self._d_types_rev()[entity]:
                    results.append(child)
                    _descendants(child)

        _descendants(input_text)

        if not len(results) and ' ' in input_text:
            return self.descendants(input_text.replace(' ', '_'))

        return results

    def descendants_and_self(self,
                             input_text: str) -> list:
        s = set()
        s.add(input_text)
        [s.add(x) for x in self.descendants(input_text)]
        return sorted(s)

    def parents(self,
                input_text: str) -> list:
        input_text = input_text.lower().strip()
        if input_text in self._d_types_fwd():
            return self._d_types_fwd()[input_text]

        if ' ' in input_text:
            return self.parents(input_text.replace(' ', '_'))

        return []

    def parents_and_self(self,
                         input_text: str) -> list:
        s = set()
        s.add(input_text)
        [s.add(x) for x in self.parents(input_text)]
        return sorted(s)

    def ancestors(self,
                  input_text: str) -> list:
        results = []
        input_text = input_text.lower().strip()

        def _ancestors(entity: str):
            if entity in self._d_types_fwd():
                for parent in self._d_types_fwd()[entity]:
                    results.append(parent)
                    _ancestors(parent)

        _ancestors(input_text)

        if not len(results) and ' ' in input_text:
            return self.ancestors(input_text.replace(' ', '_'))

        return results

    def ancestors_and_self(self,
                           input_text: str) -> list:
        s = set()
        s.add(input_text)
        [s.add(x) for x in self.ancestors(input_text)]
        return sorted(s)
