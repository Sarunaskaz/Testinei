import pytest
import funkcijos as fn
from unittest.mock import patch

def test_skip(): # praleisti kazkokius testus
    savaites_diena = 'sekmadienis'
    if savaites_diena == 'sekmadienis':
        pytest.skip('Praleidziam si testa')
    assert fn.apskaiciuoti_plota(5,4) == 20

@pytest.fixture
def gauti_klientu_sarasa():
    return [1,2,3,4,5,6]


def test_fikstura(gauti_klientu_sarasa):
    assert len(gauti_klientu_sarasa) == 6



@pytest.fixture
def ploto_duomenys():
    ilgis = 5
    plotis = 10
    return ilgis, plotis

def test_apskaiciuoti_plota(ploto_duomenys):
    ilgis, plotis = ploto_duomenys
    assert fn.apskaiciuoti_plota(ilgis, plotis) == 50

@pytest.fixture
def mazo_ploto_duomenys():
    return 2,5

def test_apskaiciuoti_maza_plota(mazo_ploto_duomenys):
    ilgis, plotis = mazo_ploto_duomenys
    assert fn.apskaiciuoti_plota(ilgis, plotis) == 10


@pytest.fixture
def mock_gauti_orus_response():
    return {'temperatura': 20, 'miestas': 'Vilnius'}

@patch('funkcijos.gauti_orus')
def test_apsirengti_siltai(mock_gauti_orus, mock_gauti_orus_response):
    mock_gauti_orus.return_value = mock_gauti_orus_response['temperatura']
    assert fn.apsirengti_siltai('Vilnius') == True

