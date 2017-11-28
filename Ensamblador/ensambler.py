
#from tkinter import Tk, Text, INSERT
import mnemonicos as mne


class Ensambler(object):


	def __init__(self, fileName):
	
		#Nombre del archivo
		self.fileName = fileName
		#Lineas del Archivo
		self.fileLines = []
		#Contador de Localidades
		self.cl = 0
		#Tamaño
		self.size = 0
		#Opcode
		self.code = ""
		#Intruccion
		self.instruction = ""
		#Contador de operadores
		self.num_ope = 0
		#Operandos
		self.operands = []
		# Tabla de simbolos
		self.TS = []
		# Codigo Objeto
		self.LST = []

		#self.window = Tk()
		#self.window.geometry('400x50')

	def leerArchivo(self):
		file = open(self.fileName, "r")
		for line in file:
			line = line.replace("\n", "")
			line = line.replace("\t", "")
			self.fileLines.append(line)
		file.close()

	#Primera Pasada
	def first_pass(self):
		for line in self.fileLines:
			self.clean_line(line)
			self.get_label()
			self.get_operands()
			#Aqui lo que hare en ves de la cadena Error hara que se llame una funcion que regre None en caso de que 
			# no exista el opcode y envie un mensaje en pantalla
			self.code, self.size = mne.map_mnem.get(self.instruction,"Error")(self.operands,self.num_ope,True)
			print(self.size)
			self.cl += self.size 
			lst = {"CL": self.cl, "Code": self.code}
			self.LST.append(lst)
		print(self.LST)


	#Quitar Comentarios
	def clean_line(self,line):
		line = line.split(";")
		self.instruction = line[0].upper().replace(",","")

	# Obtener y guardar etiqueta si existe
	def get_label(self):

		label = self.instruction.split(":")

		if len(label) > 1:

			if label[0] in mne.v_ops or label[0] in mne.map_mnem:
				print("Error etiqueta invalida")

			element_TS = { "Nombre": label[0], "Valor": str(hex(self.cl)), "Def": "Si"}

			self.TS.append(element_TS)

			del label[0]

		self.instruction = label[0]

	#Obtener los operandos y la instruccion
	def get_operands(self):
		line = self.instruction.split()
		self.operands = [operand for operand in line]
		self.instruction = self.operands[0]
		del self.operands[0]
		self.num_ope = len(self.operands)

		
		




aux = Ensambler("1.txt")
aux.leerArchivo()
aux.first_pass()