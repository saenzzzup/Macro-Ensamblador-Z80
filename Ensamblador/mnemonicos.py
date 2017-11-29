#ValidOperands
v_ops=[
"A","B","C","D","E","H","L","R","I","BC","DE","HL","AF","AF'","SP","IX","IY",
"NZ","Z","NC","C","PQ","PE","P","M","(HL)","(IX)","(IY)","(BC)","(DE)","(IY+",
"(IX+","(SP)","(C)"
]

v_jump = ["JP","JR","CALL","DJNZ"]


TS = {}

#LD A,r
def LDAA():
	return "7F",1

def LDAB():
	return "78",1

def LDAC():
	return "79",1

def LDAD():
	return "7A",1

def LDAE():
	return "7B",1

def LDAH():
	return "7C",1

def LDAL():
	return "7D",1

def LDAHL():
	return "7E",1

 ##AgregarDireccion
def LDAIX(dire):
	return "DD7E"+dire,3

 ##AgregarDireccion
def LDAIY(dire):
	return "FD7E"+dire,3
 
 ##AgregarDireccion
def LDAnn(dire):
	return "3E"+dire,2

def LDABC():
	return "0A",1

def LDADE():
	return "1A",1

 ##AgregarDireccion
def LDANN(dire):
	return "3A"+dire,3

def LDAI():
	return "ED57",2

def LDAR():
	return "ED5F",2

#LD B,r
def LDBA():
	return "47",1

def LDBB():
	return "40",1

def LDBC():
	return "41",1

def LDBD():
	return "42",1

def LDBE():
	return "43",1

def LDBH():
	return "44",1

def LDBL():
	return "45",1

def LDBHL():
	return "46",1

 ##AgregarDireccion
def LDBIX(dire):
	return "DD46"+dire,3

 ##AgregarDireccion
def LDBIY(dire):
	return "FD46"+dire,3

 ##AgregarDireccion
def LDBnn(dire):
	return "06"+dire,2

#LD C,r
def LDCA():
	return "4F",1

def LDCB():
	return "48",1

def LDCC():
	return "49",1

def LDCD():
	return "4A",1

def LDCE():
	return "4B",1

def LDCH():
	return "4C",1

def LDCL():
	return "4D",1

def LDCHL():
	return "4E",1

 ##AgregarDireccion
def LDCIX(dire):
	return "DD4E"+dire,3

 ##AgregarDireccion
def LDCIY(dire):
	return "FD4E"+dire,3

 ##AgregarDireccion
def LDCnn(dire):
	return "0E"+dire,2

#LD D,r
def LDDA():
	return "57",1

def LDDB():
	return "50",1

def LDDC():
	return "51",1

def LDDD():
	return "52",1

def LDDE():
	return "53",1

def LDDH():
	return "54",1

def LDDL():
	return "55",1

def LDDHL():
	return "56",1

 ##AgregarDireccion
def LDDIX(dire):
	return "DD56"+dire,3

 ##AgregarDireccion
def LDDIY(dire):
	return "FD56"+dire,3

 ##AgregarDireccion
def LDDnn(dire):
	return "16"+dire,2

#LD E,r
def LDEA():
	return "5F",1

def LDEB():
	return "58",1

def LDEC():
	return "59",1

def LDED():
	return "5A",1

def LDEE():
	return "5B",1

def LDEH():
	return "5C",1

def LDEL():
	return "5D",1

def LDEHL():
	return "5E",1

 ##AgregarDireccion
def LDEIX(dire):
	return "DD5E"+dire,3

 ##AgregarDireccion
def LDEIY(dire):
	return "FD5E"+dire,3

 ##AgregarDireccion
def LDEnn(dire):
	return "1E"+dire,2

#LD H,r
def LDHA():
	return "67",1

def LDHB():
	return "60",1

def LDHC():
	return "61",1

def LDHD():
	return "62",1

def LDHE():
	return "63",1

def LDHH():
	return "64",1

def LDHL():
	return "65",1

def LDHHL():
	return "66",1

 ##AgregarDireccion
def LDHIX(dire):
	return "DD66"+dire,3

 ##AgregarDireccion
def LDHIY(dire):
	return "FD66"+dire,3

 ##AgregarDireccion
def LDHnn(dire):
	return "26"+dire,2

#LD L,r
def LDLA():
	return "6F",1

def LDLB():
	return "68",1

def LDLC():
	return "69",1

def LDLD():
	return "6A",1

def LDLE():
	return "6B",1

def LDLH():
	return "6C",1

def LDLL():
	return "6D",1

def LDLHL():
	return "6E",1

 ##AgregarDireccion
def LDLIX(dire):
	return "DD6E"+dire,3

 ##AgregarDireccion
def LDLIY(dire):
	return "FD6E"+dire,3

 ##AgregarDireccion
def LDLnn(dire):
	return "2E"+dire,2

#LD HL,r
def LDHLA():
	return "77",1

def LDHLB():
	return "70",1

def LDHLC():
	return "71",1

def LDHLD():
	return "72",1

def LDHLE():
	return "73",1

def LDHLH():
	return "74",1

def LDHLL():
	return "75",1

 ##AgregarDireccion
def LDHLnn(dire):
	return "36"+dire,2

#LD (BC),A
def LDBCA():
	return "02",1

#LD (DE),A
def LDDEA():
	return "12",1

#LD (NN),A
 ##AgregarDireccion
def LDNNA(dire):
	return "32"+dire,1

#LD (IX+d),r
def LDIXdA(dire):
	return "DD77"+dire,3

def LDIXdB(dire):
	return "DD70"+dire,3

def LDIXdC(dire):
	return "DD71"+dire,3

def LDIXdD(dire):
	return "DD72"+dire,3

def LDIXdE(dire):
	return "DD73"+dire,3

def LDIXdH(dire):
	return "DD74"+dire,3

def LDIXdL(dire):
	return "DD75"+dire,3

 ##AgregarDireccion
def LDIXdnn(dire):
	return "DD36"+dire,4

#LD (IY+d),r
def LDIYdA(dire):
	return "FD77"+dire,1

def LDIYdB(dire):
	return "FD70"+dire,1

def LDIYdC(dire):
	return "FD71"+dire,1

def LDIYFD(dire):
	return "FD72"+dire,1

def LDIYdE(dire):
	return "FD73"+dire,1

def LDIYdH(dire):
	return "FD74"+dire,1

def LDIYdL(dire):
	return "FD75"+dire,1

 ##AgregarDireccion
def LDHLnn(dire):
	return "FD36"+dire,3

#LD I,A
def LDIA():
	return "ED47",2

#LD R,A
def LDRA():
	return "ED4F",2

#LD BC,(nn)
def LDBCNN(dire):
	return "ED4B"+dire,4

#LD DE,(nn)
def LDDENN(dire):
	return "ED5B"+dire,4

#LD HL,(nn)
def LDHLNN(dire):
	return "2A"+dire,4

#LD SP,(nn)
def LDSPNN(dire):
	return "ED7B"+dire,4

#LD IX,(nn)
def LDIXNN(dire):
	return "DD2A"+dire,4

#LD IY,(nn)
def LDIYNN(dire):
	return "FD2A"+dire,4

#LD (nn),BC
def LDNNBC(dire):
	return "ED43"+dire,4

#LD (nn),DE
def LDNNDE(dire):
	return "ED53"+dire,4

#LD (nn),HL
def LDNNHL(dire):
	return "22"+dire,4

#LD (nn),SP
def LDNNSP(dire):
	return "ED73"+dire,4

#LD (nn),IX
def LDNNIX(dire):
	return "DD22"+dire,4

#LD (nn),IY
def LDNNIY(dire):
	return "FD22"+dire,4

#PUSH BC
def PUSHBC(dire):
	return "C5"+dire,4

#PUSH DE
def PUSHDE(dire):
	return "D5"+dire,4

#PUSH HL
def PUSHHL(dire):
	return "E5"+dire,4

#PUSH AF
def PUSHAF(dire):
	return "F5"+dire,4

#PUSH IX
def PUSHIX(dire):
	return "DDE5"+dire,4

#PUSH IY
def PUSHIY(dire):
	return "FDE5"+dire,4

#POP BC
def PUSHBC(dire):
	return "C1"+dire,4

#POP DE
def PUSHDE(dire):
	return "D1"+dire,4

#POP HL
def PUSHHL(dire):
	return "E1"+dire,4

#POP AF
def PUSHAF(dire):
	return "F1"+dire,4

#POP IX
def PUSHIX(dire):
	return "DDE1"+dire,4

#POP IY
def PUSHIY(dire):
	return "FDE1"+dire,4

#JP nn
def JPnn(dire):
	return "C3"+dire,3

#JP cc,nn
def JPCCnn(dire):
	return "C2"+dire,3

#MappnngOpcodes
map_mnem={
 "LD A,A": LDAA, "LD A,B":LDAB, "LD A,C":LDAC, "LD A,NN": LDAnn, "JP nn":JPnn, "JP cc,nn":JPCCnn,
}



