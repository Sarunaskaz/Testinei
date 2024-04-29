
# 1 užduotis
# sukurkite funkciją, kuri prideda elementą prie sąrašo, jeigu tas elementas dar neegzistuoja (sąrašas visada yra unikalus)
# jūsų funkcija visada turi grąžinti rikiuoti sąrašą (nuo mažiausio iki didžiausio)
# parašykite šiai funkcijai keletą unit testų, naudokite setUp ir tearDown

def prideti_elementa(elementas,element_sarasas):
    if elementas not in element_sarasas:
            element_sarasas.append(elementas)
    else:
          return 'Elementas jau yra sarase'
    return sorted(element_sarasas)

# Patobulinti, kad mestu sarasa one klaida 'Elementas jau yra sarase'



# 2 užduotis
# Parašykite funkciją ar_lyginis, kuri patikrina, ar duotas sveikasis skaičius yra nelyginis.
# Tada parašykite testus, kurie patikrina, ar ši funkcija veikia tinkamai, naudodami assertTrue ir assertFalse.

def ar_lyginis(sk):
    return sk % 2 != 0


# 3 užduotis
# Parašykite funkciją ar_palindromas, kuri patikrina, ar duotas tekstas yra palindromas (skaitant atvirkštine tvarka jis vis tiek skaitomas taip pat). 
# Tada parašykite testus, kurie patikrina, ar ši funkcija veikia tinkamai, naudodami assertTrue ir assertFalse.

def ar_palindromas(zodis, zodis2):
     return zodis == zodis2[::-1]




# 4 užduotis
# Parašykite funkciją palyginti_sarasus, kuri patikrina, ar duoti sąrašai yra lygūs. 
# Tada parašykite testus, kurie naudoja assertEqual ir assertNotEqual, kad patikrintų, ar ši funkcija veikia tinkamai.

def palyginti_sarasus(sar1, sar2):
      return sar1 == sar2

      
# a = [1,2,3,4,5,6,7,8,9]
# b = [1,1,1,1,1,1,1,1,1]
# c= [1,2,3,4,5,6,7,8,9]

# print(palyginti_sarasus(a,c))

