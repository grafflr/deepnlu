#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os


def get_ontology_name(ontology_name: object = None) -> list:
    """ Consistent Retrieval of Ontology Name
        https://github.com/grafflr/graffl-core/issues/135 """

    if ontology_name is None:

        # function copied from 'EnvIO.as_list(...)'
        if 'GRAFFL_ONTOLOGIES' in os.environ:
            values = [x.strip()
                      for x in os.environ['GRAFFL_ONTOLOGIES'].split(',')]
            return [x for x in values if x and len(x)]

        raise ValueError('No Ontology Name Specified')

    else:

        ontology_name_type = type(ontology_name)

        if ontology_name_type == str:
            return [ontology_name]

        elif ontology_name_type == list:
            return ontology_name

        raise ValueError(f"Unrecognized Data Type: {ontology_name_type}")
