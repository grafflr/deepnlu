# -*- coding: UTF-8 -*-
import pprint


from deepnlu import DeepNluAPI


def run(ontology_name, input_text):

    api = DeepNluAPI()
    assert api

    ontologies = ontology_name.split(',')
    ontologies = [x.strip() for x in ontologies]
    ontologies = [x for x in ontologies if x and len(x)]

    svcresult = api.handle_text(input_text=input_text,
                                ontologies=ontologies)
    assert svcresult

    tokens = [x['normal'] for x in svcresult[0][0]['tokens'] if 'swaps' in x]
    print(tokens)


def main(ontology_name, input_text):
    run(ontology_name, input_text)


if __name__ == "__main__":
    import plac

    plac.call(main)
