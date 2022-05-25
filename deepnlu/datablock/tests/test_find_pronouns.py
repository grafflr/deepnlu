from baseblock import Enforcer

from deepnlu.datablock.svc import FindPronouns


def test_find_pronouns() -> None:

    svc = FindPronouns()
    assert svc

    Enforcer.is_list(svc.all())

    assert svc.has_pronoun('good job, you!')
    assert svc.has_pronoun('I went home')
    assert svc.has_pronoun('where are we now???')

    assert not svc.has_pronoun('where are wee now???')
    assert not svc.has_pronoun('good job, u!')
    assert not svc.has_pronoun('II went home')


def main():
    test_find_pronouns()


if __name__ == "__main__":
    main()
