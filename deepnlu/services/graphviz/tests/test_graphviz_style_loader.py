

from baseblock import Enforcer


from imaginor.graphviz.dmo import GraphvizStyleLoader


def test_component():
    dmo = GraphvizStyleLoader('nlu')
    assert dmo

    d_style = dmo.style()
    Enforcer.is_dict(d_style)


def main():
    test_component()


if __name__ == "__main__":
    main()
