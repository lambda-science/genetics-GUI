#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import filedialog
from tkinter.messagebox import *
from tkinter import *


class windowMenuBar(Frame):

	def __init__(self, root=None):
		Frame.__init__(self, root)
		self.root = root
		self.menu = Menu(root)
		self.createMenuBar()
		self.seq = ""
		root.config(menu=self.menu)

	def createMenuBar(self):
		self.createFileMenu()
		self.createToolMenu()

	def createFileMenu(self):
		FileMenu = Menu(self.menu, tearoff=0)
		openFile = self.menu.register(self.openFastaFile)
		exit = self.menu.register(self.exit)
		FileMenu.add_command(label="Open", command=openFile)
		FileMenu.add_command(label="Exit", command=exit)
		self.menu.add_cascade(label="File", menu=FileMenu)

	def createToolMenu(self):
		ToolMenu = Menu(self.menu, tearoff=0)
		ToolMenu.add_command(label="Codon Table", command=lambda: self.showCodonTable())
		self.menu.add_cascade(label="Tool", menu=ToolMenu)

	def showCodonTable(self):
		self.codonWindow = Toplevel(self)
		self.codonTable = Label(self.codonWindow, text="""
TTT F Phe      TCT S Ser      TAT Y Tyr      TGT C Cys  
TTC F Phe      TCC S Ser      TAC Y Tyr      TGC C Cys  
TTA L Leu      TCA S Ser      TAA * Ter      TGA * Ter  
TTG L Leu      TCG S Ser      TAG * Ter      TGG W Trp  

CTT L Leu      CCT P Pro      CAT H His      CGT R Arg  
CTC L Leu      CCC P Pro      CAC H His      CGC R Arg  
CTA L Leu      CCA P Pro      CAA Q Gln      CGA R Arg  
CTG L Leu      CCG P Pro      CAG Q Gln      CGG R Arg  

ATT I Ile      ACT T Thr      AAT N Asn      AGT S Ser  
ATC I Ile      ACC T Thr      AAC N Asn      AGC S Ser  
ATA I Ile      ACA T Thr      AAA K Lys      AGA R Arg  
ATG M Met      ACG T Thr      AAG K Lys      AGG R Arg  

GTT V Val      GCT A Ala      GAT D Asp      GGT G Gly  
GTC V Val      GCC A Ala      GAC D Asp      GGC G Gly  
GTA V Val      GCA A Ala      GAA E Glu      GGA G Gly  
GTG V Val      GCG A Ala      GAG E Glu      GGG G Gly""")
		self.codonTable.pack()

	def openFastaFile(self):
		a = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("fasta files","*.fasta"),("all files","*.*")))
		f=open(a)
		contenu=f.read()
		CleanContenu = self.fastaConvert(contenu)[1]
		self.seq = CleanContenu
		self.event_generate("<<newDNA>>")

	def getDNA(self):
		return self.seq

	def fastaConvert(self, fastaString):
	    endLineIndex = fastaString.index('\n')
	    title = fastaString[:endLineIndex]
	    sequence = fastaString[endLineIndex+1:]
	    sequence = sequence.replace("\n", "");
	    sequence = sequence.replace("\r", "");
	    return [title, sequence]

	def exit(self):
		showinfo("Alerte","Je quitte l'application")
		self.root.quit()