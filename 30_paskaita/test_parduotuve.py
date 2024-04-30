from parduotuve import Parduotuve, Preke
import pytest

@pytest.fixture
def parduotuves_valdymas():
    valdymas = Parduotuve()
    valdymas.prideti_preke((Preke('kede',120.3, 5)))
    valdymas.prideti_preke(Preke('suolas', 200, 10))
    valdymas.prideti_preke(Preke('taburete', 28, 100))
    return valdymas

def test_prideti_preke(parduotuves_valdymas):
    preke = Preke('taburete', 28, 100)
    preke2 = Preke('suolas', 210, 11)
    naujos_prekes = parduotuves_valdymas.prideti_preke(preke)
    assert preke in naujos_prekes
    assert preke2 not in naujos_prekes

def test_prideti_nauja_preke(parduotuves_valdymas):
    preke = Preke('taburete', 28, 100)
    naujos_prekes = parduotuves_valdymas.prideti_preke(preke)
    preke2 = parduotuves_valdymas.gauti_preke_pagal_index(3)
    assert preke.pavadinimas == preke2.pavadinimas


def test_gauti_preke(parduotuves_valdymas):
    prekes = parduotuves_valdymas.gauti_prekes()
    assert len(prekes) == 3
    naujos_prekes = parduotuves_valdymas.prideti_preke(Preke('taburete', 28, 100))
    assert len(naujos_prekes) == 4

def test_istrinti_preke(parduotuves_valdymas):
    preke = parduotuves_valdymas.istrinti_preke(0)
    assert preke not in parduotuves_valdymas.gauti_prekes()


# 1) iskviesti metoda atnaujinti preke, pateikent nauja prekes objekta
# 2) gauti pagal indeksa ir patikrinti ar tos reiksmes yra matomos

def test_atnaujinti_preke(parduotuves_valdymas):
    preke = Preke('kede',120.3, 5)
    atnauj_preke = Preke('Suolas',120.3, 5)

    assert preke != parduotuves_valdymas.atnaujinti_preke(atnauj_preke)
    


