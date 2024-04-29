from send_email import pranesti_vartotojui, skaiciavimas, nuskaityti_faila, skaiciu_suma, vidurkis, zodziu_skaicius, unikalios_reiksmes,patvirtinti_apmokejima,patvirtinti_apmokejima_ar_yra
import pytest
from unittest.mock import patch, mock_open
from pytest_mock import mocker

@pytest.fixture
def mock_send_email():
    with patch('send_email.send_email') as mocked_send_email: # Nurodom kuria funkcija ignoruosim
        yield mocked_send_email # yield grazina ivyki

def test_pranesti_vartotojui(mock_send_email):
    email = 'siuntejas.gmail.com'
    ivykis = 'Susitikimas'
    pranesti_vartotojui(email,ivykis)
    mock_send_email.assert_called_once() # Testuoja ar mockinama funkcija buvo iskviestas tik viena karta
    args, _ = mock_send_email.call_args # args rodys kiek turime kintamuju 
    assert args[0] == "antanas@gmail.com"
    assert len(args) == 4

@pytest.fixture
def mock_daugyba():
    with patch('send_email.daugyba') as mocked_daugyba: 
        # send.email yra failo pavadinimas .daugyba musu funkcija kuria mockinam
        # patch uztikrina, kad bus sukurtas ivikio objektas is kurio passimti veiksmus
        # ir uztikrins, kad nurodyta funkcija nebus iskvieciama
        yield mocked_daugyba # yield grazina ivyki su svieziausiom reiksmem

def test_skaiciavimas(mock_daugyba): # mock_daugyba pasijamam mockinimo funkcija
    skaiciavimas(1,1)
    mock_daugyba.assert_not_called()
    skaiciavimas(2,5)
    mock_daugyba.assert_called_once()


def test_nuskaityti_faila(mocker):
    mocker.patch('builtins.open', mock_open(read_data='Tekstas kuri "tarkim" nuskaite open')) # Nurodom ka norim nutildyti su: 'builtins.opens'
    rez_kurio_tikimes = 'Tekstas kuri "tarkim" nuskaite open' # Tekstas kuris butu jeigu nemockintume
    rezultatas = nuskaityti_faila('Duomenys.txt') # Nuskaityti faila
    assert rez_kurio_tikimes == rezultatas # Tikrinam

@pytest.fixture
def skaiciu_uzpildymas():
    sarasas = [1,2,3,4,5]
    return sarasas

def test_skaiciu_suma(skaiciu_uzpildymas):
    assert skaiciu_suma(skaiciu_uzpildymas) == 15

@pytest.fixture
def skirtingi_sarasai1():
    sarasas = [1,2,3,4,5]
    return sarasas

@pytest.fixture
def skirtingi_sarasai2():
    sarasas = [10,20,30,40,5,5]
    return sarasas

@pytest.fixture
def skirtingi_sarasai3():
    sarasas = [0.3,0.4,0.5]
    return sarasas

def test_vidurkis(skirtingi_sarasai1,skirtingi_sarasai2, skirtingi_sarasai3):
    assert vidurkis(skirtingi_sarasai1) == sum(skirtingi_sarasai1) / len(skirtingi_sarasai1)
    assert vidurkis(skirtingi_sarasai2) == sum(skirtingi_sarasai2) / len(skirtingi_sarasai2)
    assert vidurkis(skirtingi_sarasai3) == sum(skirtingi_sarasai3) / len(skirtingi_sarasai3)
    assert vidurkis([1,2,3, 'p']) == 'klaida'

@pytest.fixture
def tekstas():
    tekstas = 'Siandien, jau, penktadienis, beveik, savaitgalis'
    return tekstas
@pytest.fixture
def tekstas1():
    tekstas = 'Savaitgali zadamas, pagaliau, siltesnis, oras, negu, siandien'
    return tekstas
#3uzd
def test_zodziu_skaicius(tekstas):
    tiketinas_rezultatas = zodziu_skaicius(tekstas)
    assert tiketinas_rezultatas == 5

#4uzd
def test_unikalios_reiksmes(skirtingi_sarasai2):
    tiketinas_rezultatas = unikalios_reiksmes(skirtingi_sarasai2)
    assert tiketinas_rezultatas == [10,20,30,40,5]

#----------------------
# Bank uzd:.

def test_patvirtinti_apmokejima():
    assert patvirtinti_apmokejima('LT877777', 250) == True
    assert patvirtinti_apmokejima('LT877777', 300) == False

@pytest.fixture
def test_patvirtinti_apmokejima():
    assert patvirtinti_apmokejima('LT5555', 290) == True
    assert patvirtinti_apmokejima('LT5555', 400) == False
@pytest.fixture
def mock_patvirtinti_apmokejima_atsakymas():
    return True
@patch('send_email.patvirtinti_apmokejima')
def test_patvirtinti_apmokejima_ar_yra(mock_patvirtinti_apmokejima, mock_patvirtinti_apmokejima_atsakymas):
    mock_patvirtinti_apmokejima.return_value = True
    mock_patvirtinti_apmokejima.return_value = mock_patvirtinti_apmokejima_atsakymas
    assert patvirtinti_apmokejima_ar_yra("LV5433", 250) == "Banko sąskaita LV5433 gali atlikti mokėjimą"
@patch('send_email.patvirtinti_apmokejima')
def test_patvirtinti_apmokejima_ar_nera(mock_patvirtinti_apmokejima):
    mock_patvirtinti_apmokejima.return_value = False
    assert patvirtinti_apmokejima_ar_yra("LV5433", 259) == "Banko sąskaita LV5433 negali atlikti mokėjimą"