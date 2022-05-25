# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from baseblock import Enforcer

from deepnlu.datablock.svc import FindRoles


def test_service():
    svc = FindRoles()
    assert svc

    Enforcer.is_nonempty_list(svc.roles())
    Enforcer.is_nonempty_list(svc.departments())
    Enforcer.is_nonempty_list(svc.activities())

    Enforcer.is_nonempty_list(svc.roles_by_department('research'))
    Enforcer.is_nonempty_list(svc.departments_by_role('architect'))
    Enforcer.is_nonempty_list(svc.roles_by_activity('trend analysis'))
    Enforcer.is_nonempty_list(svc.activities_by_role('analyst'))
    Enforcer.is_nonempty_list(svc.activities_by_department('accounting'))
    Enforcer.is_nonempty_list(svc.departments_by_activity('auditing'))

    Enforcer.is_nonempty_list(svc.random_departments(3))
    Enforcer.is_nonempty_list(svc.random_roles(3))
    Enforcer.is_nonempty_list(svc.random_activities(3))

    Enforcer.is_str(svc.random_department())
    Enforcer.is_str(svc.random_role())
    Enforcer.is_str(svc.random_activity())


def main():
    test_service()


if __name__ == "__main__":
    main()
