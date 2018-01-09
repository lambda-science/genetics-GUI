from tkinter import *

class dnaTrans(Frame):

	def __init__(self, root=None):
		Frame.__init__(self, root)
		self.root = root
		self.presentator = Text(root)
		self.createPresentator()
		self.seq = ""
		self.protSeq = ""

	def createPresentator(self):
		self.textframe = Frame(self)
		self.textframe.grid(row=1)
		self.scrollBar = Scrollbar(self.textframe)
		self.scrollBar.grid(row=0, column=1, sticky=N+S+E)

		self.Seq = Text(self.textframe, width=60, heigh=10, state=DISABLED, yscrollcommand=self.scrollBar.set)
		self.scrollBar.config(command=self.Seq.yview)
		self.Seq.grid(row=0, column=0, sticky=N+S+E+W)

		menuframe = Frame(self)
		menuframe.grid(row=0)
		self.cadreVar = IntVar()
		Radiobutton(menuframe, text="Cadre 0", variable=self.cadreVar, value=0, command=self.updateSeq).grid(row=0, column=0)
		Radiobutton(menuframe, text="Cadre 1", variable=self.cadreVar, value=1, command=self.updateSeq).grid(row=0, column=1)
		Radiobutton(menuframe, text="Cadre 2", variable=self.cadreVar, value=2, command=self.updateSeq).grid(row=0, column=2)


		self.numberLetterVar = IntVar()
		Radiobutton(menuframe, text="1 lettre", variable=self.numberLetterVar, value=0, command=self.updateSeq).grid(row=0, column=3)
		Radiobutton(menuframe, text="3 lettres", variable=self.numberLetterVar, value=1, command=self.updateSeq).grid(row=0, column=4)

	def onUpdateProtEvent(self, event):
		self.seq=event.widget.getDNA()
		self.protSeq = self.traduction(self.seq, self.cadreVar, self.numberLetterVar)
		self.Seq["state"]=NORMAL
		self.Seq.delete("0.0", END)
		self.Seq.insert(INSERT, self.protSeq)
		self.Seq["state"]=DISABLED

	def getProt(self):
		seq= self.Seq.get(1.0, END)
		seq=seq.strip(" \n")
		return seq

	def updateSeq(self):
		self.protSeq = self.traduction(self.seq, self.cadreVar, self.numberLetterVar)
		self.Seq["state"]=NORMAL
		self.Seq.delete("0.0", END)
		self.Seq.insert(INSERT, self.protSeq)
		self.Seq["state"]=DISABLED


	def traduction(self, sequence, cadre, lettre):
		codontable = {
	'ATA':['I','Ile'], 'ATC':['I','Ile'], 'ATT':['I','Ile'], 'ATG':['M','Met'],
	'ACA':['T','Thr'], 'ACC':['T','Thr'], 'ACG':['T','Thr'], 'ACT':['T','Thr'],
	'AAC':['N','Asn'], 'AAT':['N','Asn'], 'AAA':['K','Lys'], 'AAG':['K','Lys'],
	'AGC':['S','Ser'], 'AGT':['S','Ser'], 'AGA':['R','Arg'], 'AGG':['R','Arg'],
	'CTA':['L','Leu'], 'CTC':['L','Leu'], 'CTG':['L','Leu'], 'CTT':['L','Leu'],
	'CCA':['P','Pro'], 'CCC':['P','Pro'], 'CCG':['P','Pro'], 'CCT':['P','Pro'],
	'CAC':['H','His'], 'CAT':['H','His'], 'CAA':['Q','Gln'], 'CAG':['Q','Gln'],
	'CGA':['R','Arg'], 'CGC':['R','Arg'], 'CGG':['R','Arg'], 'CGT':['R','Arg'],
	'GTA':['V','Val'], 'GTC':['V','Val'], 'GTG':['V','Val'], 'GTT':['V','Val'],
	'GCA':['A','Ala'], 'GCC':['A','Ala'], 'GCG':['A','Ala'], 'GCT':['A','Ala'],
	'GAC':['D','Asp'], 'GAT':['D','Asp'], 'GAA':['E','Glu'], 'GAG':['E','Glu'],
	'GGA':['G','Gly'], 'GGC':['G','Gly'], 'GGG':['G','Gly'], 'GGT':['G','Gly'],
	'TCA':['S','Ser'], 'TCC':['S','Ser'], 'TCG':['S','Ser'], 'TCT':['S','Ser'],
	'TTC':['F','Phe'], 'TTT':['F','Phe'], 'TTA':['L','Leu'], 'TTG':['L','Leu'],
	'TAC':['Y','Tyr'], 'TAT':['Y','Tyr'], 'TAA':['*','***'], 'TAG':['*','***'],
	'TGC':['C','Cys'], 'TGT':['C','Cys'], 'TGA':['*','***'], 'TGG':['W','Trp']
	}
		sequenceCodon = [ sequence[j:j+3] for j in range(cadre.get(), len(sequence), 3) ]
		sequenceProteine = [ codontable[i][lettre.get()] for i in sequenceCodon if i in codontable ]
		return ''.join(sequenceProteine)