# -*- coding: utf-8 -*-
import tkinter as tk
import os, errno
from tkinter import filedialog

from macros import Macros
from ensambler import Ensambler

class PopUP:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.frame.pack()

	def addMessage(self, title, messag, scale = '400x50'):
		self.master.title(title)
		self.master.geometry(scale)
		self.text = tk.Text(self.frame)
		self.text.insert(tk.INSERT, messag)
		self.text.pack()

class MainApplication:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)

		self.leftFrame = tk.Frame(self.frame)
		self.rightFrame = tk.Frame(self.frame)
		self.bottomFrame = tk.Frame(self.frame)

		self.check = tk.IntVar()
		self.filename = ""
		self.directory = ""
		self.mac = None
		self.cicle = 0

		self.meButton = tk.Button(self.leftFrame, text="Macroensamblar", command = self.macroEnsamblar)
		self.enButton = tk.Button(self.rightFrame, text="Ensamblar", command = self.ensamblar)
		self.infoButton = tk.Button(self.bottomFrame, text="i", command = self.showInfo, fg="blue")

		self.meButton.config(height = 10, width = 20)
		self.enButton.config(height = 10, width = 20)
		self.infoButton.config(height = 1, width = 1)

		self.checkTables = tk.Checkbutton(self.leftFrame, text="Crear Tablas", variable = self.check, onvalue=1, offvalue=0)

		self.text = tk.Label(self.rightFrame, text= "® FI UNAM")
	
		self.meButton.pack()
		self.enButton.pack()
		self.infoButton.pack()
		self.checkTables.pack(side = tk.LEFT)
		self.text.pack(side = tk.RIGHT)	
		self.leftFrame.pack(side = tk.LEFT)
		self.rightFrame.pack(side = tk.RIGHT)
		self.bottomFrame.pack(side = tk.BOTTOM)
		self.frame.pack()

	def close_windows(self):
		self.master.destroy()

	def showInfo(self):
		self.newWindow = tk.Toplevel(self.master)
		self.pop = PopUP(self.newWindow)
		self.pop.addMessage("Información",
			"Proyecto Final FI UNAM 2018-1 \n" +
			"Ensamblador y macroensamblador de chip Z80\n" +
			"Creadores: \n"+
			"\t- Rodrigo Germán López \n" +
			"\t- Ricardo Hernández Gómez \n" +
			"\t- Omar Lemuz Fuentes\n" +
			"\t- Ricardo Sáenz Barragán \n" +
			"Materia: \n" +
			"\tEstructura y Programación de computadoras\n"+
			"Profesor encargado: \n" +
			"\t- Ing. Alberto Templos Carbajal\n" +
			"MIT License",
			scale = '400x300'
			)

	def fileOpener(self):
		self.filename = filedialog.askopenfilename() #Agregar excepcion
		if not self.filename:
			self.newWindow = tk.Toplevel(self.master)
			self.pop = PopUP(self.newWindow)
			self.pop.addMessage("Archivo", "No se seleccióno un archivo.")
			return

		if os.name == 'nt':
			self.directory = self.filename[:self.filename.rfind("\\")] + "\\Out\\"
		else:
			self.directory = self.filename[:self.filename.rfind("/")] + "/Out/"	

		try:
			os.makedirs(self.directory)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise

	def ensamblar(self):

		self.fileOpener()

		ens = Ensambler(self.filename)
		ens.leerArchivo()


		try:
			ens.first_pass()
			ens.Second_pass()
		except Exception as ex: 
			self.newWindow = tk.Toplevel(self.master)
			self.pop = PopUP(self.newWindow)
			self.pop.addMessage("Error", str(ex))
			return

		fileOut = open (self.directory + "out.co", "w+")
		for line in ens.CO:
			fileOut.write(line)
		fileOut.close()

	def macroEnsamblar(self):
	
		self.fileOpener()

		while(self.macroCicles()):
			self.filename = self.directory + "out"+ str(self.cicle) +".ASM"
			self.cicle += 1


		self.newWindow = tk.Toplevel(self.master)
		self.pop = PopUP(self.newWindow)
		self.pop.addMessage("Información",
			"Archivo .ASM creado en: \n" +
			self.directory)

	def macroCicles(self):
		mac = Macros(self.filename)
		mac.leerArchivo()

		try:
			mac.addMacros()
		except Exception as ex: 
			self.newWindow = tk.Toplevel(self.master)
			self.pop = PopUP(self.newWindow)
			self.pop.addMessage("Error", str(ex))
			return

		try:
			mac.generarArchivo(self.directory + "out"+ str(self.cicle) +".ASM")
		except Exception as ex: 
			self.newWindow = tk.Toplevel(self.master)
			self.pop = PopUP(self.newWindow)
			self.pop.addMessage("Error", str(ex))
			return

		if self.check.get() == 1:
			self.writeTablesText(mac, self.directory+str(self.cicle))
			self.filename = self.directory + "TableOut"+ str(self.cicle) +".txt"

		return mac.existsNestedMacro

	def writeTablesText(self, mac, filename):
		tableText = open(filename + "Tables.txt", "w+")
		count = 1
		tableText.write("CMNT\tNOMBRE\tAMDT\tAALA\n")
		for name in mac.MDTList:
			tableText.write(str(count) + "\t" + name + "\t" +str(mac.MNT[name][0]) + "\t" + str(mac.MNT[name][1]) + "\n")
			count += 1
		count = 1
		tableText.write("CMDT\tCUERPO\n")
		for name in mac.MDTList:
			for line in mac.MDT[name]:
				tableText.write(str(count) + "\t" + line + "\n")
				count += 1
		count = 1
		tableText.write("CALA\tARG FORMAL\tARG ACTUAL\n")
		for name in mac.MDTList:
			for arg in mac.ALA[name]:
				tableText.write(str(count) + "\t" + arg + "\t" + mac.ALA[name][arg] + "\n")
				count += 1
		tableText.close()

if __name__ == "__main__":
	root = tk.Tk()
	root.title("Macro-Ensamblador")
	app = MainApplication(root)
	root.mainloop()


