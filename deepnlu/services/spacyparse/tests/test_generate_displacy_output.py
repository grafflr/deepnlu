# -*- coding: UTF-8 -*-


from pprint import pprint

from baseblock import Enforcer

from deepnlu.services.spacyparse.svc import ParseInputTokens
from deepnlu.services.spacyparse.svc import GenerateDisplacyOutput
from deepnlu.services.segmenter import Segmenter
from deepnlu.recipe.dmo import SentenceHandlerOneShot
from deepnlu.owlblock.bp import FindOntologyData


def execute(input_text: str):

    

    handle_sentence = SentenceHandlerOneShot(
        FindOntologyData()).process

    paragraphs = []
    for input_sentence in Segmenter().input_text(input_text):
        paragraphs.append([handle_sentence(x)
                           for x in input_sentence])

    parser = ParseInputTokens()
    assert parser

    displacy = GenerateDisplacyOutput()
    assert displacy

    result_1 = parser.process(paragraphs)
    Enforcer.is_list(result_1)

    result_2 = displacy.process(result_1)
    pprint(result_2)


def test_parse_input_tokens():
    execute("""what would a company that had the motto "Proficimus More Irretenti" be likely to do ?""")


def main():
    test_parse_input_tokens()


if __name__ == "__main__":
    main()
