# -*- coding: UTF-8 -*-
import os


from baseblock import EnvIO
from baseblock import FileIO


from deepnlu.services.erogito.parse.svc import GenerateDisplacyOutput


def test_service():

    relative_path = 'apps/recipes/deepnlu/regression/output/Grafflr-Core-0020-003.json'

    file_path = os.path.normpath(os.path.join(
        EnvIO.str_or_exception('GRAFFLR_HOME'),
        relative_path))

    FileIO.exists_or_error(file_path)

    tokens = FileIO.read_json(file_path)

    svc = GenerateDisplacyOutput()
    assert svc

    svc.process(tokens)


def main():
    test_service()


if __name__ == "__main__":
    main()
