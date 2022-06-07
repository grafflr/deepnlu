import os

from baseblock import FileIO
from baseblock import Enforcer

from deepnlu.owlblock.bp import FindOntologyData


absolute_path = os.path.normpath(
    os.path.join(os.getcwd(), 'resources/regression/ontologies'))
FileIO.exists_or_error(absolute_path)


class TestFindOntologyData(object):

    def __init__(self,
                 ontology_name: str):
        self.bp = FindOntologyData(
            ontologies=[ontology_name],
            absolute_path=absolute_path)
        assert self.bp

    def find_synonyms(self):
        assert self.bp.find_canon('set to close') == 'closure'
        assert self.bp.find_variants('closure') == ['closure', 'set to close']
        assert self.bp.is_canon('closure')
        assert self.bp.is_variant('set to close')


def runner(ontology_name: str) -> None:
    bp = TestFindOntologyData(ontology_name)
    bp.find_synonyms()


def main():
    runner('unitest')


if __name__ == "__main__":
    main()
