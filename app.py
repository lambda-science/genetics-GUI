from tkinter import *
from windowMenu import *
from dnaPresentator import *
from dnaGen import *
from dnaTranslation import *
from nucleotidCounter import *
from dnaConv import *


root = Tk()

menuBar = windowMenuBar(root)
menuBar.grid()

frameFirst = Frame()
frameFirst.grid(row=0)
dnaGen = dnaGen(frameFirst)
nucCount = nucCounter(frameFirst)
dnaGen.grid(row=0)
nucCount.grid(row=0, column=1)

frameTop = Frame()
frameTop.grid(row=1)
dnaPresenter = dnaPresentator(frameTop)
dnaPresenter.grid(row=0)

frameConv = Frame()
frameConv.grid(row=2)
dnaConv = dnaConv(frameConv)
dnaConv.grid(row=0)

frameThird=Frame()
frameThird.grid(row=3, sticky=N+S+E+W)
dnaTrans = dnaTrans(frameThird)
dnaTrans.grid(row=0)

root.bind_all("<<newDNA>>", dnaPresenter.newDNA)
root.bind_all("<<updateDNA>>", nucCount.onUpdateDnaSequenceEvent)
root.bind_all("<<updateDNA>>", dnaConv.onUpdateDnaSequenceEvent, add="+")
root.bind_all("<<updateProt>>", dnaTrans.onUpdateProtEvent)

root.mainloop()