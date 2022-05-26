# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find spaCy NER (Named Entity Recognition) Types """


from baseblock import Enforcer
from baseblock import BaseObject

from deepnlu.datablock.dmo import NerTypeFinder
from deepnlu.datablock.dmo import NerDepthFinder
from deepnlu.datablock.dmo import NerPalleteLookup
from deepnlu.datablock.dmo import NerTaxonomyFinder


class FindNER(BaseObject):
    """ Find spaCy NER (Named Entity Recognition) Types """

    def __init__(self,
                 ontologies: list):
        """ Change History

        Created:
            13-Oct-2021
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/36
        Updated:
            14-Oct-2021
            craig@grafflr.ai
            *   defect fixing updates
                https://github.com/grafflr/graffl-core/issues/42
        Updated:
            22-Oct-2021
            craig@grafflr.ai
            *   replace manual depth dictionary with autogenerated values
                https://github.com/grafflr/graffl-core/issues/89#issuecomment-950061167
        Updated:
            27-Oct-2021
            craig@grafflr.ai
            *   refactor functions into domain components in pursuit of
                https://github.com/grafflr/graffl-core/issues/94
        Updated:
            1-Feb-2022
            craig@grafflr.ai
            *   make ontology param consistent; permit multiple values
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027468040
        Updated:
            26-May-2022
            craig@grafflr.ai
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7

        Args:
            ontologies (list): one-or-more Ontology models to use in processing
        """
        BaseObject.__init__(self, __name__)
        if self.isEnabledForDebug:
            Enforcer.is_list(ontologies)

        self._find_depth = NerDepthFinder(ontologies).process
        self._find_type = NerTypeFinder(ontologies)
        self._find_pallete = NerPalleteLookup(ontologies)
        self._find_taxonomy = NerTaxonomyFinder(ontologies)

    def is_ner(self,
               input_text: str) -> bool:
        return self._find_taxonomy.is_ner(input_text)

    def color(self,
              ner: str) -> str:
        return self._find_pallete.lookup(ner)

    def colors(self):
        return self._find_pallete.colors()

    def depth(self,
              ner: str) -> int or None:
        return self._find_depth(ner)

    @staticmethod
    def _cleanse(input_text: str) -> str:
        if '_' in input_text:
            input_text = input_text.replace('_', ' ')
        return input_text

    def find_spacy_ner(self,
                       input_text: str) -> list or None:
        input_text = self._cleanse(input_text)
        return self._find_type.spacy(input_text)

    def find_graffl_ner(self,
                        input_text: str) -> list or None:
        input_text = self._cleanse(input_text)
        return self._find_type.graffl(input_text)

    def find_ner(self,
                 input_text: str) -> str or None:
        """Find NER from either the GRAFFL or spaCy taxonomy

        Reference:
            https://github.com/grafflr/graffl-core/issues/55#issuecomment-944572462

        Args:
            input_text (str): any input entity

        Returns:
            str or None: NER
        """
        input_text = self._cleanse(input_text)

        ners = []

        graffl_ners = self.find_graffl_ner(input_text)
        if graffl_ners:
            [ners.append(x) for x in graffl_ners]

        spacy_ners = self.find_spacy_ner(input_text)
        if spacy_ners:
            [ners.append(x) for x in spacy_ners]

        if not len(ners):
            ners.append("NER")

        if len(ners) == 1:
            return ners[0]

        d_depth = {self._find_depth(x): x for x in ners}
        return d_depth[max(d_depth)]
