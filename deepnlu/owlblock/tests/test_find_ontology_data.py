import os
from baseblock import Enforcer


from deepnlu.owlblock.bp import FindOntologyData


absolute_path = os.path.normpath(os.path.join(os.getcwd(), 'resources'))

bp = FindOntologyData(
    ontologies=['nursing'],
    absolute_path=absolute_path)
assert bp


def test_find_comments():
    Enforcer.is_dict(bp.comments())


def test_find_labels():
    Enforcer.is_list(bp.labels())


def test_find_effects():
    Enforcer.is_dict(bp.effects())


def test_find_effects_rev():
    Enforcer.is_dict(bp.effects_rev())


def main():
    test_find_comments()
    test_find_labels()
    test_find_effects()
    test_find_effects_rev()


if __name__ == "__main__":
    main()
