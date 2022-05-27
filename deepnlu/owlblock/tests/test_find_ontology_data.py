import os
from baseblock import Enforcer


from deepnlu.owlblock.bp import FindOntologyData


absolute_path = os.path.normpath(
    os.path.join(os.getcwd(), 'resources/data/owl'))

bp = FindOntologyData(
    ontologies=['nursing'],
    absolute_path=absolute_path)
assert bp


def test_find_comments():
    Enforcer.is_dict(bp.comments())


def test_find_labels():
    Enforcer.is_dict(bp.labels())
    Enforcer.is_dict(bp.labels_rev())


def test_find_types():
    print(bp.types())
    print(bp.types_rev())


def test_find_effects():
    Enforcer.is_dict(bp.effects())
    Enforcer.is_dict(bp.effects_rev())


def test_lookup():
    Enforcer.is_dict(bp.lookup())

def test_synonyms():
    Enforcer.is_dict(bp.synonyms())
    Enforcer.is_dict(bp.synonyms_rev())


def main():
    # test_find_comments()
    # test_find_labels()
    # test_find_effects()
    # test_find_effects_rev()
    # test_find_types()
    # test_lookup()
    test_synonyms()


if __name__ == "__main__":
    main()
