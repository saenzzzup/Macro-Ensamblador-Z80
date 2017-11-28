# -*- coding: utf-8 -*-
import tkinter as tk
import os, errno
from tkinter import filedialog

from macros import Macros

def macroEnsamblar():
	
	filename = filedialog.askopenfilename() #Agregar excepcion
	vuelta = 0

	directory = filename[:filename.rfind("/")] + "/outMacro/"

	try:
		os.makedirs(directory)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

	mac = Macros(filename)
	mac.leerArchivo()
	mac.addMacros()
	mac.generarArchivo(directory + "out"+ str(vuelta) +".txt")
	writeTablesText(mac, directory+str(vuelta))
	filename = directory + "out"+ str(vuelta) +".txt"
	vuelta += 1

	while(mac.existsNestedMacro):
		mac = Macros(filename)
		mac.leerArchivo()
		mac.addMacros()
		mac.generarArchivo(directory + "out"+ str(vuelta) +".txt")
		writeTablesText(mac, directory+str(vuelta))
		filename = directory + "out"+ str(vuelta) +".txt"
		vuelta += 1

def ensamblar():
	pass

def writeTablesText(mac, filename):
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

class MainApplication:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)

		self.meButton = tk.Button(master, text="Macroensamblar", command = macroEnsamblar)

		self.enButton = tk.Button(master, text="Ensamblar", command = ensamblar)

		self.meButton.config(height = 5, width = 20)
		self.meButton.grid(row = 0, column = 0, padx = 5, pady = 5)
		self.enButton.config(height = 5, width = 20)
		self.enButton.grid(row = 0, column = 1, padx = 5, pady = 5)

		self.meButton.pack()
		self.enButton.pack()
		self.frame.pack()

	def close_windows(self):
		self.master.destroy()

if __name__ == "__main__":
	root = tk.Tk()
	root.title("Macro-Ensamblador")
	app = MainApplication(root)
	root.mainloop()


