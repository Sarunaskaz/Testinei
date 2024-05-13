import sqlite3
import datetime

class Mechanikai:

    def __init__(self, vardas, pavarde, el_pastas, valadinis_atlyginimas, specializacija):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas
        self.valadinis_atlyginimas = valadinis_atlyginimas
        self.specializacija = specializacija

class Klientai:
    def __init__(self, vardas, pavarde, el_pastas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas

class Kliento_automobilis:
    def __init__(self,valstybinis_nr, marke,modelis,kliento_id):
        self.varlstybinis_nr = valstybinis_nr
        self.marke = marke
        self.modelis = modelis
        self.kliento_id= kliento_id

class Remontas:
    def __init__(self,kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija):
        self.kliento_id = kliento_id
        self.mechaniko_id = mechaniko_id
        self.darbo_pradzia = darbo_pradzia
        self.darbo_pabaiga = darbo_pabaiga
        self.darbo_kaina = darbo_kaina
        self.remonto_kategorija = remonto_kategorija


class Autoservisas:
    def __init__(self):
        self.conn = sqlite3.connect('autoserviso_duomenys.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS mechanikai(
            mechaniko_id INTEGER PRIMARY KEY,
            vardas VARCHAR(50) NOT NULL,
            pavarde VARCHAR(50) NOT NULL,
            el_pastas TEXT,
            valadinis_atlyginimas DOUBLE,
            specializacija VARCHAR(50) NOT NULL)""")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS klientai(
            kliento_id INTEGER PRIMARY KEY,
            vardas VARCHAR(50) NOT NULL,
            pavarde VARCHAR(50) NOT NULL,
            el_pastas TEXT)""")
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS kliento_automobilis(
            Kliento_automobilis_id INTEGER PRIMARY KEY,
            valstybinis_nr TEXT,
            marke TEXT,
            modelis TEXT,
            kliento_id INTEGER,
            FOREIGN KEY (kliento_id) REFERENCES klientai(kliento_id))""")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS remontas(
            remonto_id INTEGER PRIMARY KEY,
            kliento_id INTEGER,
            mechaniko_id INTEGER,         
            darbo_pradzia DATE,
            darbo_pabaiga DATE,
            darbo_kaina DOUBLE,
            remonto_kategorija TEXT,
            FOREIGN KEY (kliento_id) REFERENCES klientai(kliento_id),
            FOREIGN KEY (mechaniko_id) REFERENCES mechanikai (mechaniko_id))""")
        
    def prideti_mechanika(self, vardas, pavarde, el_pastas, valadinis_atlyginimas, specializacija):
        mechanikas = Mechanikai(vardas, pavarde, el_pastas, valadinis_atlyginimas, specializacija)
        self.cursor.execute("INSERT INTO mechanikai (vardas, pavarde, el_pastas, valadinis_atlyginimas, specializacija) VALUES (?, ?, ?, ?, ?)", (vardas, pavarde, el_pastas, valadinis_atlyginimas, specializacija))
        self.conn.commit()
        return mechanikas
    


    def prideti_klienta(self, vardas, pavarde, el_pastas):
        klientas = Klientai(vardas, pavarde, el_pastas)
        self.cursor.execute("INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?, ?, ?)", (vardas, pavarde, el_pastas))
        self.conn.commit()
        return klientas

    def prideti_automobili(self, valstybinis_nr, marke, modelis, kliento_id):
        kliento_automobilis = Kliento_automobilis(valstybinis_nr, marke, modelis, kliento_id)
        self.cursor.execute("INSERT INTO kliento_automobilis (valstybinis_nr, marke, modelis, kliento_id) VALUES (?, ?, ?,?)", (valstybinis_nr, marke, modelis, kliento_id))
        self.conn.commit()
        return kliento_automobilis

    # def __init__(self,kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija):

    def prideti_remonta(self, kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, remonto_kategorija):
        remontas = Remontas(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina= 1, remonto_kategorija=remonto_kategorija)
        date_format = "%Y-%m-%d %H:%M"
        darboPradzia_object = datetime.datetime.strptime(darbo_pradzia, date_format)
        darboPabaiga_object = datetime.datetime.strptime(darbo_pabaiga, date_format)
        valandos = darboPabaiga_object - darboPradzia_object
        val_atlyginimas = valandos.total_seconds()/3600
        valandinis = self.gauti_ikaini(mechaniko_id)
        darbo_kaina = val_atlyginimas * valandinis *2
        self.cursor.execute("INSERT INTO remontas (kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija) VALUES (?, ?, ?, ?, ?, ?)", (kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija))
        self.conn.commit()
        return remontas
    
    def gauti_ikaini(self, mechaniko_id):
        self.cursor.execute(f'SELECT valadinis_atlyginimas FROM mechanikai WHERE mechaniko_id = {mechaniko_id}')
        valandinis = self.cursor.fetchone()
        return float(valandinis[0])
    
    def kiek_klientas_sumokejas_is_viso(self,isViso):
        self.cursor.execute(f'SELECT SUM(darbo_kaina) FROM remontas WHERE kliento_id = {isViso}')
        rezultatas = self.cursor.fetchall()
        print(rezultatas)

    def kiek_klientas_sumokejas_is_viso_uz_viena_auto(self,klientas,auto_id):
        self.cursor.execute(f'SELECT SUM(darbo_kaina) FROM remontas JOIN kliento_automobilis USING(kliento_id) WHERE kliento_id = {klientas} AND kliento_automobilis_id = {auto_id}')
        rezultatas = self.cursor.fetchall()
        print(rezultatas)


    def perziureti_irasus(self, lentele):
        self.cursor.execute(f'SELECT * FROM {lentele}')
        rezultattu_sarasas = self.cursor.fetchall()
        print('Irasai pagal jusu uzklausa: ')
        for rezultatas in rezultattu_sarasas:
            print(rezultatas)

    def laisvi_mechanikai(self, darbo_pradzia, darbo_pabaiga, mechaniko_id):
        self.cursor.execute(f'SELECT * FROM remontas WHERE  mechaniko_id ={mechaniko_id} AND (darbo_pradzia BETWEEN {darbo_pradzia} AND {darbo_pabaiga}) <= (darbo_pabaiga BETWEEN {darbo_pradzia} AND {darbo_pabaiga})')
        rezultattu_sarasas = self.cursor.fetchall()
        print(rezultattu_sarasas)

autoservisas = Autoservisas()
# autoservisas.prideti_mechanika("Tomas","Tomke","tomke@gmail.com", 8.5, "Elektra")
# autoservisas.prideti_klienta('Silvester','Stalone', 'Stalone@gmail.com')
# autoservisas.prideti_automobili('KLA 329', 'BMW', 'E35', 1)
# autoservisas.prideti_remonta(1,1,'2024-05-11','2024-05-20',320.1, 'elektra')
