# self reikalingas, kad butu galima kreiptis i pacia klase

class Receptas:
    def __init__(self, pavadinimas, ruosimo_laikas, ingridientu_sar):
        self.pavadinimas = pavadinimas
        self.paruosimo_laikas = ruosimo_laikas
        self.ingridientu_sarasas = ingridientu_sar

class ReceptuValdymas:
    def __init__(self):
        self.receptai = []

    def gauti_pav(self):
        return [receptas.pavadinimas for receptas in self.receptai]

    def prideti_recepta(self, receptas):
        self.receptai.append(receptas)

    def gauti_receptus_pagal_laika(self, maksimalus_laikas):
        # rezultatai = []
        # for receptas in self.receptai:
        #     if receptas['ruosimo_laikas'] <= maksimalus_laikas:
        #         rezultatai.append(receptas)
        # return rezultatai
        return [receptas for receptas in self.receptai if receptas.paruosimo_laikas <= maksimalus_laikas] # su list comprehantion, tas pats kaip nuo 16-20


# 1 užduotis
# papildykite klasę ReceptųValdymas pridedant metodą pasalinti_recepta, šis metodas turi panaikinti receptą iš receptų sąrašo,
# pagal pateiktą pavadinimą
# parašykite testą, kad įsitikintumėte ar jūsų metodas veikia tinkamai
    def pasalinti_recepta_pagal_pavadinima(self,pav):
        self.receptai = [receptas for receptas in self.receptai if receptas.pavadinimas != pav]
        # rezultatai = []
        # for receptas in self.receptai:
        #     if receptas.pavadinimas != pav:
        #         rezultatai.append()
        # self.receptai = rezultatai


        # for receptas in self.receptai:
        #     if receptas == recepto_pav:
        #         self.receptai.remove(receptas.pavadinimas)
        #         return True
        # return False
# 2 užduotis
# Sukurkite metodą gauti_receptus_pagal_zodi(), kuris grąžina sąrašą receptų, kurių pavadinimuose yra nurodytas žodis.
# patikrinkite ar metodas veikia tinkamai, parašydami unit testą
    def gauti_receptus_pagal_zodi(self, zodis):
        return [receptas.pavadinimas for receptas in self.receptai if zodis in receptas.pavadinimas]
# 3 užduotis
# Sukurkite metodą gauti_bendra_ruosimo_laika(), kuris grąžina visų receptų bendrą ruošimo laiką.
# patikrinkite ar metodas veikia tinkamai, parašydami unit testą


    def gauti_bendra_ruosimo_laika(self):
        laiku_sarasas = [receptas.paruosimo_laikas for receptas in self.receptai]
        return sum(laiku_sarasas)
    
    def atrinti_pagal_ingredintus(self, ingredientas= 'bulvės'):
        atrinkti = []
        for receptas in self.receptai:
            for produktas in receptas.ingridientu_sarasas:
                if produktas == ingredientas:
                    atrinkti.append(receptas)
                    break
        return atrinkti


# 4 užduotis
# Pridėkite metodą isvalyti_receptus(), kuris išvalytų visus receptus iš sąrašo.
# patikrinkite ar metodas veikia tinkamai, parašydami unit testą

    def isvalyti_receptus(self):
        self.receptai = []