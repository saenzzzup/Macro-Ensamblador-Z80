
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
			self.get_label(True)
			self.get_operands()
			#Si son opcodes con un operando

			if self.num_ope == 1:
				#Si son opcodes de brinco
				if self.instruction == "JP":
					self.instruction = self.instruction + " " + "nn"
					size = mne.map_mnem.get(self.instruction,"Error")(True,"0000")

				elif self.instruction == "JR":
					self.instruction = self.instruction + " " + "e"
					size = mne.map_mnem.get(self.instruction,"Error")(True,"0000")

				elif self.operands[0].isdigit():
					self.instruction = self.instruction + " "+"n"
					size = mne.map_mnem.get(self.instruction,"Error")(True,"0000")

				elif self.operands[0][:3] in mne.v_ops:
					self.instruction = self.instruction + " " + self.operands[0]
					size = mne.map_mnem.get(self.instruction,"Error")(True)

				else:
					self.instruction = self.instruction + " "+"n"
					size = mne.map_mnem.get(self.instruction,"Error")(True,"0000")

				
				self.cl += size

			elif self.num_ope == 2:
				aux = self.operands[0]
				aux2 = self.operands[1]
				band = False

				if self.operands[0][:4] == "(IX+":
					aux = "(IX+d)"
					band = True

				elif self.operands[0][:4] == "(IY+":
					aux = "(IY+d)"
					band = True

				elif self.operands[0][1:-1].isalnum():
					aux = "(nn)"
					band = True

				if self.instruction == "JP":
					aux2 = "nn"
					band = True

				elif self.instruction == "JR":
					aux2 = "e"
					band = True

				elif self.instruction in mne.v_jump:
					aux2 = "nn"
					band = True

				elif self.operands[1].isdigit():
					aux2 = "n"
					band = True

				elif self.operands[1][1:-1].isalnum():
					aux2 = "(nn)"
					band = True

				self.instruction = self.instruction + " " +aux+","+aux2

				if band:
					size = mne.map_mnem.get(self.instruction,"Error")(True,"0000")
				else:
					size = mne.map_mnem.get(self.instruction,"Error")(True)

				self.cl += size

			else:
				print("Error")

		print(self.TS)

	#Segunda Pasada
	def Second_pass(self):
		num = "00"

		for line in self.fileLines:
			self.clean_line(line)
			self.get_label(False)
			self.get_operands()
			
			if self.num_ope == 1:
				if self.instruction in mne.v_jump:
					if self.instruction == "JP":
						x = str(self.TS.get(self.operands[0],None))
						x = num[len(x):] + x
						if x == "000None":
							print("Error")
						else:
							self.instruction = self.instruction + " " + "nn"
							code = mne.map_mnem.get(self.instruction,"Error")(False,x[2:]+x[:-2])

				elif self.operands[0].isdigit():
					self.instruction = self.instruction + " "+"n"
					code = mne.map_mnem.get(self.instruction,"Error")(False,num[len(self.operands[0]):]+self.operands[0])

				elif self.operands[0][:3] in mne.v_ops:
					self.instruction = self.instruction + " " + self.operands[0]
					code = mne.map_mnem.get(self.instruction,"Error")(False)

				else:
					x = str(self.TS.get(self.operands[0],None))
					self.instruction = self.instruction + " "+"n"
					code = mne.map_mnem.get(self.instruction,"Error")(False,x)


				self.CO.append(code)

			elif self.num_ope == 2:
				aux = self.operands[0]
				aux2 = self.operands[1]
				dire = ""
				dire2 = ""

				if self.operands[0][:4] == "(IX+":
					aux = "(IX+d)"
					dire = self.operands[0][4:-2]
					dire = dire[2:]+dire[:-2]

				elif self.operands[0][:4] == "(IY+":
					aux = "(IY+d)"
					dire = self.operands[0][4:-2]
					dire = dire[2:]+dire[:-2]

				elif self.operands[0][1:-1].isalnum():
					aux = "(nn)"
					dire = self.operands[0][1:-2]
					dire = dire[2:]+dire[:-2]
				

				if self.instruction == "JP":
					aux2 = "nn"
					dire2 = self.TS[self.operands[1]]
					dire2 = dire2[2:]+dire2[:-2]

				elif self.instruction == "JR":
					aux2 = "e"
					dire2 = self.TS[self.operands[1]]
					dire2 = dire2[2:]+dire2[:-2]

				elif self.operands[1].isdigit():
					aux2 = "n"
					dire2 = self.operands[1]

				elif self.operands[1][1:-1] in self.TS.keys():
					aux2 = "(nn)"
					dire2 = self.TS[self.operands[1][1:-1]]
					dire2 = dire2[2:]+dire2[:-2]

				elif self.operands[1][1:-1].isalnum():
					aux2 = "(nn)"
					dire2 = self.operands[0][1:-2]
					dire2 = dire2[2:]+dire2[:-2]

				
				self.instruction = self.instruction + " " +aux+","+aux2
				if dire != "" or dire2 != "":
					code = mne.map_mnem.get(self.instruction,"Error")(False,dire+dire2)

				else:
					code = mne.map_mnem.get(self.instruction,"Error")(False)
					
				self.CO.append(code) 

				
		print(self.CO)


	#Quitar Comentarios
	def clean_line(self,line):
		line = line.split(";")
		if line[0] != "":
			self.instruction = line[0].replace(","," ")

	# Obtener y guardar etiqueta si existe
	def get_label(self,first_pass):
		num = "0000"
		label = self.instruction.split(":")

		if len(label) > 1:

			if label[0] in mne.v_ops or label[0] in mne.map_mnem:
				print("Error etiqueta invalida")

			if first_pass:
				if label[1].strip()[:3] == "EQU":
					aux = label[1][5:]
					aux = num[len(aux)+2:]+aux
				else:
					aux = hex(self.cl).upper().replace("X","")
					aux = num[len(aux):]+aux

				self.TS[label[0].strip()] = aux

			del label[0]


		self.instruction = label[0]

	#Obtener los operandos y la instruccion
	def get_operands(self):
		line = self.instruction.split()
		self.operands = [operand for operand in line]
		if len(self.operands) > 0:
			self.instruction = self.operands[0]
			del self.operands[0]
			self.num_ope = len(self.operands)

		
	
aux = Ensambler("1.txt")
aux.leerArchivo()
aux.first_pass()
aux.Second_pass()

