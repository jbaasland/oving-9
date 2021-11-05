# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:42:11 2021

@author: Johannes
"""

class quizlager:
	def __init__(self, q, a, alt):
		self.q = q
		self.a = a
		self.alt = alt
	def __str__(self):
		resultat = self.q
		for i, alternativ in enumerate(self.alt):
			resultat += f"\n{i}: {alternativ}"
		return resultat
	def sjekk_svar(self, ans):
		if ans == self.a:
			return True
		else:
			return False
	def korrekt_svar_tekst(self):
		answer = self.alt[self.a]
		return f"Riktig svar er {answer}"
		
def qfunction():
	qlist = []
	with open("sporsmaalsfil.txt") as questions:
		for i, qs in enumerate(questions):
			splitqs = qs.split(":")
			questions = splitqs[0].strip()
			answer = int(splitqs[1].strip())
			alternatives = splitqs[2].strip("][\n ")
			alternatives = alternatives.split(", ")
			qlist.append(quizlager(questions, answer, alternatives))
	return qlist

if __name__ == "__main__":
    spiller1poeng = 0
    spiller2poeng = 0
    qlista = qfunction()
    for i in range(len(qlista)):
        print(qlista[i])
        print("\n")
        fortsetter = True
        while fortsetter == True:
            try:
                spiller1input = int(input("Spiller 1 svar: "))
                spiller2input = int(input("Spiller 2 svar: "))
                fortsetter = False
            except ValueError:
                print("Int ok takk :)")
        if qlista[i].sjekk_svar(spiller1input) == True:
            spiller1poeng += 1
            print("\nSpiller 1 korrekt")
        else:
            print("\nSpiller 1 feil")
        if qlista[i].sjekk_svar(spiller2input) == True:
            spiller2poeng += 1
            print("Spiller 2 korrekt\n")
        else:
            print("Spiller 2 feil\n")
        print(qlista[i].korrekt_svar_tekst())
    print("\nSpiller 1 har " + str(spiller1poeng) + " poeng")
    print("Spiller 2 har " + str(spiller2poeng) + " poeng \n")