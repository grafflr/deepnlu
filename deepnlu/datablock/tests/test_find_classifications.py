import os

from baseblock import EnvIO
from baseblock import FileIO

from deepnlu.datablock.svc import FindClassifications


def test_load() -> None:

    #   TODO:
    #   20220528    DEEPNLU-16-1140324490       Describing a path to 'grafflr-core' from within 'deepnlu'
    #                                           is borne of present necessity but needs to be fixed later

    absolute_path = os.path.normpath(
        os.path.join(
            # EnvIO.str_or_exception('GRAFFLR_HOME'),
            os.getcwd(),
            # 'apps/blocks/datablock/datablock/os/manifest',
            'deepnlu/datablock/os/manifest/chitchat'))
    # 'chitchat'))

    FileIO.exists_or_error(absolute_path)

    svc = FindClassifications('chitchat', absolute_path)
    assert svc

    assert svc.include_one_of is not None
    assert svc.include_all_of is not None
    assert svc.exclude_one_of is not None
    assert svc.exclude_all_of is not None

    # assert svc.score('RANDOM_CATEGORIES#3')


def main():
    test_load()


if __name__ == "__main__":
    main()
