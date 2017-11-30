# -*- coding: utf-8 -*-
import io
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
		self.valid_sintx = True

	""" 
	Abrir documento y cargar a memoria, elimina espacios en blanco y tabulaciónes

	"""
	def leerArchivo(self):
		file = io.open(self.fileName, encoding='latin-1')

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
		fileLines = filter(lambda a: a != "", self.fileLines)
		for line in fileLines:
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
						op1 = "(IX + d)"
						band = True

					elif self.terms[0][:4] == "(IY+":
						op1 = "(IY + d)"
						band = True

					elif self.terms[0][1:-1].isalnum():
						op1 = "(NN)"
						band = True

					elif self.instruction == "JP" or self.instruction == "CALL":
						op2 = "NN"
						op1 = op1.upper()
						band = True

					elif self.instruction == "JR":
						op2 = "e"
						op1 = op1.upper()
						band = True

					elif self.terms[1][:4] == "(IX+":
						op2 = "(IX + d)"
						band = True

					elif self.terms[1][:4] == "(IY+":
						op2 = "(IY + d)"
						band = True

					elif self.terms[1][1:-1].isalnum() and self.terms[1][:1] == "(":
						op2 = "(NN)"
						band = True

					elif self.terms[1].isalnum() and len(self.terms[0]) == 2:
						op2 = "NN"
						band = True

					elif self.terms[1].isalnum():
						op2 = "N"
						band = True
					
					self.instruction = self.instruction + " " + op1 + ", " + op2
					
				elif num_ter == 1:
					op1 = self.terms[0]

					if self.terms[0] in  mne.v_ops:
						op1 = self.terms[0]

					elif self.instruction == "JP" or self.instruction == "CALL":
						op1 = "NN"
						band = True
						
					elif self.instruction == "JR" or self.instruction == "DJNZ":
						op1 = "e"
						band = True

					elif self.terms[0][:4] == "(IX+":
						op1 = "(IX + d)"
						band = True

					elif self.terms[0][:4] == "(IY+":
						op1 = "(IY + d)"
						band = True


					elif self.terms[0][1:-1].isalnum() and self.terms[0][:1] == "(":
						op1 = "(NN)"
						band = True

					elif self.terms[0].isalnum():
						op1 = "N"
						band = True

					self.instruction = self.instruction + " " + op1

				elif num_ter > 2:
					messag = "Error numero de terminas mayor a 2"
					raise Exception(messag)

				try:
					if band:
						size = mne.map_mnem.get(self.instruction,None)(True,"0000")
					else:
						size = mne.map_mnem.get(self.instruction,None)(True)
				except Exception as ex:
					messag = "Error intruccion desconocida: " +line+ "\n Verifique la intruccion o los terminos a operar"
					raise Exception(messag)

				if size == None:
					messag = "Error intruccion desconocida \n Verifique la intruccion o los terminos a operar"
					raise Exception(messag)
			
				aux =  hex(self.cl)[2:].upper()
				self.list_cl.append("0000"[len(aux):] + aux)
				self.cl += size

			else:
				messag = "Error en sitaxis: " + line
				raise Exception(messag)


		aux = hex(self.cl-1)[2:].upper()
		self.size = "00"[len(aux):] + aux
		self.dir_in_c = self.list_cl[0]
		self.CO.append(self.size)
		self.CO.append(self.dir_in_c)

	""" 
	Segunda pasada del ensamblador.
	Calcula el codigo de cada instrucción
	Optiene el codigo objeto

	"""
	def Second_pass(self):
		num = "00"
		cont = 0
		fileLines = filter(lambda a: a != "", self.fileLines)
		for line in fileLines:
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
							aux = "(NN)"
							dire = self.TS[self.terms[0][1:-1]]
							dire = dire[2:]+dire[:-2]

						elif self.terms[0] in  mne.v_ops and self.terms[1] in  mne.v_ops:
							aux = self.terms[0]
							aux2 = self.terms[1]

						elif self.terms[0][:4] == "(IX+":
							aux = "(IX + d)"
							dire = self.terms[0][4:-2]

						elif self.terms[0][:4] == "(IY+":
							aux = "(IY + d)"
							dire = self.terms[0][4:-2]

						elif self.terms[0][1:-1].isalnum():
							aux = "(NN)"
							dire = self.terms[0][1:-2]
							dire = dire[2:]+dire[:-2]

						elif self.instruction == "JP":
							aux2 = "NN"
							aux = aux.upper()
							dire2 = self.TS[self.terms[1]]
							dire2 = dire2[2:]+dire2[:-2]

						elif self.instruction == "JR":
							aux2 = "e"
							aux = aux.upper()
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

						elif self.terms[1][:4] == "(IX+" or self.terms[1][:2] == "IX":
							aux2 = "(IX + d)"
							dire2 = self.terms[1][4:-1]

						elif self.terms[1][:4] == "(IY+" or self.terms[1][:2] == "IY":
							aux2 = "(IY + d)"
							dire2 = self.terms[1][4:-1]

						elif self.terms[1][1:-1] in self.TS.keys():
							aux2 = "(NN)"
							dire2 = self.TS[self.terms[1][1:-1]]
							dire2 = dire2[2:]+dire2[:-2]

						elif self.terms[1] in self.TS.keys() and self.instruction == "LD":
							aux2 = "N"
							dire2 = self.TS[self.terms[1]]

						elif self.terms[1] in self.TS.keys():
							aux2 = "(NN)"
							dire2 = self.TS[self.terms[1]]

						elif self.terms[1].isdigit():
							aux2 = "N"
							dire2 = self.terms[1]

						elif self.terms[1][1:-1].isalnum() and self.terms[1][:1] == "(":
							aux2 = "(NN)"
							dire2 = self.terms[1][1:-2]
							dire2 = dire2[2:]+dire2[:-2]

						elif self.terms[1].isalnum():
							aux2 = "NN"
							dire2 = self.terms[1][:-1]
							dire2 = dire2[2:]+dire2[:-2]

						self.instruction = self.instruction + " " + aux + ", " + aux2
						
						try:
							if dire != "" or dire2 != "":
								code = mne.map_mnem.get(self.instruction,None)(False,dire+dire2)

							else:
								code = mne.map_mnem.get(self.instruction,None)(False)
						except Exception as ex:
							messag = "Error intruccion desconocida: " +line+ "\n Verifique la intruccion o los terminos a operar"
							raise Exception(messag)

				elif num_ter == 1:
						aux = self.terms[0]
						dire = ""

						if self.terms[0][1:-1] in self.TS.keys():
							aux = "(NN)"
							dire = self.TS[self.terms[0][1:-1]]
							dire = dire[2:]+dire[:-2]

						elif self.instruction == "JP":
							aux = "NN"
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


						elif self.terms[0] in self.TS.keys():
							aux = "N"
							dire = self.TS[self.terms[0]]

						elif self.terms[0] in  mne.v_ops:
							aux = self.terms[0]

						elif self.terms[0][:4] == "(IX+":
							aux = "(IX + d)"
							dire = self.terms[0][4:-2]

						elif self.terms[0][:4] == "(IY+":
							aux = "(IY + d)"
							dire = self.terms[0][4:-1]

						elif self.instruction == "DL":
							aux = "NN"
							dire = self.list_cl[cont]
							self.TS[self.terms[0].strip()] = dire


						elif self.terms[0][1:-1].isalnum():
							aux = "(NN)"
							dire = self.terms[0][1:-2]
							dire = dire[2:]+dire[:-2]
						
						elif self.terms[0].isdigit():
							aux = "N"
							dire = "00"[len(self.terms[0]):]+self.terms[0]

						self.instruction = self.instruction + " "+ aux


						try:
							if dire != "":
								code = mne.map_mnem.get(self.instruction,None)(False,dire)
							else:
								code = mne.map_mnem.get(self.instruction,None)(False)
						except Exception as ex:
							messag = "Error intruccion desconocida: " +line+ "\n Verifique la intruccion o los terminos a operar"
							raise Exception(messag)

				if num_ter == 0:
					try:
						code = mne.map_mnem.get(self.instruction,None)(False)
					except Exception as ex:
						messag = "Error intruccion desconocida: " +line+ "\n Verifique la intruccion o los terminos a operar"
						raise Exception(messag)

				if code == None:
					messag = "Intruccion desconocida: " + self.intruccion + "\nError en la primera pasada no completada"
					raise Exception(messag)

				self.CO.append(code)
				cont += 1

			else:
				messag = "Intruccion desconocida: " + line + "\nError en la primera pasada no completada"
				raise Exception(messag)

		self.CO.append(self.dir_in_e)

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
				messag = "Error etiqueta invalida"
				raise Exception(messag)

			if first_pass:
				if label[1].strip()[:3] == "EQU":
					aux = label[1][5:]
					aux = num[len(aux)+2:]+aux

				else:
					aux = hex(self.cl).upper()[2:]
					aux = num[len(aux):]+aux

				if label[0].strip() in self.TS:
					messag = "Error valor repetido en la tabla"
					raise Exception(messag)

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

