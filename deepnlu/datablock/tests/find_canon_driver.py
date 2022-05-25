

from datablock.svc import FindSynonyms
from baseblock import Stopwatch


import os


def runner(ontology_name: str,
           input_text: str) -> None:

    finder = FindSynonyms(ontology_name)
    print(finder.find_canon(input_text))


def main(ontology_name, input_text):
    runner(ontology_name, input_text)


if __name__ == "__main__":
    import plac

    plac.call(main)
