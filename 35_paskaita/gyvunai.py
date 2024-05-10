
import sqlite3

class Gyvunas:
    def __init__(self, vardas ,amzius, svoris):
        self.vardas = vardas
        self.amzius = amzius
        self.svoris = svoris

class Prieglauda:
    def __init__(self):
        self.gyvunu_sarasas = []
        print(self.gyvunu_sarasas)

    def prideti_gyvuna(self,gyvunas):
        self.gyvunu_sarasas.append(gyvunas)

    def istrinti_gyvuna(self,vardas):
        neistrinti = []
        for gyvunas in self.gyvunu_sarasas: 
            if vardas != gyvunas.vardas:
                neistrinti.append(gyvunas)
        self.gyvunu_sarasas = neistrinti

    def grazintu_pagal_amziu(self,amzius):
        metai = []
        for gyvunas in self.gyvunu_sarasas:
            if amzius == gyvunas.amzius:
                metai.append(gyvunas)
            return  metai





gyvunai = [{"vardas":"Brisius", "amzius": 10}, {"vardas":"kate","amzius":5}]

skaicius = 1

prieglauda1 = Prieglauda()
prieglauda2 = Prieglauda()

gyvunas1 = Gyvunas("Testis" , 4 , 2)
gyvunas2 = Gyvunas("Brisius" , 12 , 25)
prieglauda1.prideti_gyvuna(gyvunas1)
prieglauda1.prideti_gyvuna(gyvunas2)
prieglauda1.istrinti_gyvuna("Testis")

# print("Cia returnina pagal amziu" , prieglauda1.grazintu_pagal_amziu(12))
# rezultatas = prieglauda1.grazintu_pagal_amziu(12)
# for gyvunas in rezultatas:
#     print(gyvunas.vardas)
# print("^amzius2")


# print(prieglauda1.gyvunu_sarasas)

gyvunas3 = {
        "vardas": "kazkas",
        "amzius": 5,
        "svoris": 10
}

prieglauda1.gyvunu_sarasas.append(gyvunas1)
prieglauda1.gyvunu_sarasas.append(gyvunas2)
# prieglauda1.gyvunu_sarasas.append(gyvunas3)

# print('-----------------------------------')
# for gyvunas in prieglauda1.gyvunu_sarasas:
#     print(gyvunas.vardas)


# print(gyvunas3["vardas"])
# print(gyvunas1.vardas)

# print("----------------------------------------")

class Motociklas:
    def __init__(self ,marke, modelis, metai):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai

    def uzkurti(self):
        print(F"motociklas {self.marke} {self.modelis} buvo uzkurtas")

motociklas1 = Motociklas("KTM" , "EXC450" , 2016)       #objektas turintis tam tikras savybes
# print(motociklas1.marke) 
# print(motociklas1.modelis)
# print(motociklas1.metai)

# motociklas1.uzkurti()

motociklas2 = Motociklas("Suzuki" , "DRZ400" , 2006)
# motociklas2.uzkurti()

motociklas = {"marke": "Honda" , "modelis": "CRF250" , "metai" : 2018}
# print(motociklas["modelis"])

# print(type(motociklas))
zodis = "labas"
# print(type(zodis))
zodis = zodis.upper()
# print(zodis)

skaicius2 = 5
# print(type(skaicius2))

# print(type(motociklas1))



tv_kanalai = [
    {"padavinimas": "LRT", "programa": [{"savaites_diena": 1, "laidos": [{"laikas": "8:00", "pavadinimas": "Gustavo Enciklopedija", "dalyviai": [{"vardas": "Gustavas"}]}]}]}
]
# print(tv_kanalai[0]["programa"][0]["laidos"][0]["dalyviai"][0]["vardas"])


# print(prieglauda1.gyvunu_sarasas[0].vardas)
# print(type(prieglauda1.gyvunu_sarasas[0].vardas))

# sukurti klase baznycia (kunigo vardas, adresas, statybos metai)
# sukurti klase Vyskupija viena property - baznyciu_sarasas
# sukurti viena Vyskupija
# sukurti kelias baznycias

class Baznycia:
    def __init__(self ,kunigo_vardas, adresas, statybos_metai, vyskupijos_id):
        self.kunigo_vardas = kunigo_vardas
        self.adresas = adresas
        self.statybos_metai = statybos_metai
        self.vyskupijos_id = vyskupijos_id

class Vyskupija:
    def __init__(self):
        self.baznyciu_sarasas = []
        self.conn = sqlite3.connect('Vyskupija.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS vyskupija
                            (vyskupijos_id INTEGER PRIMARY Key,
                            pavadinimas TEXT)
                            """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS baznycia(
                            baznycios_id INTEGER PRIMARY Key,
                            kunigo_vardas VARCHAR(50)NOT NULL,
                            statybos_metai TEXT,
                            adresas TEXT,
                            metai TEXT,
                            vyskupijos_id INTEGER,
                            FOREIGN KEY (vyskupijos_id) REFERENCES vyskupija(vyskupijos_id))""")
        # self.cursor.execute(""" INSERT INTO vyskupija (pavadinimas) VALUES ('katedra')""")
        self.conn.commit()
                            
    def prideti_baznycia(self, baznycia):
        self.baznyciu_sarasas.append(baznycia)
    


    def prideti_baznycia(self,baznycia):
        self.cursor.execute('INSERT INTO baznycia (kunigo_vardas, adresas, statybos_metai, vyskupijos_id) VALUES (?,?,?,?)', (baznycia.kunigo_vardas, baznycia.adresas, baznycia.statybos_metai, baznycia.vyskupijos_id))
        self.conn.commit()
        # self.baznyciu_sarasas.append(baznycia)

    def spausdinam_vyskupija(self):
        self.cursor.execute("SELECT * FROM vyskupija")
        vyskupijos = self.cursor.fetchall()
        for baznycia in vyskupijos:
            print(baznycia)

    def spausdinam_baznycias(self):
        self.cursor.execute("SELECT * FROM baznycia")
        baznycios = self.cursor.fetchall()
        for baznycia in baznycios:
            print(baznycia)

    def istrinti_baznycia(self,metai):
        self.cursor.execute(f'DELETE FROM baznycia WHERE statybos_metai = {metai}')
        self.conn.commit()
    #sukurti metoda, kuris leis atnaujinti informacija vienai baznyciai, naudokite input
    
    # def baznycios_atnaujinimas(self):
        

    def __del__(self):
        self.conn.close()


# sukurti du metodus 
# istrinti baznycia, kuri leis istrinti baznycia pagal baznycios pavadinima, pavadinima turite pateikti kaip argumenta


baznycia1 = Baznycia("Plonas_kunigas" , "Laisves prospektas 59" , 2000, 1)
baznycia2 = Baznycia("Storas_kunigas" , "Laisves prospektas 95" , 1985,2)
baznycia3 = Baznycia("Steponas_kunigas" , "Gedimino 95" , 1964,3)

vyskupija = Vyskupija()

# print(baznycia1.adresas)

# vyskupija.prideti_baznycia(baznycia1)
# vyskupija.prideti_baznycia(baznycia2)
# vyskupija.prideti_baznycia(baznycia3)
# vyskupija.istrinti_baznycia(2000)

# print(vyskupija.baznyciu_sarasas[0].adresas)
# print(vyskupija.baznyciu_sarasas[2].adresas)
