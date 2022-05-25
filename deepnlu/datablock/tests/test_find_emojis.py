

import os
from pprint import pprint

from baseblock import Enforcer
from baseblock import Stopwatch


from datablock.svc import FindEmojis

svc = FindEmojis()
assert svc


def test_random():
    Enforcer.is_nonempty_list(svc.all())
    Enforcer.is_str(svc.random())

    for i in range(1, 6):
        Enforcer.is_str(svc.random(funny=i))
        Enforcer.is_str(svc.random(positive=i))
        Enforcer.is_str(svc.random(funny=i, positive=i))


def test_cluster():
    for i in range(0, 15):
        result = svc.by_cluster(i)
        if result is not None:
            Enforcer.is_nonempty_list(result)

    Enforcer.is_nonempty_list(svc.in_same_cluster('mermaid'))


def test_gender():
    for gender in ['M', 'F', 'U']:
        Enforcer.is_nonempty_list(svc.by_gender(gender))

    Enforcer.is_nonempty_list(svc.with_same_gender('merman'))


def test_funny():
    for i in range(1, 6):
        Enforcer.is_nonempty_list(svc.by_funny_level(i))

    assert not svc.just_as_funny('what')
    Enforcer.is_nonempty_list(svc.just_as_funny('sweat_smile'))

    assert not svc.funnier('what')
    Enforcer.is_nonempty_list(svc.funnier('sweat_smile'))


def test_irony():
    Enforcer.is_nonempty_list(svc.ironic_emojis())
    Enforcer.is_str(svc.random_ironic_emoji())


def test_positive():
    for i in range(1, 6):
        Enforcer.is_nonempty_list(svc.by_positive_level(i))

    assert not svc.just_as_positive('what')
    Enforcer.is_nonempty_list(svc.just_as_positive('raised_hands'))


def test_faces():
    Enforcer.is_nonempty_list(svc.faces())
    Enforcer.is_str(svc.random_face())


def main():
    test_faces()
    test_positive()
    test_irony()
    test_funny()
    test_gender()
    test_cluster()
    test_random()


if __name__ == "__main__":
    main()
