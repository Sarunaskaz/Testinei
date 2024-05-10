import sqlite3

conn = sqlite3.connect('ligonones_duomenys.db')
cursor = conn.cursor()

#---------------GYDYTOJAI----------------
cursor.execute("""
        CREATE TABLE IF NOT EXISTS gydytojai(
               gydytojo_id INTEGER PRIMARY KEY,
               vardas VARCHAR(50) NOT NULL,
               pavarde VARCHAR(50) NOT NULL,
               specializacija VARCHAR(50) NOT NULL,
               el_pastas TEXT)
""")

#---------------PACIENTAI----------------
cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientai(
               paciento_ID INTEGER PRIMARY KEY,
               vardas VARCHAR(50) NOT NULL,
               pavarde VARCHAR(50) NOT NULL,
               gimimo_data TEXT,
               lytis VARCHAR(15),
               el_pastas TEXT,
               gydytojo_id INTEGER,
               FOREIGN KEY (gydytojo_id) REFERENCES gydytojai(gydytojo_id))
""")

#---------------SUSITIKIMAI----------------
cursor.execute("""
            CREATE TABLE IF NOT EXISTS susitikimai(
               susitikimo_id INTEGER PRIMARY KEY,
               paciento_ID INTEGER,
               gydytojo_id INTEGER,
               data_laikas TEXT,
               susitikimo_paskirtis TEXT,
               komentarai_pastabos TEXT,
               FOREIGN KEY (paciento_ID) REFERENCES pacientai(paciento_ID),
               FOREIGN KEY (gydytojo_id) REFERENCES gydytojai(gydytojo_id)

            )
""")



# cursor.execute('INSERT INTO gydytojai (vardas, pavarde, specilizacija, el_pastas) VALUES(?,?,?,?)', ('Ona','Onute','seimos gydytoja','Ona@gydytoja.lt'))
#---------------GYDYTOJAI----------------
# nauji_gydytojai = [
#     ('Danielius','Danelevicius','chirurgija','Danielius@gydytojai.lt'),
#     ('Ponas','Krabas','Odontologas','Ponas@gydytojai.lt'),
#     ('Stepas','Sofinis','Pediatras','Stepas@gydytojai.lt'),
#     ('Karolina','Kelmyte','seimos gydytoja','Karolina@gydytojai.lt'),
#     ('Diana','Delfinaite','Odontologe','Diana@gydytojai.lt'),
#     ('Egle','Sese','Pediatre','Egle@gydytojai.lt'),
#     ('Marta','Mertise','chirurgija','Marta@gydytojai.lt'),
    
# ]
# cursor.executemany('INSERT INTO gydytojai (vardas,pavarde,specilizacija,el_pastas) VALUES (?,?,?,?)', nauji_gydytojai)

# cursor.execute('SELECT * FROM gydytojai;')
# rezultatai = cursor.fetchall() # fetchall - grazina visas uzklausas po paleidimo
# for zmogus in rezultatai:
#     print(zmogus)




#---------------PACIENTAI----------------
# nauji_pacientai = [
#     # ('Lukas','Azukas','1993-04-28', 'Vyras','Lukas@zmogus.lt',2),
#     # ('Batuotas','Katinas','1997-02-29', 'Vyras','Batuotas@zmogus.lt',7),
#     # ('Srekas','Zalias','1969-01-3', 'Vyras','Srekas@zmogus.lt',5),
#     # ('Cameron','Diaz','1968-03-08', 'Moteris','Cameron@zmogus.lt',3),
#     ('Salma','Haja','1969-01-16', 'Moteris','Salma@zmogus.lt',1)
#     # ('Tom','Hanks','1961-12-01', 'Vyras','Tom@zmogus.lt',2),
#     # ('Stewert','Little','2001-05-14', 'Vyras','Stewert@zmogus.lt',2)
# ]
# cursor.executemany('INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?,?,?,?,?,?)', nauji_pacientai)

#---------------SUSITIKIMAI----------------

# nauji_susitikimai = [
#     (2,8,'2024-05-08','operacija','grazidiena'),
#     (1,8,'2024-05-08','trauma','negrazi grazidiena'),
#     (3,5,'2024-05-08','reguliari patikra','grazidiena'),
#     (2,2,'2024-02-25','operacija','negrazi grazidiena'),
#     (7,3,'2024-02-25','reguliari patikra','negrazi grazidiena'),
# ]

# cursor.executemany('INSERT INTO susitikimai (paciento_ID, gydytojo_id, data_laikas, susitikimo_paskirtis, komentarai_pastabos) VALUES (?,?,?,?,?)', nauji_susitikimai)


# 3. Atlikite šias užklausas:

# -------------------------3.1------------------------
# 1. Visi pacientai, kurių gimimo data yra mažiau nei 1970-01-01 turėtų būti priskirti gydytojui, kurio ID yra 1

# cursor.execute(f'UPDATE pacientai SET gydytojo_id = 1 WHERE gimimo_data < "1970-01-01"')
# cursor.execute(f'SELECT * FROM pacientai WHERE gimimo_data < "1970-01-01" AND gydytojo_id = 1')
# rezultatai = cursor.fetchall()
# for pacientas in rezultatai:
#     print(pacientas)

# print('----------------------------------')

# 2. Raskite visus susitikimus, kurie vyksta šiandien. (rezultate norime matyti kliento vardą ir pavardę, gydytojo vardą ir pavardę ir susitikimo paskirtį

# cursor.execute('SELECT gydytojai.vardas, gydytojai.pavarde, pacientai.vardas, pacientai.pavarde, susitikimai.susitikimo_paskirtis FROM susitikimai JOIN gydytojai ON gydytojai.gydytojo_id = susitikimai.gydytojo_id JOIN pacientai on susitikimai.paciento_id WHERE data_laikas = "2024-05-08" ')
# susitikimai = cursor.fetchall()
# for susitikimas in susitikimai:
#     print(susitikimas)

# print('----------------------------------')

# 3. Sukurkite užklausą, kuri ištrintų visus susitikimus, kurie įvyko daugiau nei 6 mėnesiai nuo šiandienos datos.


# cursor.execute('DELETE FROM susitikimai WHERE data_laikas BETWEEN "2023-12-08" AND "2024-05-08"')
# rezultatai = cursor.fetchall()
# for istrinimas in rezultatai:
#     print(istrinimas)

# print('----------------------------------')
# 4. Parašykite užklausą, kuri rastų gydytojų vardus ir pavardes, kuriems yra priskirti pacientai, kurių susitikimo paskirtyje yra žodis "trauma"
cursor.execute(f'SELECT gydytojai.vardas, gydytojai.pavarde, susitikimai.susitikimo_paskirtis FROM susitikimai JOIN gydytojai ON gydytojai.gydytojo_id = susitikimai.gydytojo_id WHERE susitikimo_paskirtis = "trauma"')
rezultatai = cursor.fetchall()
for pacientas in rezultatai:
    print(pacientas)


# 5. Raskite visus pacientus, kurių gydytojo specializacija yra chirurgija ir susitikimo paskirtis yra operacija.
# cursor.execute(f'SELECT * FROM pacientai JOIN gydytojai ON gydytojai.gydytojo_id = pacientai.gydytojo_id JOIN susitikimai ON susitikimai.gydytojo_id = gydytojai.gydytojo_id WHERE specilizacija = "chirurgija" AND susitikimo_paskirtis = "operacija"')
# rezultatai = cursor.fetchall()
# for pacientas in rezultatai:
#     print(pacientas)
# conn.commit()
# conn.close()
