from deepnlu.services.autotaxo.svc import GenerateTaxonomyTTL
from deepnlu.services.autotaxo.svc import GenerateTaxonomyDataFrame


def test_service():
    assert GenerateTaxonomyTTL()
    assert GenerateTaxonomyDataFrame()