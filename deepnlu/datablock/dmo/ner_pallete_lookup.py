# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find a Pallete to associate to NER types """


import os
import pprint
from random import randint

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.datablock.dmo import GenericClassLoader


class NerPalleteLookup(BaseObject):
    """ Find a Pallete to associate to NER types """

    _d_merge_taxorev = None

    def __init__(self,
                 ontologies: list):
        """ Change History

        Created:
            27-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/94
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   enforce ontologies as a list param in domain components
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370

        Args:
            ontologies (list): one-or-more Ontology models to use in processing
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(ontologies)

        self._d_palletes = self._load_config()

        load = GenericClassLoader().load

        self.__taxorev = {
            x: load(package_name=x,
                    class_suffix="NerTaxonomyRev",
                    module_suffix="ner_taxonomy_rev") for x in ontologies}

        self._d_assoc = self._configure()

    @staticmethod
    def _load_config() -> dict:
        path = os.path.normpath(os.path.join(
            EnvIO.str_or_exception("GRAFFLR_HOME"),
            "apps/blocks/datablock/resources/data/palletes.yaml"))

        FileIO.exists_or_error(path)

        return FileIO.read_yaml(path)['palletes']

    def _configure(self) -> int or None:

        def merge() -> dict:
            d = {}
            for ontology_name in self.__taxorev:
                d_finder = self.__taxorev[ontology_name].data()
                for k in d_finder:
                    if k not in d:
                        d[k] = d_finder[k]
                    else:
                        [d[k].append(x) for x in d_finder[k]]
            return d

        def get_dict() -> dict:
            if not self._d_merge_taxorev:
                self._d_merge_taxorev = merge()

            return self._d_merge_taxorev

        d = get_dict()

        keys = sorted(d.keys())
        pallete_keys = sorted(self._d_palletes.keys())

        used_keys = []

        d_assoc = {}
        for i in range(len(keys)):

            def pallete_key(n: int) -> int:
                x = randint(0, len(pallete_keys) - 1)
                if x not in used_keys:
                    used_keys.append(x)
                    return x
                if n > len(pallete_keys):
                    return 0
                return pallete_key(n + 1)

            ners = d[keys[i]]
            pallete = pallete_keys[pallete_key(0)]
            colors = self._d_palletes[pallete]['colors']

            for j in range(len(ners)):
                if ners[j] not in d_assoc:

                    def color_key() -> int:
                        if j >= len(colors):
                            return 0
                        return j

                    d_assoc[ners[j]] = f"#{colors[color_key()]}"

        return d_assoc

    def lookup(self,
               input_text: str) -> str:
        return self._d_assoc[input_text]

    def colors(self) -> dict:
        return self._d_assoc
