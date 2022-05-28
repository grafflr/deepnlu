from random import sample

from deepnlu.services import ExtractTextacyKeyterms


def driver(input_text: str):
    svc = ExtractTextacyKeyterms()
    assert svc

    if input_text == "random":
        from deepnlu.datablock.os import list_of_questions
        input_text = sample(list_of_questions, 1)[0]
        print(input_text)

    results = svc.process(
        top_n=5,
        input_text=input_text)

    assert results


def main(input_text):
    driver(input_text)


if __name__ == '__main__':
    import plac

    plac.call(main)
