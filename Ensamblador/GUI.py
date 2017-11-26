# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog

from macros import Macros

master = Tk()

def macroEnsamblar():
	
	filename = filedialog.askopenfilename() #Agregar excepcion
	vuelta = 0
	
	mac = Macros(filename)
	mac.leerArchivo()
	mac.addMacros()
	mac.generarArchivo("out"+ str(vuelta) +".txt")
	imprimirMDT(mac, filename)
	imprimirMNT(mac, filename)
	imprimirALA(mac, filename)
	filename = "out"+ str(vuelta) +".txt"
	vuelta += 1

	while(mac.existsNestedMacro):
		mac = Macros(filename)
		mac.leerArchivo()
		mac.addMacros()
		mac.generarArchivo("out"+ str(vuelta) +".txt")
		imprimirMDT(mac, filename)
		imprimirMNT(mac, filename)
		imprimirALA(mac, filename)
		filename = "out"+ str(vuelta) +".txt"
		vuelta += 1

def ensamblar():
	pass

def imprimirMDT(mac, filename):
	tablaMDT = open(filename + "MDT", "w+")
	contador = 1

	tablaMDT.write("CMDT\tCUERPO\n")
	for name in mac.MDTList:
		for line in mac.MDT[name]:
			tablaMDT.write(str(contador) + "\t" + line + "\n")
			contador += 1
	tablaMDT.close()

def imprimirMNT(mac, filename):
	tablaMNT = open(filename + "MNT", "w+")
	contador = 1

	tablaMNT.write("CMNT\tNOMBRE\tAMDT\tAALA\n")
	for name in mac.MDTList:
		tablaMNT.write(str(contador) + "\t" + name + "\t" +str(mac.MNT[name][0]) + "\t" + str(mac.MNT[name][1]) + "\n")
		contador += 1
	tablaMNT.close()

def imprimirALA(mac, filename):
	tablaALA = open(filename + "ALA", "w+")
	contador = 1
	tablaALA.write("CALA\tARG FORMAL\tARG ACTUAL\n")

	for name in mac.MDTList:
		for arg in mac.ALA[name]:
			tablaALA.write(str(contador) + "\t" + arg + "\t" + mac.ALA[name][arg] + "\n")
			contador += 1
	tablaALA.close()

#Botones
meButton = Button(master, text="Macroensamblar", command = macroEnsamblar)
meButton.config(height = 5, width = 20)
meButton.grid(row = 1, column = 0, padx = 5, pady = 5)


enButton = Button(master, text="Ensamblar", command = ensamblar)
enButton.config(height = 5, width = 20)
enButton.grid(row = 1, column = 1, padx = 5, pady = 5)

#imprimirMDT()
mainloop()

