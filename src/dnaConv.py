#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

class dnaConv(Frame):

	def __init__(self, root=None):
		Frame.__init__(self, root)
		self.root = root
		self.presentator = Text(root)
		self.createPresentator()
		self.seq = ""

	def createPresentator(self):
		self.titre = Label(self, text="Sequence d'ADN")
		self.titre.grid(row = 0, column=0, sticky=W)

		self.comp = IntVar()
		self.reverse = IntVar()

		self.menuframe = Frame(self)
		self.menuframe.grid(row=0)
		Checkbutton(self.menuframe, text="Complementaire", variable=self.comp, command=self.updateSeq).grid(row=0, column=1, sticky = E)
		Checkbutton(self.menuframe, text="Inverse", variable=self.reverse, command=self.updateSeq).grid(row=0, column=2, sticky = E)
		
		self.textframe = Frame(self)
		self.textframe.grid(row=1)
		self.scrollBar = Scrollbar(self.textframe)
		self.scrollBar.grid(row=1, column=1, sticky=N+S+E)
		self.Seq = Text(self.textframe, width=60, heigh=10, state=DISABLED, yscrollcommand=self.scrollBar.set)
		self.scrollBar.config(command=self.Seq.yview)
		self.Seq.grid(row=1, column=0, sticky=N+S+E+W)

	def onUpdateDnaSequenceEvent(self, event):
		self.seq=event.widget.getDNA()
		self.Seq["state"]=NORMAL
		self.Seq.delete("0.0", END)
		self.Seq.insert(INSERT, self.seq)
		self.Seq["state"]=DISABLED
		self.event_generate("<<updateProt>>")

	def updateSeq(self):
		self.Seq["state"]=NORMAL
		self.Seq.delete("0.0", END)
		if self.comp.get() == 1 and self.reverse.get() == 1:
			self.Seq.insert(INSERT, self.reverseSeq(self.complementarySeq(self.seq)))
		elif self.comp.get() == 1:
			self.Seq.insert(INSERT, self.complementarySeq(self.seq))
		elif self.reverse.get() == 1:
			self.Seq.insert(INSERT, self.reverseSeq(self.seq))
		else:
			self.Seq.insert(INSERT, self.seq)
		self.Seq["state"]=DISABLED
		self.event_generate("<<updateProt>>")

	def complementarySeq(self, seq):
		codeComplementaire = {"A":"T", "T":"A", "G":"C", "C":"G"}
		complementarySeq = [ codeComplementaire[i] for i in seq ]
		return ''.join(complementarySeq)
	
	def reverseSeq(self, seq):
		return seq[::-1]
			
	def getDNA(self):
		seq= self.Seq.get(1.0, END)
		seq=seq.strip(" \n")
		return seq