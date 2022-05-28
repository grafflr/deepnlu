import os
from pprint import pprint


from baseblock import Stopwatch
from baseblock import Enforcer


from deepnlu.owlblock.bp import FindOntologyData


absolute_path = os.path.normpath(
    os.path.join(os.getcwd(), 'resources/testing'))

bp = FindOntologyData(
    ontologies=['unitest'],
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


def test_spans():
    Enforcer.is_dict(bp.spans())


def test_trie():
    Enforcer.is_dict(bp.trie())


def test_graffl_ner():
    Enforcer.is_dict(bp.graffl_ner())
    Enforcer.is_dict(bp.graffl_ner_rev())


def test_spacy_ner():
    Enforcer.is_dict(bp.spacy_ner())
    Enforcer.is_dict(bp.spacy_ner_rev())


def test_ner_depth():
    Enforcer.is_dict(bp.ner_depth())
    Enforcer.is_dict(bp.ner_depth_rev())


def test_ner_taxonomy():
    Enforcer.is_dict(bp.ner_taxonomy())
    Enforcer.is_dict(bp.ner_taxonomy_rev())


def test_ner_pallete_lookup():
    """ Given a NER return a Hex Color Code """
    result = bp.ner_pallete_lookup('EVENT')
    Enforcer.is_str(result)
    assert result.startswith('#')  # e.g., '#6fcb9f'
    assert len(result) == 7


def test_find_ner():

    sw = Stopwatch()
    bp.find_ner('staff')
    bp.find_ner('staff')
    bp.find_ner('staff')
    bp.find_ner('staffing level')
    result = bp.find_ner('staff')
    print(str(sw))

    assert result == "AGENT"


def test_find_synonyms():

    assert bp.find_canon('set to close') == 'closure'
    assert bp.find_variants('closure') == ['closure', 'set to close']

    assert bp.is_canon('closure')
    assert bp.is_variant('set to close')


def main():
    # test_find_comments()
    # test_find_labels()
    # test_find_effects()
    # test_find_effects_rev()
    # test_find_types()
    # test_lookup()
    # test_synonyms()
    # test_spans()
    # test_trie()
    # test_graffl_ner()
    # test_spacy_ner()
    # test_ner_depth()
    # test_ner_taxonomy()
    # test_ner_pallete_lookup()
    # test_find_ner()
    test_find_synonyms()


if __name__ == "__main__":
    main()
