import sqlite3

#Prisijungimas prie duombazes, jeigu neranda sukuria pats
conn = sqlite3.connect('duomenu_baze.db')   

#Sukuriam objekta kuris leis vygdyti uzduotis
cursor = conn.cursor()

#Sukurima Queri
# cursor.execute('''CREATE TABLE IF NOT EXISTS zmones
#                (id INTEGER PRIMARY KEY,
#                vardas TEXT,
#                amzius INTEGER)''')

# cursor.execute('INSERT INTO zmones (vardas, amzius) VALUES(?, ?)', ('Jonas', 30)) # Prie Values ? reiskia reiksmes kuriu siuo metu nezinom
# cursor.execute('INSERT INTO zmones (vardas, amzius) VALUES(?, ?)', ('Petras', 40))
# cursor.execute('INSERT INTO zmones (vardas, amzius) VALUES(?, ?)', ('Ona', 20))

# cursor.execute('SELECT * FROM zmones;')
# rezultatai = cursor.fetchall() # fetchall - grazina visas uzklausas po paleidimo
# for zmogus in rezultatai:
#     print(zmogus)
# print(type(rezultatai))
# print('----------------------------------')



# cursor.execute('SELECT * FROM zmones WHERE amzius > 25') # harcodinom kintamaji
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)

# print('----------------------------------')

# #Tokia pati uzklausa tik kiti kintamieji
# amzius = 25
# cursor.execute(f'SELECT * FROM zmones WHERE amzius > {amzius}') #Priskyrem kintamaji
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)
# print('----------------------------------')
# # ta pati uzd, taciau dazniau naudojamas su uzklausomis
# cursor.execute(f'SELECT * FROM zmones WHERE amzius > ?', (25,))
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)
# print('----------------------------------')

# cursor.execute("UPDATE zmones SET amzius = ? WHERE vardas = ?", (31,'Jonas'))
# cursor.execute(f'SELECT * FROM zmones WHERE amzius > ?', (25,))
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)
# print('----------------------------------')

# ka_istrinti = input('Iveskite ka istrinti: ')
# cursor.execute('DELETE FROM zmones WHERE vardas = ?', (ka_istrinti,))
# cursor.execute(f'SELECT * FROM zmones WHERE amzius > ?', (25,))
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)

# print('----------------------------------')

cursor.execute("""
    CREATE TABLE IF NOT EXISTS klientai (
               kliento_id INTEGER PRIMARY KEY,
               vardas VARCHAR(50) NOT NULL,
               pavarde VARCHAR(50) NOT NULL,
               el_pastas TEXT)""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS prekes (
               prekes_id INTEGER PRIMARY KEY,
               pavadinimas TEXT NOT NULL,
               kaina REAL)""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS uzsakymai (
               uzsakymo_id INTEGER PRIMARY KEY,
               kliento_id INTEGER,
               prekes_id INTEGER,
               kiekis INTEGER,
               FOREIGN KEY (kliento_id) REFERENCES klientai(kliento_id),
               FOREIGN KEY (prekes_id) REFERENCES prekes(prekes_id))""")

# cursor.execute('INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?,?,?)', ('Jonas', 'Jonaitis','Jonas@gmail.com'))
# cursor.execute('INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?,?,?)', ('petras', 'Petraitis','Petras@gmail.com'))
# cursor.execute('INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?,?,?)', ('Ponas', 'Krabas','Krabas@gmail.com'))

# cursor.execute('INSERT INTO prekes (pavadinimas, kaina) VALUES (?,?)', ('Kava', 7.99))
# cursor.execute('INSERT INTO prekes (pavadinimas, kaina) VALUES (?,?)', ('Arbata', 5.99))

# cursor.execute('INSERT INTO uzsakymai (kliento_id, prekes_id, kiekis) VALUES (?,?,?)', (1,1,2))
# cursor.execute('INSERT INTO uzsakymai (kliento_id, prekes_id, kiekis) VALUES (?,?,?)', (2,2,5))

#Gaunam uzsakymus\

cursor.execute('SELECT * FROM uzsakymai')
uzsakymai = cursor.fetchall()

for uzsakymas in uzsakymai:
    print(uzsakymas)

print('----------------------------------')
cursor.execute('SELECT uzsakymo_id, vardas, pavarde, pavadinimas, kiekis FROM uzsakymai JOIN klientai ON klientai.kliento_id = uzsakymai.kliento_id JOIN prekes ON uzsakymai.prekes_id = prekes.prekes_id')

uzsakymai_kliento_data = cursor.fetchall()
for uzsakymas in uzsakymai_kliento_data:
    print(uzsakymas)

try:
    cursor.execute('BEGIN TRANSACTION')
    cursor.execute('INSERT INTO klientai (vardas,pavarde,el_pastas) VALUES (?,?,?)', ('Tonas','Tomaitis','tomaitis@gmail.com'))
    cursor.execute('UPDATE klientai SET el_pastas = ? WHERE kliento_id = ?',('antanas@gmail.com', '3'))
    conn.commit()
    print("GREAT SUCSESS!")
except Exception as e:
    conn.rollback() # rollback grazins i 113 eilute kur prasideda transakcija
    print('Transakcija atsaukta', e)
finally:
    conn.close()


conn = sqlite3.connect('duomenu_baze.db')
cursor = conn.cursor() # antra karta sukuriam/inisilazinom kursoriu, nes pries tai buves susijes su sesija, kuri yra uzdaryta
cursor.execute('SELECT * FROM klientai')
klientai = cursor.fetchall()

for klientas in klientai:
    print(klientas)

print('----------------------------------')

nauji_klientai = [
    ('Juozas','Juozaitis', 'Juozas@juozaitis.com'),
    ('Kazys', 'Kazauskas', 'kaz@kaz.com')
]

cursor.executemany('INSERT INTO klientai (vardas,pavarde,el_pastas) VALUES (?,?,?)', nauji_klientai)
cursor.execute('SELECT * FROM klientai')
klientai = cursor.fetchall()

for klientas in klientai:
    print(klientas)
print('----------------------------------')


naujos_prekes = [
    ('pomirdoras', 0.99),
    ('agurkas', 0.3)
]

cursor.executemany('INSERT INTO prekes (pavadinimas,kaina) VALUES (?,?)', naujos_prekes)
cursor.execute('SELECT * FROM prekes')
prekes = cursor.fetchall()

for prekes in prekes:
    print(prekes)

conn.commit()
conn.close()