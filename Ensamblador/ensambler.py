
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
		self.TS = {}
		# Codigo Objeto
		self.CO = []
		#Aux
		self.x = 0

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
			if self.num_ope == 1:
				if self.instruction in mne.v_jump:
					if self.instruction == "JP":
						self.x = self.TS[operands[0]]
						print("l")
						print(self.x)


				if self.operands[0] in mne.v_jump:
					self.instruction = self.instruction + " " + self.operands[0]+","+self.operands[1]

				if self.operands[0][1:-1].isnumeric():
					self.instruction = self.instruction + " " + self.operands[0]+","+self.operands[1]


				if self.num_ope == 1:
					if self.instruction in mne.v_jump:
						self.operands[0] = "nn"
						self.instruction = self.instruction + " " + self.operands[0]
						code, size = mne.map_mnem.get(self.instruction,"Error")("0000")
						self.cl += size 
			else:
				
			#Valida si no es opcode valido
				print(self.instruction)
			#code, size = mne.map_mnem.get(self.instruction,"Error")()
			
			#lst = "CL: " + str(self.cl) + " Code: " + code
			#self.CO.append(code)
		print(self.CO)
		print(self.cl)
		print(self.TS)


	def Second_pass(self):
		for line in self.fileLines:
			self.clean_line(line)
			self.get_label()
			self.get_operands()
			
			if self.instruction in mne.v_jump:

				if len(self.operands) == 2:
					aux = self.operands[1]
				else:
					aux = self.operands[0]

				if aux in self.TS.keys():
					self.x = self.TS[aux]
					self.instruction = self.instruction + " " + "nn"
					code, size = mne.map_mnem.get(self.instruction,"Error")(str(self.x))
					self.CO.append(code)

				else:
					print("Error")
			else:
				if self.num_ope == 2:
					self.instruction = self.instruction + " " + self.operands[0]+","+self.operands[1]
				if self.num_ope == 1:
					self.instruction = self.instruction + " " + self.operands[0]
				code, size = mne.map_mnem.get(self.instruction,"Error")()
				self.CO.append(code)
		print(self.CO)


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
			#Quitar espacio al inicio
			self.TS[label[0].strip()] = self.cl

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
aux.Second_pass()

