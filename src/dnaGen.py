#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from random import choice

class dnaGen(Frame):

	def __init__(self, root=None):
		Frame.__init__(self, root)
		self.root = root
		self.presentator = Text(root)
		self.createPresentator()
		self.seq = ""

	def createPresentator(self):

		label = Label(self, text="Longeur de la chaine")
		label.grid(column=1, row=0, sticky=W)

		value = IntVar(value="100") 
		entry = Entry(self)
		ValidCommand = (entry.register(self.valideCmd), "%S")
		InvalidCommand = (entry.register(self.invalideCmd), "%S")
		entry = Entry(self, width = 10)
		entry['textvariable']=value
		entry['validate']="key",
		entry['validatecommand']=ValidCommand
		entry['invalidcommand']=InvalidCommand
		entry.grid(column=2, row=0)

		gen = Button(self, text="Génerer", command=lambda: self.generate(value))
		gen.grid(column=0, row=0)

	def generate(self, size):
		""" Function that generate a random DNA sequence, generate newDNA event"""
		s = []
		adn =["A","T","C","G"]
		for i in range(size.get()):
			s.append(choice(adn))
		self.seq = ''.join(s)
		self.event_generate("<<newDNA>>")

	def getDNA(self):
		return self.seq 

	def valideCmd(self, a):
		"""Function made to verify if the entry is a number"""
		if a.isdigit():
			return True
		else:
			return False

	def invalideCmd(self, a):
		""" Generate a windows error box if the entry is not a number"""
		t = Toplevel(self)
		Label(t, text="Erreur: entrée invalide").pack()
		Button(t, text="OK", command=t.destroy).pack()