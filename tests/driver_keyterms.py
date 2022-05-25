

from deepnlu.services.erogito import ErogitoAPI


def driver(input_text: str):
    api = ErogitoAPI()
    assert api

    if input_text == "random":
        from deepnlu.datablock.svc import FindQuestions
        input_text = FindQuestions().random()
        print (input_text)

    result = api.keyterms(input_text)

    [print(x) for x in result]


def main(input_text):
    driver(input_text)


if __name__ == '__main__':
    import plac

    plac.call(main)
