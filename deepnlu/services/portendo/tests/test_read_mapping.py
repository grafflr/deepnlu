

import os
from pprint import pprint

from baseblock import Enforcer

from deepnlu.services.portendo.svc import ReadMapping


def test_service():

    schema_name = "test_intents.yml"
    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources/testing'))

    svc = ReadMapping(
        schema_name=schema_name,
        absolute_path=absolute_path)
    assert svc

    actual_result = svc.index()
    pprint(actual_result)

    expected_result = {
        "exclude_all_of": {},
        "exclude_one_of": {},
        "include_one_of": {},
        "startswith": {},
        "include_all_of": {
            "animal": [{
                "mappings": [
                    "Favorite_Animal_Response#1"
                ],
                "terms":[
                    "favorite"
                ]
            }],
            "late": [{
                "mappings": [
                    "Late_Transport"
                ],
                "terms":[
                    "transport"
                ]
            }
            ]},
        "mapping": {
            "Favorite_Animal_Response#1": [{
                "include_all_of": [
                    "favorite",
                    "animal"
                ]
            }],
            "Late_Transport": [{
                "include_all_of": [
                    "late",
                    "transport"
                ]
            }]
        },
        "scoring": {
            "Favorite_Animal_Response#1": 0.0,
            "Late_Transport": 0.0
        },
    }

    assert actual_result == expected_result


def main():
    test_service()


if __name__ == "__main__":
    main()
