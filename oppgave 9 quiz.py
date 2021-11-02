# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:42:11 2021

@author: Johannes
"""

class quizlager:
    def __init__(self, q, a, alt):
        self.q = list()
        self.a = list()
        self.alt = list()
    def __str__(self):
        resultat = self.q
        for i, alternativ in enumerate(self.a):
            resultat += f"\n{i+1}: {alternativ}"
        return resultat
    def sjekk_svar(self, a):
        if a == self.a:
            return True
        else:
            return False
    def korrekt_svar_tekst(self):
        return self.alt[self.a]
        

qdict = {}
with open("sporsmaalsfil.txt") as questions:
    for i in questions:
        spliti = i.split(":")
        questions = spliti[0].strip()
        answer = int(spliti[1].strip())
        alternatives = spliti[2].strip("][\n ")
        print(alternatives)

            
            
"""
quiztest = quizlager(qs, ans, alts)
for i in enumerate(qs):
    print(quiztest)
if __name__ = "__main__"
"""