
import mnemonicos as mne


class Ensambler(object):

	"""Clase encargada de hacer las dos pasadas para el ensamblado chip z80.
		Attributes:
			fileName  	(str)  		: Nombre del archivo a ensamblar
			fileLines 	(list) 		: Archivo cargado en Memoria
			cl 		  	(int)  		: Contador de localidades
			size 	  	(int)  		: Tamaño del Archivo
			instruction (str)  		: Instruccion en la linea actual del archivo
			dir_in_c 	(str)		: Dirección de inicio de carga
			dir_in_e 	(str)		: Dirección de inicio de ejercución
			list_cl 	(list)		: Lista de contador de localidades
			terms 		(list)		: Lista de terminos de la instrucción
			TS 			(HashTable) : Tabla de simbolos
			CO 			(list)		: Codigo Objeto
			valid 		(boolean)	: Variable booleana para confirmar que la primera pasada se completo
			valid_sintx (boolean)	: Variable booleana	para confirmar la sintaxis de la instrucción
			"""

	def __init__(self, fileName):
		""" Args:
				fileName (str): Nombre de archivo .ASM a ensamblar
		"""
		self.fileName = fileName
		self.fileLines = []
		self.cl = 0
		self.size = 0
		self.dir_in_c = ""
		self.dir_in_e = ""
		self.instruction = ""
		self.list_cl = []
		self.terms = []
		self.TS = {}
		self.CO = []
		self.valid = True
		self.valid_sintx = True

	""" 
	Abrir documento y cargar a memoria, elimina espacios en blanco y tabulaciónes

	"""
	def leerArchivo(self):
		file = open(self.fileName, "r")
		for line in file:
			line = line.replace("\n", "")
			line = line.replace("\t", "")
			self.fileLines.append(line)
		file.close()

	""" 
	Primera pasada del ensamblador.
	Actualiza el contador de localidades
	LLena tabla de simbolos para su traducción

	"""
	def first_pass(self):
		for line in self.fileLines:
			self.clean_line(line)
			self.get_label(True)
			if self.valid_sintx:
				num_ter = self.get_terms()
				op1 = ""
				op2 = ""
				band = False

				if self.dir_in_e == "":
					if self.instruction in mne.v_op:
						aux =  hex(self.cl)[2:].upper()
						aux = "0000"[len(aux):] + aux
						self.dir_in_e = aux

				if num_ter == 2:
					op1 = self.terms[0]
					op2 = self.terms[1]

					if self.terms[0] in  mne.v_ops and self.terms[1] in  mne.v_ops:
						op1 = self.terms[0]
						op2 = self.terms[1]

					elif self.terms[0][:4] == "(IX+":
						op1 = "(IX+d)"
						band = True

					elif self.terms[0][:4] == "(IY+":
						op1 = "(IY+d)"
						band = True

					elif self.terms[0][1:-1].isalnum():
						op1 = "(nn)"
						band = True

					elif self.terms[1].isdigit():
						op2 = "n"
						band = True

					elif self.instruction == "JP" or self.instruction == "CALL":
						op2 = "nn"
						band = True

					elif self.instruction == "JR":
						op2 = "e"
						band = True

					elif self.terms[1][1:-1].isalnum():
						op2 = "(nn)"
						band = True

					elif self.terms[1].isalnum():
						op2 = "nn"
						band = True

					self.instruction = self.instruction + " " + op1 + "," + op2

				elif num_ter == 1:
					op1 = self.terms[0]

					if self.terms[0] in  mne.v_ops:
						op1 = self.terms[0]

					elif self.instruction == "JP" or self.instruction == "CALL":
						op1 = "nn"
						band = True
						
					elif self.instruction == "JR" or self.instruction == "DJNZ":
						op1 = "e"
						band = True

					elif self.terms[0].isalnum():
						op1 = "n"
						band = True

					self.instruction = self.instruction + " " + op1

				elif num_ter > 2:
					print("Error numero de terminas mayor a 2")
					self.valid = False
					break

				print(self.instruction)
				if band:
					size = mne.map_mnem.get(self.instruction,"Error")(True,"0000")
				else:
					size = mne.map_mnem.get(self.instruction,"Error")(True)
				
				aux =  hex(self.cl)[2:].upper()
				self.list_cl.append("0000"[len(aux):] + aux)
				self.cl += size

			else:
				self.valid = False
				break


		self.size = hex(self.cl-1)[2:]
		self.dir_in_c = self.list_cl[0]
		self.CO.append(self.size)
		self.CO.append(self.dir_in_c)
		print(self.TS)
		print(self.list_cl)

	""" 
	Segunda pasada del ensamblador.
	Calcula el codigo de cada instrucción
	Optiene el codigo objeto

	"""
	def Second_pass(self):
		num = "00"
		cont = 2
		if self.valid:
			for line in self.fileLines:
				self.clean_line(line)
				self.get_label(False)
				if self.valid_sintx:
					num_ter = self.get_terms()

					if num_ter == 2:
						aux = self.terms[0]
						aux2 = self.terms[1]
						dire = ""
						dire2 = ""

						if self.terms[0][1:-1] in self.TS.keys():
							aux = "(nn)"
							dire = self.TS[self.terms[0][1:-1]]
							dire = dire[2:]+dire[:-2]

						if self.terms[0] in  mne.v_ops and self.terms[1] in  mne.v_ops:
							aux = self.terms[0]
							aux2 = self.terms[1]

						elif self.terms[0][:4] == "(IX+":
							aux = "(IX+d)"
							dire = self.terms[0][4:-2]
							dire = dire[2:]+dire[:-2]

						elif self.terms[0][:4] == "(IY+":
							aux = "(IY+d)"
							dire = self.terms[0][4:-2]
							dire = dire[2:]+dire[:-2]

						elif self.terms[0][1:-1].isalnum():
							aux = "(nn)"
							dire = self.terms[0][1:-2]
							dire = dire[2:]+dire[:-2]

						elif self.terms[1].isdigit():
							aux2 = "n"
							dire2 = self.terms[1]

						elif self.terms[1][1:-1] in self.TS.keys():
							aux2 = "(nn)"
							dire2 = self.TS[self.terms[1][1:-1]]
							dire2 = dire2[2:]+dire2[:-2]

						elif self.terms[1] in self.TS.keys():
							aux2 = "nn"
							dire2 = self.TS[self.terms[1]]

						elif self.instruction == "JP":
							aux2 = "nn"
							dire2 = self.TS[self.terms[1]]
							dire2 = dire2[2:]+dire2[:-2]

						elif self.instruction == "JR":
							aux2 = "e"
							dire2 = self.TS[self.terms[1]]
							direnew = int(dire2,16)
							direact = int(str(self.list_cl[cont+1]),16)
							dire2 = direnew-direact
							if dire2 < 0:
								dire2 =bin(dire2)[3:]
								dire2 = "00000000"[len(dire2):] + dire2
								pos = 0
								dire1 = ""
								for char in dire2:
									if char == '0':
										dire1 += '1'
									else:
										dire1 += dire2[pos:]
										break
									pos+=1

								dire2 = (hex(int(dire1[:4],2))[2:] + hex(int(dire1[4:],2))[2:]).upper()
							else:
								dire2 = hex(dire2)[2:]

						elif self.terms[1][1:-1].isalnum():
							aux2 = "(nn)"
							dire2 = self.terms[0][1:-2]
							dire2 = dire2[2:]+dire2[:-2]

						self.instruction = self.instruction + " " + aux + "," + aux2

						if dire != "" or dire2 != "":
							code = mne.map_mnem.get(self.instruction,"Error")(False,dire+dire2)

						else:
							code = mne.map_mnem.get(self.instruction,"Error")(False)

					elif num_ter == 1:
						aux = self.terms[0]
						dire = ""

						if self.terms[0][1:-1] in self.TS.keys():
							aux = "(nn)"
							dire = self.TS[self.terms[0][1:-1]]
							dire = dire[2:]+dire[:-2]

						if self.terms[0] in  mne.v_ops:
							aux = self.terms[0]

						elif self.terms[0][:4] == "(IX+":
							aux = "(IX+d)"
							dire = self.terms[0][4:-2]
							dire = dire[2:]+dire[:-2]

						elif self.terms[0][:4] == "(IY+":
							aux = "(IY+d)"
							dire = self.terms[0][4:-2]
							dire = dire[2:]+dire[:-2]

						elif self.terms[0][1:-1].isalnum():
							aux = "(nn)"
							dire = self.terms[0][1:-2]
							dire = dire[2:]+dire[:-2]

						elif self.instruction == "DL":
							x = str(self.TS.get(self.terms[0],None))

						elif self.instruction == "JP":
							aux = "nn"
							dire = str(self.TS.get(self.terms[0],None))
							dire = dire[2:]+dire[:-2]

						elif self.instruction == "JR":
							aux2 = "e"
							dire = self.TS[self.terms[0]]
							direnew = int(dire2,16)
							direact = int(str(self.list_cl[cont+1]),16)
							dire = direnew - direact
							if dire2 < 0:
								dire2 =bin(dire2)[3:]
								dire2 = "00000000"[len(dire2):] + dire2
								pos = 0
								dire1 = ""
								for char in dire2:
									if char == '0':
										dire1 += '1'
									else:
										dire1 += dire2[pos:]
										break
									pos+=1

								dire = (hex(int(dire1[:4],2))[2:] + hex(int(dire1[4:],2))[2:]).upper()
							else:
								dire = hex(dire2)[2:]

						elif self.terms[0][1:-1].isalnum():
							aux = "(nn)"
							dire = self.terms[0][1:-2]
							dire = dire[2:]+dire[:-2]
						
						elif self.terms[0].isdigit():
							aux = "n"
							dire = "00"[len(self.terms[0]):]+self.terms[0]

						
						self.instruction = self.instruction + " "+ aux

						if dire != "":
							code = mne.map_mnem.get(self.instruction,"Error")(False,dire)
						else:
							code = mne.map_mnem.get(self.instruction,"Error")(False)

					if num_ter == 0:
						code = mne.map_mnem.get(self.instruction,"Error")(False)

					self.CO.append(code)
					cont += 1

				else:
					self.valid = False
					break
		else:
			print("Error en la primera pasada no completada")

		self.CO.append(self.dir_in_e)
		print(self.CO)


	"""
	Quitar comentarios de la linea y dejar solo la instrucción
		
	"""
	def clean_line(self,line):
		line = line.split(";")
		if line[0] != "":
			self.instruction = line[0].replace(","," ")
		else:
			self.valid_sintx = False

	"""
	Obtener etiqueta si es definición y almacenarla en la tabla de simbolos
	Separar la intrucción de la etiqueta
		
	"""
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
					aux = hex(self.cl).upper()[2:]
					aux = num[len(aux):]+aux

				if label[0].strip() in self.TS:
					print("Error valor repetido en la tabla")
					self.valid_sintx = False

				else:
					self.TS[label[0].strip()] = aux

			del label[0]

		self.instruction = label[0]


	"""
	Obtener los terminos y la instrucción
		
	"""
	def get_terms(self):
		line = self.instruction.split()
		self.terms = [operand for operand in line]
		if len(self.terms) > 0:
			self.instruction = self.terms[0]
			del self.terms[0]
		return len(self.terms)

	
aux = Ensambler("1.txt")
aux.leerArchivo()
aux.first_pass()
aux.Second_pass()
fileOut = open ("1.co", "w+")
for line in aux.CO:
	fileOut.write(line)
fileOut.close()
