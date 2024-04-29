import smtplib

def send_email(sender, receiver, subject, body):
    smtp_server = "gmail.com"
    smtp_port = 777

    with smtplib.SMTP() as server:
        server.sendmail(sender, receiver, subject, body)

def pranesti_vartotojui(email, ivykis):
    sender = "antanas@gmail.com"
    subject = "Tema"
    body = f"Sveiki, jus gavote email {ivykis}"
    send_email(sender, email, subject, body)

def daugyba(num1, num2):
    return num1 * num2

def skaiciavimas(num1, num2):
    if num1 == num2:
        return num1 * num2
    return daugyba(num1, num2)


#------------------------
#Kitas budas atsidaryti faila

def nuskaityti_faila(failo_nuoroda):
    with open(failo_nuoroda, 'r') as failas:
        duomenys = failas.read()
        return duomenys

# print(nuskaityti_faila('28_paskaita/mocking/tekstas.txt')) funkcijos patikrinimas

# 1 užduotis
# Parašykite funkciją skaiciu_suma(skaiciai), kuri priima sąrašą skaičių ir grąžina jų sumą.
# Parašykite testą, kuris patikrina, ar funkcija teisingai suskaičiuoja skaičių sumą, panaudojant fixture duomenis su įvairiais skaičių sąrašais.

def skaiciu_suma(skaiciai):
    return sum(skaiciai)

# 2 užduotis
# Parašykite funkciją vidurkis(skaiciai), kuri priima sąrašą skaičių ir grąžina jų vidurkį.
# Parašykite testą, kuris tikrina, ar funkcija teisingai skaičiuoja skaičių sąrašo vidurkį, naudojant fixture duomenis su skirtingais skaičių sąrašais.

def vidurkis(skaiciai):
    for sk in skaiciai:
        if not (isinstance(sk, int) or isinstance(sk, float)):
            return 'klaida'
    return sum(skaiciai) / len(skaiciai)

# 3 užduotis
# Parašykite funkciją zodziu_skaicius(tekstas), kuri priima teksto eilutę ir grąžina jos žodžių skaičių.
# Parašykite testą, kuris patikrina, ar funkcija teisingai skaičiuoja žodžių skaičių teksto eilutėje, naudojant fixture duomenis su skirtingomis teksto eilutėmis.

def zodziu_skaicius(tekstas):
    return len(tekstas.split())

# 4 užduotis
# Parašykite funkciją unikalios_reiksmes(sarasas), kuri priima sąrašą ir grąžina jo unikalų elementų sąrašą.
# Parašykite testą, kuris patikrina, ar funkcija teisingai grąžina unikalų elementų sąrašą, naudojant fixture duomenis su įvairiais sąrašais.

# 1pvz:.
def unikalios_reiksmes(sarasas):
    sarasas_unikaliu = []
    for x in sarasas:
        if not x in sarasas_unikaliu:
            sarasas_unikaliu.append(x)
    return sarasas_unikaliu

# 1 užduotis
# Parašykite funkciją patvirtinti_apmokejima(saskaitos_numeris, suma), kuri kreipiasi į kitą funkciją (patikrinti_likutį(sąskaitos_numeris, suma) šioje funkcijoje galite turėti dictionary, kurio viduje saugosite banko sąskaitų numerius ir jų likučius)
# funkcija patikrinti_likutį tiesiog grąžina True, jeigu sąskaitos likutis yra pakankamas, False jeigu lėšų yra per mažai.
# Funkcija patvirtinti_apmokejima grąžins suformuotą tekstą "Banko sąskaita xxxx-xxxx-xxxx gali/negali atlikti mokėjimą", šis pranešimas bus formuojamas priklausomai nuo patvirtinti_apmokėjimą atsakymo
# Parašykite testų, kurie testuoja tik patvirtinti_apmokejima funkcijos veikimą, todėl jums reikės mockinti patikrinti likutį funkcijos veikimą.

def patvirtinti_apmokejima(saskaitos_numeris, suma):
    saskaitos = {
        "LT5555": 300,
        "LV5433": 250,
        "EE4532": 200
    }
    if saskaitos[f'{saskaitos_numeris}']>= suma:
        return True
    return False
def patvirtinti_apmokejima_ar_yra(saskaitos_numeris, suma):
    pakanka = patvirtinti_apmokejima(saskaitos_numeris, suma)
    return f"Banko sąskaita {saskaitos_numeris} {'gali' if pakanka else 'negali'} atlikti mokėjimą"



# 2 užduotis
# Parašykite funkciją analizuoti_excel(failo_kelias), kuri nuskaito duomenis iš Excel failo ir juos analizuoja. Duomenys yra pateikti lentelės pavidalu, kur pirmoje eilutėje yra stulpelių pavadinimai, o kiekvienoje sekančioje eilutėje yra įrašyti duomenys.

# Funkcija turi atlikti šiuos veiksmus:

# Nuskaityti duomenis iš Excel failo, kurio kelias nurodytas parametre failo_kelias.
# Apskaičiuoti vidurkį kiekvienam stulpeliui, kuriame yra skaičiai.
# Grąžinti žodyną, kuriame stulpelių pavadinimai yra raktai, o vidurkiai yra atitinkamos reikšmės.
# Parašykite bent du testus funkcijai analizuoti_excel, kurie padengtų šiuos scenarijus:

# Tikrinamas vidurkis kiekvienam stulpeliui, kai yra duomenys.
# Tikrinamas atitinkamo klaidingo duomenų formato apdorojimas, kai yra neteisingi duomenys Excel faile.

# Norėdami nuskaityti duomenis iš Excel failo ir juos analizuoti, galite naudoti pandas biblioteką. Tačiau, užduoties dalyje, susijusioje su testais, turite naudoti mocking'ą, kad būtų simuliuojamas tikras failo skaitymas ir analizė.
