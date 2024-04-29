import pytest
from gyvunu_prieglauda.gyvunu_prieglauda import Gyvunas, GyvunuPrieglauda


@pytest.fixture
def GyvunuPrieglaudu_valdymas():
    valdymas = GyvunuPrieglauda()
    valdymas.prideti_gyvuna(Gyvunas(2013,'Suo','Tobis', 10))
    valdymas.prideti_gyvuna(Gyvunas(2015,'kate','murkis', 7))
    valdymas.prideti_gyvuna(Gyvunas(2011,'Suo','Lokis', 20))
    return valdymas

def test_gauti_pagal_rusis(GyvunuPrieglaudu_valdymas):
    sunys = GyvunuPrieglaudu_valdymas.gauti_pagal_rusis('Suo')
    assert sunys == [GyvunuPrieglaudu_valdymas.gyvunai[0],GyvunuPrieglaudu_valdymas.gyvunai[2]]
    assert len(sunys) == 2

