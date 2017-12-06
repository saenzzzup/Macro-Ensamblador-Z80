import mnemonicos as mne

class Assembler(object):

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
	"""

	def __init__(self, fileName):
		""" Args:
				fileName (str): Nombre de archivo .ASM a ensamblar
		"""
		self.fileName = fileName
		self.fileLines = []
		self.cl = 0
		self.dir_in_e = ""
		self.size = 0
		self.dir_in_c = ""
		self.instruction = ""
		self.operands = []
		self.label = ""
		self.list_cl = []
		self.TS = {}
		self.CO = []
		self.band = False

	""" 
	Abrir documento y cargar a memoria, elimina espacios en blanco y tabulaciónes

	"""
	def leerArchivo(self):
		file = open(self.fileName, "r")
		for line in file:
			line = line.replace("\n", "")
			line = line.replace("\t", "")
			if len(line) > 0:
				self.fileLines.append(line)
		file.close()

	""" 
	Primera pasada del ensamblador.
	Actualiza el contador de localidades
	LLena tabla de simbolos para su traducción

	"""
	def first_pass(self):
		num_line = 1
		for line in self.fileLines:
			self.sintax_line(line,num_line)
			self.partition_line(line,num_line)
			self.set_table_symbols(num_line)
			self.valid_instruction(num_line)
			self.valid_operands(num_line)
			self.band = False

			if self.dir_in_e == "":
				if self.instruction not in mne.v_directives:
					aux =  hex(self.cl)[2:].upper()
					self.dir_in_e = "0000"[len(aux):] + aux

			if len(self.operands) == 2:
				op1 = self.get_type_operand(self.operands[0])	
				op2 = self.get_type_operand(self.operands[1])
				op2 = ", "+op2

			elif len(self.operands) == 1:
				op1 = self.get_type_operand(self.operands[0])
				op2 = ""

			ints = (self.instruction + " " + op1 + op2).strip()
			size = mne.map_mnem.get(ints,None)

			if size == None:
				messag = "Error en la instrucción de la linea "+ str(num_line) +"\n Verifique que los terminos a operar sean los permitidos"
				raise Exception(messag)

			else:
				if self.band:
					if self.instruction in mne.mne_aux and (op2 == ", (IX + d)" or op2 == ", (IY + d)"):
						size = size(True,self.operands[0],"0000")
					else:
						size = size(True,"0000")
				else:
					size = size(True)

			num_line +=1
			aux = hex(self.cl)[2:].upper()
			aux = "0000"[len(aux):] + aux
			self.list_cl.append(aux)
			self.cl += size

		self.size = aux
		self.dir_in_c = self.list_cl[0]
		
	""" 
	Segunda pasada del ensamblador.
	Calcula el codigo de cada instrucción
	Optiene el codigo objeto

	"""
	def Second_pass(self):
		num_line = 1
		for line in self.fileLines:
			self.sintax_line(line,num_line)
			self.partition_line(line,num_line)
			self.band = False

			if len(self.operands) == 2:
				op1 = self.get_type_operand(self.operands[0])
				op2 = self.get_type_operand(self.operands[1])

				if self.instruction == "JR":
					dire = self.get_JR_dire(self.operands[1],num_line)

				else:
					dire = self.get_dire(self.operands[0],op1,num_line)
					dire += self.get_dire(self.operands[1],op2,num_line)

				op2 = ", "+op2

			elif len(self.operands) == 1:
				op1 = self.get_type_operand(self.operands[0])
				op2 = ""

				if self.instruction == "JR":
					dire = self.get_JR_dire(self.operands[0],num_line)

				else:
					dire = self.get_dire(self.operands[0],op1,num_line)

			ints = (self.instruction + " " + op1 + op2).strip()
		
			code = mne.map_mnem.get(ints,None)

			if code == None:
				messag = "Error en la instrucción de la linea "+ str(num_line) +"\n Verifique que los terminos a operar sean los permitidos"
				raise Exception(messag)

			else:
				if self.band:
					if self.instruction in mne.mne_aux and (op2 == ", (IX + d)" or op2 == ", (IY + d)"):
						code = code(False,self.operands[0],dire)
					else:
						code = code(False,dire)
				else:
					code = code(False)

			num_line +=1
			self.CO.append(code)

	"""
		Optener la dirección o el valodr de la etiquetas y/o de las constantes definidas cuando la intrucción es JR
	"""
	def get_JR_dire(self,op,num_line):
		dire = self.TS[op]
		direnew = int(dire,16)
		direact = int(str(self.list_cl[num_line]),16)
		dire = direnew - direact
		#Complemento a 2
		if dire < 0:
			num_line = 0
			dire = bin(dire)[3:]
			dire = "00000000"[len(dire):] + dire
			dire1 = ""
			for char in dire:
				if char == '0':
					dire1 += '1'
				else:
					dire1 += dire[num_line:]
					break
				num_line+=1
			dire = (hex(int(dire1[:4],2))[2:] + hex(int(dire1[4:],2))[2:]).upper()
		else:
			dire = hex(dire)[2:]

		return dire

	"""
		Optener la dirección o el valodr de la etiquetas y/o de las constantes definidas  
	"""
	def get_dire(self,op,op_1,num_line):
		dire = ""
		if op not in mne.v_ops:
			if op_1 == "(IX + d)" or op_1 ==  "(IY + d)":
				dire = op[4:-2]

			elif op_1 == "(NN)":
				if op[1:-1] in self.TS.keys():
					dire = self.TS[op[1:-1]]

				elif op[1:-1].isalnum():
					dire = "00"[len(op):] + op[1:-2]

				else:
					messag = "Error, la etiqueta de la linea " + str(num_line) + " nunca fue definida."
					raise Exception(messag)

			elif op_1 == "NN":
				if op in self.TS.keys():
					dire = self.TS[op]

				elif op.isalnum():
					dire = "00"[len(op):] + op[:-1]

				else:
					messag = "Error, la etiqueta de la linea " + str(num_line) + " nunca fue definida."
					raise Exception(messag)

			elif op_1 == "N":
				dire = "00"[len(op):] + op

		if len(dire)>3:
			dire = dire[2:]+dire[:-2]

		return dire

	"""
		Optener el tipo de operando que es, si es un registro,numero o una dirección.
	"""
	def get_type_operand(self,op):
		if op not in mne.v_ops:
			self.band = True
			if op[:4] == "(IX+":
				op = "(IX + d)"
			elif op[:4] == "(IY+":
				op = "(IY + d)"
			elif op[:1] == "(":
				op = "(NN)"
			elif op == "":
				self.band = False
			elif op.isdigit():
				op = "N"
			elif op.isalnum():
				op = "NN"
			else:
				op = ""
		return op

	"""
		Agregar a la tabla de simbolos la etiqueta y validar que no sea una palabra reservada.
	"""
	def set_table_symbols(self,num_line):
		if self.label != "":

			if self.label not in mne.v_ops:

				if self.label not in mne.v_mnemonicos:

					if self.label not in self.TS:

						if self.instruction == "EQU":
							self.TS[self.label] = self.operands[0]

						else:
							aux = hex(self.cl).upper()[2:]
							self.TS[self.label] = "0000"[len(aux):]+aux

					else:
						messag = "Error, la etiqueta de la linea " + str(num_line) + " ya fue definida."
						raise Exception(messag)

				else:
					messag = "Error, la etiqueta de la linea " + str(num_line) +" no puede ser ningun mnemonico\ndebido a que son palabras reservadas, cheque el manual para conocer las palabras reservadas."
					raise Exception(messag)
			else:
				messag = "Error, la etiqueta de la linea " + str(num_line)+ " no puede ser ningun operando\ndebido a que son palabras reservadas, cheque el manual para conocer las palabras reservadas"
				raise Exception(messag)

	"""
		Validar que exista la intrucción.
	"""
	def valid_instruction(self,num_line):
		if self.instruction not in mne.v_mnemonicos:
			messag = "Error, la intrucción de la linea " + str(num_line)  + " no es valida"
			raise Exception(messag)

	"""
		Validar sintaxis de los operandos.
	"""
	def valid_operands(self,num_line):
		for operand in self.operands:
			if operand not in mne.v_ops:
				if "(" in operand and ")" not in operand:
					messag = "Error, el operando "+ operand + " ,de la instrucción de la linea " + str(num_line)  + " le faltan parentesis."
					raise Exception(messag)
				elif "(" not in operand and ")" in operand:
					messag = "Error, el operando "+ operand + " ,de la instrucción de la linea " + str(num_line)  + " le faltan parentesis."
					raise Exception(messag)


	"""
		Obtener la etiqueta, la intruccion y los operandos de la linea recibida.
	"""
	def partition_line(self,line,num_line):

		line = (line.split(";")[0]).split(":")

		if len(line) == 2:
			self.label = line[0].strip()
			line = line[1]

		elif len(line) == 1:
			self.label = ""
			line = line[0]

		line = line.replace(", ",",").replace(" ,",",").strip()

		num = line.find(" ")

		if num == -1:
			num = len(line)

		self.instruction = line[:num]

		line = line[num:].strip()

		self.operands = line.split(",")

	"""
		Validar que la sintaxis de la linea sea correcta.
		Que no haya más de una definición de una etiqueta en la linea recibida.
	"""
	def sintax_line(self,line,num_line):
		num_eti = (line.split(";")[0]).count(":")

		if num_eti == 1:
			line = line.split(":")
			if line[0] == "":
				messag = "Error, la etiqueta de la intrucción de la linea " + str(num_line) + ", está vacia."
				raise Exception(messag)

		elif num_eti != 0:
			messag = "Error en la linea " + str(num_line) + ", existe más de un definición de etiqueta."
			raise Exception(messag)

	"""	
		Imprime en un archivo con terminación .Tco  una tabla que contiene el codigo objeto y el 
		contador de localidades que le correponde a cada instrucción.
	"""
	def print_tabla(self):
		tabla = open(self.fileName[:-4] + ".Tco", "w+")
		contador = 1
		tabla.write("Tabla:\nLinea\t\t  CO\t\t CL\t\t   Intrucción\n")
		for co in self.CO:
			if len(co) >= 8:
				tabla.write(str(contador) + "\t\t" + co + "\t" + str(self.list_cl[contador-1]) + "\t\t" + str(self.fileLines[contador-1]) + "\n")
			else:
				tabla.write(str(contador) + "\t\t" + co + "\t\t" + str(self.list_cl[contador-1]) + "\t\t" + str(self.fileLines[contador-1]) + "\n")
			
			contador += 1

		tabla.write("\nTabla de Simbolos:\nNombre\t\tValor\n")
		for valor in self.TS:
			tabla.write(valor + "\t\t" +self.TS[valor]+"\n")

		print("Tabla Creada")
		tabla.close()

	"""	
		Imprime en un archivo con terminación .co el codigo objeto.
	"""
	def print_co(self):
		codigo_objeto = open(self.fileName[:-4] + ".co", "w+")
		self.CO.insert(0,str(self.size))
		self.CO.insert(1,self.dir_in_c)
		self.CO.append(self.dir_in_e)
		for co in self.CO:
			codigo_objeto.write(co)
		print("Codigo Objeto Creada")
		codigo_objeto.close()


aux = Assembler("8.txt")
aux.leerArchivo()
aux.first_pass()
aux.Second_pass()
aux.print_tabla()
aux.print_co()