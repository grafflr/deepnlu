

from datablock.svc import FindSynonyms
from baseblock import Stopwatch


import os


def test_skills():

    os.environ['GRAFFL_ONTOLOGIES'] = "skills"
    finder = FindSynonyms()

    print(finder.find_canon("national_economic_policy"))
    assert finder.find_canon(
        "national_economic_policy") == "national_economic_policy"

    print(finder.find_canon("serial_innovator"))


def test_nursing():

    os.environ['GRAFFL_ONTOLOGIES'] = "nursing"
    finder = FindSynonyms()

    # https://github.com/grafflr/graffl-core/issues/46
    assert finder.find_canon('registered_nurse') == "registered_nurse"

    assert finder.find_canon(
        "american_nursing_association") == "american_nurses_association"

    assert finder.find_canon(
        "american nursing association") == "american_nurses_association"

    assert finder.find_canon(
        "american_nurses_association") == "american_nurses_association"

    assert finder.fwd_data()
    assert len(finder.fwd_data()) > 1

    assert finder.rev_data()
    assert len(finder.rev_data()) > 1

    assert not finder.find_variants('nurse22')
    assert finder.find_variants('nurse')
    assert len(finder.find_variants('nurse')) > 1

    assert not finder.find_canon('nurses22')
    assert finder.find_canon('nurses')
    assert finder.find_canon('nurses') == 'nurse'

    assert finder.is_variant('nurses')
    assert not finder.is_variant('nurses22')

    assert finder.is_canon('nurse')
    assert not finder.is_canon('nurse22')


def test_multiple():

    os.environ['GRAFFL_ONTOLOGIES'] = "skills, nursing, medical"
    finder = FindSynonyms()

    import pprint
    pprint.pprint(finder.fwd_data())

    assert finder.fwd_data()
    assert len(finder.fwd_data()) > 1

    assert finder.rev_data()
    assert len(finder.rev_data()) > 1

    assert finder.find_canon('nurses') == 'nurse'


def main():
    test_multiple()


if __name__ == "__main__":
    main()
