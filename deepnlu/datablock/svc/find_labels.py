# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Label Lookups """


from baseblock import BaseObject
from baseblock import get_ontology_name


from deepnlu.datablock.dmo import GenericDataFinder


class FindLabels(BaseObject):
    """ Generic Facade to interact with Label Lookups """

    def __init__(self,
                 ontology_name: object = None):
        """ Change History

        Created:
            8-Nov-2021
            craig@grafflr.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/108
        Updated:
            25-Jan-2022
            craig@grafflr.ai
            *   pass ontology-name as optional param
                https://github.com/grafflr/graffl-core/issues/135
            *   a finder initialization is a contract
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027474785    
        Updated:
            18-May-2022
            craig@grafflr.ai
            *   refactored in pursuit of
                https://github.com/grafflr/graffl-core/issues/384

        Args:
            ontology_name (object, optional): the Ontology Name(s) to use for data. Defaults to None.
        """
        BaseObject.__init__(self, __name__)
        ontologies = get_ontology_name(ontology_name)

        self._fwd = GenericDataFinder(
            class_suffix='Labels',
            module_suffix='labels',
            ontologies=ontologies).data()

        self._rev = GenericDataFinder(
            class_suffix='LabelsRev',
            module_suffix='labels_rev',
            ontologies=ontologies).data()

        self._rev_lcase = {k.lower(): self._rev[k] for k in self._rev}

    def data(self) -> dict:
        """
        Returns:
            dict: all the data
        """
        return self._fwd

    def labels(self) -> list:
        """ 
        Returns:
            list: Sorted list of all Labels for the given Ontologies
        """
        return sorted(self._rev.keys(), key=len)

    def rdf_id(self,
               input_text: str) -> str or None:
        """ Return the rdf:id form given the label form

        Args:
            input_text (str): the label form (rdfs:label)

        Returns:
            str or None: the rdf:id form (if any)
        """

        input_text = input_text.lower().strip()
        if input_text in self._rev_lcase:
            results = self._rev_lcase[input_text]

            if results and len(results):
                return results[0].upper().strip()  # RDF IDs are UPPER-cased

        if ' ' in input_text:
            return self.rdf_id(input_text.replace(' ', '_').strip())

        if not input_text.islower():
            return self.rdf_id(input_text.lower().strip())

    def label_or_self(self,
                      rdf_id: str) -> str:
        """ Return Label form or self

        Args:
            rdf_id (str): the incoming entity name (rdf:id form)

        Returns:
            str or None: the outgoing label form (rdfs:label form)
        """
        result = self.label(rdf_id)
        if result and len(result):
            return result
        return rdf_id

    def label(self,
              rdf_id: str) -> str or None:
        """ Return Label form, if exists

        Args:
            rdf_id (str): the incoming entity name (rdf:id form)

        Returns:
            str or None: the outgoing label form (rdfs:label form)
        """

        if rdf_id in self.data():
            results = self.data()[rdf_id]

            if results and len(results):
                return results[0]

        if ' ' in rdf_id:
            return self.label(rdf_id.replace(' ', '_').strip())

        if not rdf_id.islower():
            return self.label(rdf_id.lower().strip())

    def exists(self,
               input_text: str) -> bool:
        """ Check if Entity exists by ID

        Args:
            input_text (str): the incoming entity name (rdf:id form)

        Returns:
            bool: True if the entity exists
        """
        return input_text.lower().strip() in self.data()
