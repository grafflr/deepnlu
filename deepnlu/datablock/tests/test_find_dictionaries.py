from datablock.svc import FindDictionaries

finder = FindDictionaries()
assert finder


def test_find_hyphens():
    assert finder.hyphens()
    assert len(finder.hyphens())


def test_find_currency():
    assert finder.currency()
    assert len(finder.currency())


def test_find_squotes():
    assert finder.squotes()
    assert len(finder.squotes())


def test_find_dquotes():
    assert finder.dquotes()
    assert len(finder.dquotes())


def test_find_enclitics():
    assert finder.enclitics()
    assert len(finder.enclitics())


def test_find_abbreviations():
    assert finder.abbreviations()
    assert len(finder.abbreviations())
