# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Facade to find Review Comments and Categories """


from random import sample
from pprint import pprint

from itertools import product
from collections import Counter
from collections import defaultdict

from baseblock import Enforcer
from baseblock import BaseObject
from baseblock import get_ontology_name

from datablock.dmo import GenericDataFinder


class FindReviews(BaseObject):
    """ Facade to find Review Comments and Categories """

    __slots__ = (
        '_comments_fwd',
        '_comments_rev',
        '_categories',
    )

    def __init__(self):
        """
        Created:
            6-Feb-2022
            craig@grafflr.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/165
        Updated:
            25-Feb-2022
            craig@grafflr.ai
            *   refactor some logic into ask-appraisal
                https://github.com/grafflr/graffl-core/issues/199
        """
        BaseObject.__init__(self, __name__)
        ontologies = ['appraisal']  # restricted facade

        self._comments_as_list = None
        self._categories_as_list = None

        self._knockouts_fwd = GenericDataFinder(
            class_suffix='KnockoutList',
            module_suffix='knockout_list',
            ontologies=ontologies).data()

        self._knockouts_rev = GenericDataFinder(
            class_suffix='KnockoutListRev',
            module_suffix='knockout_list_rev',
            ontologies=ontologies).data()

        self._comments_fwd = GenericDataFinder(
            class_suffix='ReviewComments',
            module_suffix='review_comments',
            ontologies=ontologies).data()

        self._comments_rev = GenericDataFinder(
            class_suffix='ReviewCommentsRev',
            module_suffix='review_comments_rev',
            ontologies=ontologies).data()

        self._categories_fwd = GenericDataFinder(
            class_suffix='ReviewCategories',
            module_suffix='review_categories',
            ontologies=ontologies).data()

        self._categories_rev = GenericDataFinder(
            class_suffix='ReviewCategoriesRev',
            module_suffix='review_categories_rev',
            ontologies=ontologies).data()

    def knockouts_fwd(self) -> list:
        """ A Knockout is defined as "A line that grabs the attention of the audience and makes them want to read more"
        This is a list of Knockout Words that can be used 
        """
        return self._knockouts_fwd

    def knockouts_rev(self) -> list:
        """ A Knockout is defined as "A line that grabs the attention of the audience and makes them want to read more"
        This is a list of Knockout Words that can be used 
        """
        return self._knockouts_rev

    def knockouts_by_gram_level(self,
                                n: int) -> list:
        results = []
        for k in self.knockouts_rev():
            if len(k.split(' ')) == n:
                results.append(k)

        return results

    def implies_by_comment(self,
                           comment: str) -> list or None:
        comment = comment.lower().strip()
        if comment in self._comments_fwd:
            return self._comments_fwd[comment]

    def random_comments(self,
                        n: int) -> list:
        if not self._comments_as_list:
            self._comments_as_list = list(self._comments_fwd.keys())

        return sample(self._comments_as_list, n)

    def random_categories(self,
                          n: int) -> list:
        if not self._categories_as_list:
            self._categories_as_list = list(self._categories_fwd.keys())

        if n >= len(self._categories_as_list):
            return self._categories_as_list

        return sample(self._categories_as_list, n)

    def comments_by_category(self,
                             category: str) -> list:
        category = category.lower()
        if category in self._categories_fwd:
            return self._categories_fwd[category]

        if ' ' in category:
            return self.comments_by_category(category.replace(' ', '_'))

    def is_implies(self,
                   input_text: str) -> bool:
        """ Determine if input text is an 'implies' entity

            Assume this OWL entity

                :some_node rdf:type :Learning_Skill ;
                    rdfs:label "this is my label" ;
                    :implies :Alpha_Beta .

            Thus usage:
                is_implies('Alpha_Beta')
            would return True
        """
        input_text = input_text.lower()

        if input_text in self._comments_rev:
            return True

        if ' ' in input_text:
            return input_text.replace(' ', '_') in self._comments_rev

        return False

    def group_comments_by_category(self,
                                   comments: list) -> dict:
        """ Group a list of lists (comments) by category

            Given this input
                [
                    'comment-1'
                    'comment-2',
                    'comment-3', 
                    'comment-4',
                    'comment-5',
                    'comment-6',
                ]

            The output becomes 
                {
                    'category-1': [
                        'comment-1',
                        'comment-2',
                        'comment-3',
                        'comment-4',
                    ],
                    'category-2': [
                        'comment-5',
                    ],
                    'category-3': [
                        'comment-6',
                    ],
                }
        """
        d_results = defaultdict(list)
        for comment in comments:
            for category in self._categories_rev[comment]:
                d_results[category].append(comment)
        return dict(d_results)

    def comments_fwd(self) -> dict:
        return self._comments_fwd

    def comments_rev(self) -> dict:
        return self._comments_rev

    def categories_fwd(self) -> dict:
        return self._categories_fwd

    def categories_rev(self) -> dict:
        return self._categories_rev

    def all_comments(self) -> list:
        return list(self.comments_fwd().keys())
