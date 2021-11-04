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
		for i, alternativ in enumerate(self.a):
			resultat += f"\n{i+1}: {alternativ}"
		return resultat
	def sjekk_svar(self, a):
		if a == self.a:
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
	qlista = qfunction()
	print(qlista[0].korrekt_svar_tekst())