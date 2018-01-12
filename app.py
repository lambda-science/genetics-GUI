#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from src.windowMenu import *
from src.dnaPresenter import *
from src.dnaGen import *
from src.dnaTranslation import *
from src.nucleotidCounter import *
from src.dnaConv import *


root = Tk()
root.title("GUI-Genetics - Harajuku")

menuBar = windowMenuBar(root)
menuBar.grid()

frameDnaGen = Frame()
frameDnaGen.grid(row=0)
dnaGen = dnaGen(frameDnaGen)
nucCount = nucCounter(frameDnaGen)
dnaGen.grid(row=0)
nucCount.grid(row=0, column=1)

frameDnaPresenter = Frame()
frameDnaPresenter.grid(row=1)
dnaPresenter = dnaPresenter(frameDnaPresenter)
dnaPresenter.grid(row=0)

frameDnaConv = Frame()
frameDnaConv.grid(row=2)
dnaConv = dnaConv(frameDnaConv)
dnaConv.grid(row=0)

frameProt=Frame()
frameProt.grid(row=3, sticky=N+S+E+W)
dnaTrans = dnaTrans(frameProt)
dnaTrans.grid(row=0)

root.bind_all("<<newDNA>>", dnaPresenter.newDNA)
root.bind_all("<<updateDNA>>", nucCount.onUpdateDnaSequenceEvent)
root.bind_all("<<updateDNA>>", dnaConv.onUpdateDnaSequenceEvent, add="+")
root.bind_all("<<updateProt>>", dnaTrans.onUpdateProtEvent)

root.mainloop()