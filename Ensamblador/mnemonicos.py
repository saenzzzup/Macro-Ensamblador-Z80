

#Register 8 bits
r = {
	"B": "000",
	"C": "001",
	"D": "010",
	"E": "011",
	"H": "100",
	"L": "101",
	"A": "111",
}
#Register 16 bits
dd ={
	"BC": "00",
	"DE": "01",
	"HL": "10",
	"AF": "11",
}
#Register 16 bits
ss ={
"BC": "00",
"DE": "01",
"HL": "10",
"SP": "11",
}
#Register 16 bits
pp ={
"BC": "00",
"DE": "01",
"IX": "10",
"AF": "11",
}
#Register 16 bits
rr ={
"BC": "00",
"DE": "01",
"IY": "10",
"AF": "11",
}
#Flag Register
cc ={
"NZ": "000",
 "Z":  "001",
"NC": "010",
"C":  "011",
"PO": "100",
"PE": "101",
"P":  "110",
"M":  "111",
}
#Valid Operands
v_ops =[
"A","B","C","D","E","H","L","R","I","BC","DE","HL","AF","AF'","SP","IX","IY",
"NZ","Z","NC","C","PQ","PE","P","M","(HL)","(IX)","(IY)","(BC)","(DE)","(IY+",
"(IX+","(SP)","(C)"
]

#Opcodes Load
def LD(operand,op_count,first_pass):
	opcode = ""
	size = 0

	lds = { ""}
	if op_count < 2:
		print("error")

	elif op_count > 2:
		print("error")

	else:
		op1 = operand[0]
		op2 = operand[1]
		#Aqui son todos los casos que tiene LD 
		if op1 == "A":

			if op2 == "B":
				opcode = "78"
				size = 1
			elif op2 == "(BC)":
				opcode = "0A"
				size = 1
			elif op2 == "(HL)":
				opcode = "7E"
				size = 1




	return opcode,size

def PUSH(self,operand,op_count, first_pass):
	pass

def POP(self,operand,op_count, first_pass):
	pass

#Opcodes Exchange, Block Transfer & Block Search
def EX(self,operand,op_count, first_pass):
	pass

def EXX(self,operand,op_count, first_pass):
	pass

def LDI(self,operand,op_count, first_pass):
	pass

def LDIR(self,operand,op_count, first_pass):
	pass

def LDD(self,operand,op_count, first_pass):
	pass

def LDDR(self,operand,op_count, first_pass):
	pass

def CPI(self,operand,op_count, first_pass):
	pass

def CPIR(self,operand,op_count, first_pass):
	pass

def CPD(self,operand,op_count, first_pass):
	pass

def CPDR(self,operand,op_count, first_pass):
	pass

#Opcodes Logic & Arithmetic Group

def ADD(self,operand,op_count, first_pass):
	pass

def ADC(self,operand,op_count, first_pass):
	pass

def SUB(self,operand,op_count, first_pass):
	pass

def SBC(self,operand,op_count, first_pass):
	pass

def AND(self,operand,op_count, first_pass):
	pass

def OR(self,operand,op_count, first_pass):
	pass

def XOR(self,operand,op_count, first_pass):
	pass

def CP(self,operand,op_count, first_pass):
	pass

def INC(self,operand,op_count, first_pass):
	pass

def DEC(self,operand,op_count, first_pass):
	pass

#Opcodes Arithmetic & Control CPU Group

def DAA(self,operand,op_count, first_pass):
	pass

def CPL(self,operand,op_count, first_pass):
	pass

def NEG(self,operand,op_count, first_pass):
	pass

def CCF(self,operand,op_count, first_pass):
	pass

def SCF(self,operand,op_count, first_pass):
	pass

def NOP(self,operand,op_count, first_pass):
	pass

def HALT(self,operand,op_count, first_pass):
	pass

def DI(self,operand,op_count, first_pass):
	pass

def EI(self,operand,op_count, first_pass):
	pass

def IM(self,operand,op_count, first_pass):
	pass

#Opcodes Rotate & Shift Group

def RLCA(self,operand,op_count, first_pass):
	pass

def RLA(self,operand,op_count, first_pass):
	pass

def RRCA(self,operand,op_count, first_pass):
	pass

def RRA(self,operand,op_count, first_pass):
	pass

def RLC(self,operand,op_count, first_pass):
	pass

def RL(self,operand,op_count, first_pass):
	pass

def RRC(self,operand,op_count, first_pass):
	pass

def RR(self,operand,op_count, first_pass):
	pass

def SLA(self,operand,op_count, first_pass):
	pass

def SRA(self,operand,op_count, first_pass):
	pass

def SRL(self,operand,op_count, first_pass):
	pass

def RLD(self,operand,op_count, first_pass):
	pass

def RRD(self,operand,op_count, first_pass):
	pass

#Opcodes Bit SET,RESET & TEST Group

def BIT(self,operand,op_count, first_pass):
	pass

def SET(self,operand,op_count, first_pass):
	pass

def RES(self,operand,op_count, first_pass):
	pass

#Opcodes Jump Group

def JP(self,operand,op_count, first_pass):
	pass

def JR(self,operand,op_count, first_pass):
	pass

def DJNZ(self,operand,op_count, first_pass):
	pass

#Opcodes Call & Return Group

def CALL(self,operand,op_count, first_pass):
	pass

def RET(self,operand,op_count, first_pass):
	pass

def RETI(self,operand,op_count, first_pass):
	pass

def RETN(self,operand,op_count, first_pass):
	pass

def RST(self,operand,op_count, first_pass):
	pass

#Opcodes Input & Output Group

def IN(self,operand,op_count, first_pass):
	pass

def INI(self,operand,op_count, first_pass):
	pass

def INIR(self,operand,op_count, first_pass):
	pass

def IND(self,operand,op_count, first_pass):
	pass

def INDR(self,operand,op_count, first_pass):
	pass

def OUT(self,operand,op_count, first_pass):
	pass

def OUTI(self,operand,op_count, first_pass):
	pass

def OTIR(self,operand,op_count, first_pass):
	pass

def OUTD(self,operand,op_count, first_pass):
	pass

def OTDR(self,operand,op_count, first_pass):
	pass

#Opcodes Directives

def ORG(self,operand,op_count, first_pass):
	pass

def END(self,operand,op_count, first_pass):
	pass

def DB(self,operand,op_count, first_pass):
	pass

def DW(self,operand,op_count, first_pass):
	pass

def DL(self,operand,op_count, first_pass):
	pass

#Mapping Opcodes
map_mnem = {
	#Load Group
	"LD": LD, "PUSH": PUSH, "POP":POP,
	#Exchange, Block Transfer & Block Search Group
	"EX": EX, "EXX": EXX, "LDI": LDI, "LDIR": LDIR, "LDD": LDD, "LDDR": LDDR, "CPI": CPI,
	"CPIR": CPIR, "CPD": CPD, "CPDR": CPDR,
	#Logic & Arithmetic Group
	"ADD": ADD, "ADC": ADC, "SUB":SUB, "SBC": SBC, "AND": AND, "OR": OR, "XOR": XOR, "CP": CP,
	"INC": INC, "DEC": DEC,
	#Arithmetic & Control CPU Group
	"DAA": DAA, "CPL": CPL, "NEG": NEG, "CCF": CCF, "SCF": SCF, "NOP": NOP, "HALT": HALT, "DI": DI,
	"EI": EI, "IM": IM,
	#Rotate & Shift Group
	"RLCA": RLCA, "RLA": RLA, "RRCA": RRCA, "RRA": RRA, "RLC": RLC, "RL": RL, "RRC": RRC, "RR": RR,
	"SLA": SLA, "SRA": SRA, "SRL": SRL, "RLD": RLD, "RRD": RRD,
	#Bit SET,RESET & TEST Group
	"BIT": BIT, "SET": SET, "RES": RES,
	#Jump Group
	"JP": JP, "JR": JR, "DJNZ": DJNZ,
	#Call & Return Group
	"CALL": CALL, "RET": RET, "RETI": RETI, "RETN": RETN, "RST": RST,
	#Input & Output Group
	"IN": IN, "INI": INI, "INIR": INIR, "IND": IND, "INDR": INDR, "OUT": OUT, "OUTI": OUTI, "OTIR": OTIR,
	"OUTD": OUTD, "OTDR": OTDR,
	#Directives Group
	"ORG": ORG, "END": END, "DB": DB, "DW": DW, "DL": DL
}
        
