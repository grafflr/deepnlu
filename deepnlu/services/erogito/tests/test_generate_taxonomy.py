from erogito.autotaxo.svc import GenerateTaxonomyTTL
from erogito.autotaxo.svc import GenerateTaxonomyDataFrame


def test_service():
    assert GenerateTaxonomyTTL()
    assert GenerateTaxonomyDataFrame()