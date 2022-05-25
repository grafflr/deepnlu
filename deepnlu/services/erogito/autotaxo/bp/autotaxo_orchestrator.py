#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Orchestrate Taxonomy Generation """


from deepnlu.services.erogito.autotaxo.svc import GenerateTaxonomyDataFrame
from deepnlu.services.erogito.autotaxo.svc import GenerateTaxonomyTTL

from baseblock import BaseObject


class AutoTaxoOrchestrator(BaseObject):
    """ Orchestrate Taxonomy Generation """

    def __init__(self):
        """ Change History:

        Created:
            16-Apr-2022
            craig@grafflr.ai
            *   -   refactored out of jupyter notebook:
                    GRAFFL-286 Textacy Textrank
                    http://localhost:8888/notebooks/grafflbox/GRAFFL-286%20Textacy%20Textrank.ipynb
                -   in pursuit of
                    https://github.com/grafflr/graffl-core/issues/286
        Updated:
            2-May-2022
            craig@grafflr.ai
            *   renamed from 'generate-taxonomy'

        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_text: str,
                top_n: int = 500) -> list or None:

        df = GenerateTaxonomyDataFrame().process(
            input_text=input_text,
            top_n=top_n)

        if df is None:
            return None

        results = GenerateTaxonomyTTL().process(df)
        if not results or not len(results):
            return None

        return results
