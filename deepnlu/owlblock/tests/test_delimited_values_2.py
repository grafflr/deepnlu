import os
from pprint import pprint

from baseblock import Enforcer

from deepnlu.owlblock.bp import FindOntologyData
from deepnlu.recipe import DeepNluAPI


ONTOLOGIES = ['normal']

absolute_path = os.path.normpath(
    os.path.join(os.getcwd(), 'resources/testing'))


def test_synonyms():
    """ Critical Test Case

    Reference:
        https://github.com/grafflr/deepnlu/issues/21
        https://github.com/grafflr/deepnlu/issues/21#issuecomment-1141518333

    Purpose:
        The entity 'increase' has multiple synonyms
        -   some from the external text file
        -   others from rdfs:seeAlso
        -   per the latter, some of these are comma delimited

    Demonstrate that we can accurately match a synonym via all these sources
    """

    api = DeepNluAPI()
    assert api

    bp = FindOntologyData(
        ontologies=ONTOLOGIES,
        absolute_path=absolute_path)
    assert bp

    d_syn = bp.synonyms()
    Enforcer.is_dict(d_syn)

    assert sorted(d_syn['increase']) == [
        'doubled',  # << delimited.txt
        'increase',  # actual entity name
        'increased',  # << delimited.txt
        'increases',  # << delimited.txt
        'increasing',  # << delimited.txt
        'quadrupled',  # << rdfs:seeAlso<CSV>
        'tripled'  # << rdfs:seeAlso<CSV>
    ]

    _, tokens = api.handle_text(
        input_text="they tripled entrollment quickly",
        ontologies=ONTOLOGIES,
        absolute_path=absolute_path)

    assert 'increase' in tokens


def main():
    test_synonyms()


if __name__ == "__main__":
    main()
