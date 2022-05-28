from random import sample

from deepnlu.services.erogito import ErogitoAPI


def driver(input_text: str):
    api = ErogitoAPI()
    assert api

    if input_text == "random":
        from deepnlu.datablock.os import list_of_questions
        input_text = sample(list_of_questions, 1)[0]
        print(input_text)

    result = api.keyterms(input_text)

    [print(x) for x in result]


def main(input_text):
    driver(input_text)


if __name__ == '__main__':
    import plac

    plac.call(main)
