

from datablock.svc import FindNER
from baseblock import Stopwatch


import os


def test_palletes():
    os.environ['GRAFFL_ONTOLOGIES'] = "skills"

    finder = FindNER()
    assert finder

    print(finder.color('ROLE'))
    assert finder.color('ROLE')

    print(finder.find_ner('national_economic_policy'))
    assert finder.find_ner('national_economic_policy') == "ARTIFACT"

    print(finder.find_ner('creative'))
    assert finder.find_ner('creative') == 'SKILL'


def test_skills_ner():
    os.environ['GRAFFL_ONTOLOGIES'] = "skills"

    finder = FindNER()
    assert finder

    assert finder.find_ner("psychiatrist") == "ROLE"


def test_nursing_ner():

    os.environ['GRAFFL_ONTOLOGIES'] = "nursing"

    finder = FindNER()
    assert finder

    print(finder.find_ner('personal_touch'))
    assert finder.find_ner('personal_touch') == 'SKILL'

    print(finder.find_spacy_ner('church'))
    assert finder.find_spacy_ner('church')[0] == 'NORP'
    assert finder.find_spacy_ner('florence_nightingale')[0] == 'PERSON'

    print(finder.find_ner('church'))
    # NORP is more specific than AGENT
    assert finder.find_ner('church') == 'NORP'

    print(finder.find_ner('florence_nightingale'))
    assert finder.find_ner('florence_nightingale') == 'PERSON'

    print(finder.find_graffl_ner('church')[0])
    assert finder.find_graffl_ner('church')[0] == 'AGENT'
    assert finder.find_graffl_ner('florence_nightingale')[0] == 'AGENT'

    print(finder.find_ner('american_nurses_association'))
    assert not finder.find_spacy_ner('american_nurses_association')
    print(finder.find_graffl_ner('american_nurses_association'))
    assert finder.find_graffl_ner('american_nurses_association') == [
        'AGENT', 'ASSOC', 'GROUP']
    assert finder.find_ner('american_nurses_association') == 'ASSOC'


def test_skills_ner():
    os.environ['GRAFFL_ONTOLOGIES'] = "skills"

    finder = FindNER()
    assert finder

    print(finder.is_ner('MENTOR'))
    assert finder.is_ner('MENTOR')

    print(finder.is_ner('MENTOR2'))
    assert not finder.is_ner('MENTOR2')


def test_nursing_ner():

    finder = FindNER('questions')
    assert finder

    print(finder.is_ner('labor_event'))


def main():
    # test_palletes()
    # test_skills_ner()
    # test_nursing_ner()
    # test_skills_ner()
    test_nursing_ner()


if __name__ == "__main__":
    main()
