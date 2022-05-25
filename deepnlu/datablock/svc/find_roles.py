# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Roles """


from pprint import pprint
from random import sample
from functools import lru_cache

from baseblock import BaseObject
from baseblock import get_ontology_name

from deepnlu.datablock.dmo import GenericDataFinder


class FindRoles(BaseObject):
    """ Generic Facade to interact with Roles """

    def __init__(self):
        """
        Created:
            1-Mar-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/206#issuecomment-1055858657
        """
        BaseObject.__init__(self, __name__)
        ontologies = ['roles']  # restricted facade

        self._departments_fwd = GenericDataFinder(
            class_suffix='InDepartments',
            module_suffix='in_departments',
            ontologies=ontologies).data()

        self._departments_rev = GenericDataFinder(
            class_suffix='InDepartmentsRev',
            module_suffix='in_departments_rev',
            ontologies=ontologies).data()

        self._activities_fwd = GenericDataFinder(
            class_suffix='InActivities',
            module_suffix='in_activities',
            ontologies=ontologies).data()

        self._activities_rev = GenericDataFinder(
            class_suffix='InActivitiesRev',
            module_suffix='in_activities_rev',
            ontologies=ontologies).data()

    @lru_cache
    def activities(self) -> list:
        return sorted(self._activities_rev.keys(), key=len)

    @lru_cache
    def departments(self) -> list:
        return sorted(self._departments_rev.keys(), key=len)

    @lru_cache
    def roles(self) -> list:
        return sorted(self._departments_fwd.keys(), key=len)

    @lru_cache
    def activities_by_role(self,
                           role: str) -> list:
        role = role.lower().strip()
        if role in self._activities_fwd:
            return self._activities_fwd[role]

    @lru_cache
    def roles_by_activity(self,
                          activity: str) -> list:
        activity = activity.lower().strip()
        if activity in self._activities_rev:
            return self._activities_rev[activity]

    @lru_cache
    def activities_by_department(self,
                                 department) -> list:
        activities = set()
        for role in self.roles_by_department(department):
            results = self.activities_by_role(role)
            if results:
                [activities.add(x) for x in results]

        return sorted(activities, key=len)

    @lru_cache
    def departments_by_activity(self,
                                activity: str) -> list:
        departments = set()
        for role in self.roles_by_activity(activity):
            results = self.departments_by_role(role)
            if results:
                [departments.add(x) for x in results]

        return sorted(departments, key=len)

    def random_activities(self,
                          n: int) -> list:
        if n >= len(self.activities()):
            return self.activities()

        return sample(self.activities(), n)

    def random_activity(self) -> str:
        return self.random_activities(1)[0]

    def random_departments(self,
                           n: int) -> list:
        if n >= len(self.departments()):
            return self.departments()

        return sample(self.departments(), n)

    def random_department(self) -> str:
        return self.random_departments(1)[0]

    def random_roles(self,
                     n: int) -> list:
        if n >= len(self.roles()):
            return self.roles()

        return sample(self.roles(), n)

    def random_role(self) -> str:
        return self.random_roles(1)[0]

    @lru_cache
    def roles_by_department(self,
                            department: str) -> list or None:
        department = department.lower().strip()
        if department in self.departments():
            return self._departments_rev[department]

    @lru_cache
    def departments_by_role(self,
                            role: str) -> list or None:
        role = role.lower().strip()
        if role in self.roles():
            return self._departments_fwd[role]
