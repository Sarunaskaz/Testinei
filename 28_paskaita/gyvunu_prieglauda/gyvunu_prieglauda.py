from datetime import datetime

class Gyvunas: #sklaiusteliai nebutini klasei jeigu nieko nepaveldi
    def __init__(self, metai, rusis, vardas, svoris):
        self.metai = metai
        self.rusis = rusis
        self.vardas = vardas
        self.svoris = svoris
        self.amzius = self.apskaiciuoti_amziu(metai)

    def apskaiciuoti_amziu(self,metai):
        today = datetime.now()
        return today.year - metai

class GyvunuPrieglauda:
    def __init__(self):
        self.gyvunai = []

    def prideti_gyvuna(self, gyvunas):
        self.gyvunai.append(gyvunas)

    def pagal_svori(self, svoris):
        return [gyvunas for gyvunas in self.gyvunai if gyvunas.svoris == svoris]
    
    def gauti_pagal_rusis(self,rusis):
        return [gyvunas for gyvunas in self.gyvunai if gyvunas.rusis == rusis ]
        