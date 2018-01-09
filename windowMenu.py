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
		cmdEmpty = self.menu.register(self.cmdEmpty)
		ToolMenu = Menu(self.menu, tearoff=0)
		ToolMenu.add_command(label="Codon Table", command=cmdEmpty)
		self.menu.add_cascade(label="File", menu=ToolMenu)

	def cmdEmpty(self):
		print(1)

	def openFastaFile(self):
		a = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("fasta files","*.fasta"),("all files","*.*")))
		f=open(a)
		contenu=f.read()
		CleanContenu = self.fastaConvert(contenu)[1]
		self.seq = CleanContenu
		print(self.seq)
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