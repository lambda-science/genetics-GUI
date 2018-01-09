#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from src.countNucleotidFunction import *

class nucCounter(Frame):

	def __init__(self, root=None):
		Frame.__init__(self, root)
		self.root = root
		self.presentator = Text(root)
		self.createPresentator()

	def createPresentator(self):
		self.ACount = StringVar()
		labelA = Label(self, text="A")
		labelA.grid(column=3, row=0)
		LabelCountA = Label(self, textvariable=self.ACount)
		LabelCountA.grid(column=4, row=0)

		self.TCount = StringVar()
		labelT = Label(self, text="T")
		labelT.grid(column=5, row=0)
		LabelCountT = Label(self, textvariable=self.TCount)
		LabelCountT.grid(column=6, row=0)

		self.CCount = StringVar()
		labelC = Label(self, text="C")
		labelC.grid(column=3, row=1)
		LabelCountC = Label(self, textvariable=self.CCount)
		LabelCountC.grid(column=4, row=1)

		self.GCount = StringVar()
		labelG = Label(self, text="G")
		labelG.grid(column=5, row=1)
		LabelCountG = Label(self, textvariable=self.GCount)
		LabelCountG.grid(column=6, row=1)

	def onUpdateDnaSequenceEvent(self, event):
		seq=event.widget.getDNA()
		a = countAcidNuc(seq)
		self.ACount.set(a["A"])
		self.TCount.set(a["T"])
		self.CCount.set(a["C"])
		self.GCount.set(a["G"])
