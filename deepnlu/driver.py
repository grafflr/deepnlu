# -*- coding: UTF-8 -*-


import os
from random import sample

from baseblock import FileIO
from baseblock import Enforcer

from deepnlu.recipe.bp import DeepNluAPI

import logging
logging.getLogger('deepnlu').setLevel(logging.WARNING)


def run(ontology_name, input_text):

    api = DeepNluAPI()
    assert api

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/data/owl'))
    FileIO.exists_or_error(absolute_path)

    ontologies = ontology_name.split(',')
    ontologies = [x.strip() for x in ontologies]
    ontologies = [x for x in ontologies if x and len(x)]
    Enforcer.is_list(ontologies)
    print(f"Ontologies: {ontologies}")

    if input_text == "random":
        from deepnlu.datablock.os.qlists import list_of_questions
        input_text = sample(list_of_questions, 1)[0]
        print(f"Random Input Text: {input_text}")

    svcresult = api.handle_text(input_text=input_text,
                                ontologies=ontologies,
                                absolute_path=absolute_path)
    assert svcresult

    tokens = [x['normal'] for x in svcresult[0][0]['tokens'] if 'swaps' in x]
    print(f"Extracted Tokens (total={len(tokens)})\n\t{tokens}")


def main(ontology_name, input_text):
    run(ontology_name, input_text)


if __name__ == "__main__":
    import plac

    plac.call(main)
