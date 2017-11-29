# -*- coding: utf-8 -*-
import re

class Macros(object):
    """Clase encargada de hacer las dos pasadas para el macroensamblado chip Z80.

    Attributes:
        existsNestedMacro (Boolean): Muestra si existen macros dentro de macros.
        fileName (str): nombre del archivo a macroensamblar.
        fileLines (list): Archivo cargado a memoria
        fileLinesProgram (list): Archivo sin nemonicos
        fileLinesOut (list): Archivo con nemonicos traucidos
        MDT (hashTable): Guarda los Macros a traducir
        MDTList (list): Para conocer el orden de la MDT
        MNT (hashTable): Une a la ALA y MDT
        ALA (hashTable): Guarda valores de atributos de los Macros
    """
    def __init__(self, fileName):
        """
        Args:
            fileName (str): Nombre de archivo .ASM a ensamblar

        """
        self.existsNestedMacro = False
        self.fileName = fileName
        self._nameMacro = ""
        self.fileLines = []
        self.fileLinesProgram = []
        self.fileLinesOut = []
        self.MDT = {}
        self.MDTList = []
        self.MNT = {}
        self.ALA = {}
        self.__conditions = {}
        self.__temp = ("Null", None)
    
    def leerArchivo(self):
        """
        Abrir documento y cargar a memoria, elimina espacios en blanco y tabulaciónes
        """
        file = open(self.fileName, "r")
        for line in file:
            line = line.replace("\n", "")
            line = line.replace("\t", "")
            self.fileLines.append(line)
        self.fileLines = filter(lambda a: a != "", self.fileLines) #Elimina lineas vaciás
        file.close()
      
    def addMacros(self):
        """Primera pasada del macro ensamblador.
            Revisa donde se encuentran las Macro definiciónes.
            LLena tablas para su traducción
        """
        count = 0
        isInMacro = False
        
        for line in self.fileLines:
            if ("MACRO" in line):
                if (count == 0):
                    self.addALA(line) #Primer Macro NO anidado
                count += 1

                if line.split()[0].replace(":", "") in self.MDT.keys():
                    messag = "Más de una definición de una Macro con el mismo nombre: " + line.split()[0].replace(":", "")
                    raise Exception(messag)
                 
            if ("MEND" in line):
                count -= 1

            isInMacro = True if count > 0 else False
            if (isInMacro): 
                if("MACRO" in line) and count > 1:
                    self.existsNestedMacro = True #Existen Macros anidadas por expandir
                self.addMDT(line)
            else:
                if ("MEND" not in line): 
                    self.fileLinesProgram.append(line)

        if count != 0:
            messag = "Faltan Macros por cerrar"
            raise Exception(messag)

        self.createMNT()
    
    def addMDT(self, line):
        """Añade codigo del Macro a la tabla segun el nombre de su intrución.
        Args:
            line: linea que se añadira a la tabla.
        """
        if self._nameMacro not in self.MDT:
            self.MDT[self._nameMacro] = []
            self.MDTList.append(self._nameMacro)
            line = line.replace("MACRO", "")

        self.MDT[self._nameMacro].append(line)
  
    def addALA(self, line):
        """Añade argumentos del Macro a la tabla segun el nombre de su intrución.
        Args:
            line: linea donde se encuentran los argumentos
        """
        macroDefine = line.split()
        self._nameMacro = macroDefine[0][:-1]
        self.ALA[self._nameMacro] = {}
        if (len(macroDefine)>2):
            for val in macroDefine[2:]:
                val = val.replace(",", "")
                self.ALA[self._nameMacro][val] = None

    def createMNT(self):
        """Crea la tabla MNT para la visual¡zación final
        """
        counterAMDT = 1
        counterAALA = 1
        for key in self.MDTList:
            self.MNT[key] = [counterAMDT,counterAALA]
            counterAMDT += len(self.MDT[key])
            counterAALA += len(self.ALA[key])

    #SEGUNDA PASADA
    def generarArchivo(self, newName):
        """Genera el archivo final macro ensamblado.
        Args:
            newName: nuevo nombre del archivo .ASM sin las Macros.
        """
        inInicio = False
        hasDefinition = False
        
        for line in self.fileLinesProgram:
            if "INICIO" in line:
                inInicio = True
                
            if "END INICIO" in line:
                inInicio = False
                self.fileLinesOut.append(line)

            if not inInicio:
                define = line.split()
                if "DL" in define:
                    if define[0][:-1] not in self.__conditions:
                        if define[2] == "TRUE":
                            self.__conditions[define[0][:-1]] = True
                        elif define[2] == "FALSE":
                            self.__conditions[define[0][:-1]] = False

            if (inInicio):
                for name in self.MDTList:

                    b = r'(\s|^|$)' 
                    temName = re.match(b + name + b, line, flags=re.IGNORECASE)

                    if bool(temName):
                        self.subsMacro(line)
                        hasDefinition = True

                if hasDefinition:
                    hasDefinition = False
                    continue 
                self.fileLinesOut.append(line)
        
        fileOut = open (newName, "w+")
        for line in self.fileLinesOut:
            fileOut.write(line + "\n")
        fileOut.close()
                
    def subsMacro(self, macro):
        """Al encontrar una llamada a una Macro sustituye por su valor de tablas
        Args:
            macro: Nombre de la macro que sera sustituida.
        """
        instruct = macro.split()
        macroSearch = instruct[0]
        
        if len(instruct) > 1:
            if (len(instruct)-1) != len(self.ALA[macroSearch]):
                messag = "Faltan argumentos en una macro"
                raise Exception(messag)
        
        args = self.MDT[macroSearch][0].split()[1:] #DEFINICION: #a1 #a2 #a3 ARGUMENTOS FORMALES
        
        for i in range(len(args)):
            formVal = args[i].replace(",", "")
            newVal = instruct[1:][i].replace(",", "")
            self.ALA[macroSearch][formVal] = newVal #DAR VALOR ACTUAL AL ARGUMENTO FORMAL
        
        inCondition = False
        condition = []

        for line in self.MDT[macroSearch][1:]:
            for key in self.ALA[macroSearch].keys():
                if key in line:
                    line = line.replace(key, self.ALA[macroSearch][key]) #REEMPLAZAR ARGUMENTO FORMAL POR ACTUAL EN LINEA

            if not inCondition:
                self.__conditions[self.__temp[0]] = self.__temp[1]

            if "IF " in line:
                inCondition = True
                condition = line.split()
                continue

            if "END IF" in line:
                inCondition = False
                continue

            if inCondition:
                if condition[-1] in self.__conditions:
                    if "NOT" in condition:
                        if self.__conditions[condition[-1]]:
                            continue
                    else:
                        if not self.__conditions[condition[-1]]:
                            continue

                define = line.split()

                if "DL" in define:
                    if define[2] == "TRUE":
                        self.__temp = (define[0][:-1] ,True)
                    elif define[2] == "FALSE":
                       self.__temp = (define[0][:-1], False)

            self.fileLinesOut.append(line)
