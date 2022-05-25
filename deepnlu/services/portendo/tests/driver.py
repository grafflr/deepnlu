import os
from pprint import pprint

from baseblock import EnvIO
from baseblock import FileIO


from portendo import __version__
from portendo import Portendo


def temp() -> None:

    # input_tokens = [
    #     {
    #         "normal": "give",
    #         "swaps": {
    #             "ent": "",
    #             "canon": "give",
    #             "type": "appraisal"
    #         }
    #     },
    #     {
    #         "ent": "",
    #         "normal": "me",
    #     },
    #     {
    #         "ent": "CARDINAL",
    #         "normal": "5",
    #     },
    #     {
    #         "normal": "random_query",
    #         "swaps": {
    #             "ent": "",
    #             "canon": "random_query",
    #             "type": "classification"
    #         }
    #     },
    #     {
    #         "normal": "category",
    #         "swaps": {
    #             "ent": "",
    #             "canon": "category",
    #             "type": "appraisal"
    #         }
    #     }
    # ]

    input_tokens = [
        {
            "normal": "summarize",
        },
        {
            "normal": "the",
        },
        {
            "normal": "last",
        },
        {
            "normal": "5",
        },
        {
            "normal": "minutes",
        },
        {
            "normal": "please",
        },
    ]

    api = Portendo('chitchat')
    assert api

    api.run(input_tokens)


def main():
    temp()


if __name__ == "__main__":
    main()
