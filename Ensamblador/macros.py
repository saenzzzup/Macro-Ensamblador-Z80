# -*- coding: utf-8 -*-
import re

class Macros(object):
    
    def __init__(self, fileName):
        self.existsNestedMacro = False
        self.fileName = fileName
        self.nameMacro = ""
        self.fileLines = []
        self.fileLinesProgram = []
        self.fileLinesOut = []
        self.MDT = {}
        self.MDTList = []
        self.MNT = {}
        self.ALA = {}
    
    def leerArchivo(self):
        file = open(self.fileName, "r")
        for line in file:
            line = line.replace("\n", "")
            line = line.replace("\t", "")
            self.fileLines.append(line)
        self.fileLines = filter(lambda a: a != "", self.fileLines)
        file.close()
      
    def addMacros(self):
        count = 0
        isInMacro = False
        
        for line in self.fileLines:
            if ("MACRO" in line):
                if (count == 0):
                    self.addALA(line)
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
        if self.nameMacro not in self.MDT:
            self.MDT[self.nameMacro] = []
            self.MDTList.append(self.nameMacro)
            line = line.replace("MACRO", "")

        self.MDT[self.nameMacro].append(line)
  
    def addALA(self, line):
        macroDefine = line.split()
        self.nameMacro = macroDefine[0][:-1]
        self.ALA[self.nameMacro] = {}
        if (len(macroDefine)>2):
            for val in macroDefine[2:]:
                val = val.replace(",", "")
                self.ALA[self.nameMacro][val] = None

    def createMNT(self):
        counterAMDT = 1
        counterAALA = 1
        for key in self.MDTList:
            self.MNT[key] = [counterAMDT,counterAALA]
            counterAMDT += len(self.MDT[key])
            counterAALA += len(self.ALA[key])

    #SEGUNDA PASADA
    def generarArchivo(self, newName):
        inInicio = False
        hasDefinition = False
        
        for line in self.fileLinesProgram:
            if "INICIO" in line:
                inInicio = True
                
            if "END INICIO" in line:
                inInicio = False
                self.fileLinesOut.append(line)
            
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
        
        for line in self.MDT[macroSearch][1:]:
            for key in self.ALA[macroSearch].keys():
                if key in line:
                    line = line.replace(key, self.ALA[macroSearch][key]) #REEMPLAZAR ARGUMENTO FORMAL POR ACTUAL EN LINEA
            self.fileLinesOut.append(line)
