# -*- coding: utf-8 -*-
"""
Som del av et spørrespill skal du lage en klasse for
flervalgspørsmål (hele spillet er muligens øving 9 og 10).
Et flervalgspørsmål skal ha en spørsmålstekst, ei liste med
svaralternativer (hvert svaralternativ er en tekststreng), og
et tall som sier hvilket av svaralternativene som er korrekt.
Klassen skal ha en __str__ metode som returnerer en streng som
inneholder spørsmålsteksten og nummerte svaralternativer på et
lett leselig format. Klassen skal ha en sjekk_svar metode som
tar som parameter et heltall som representerer hvilket svar
brukeren velger. Sjekk_svar metoden skal sjekke om svaret
brukeren har oppgitt er korrekt.

for c
to personer skal spille så to forskjellige svar og
riktig/feil

se på fil enkelt_kortspill

youtube building a multiple choice quiz python tutorial 32
mike dane
mangler sjekk svar
"""
class quiz:
    def __init__(self, spor, svaralt, svar):
        self.spor = spor
        self.svaralt = svaralt
        self.svar = svar
    def __str__(self):
        return f"{self.spor}{self.svaralt}"
    def sjekk_svar(self, svar):
        if svar == self.svar:
            return True
        else:
            return False
        

sporsmaal = [
    "Hvor mange maaneder har 28 dager?\n",
    "Inneholder melkeveien melk?\n",
    "For Mount Everest ble oppdaget, hvilket fjell var det hoyeste?\n"
]

svaralternativene = [
    "(1) 1\n(2) 12\n(3) 6\n\n",
    "(1) Ja\n(2) Nei\n(3) Pass\n\n",
    "(1) Olympus Mons\n(2) K2\n(3) Mount Everest\n\n"
]

svarene = [2, 1, 3]

spurt = 0
spiller1poeng = 0
spiller2poeng = 0
for sporsmaalet in sporsmaal:
    spiller1 = quiz(sporsmaal[spurt], svaralternativene[spurt], svarene[spurt])
    print(spiller1)
    spiller1riktig = spiller1.sjekk_svar(int(input("Spiller 1 svar: ")))
    if spiller1riktig == True:
        spiller1poeng += 1
    spiller2 = quiz(sporsmaal[spurt], svaralternativene[spurt], svarene[spurt])
    print(spiller2)
    spiller2riktig = spiller2.sjekk_svar(int(input("Spiller 2 svar: ")))
    if spiller2riktig == True:
        spiller2poeng += 1
    spurt += 1
print("Spiller 1 har " + str(spiller1poeng) + " poeng")
print("Spiller 2 har " + str(spiller2poeng) + " poeng")