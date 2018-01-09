from tkinter import *

class dnaPresentator(Frame):

	def __init__(self, root=None):
		Frame.__init__(self, root)
		self.root = root
		self.presentator = Text(root)
		self.createPresentator()
		self.seq = ""

	def createPresentator(self):
		self.scrollBar = Scrollbar(self)
		self.scrollBar.grid(row=0, column=1, sticky=N+S+E)

		self.Seq = Text(self, width=60, heigh=10, state=DISABLED, yscrollcommand=self.scrollBar.set)
		self.scrollBar.config(command=self.Seq.yview)
		self.Seq.grid(row=0, column=0, sticky=N+S+E+W)

	def getDNA(self):
		seq= self.Seq.get(1.0, END)
		seq=seq.strip(" \n")
		return seq

	def newDNA(self, event):
		print("NEW DNA")
		self.seq=event.widget.getDNA()
		self.Seq["state"]=NORMAL
		self.Seq.delete("0.0", END)
		self.Seq.insert(INSERT, self.seq)
		self.Seq["state"]=DISABLED
		self.event_generate("<<updateDNA>>")
