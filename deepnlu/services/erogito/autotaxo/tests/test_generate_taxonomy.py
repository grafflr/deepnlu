from deepnlu.services.erogito.autotaxo.svc import GenerateTaxonomyTTL
from deepnlu.services.erogito.autotaxo.svc import GenerateTaxonomyDataFrame


def test_service():
    assert GenerateTaxonomyTTL()
    assert GenerateTaxonomyDataFrame()