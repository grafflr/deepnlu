import os

from baseblock import FileIO
from baseblock import Enforcer

from deepnlu.services.graphviz.dmo import GraphvizStyleLoader


def test_component():

    absolute_path = os.path.normpath(
        os.path.join(os.getcwd(), 'resources'))
    FileIO.exists(absolute_path)

    FileIO.exists_or_error(absolute_path)

    dmo = GraphvizStyleLoader(
        stylesheet_name='nlu',
        absolute_path=absolute_path)
    assert dmo

    d_style = dmo.style()
    Enforcer.is_dict(d_style)


def main():
    test_component()


if __name__ == "__main__":
    main()
