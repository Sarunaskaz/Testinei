import pytest
from receptai.receptu_valdymai import Receptas, ReceptuValdymas


@pytest.fixture
def receptu_valdymas():
    valdymas = ReceptuValdymas()
    valdymas.prideti_recepta(Receptas('Cepelinai', 120, ['Bulves', 'Mesa']))
    valdymas.prideti_recepta(Receptas('Salotos', 30, ['agurkas', 'pomidoras']))
    valdymas.prideti_recepta(Receptas('Kotletas', 45, []))
    return valdymas

def test_gauti_receptus_pagal_laika(receptu_valdymas):
    rezultatas = receptu_valdymas.gauti_receptus_pagal_laika(30)
    pavadinimai = [receptas.pavadinimas for receptas in rezultatas]
    assert pavadinimai == ['Salotos']
    assert 'Kotletas' not in pavadinimai



def test_pasalinti_recepta_pagal_pavadinima(receptu_valdymas):
    receptu_valdymas.pasalinti_recepta_pagal_pavadinima('Kotletas')
    assert 'Kotletas' not in receptu_valdymas.gauti_pav()

def test_gauti_receptus_pagal_zodi(receptu_valdymas):
    receptai_pagal_zodi = receptu_valdymas.gauti_receptus_pagal_zodi('Cepelinai')
    assert receptai_pagal_zodi == ['Cepelinai']
    assert 'Kotletas' not in receptai_pagal_zodi

def test_gauti_bendra_ruosimo_laika(receptu_valdymas):
    assert receptu_valdymas.gauti_bendra_ruosimo_laika() == 195

def test_atrinkti_ingridientus(receptu_valdymas):
    tikimes_rezultato = receptu_valdymas.receptai[0]
    assert receptu_valdymas.atrinti_pagal_ingredintus('Bulves') == [tikimes_rezultato]

def test_isvalyti_receptus(receptu_valdymas):
    receptu_valdymas.isvalyti_receptus()
    assert receptu_valdymas.receptai == []


