#ValidOperands
v_ops=[
"A","B","C","D","E","H","L","R","I","BC","DE","HL","AF","AF'","SP","IX","IY",
"nz","z","nc","c","pq","pe","p","m","(HL)","(IX)","(IY)","(BC)","(DE)","(SP)","(C)"
]
v_op = ["LD","PUSH","POP","EX","EXX","LDI","LDIR","LDD","LDDR","CPI","CPIR","CPD",
"CPDR","ADD","ADC","SUB","SBC","AND","OR","XOR","CP","INC","DEC","DAA","CPL","NEG",
"CCF","SCF","NOP","HALT","DI","EI","IM","RLCA","RLA","RRCA","RRA","RLC","RL","RRC",
"RR","SLA","SRA","SRL","RLD","RRD","BIT","SET","RES","JP","JR","DJNZ","CALL","RET",
"RETI","RETN","RST","IN","INI","INIR","IND","INDR","OUT","OUTI","OUTIR","OUTD","OTDR"
]

def DB(is_first_pass,value):
	if (is_first_pass):
		return 1
	return value

def DL(is_first_pass,value):
	if (is_first_pass):
		return 1
	return value

def EQU(is_first_pass,value):
	if (is_first_pass):
		return 0
	return ""

def END(is_first_pass):
	if (is_first_pass):
		return 0
	return ""

def NOP(is_first_pass):
	if (is_first_pass):
		return 1
	return "00"

def LDBCNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "018405"

def LDBCA(is_first_pass):
	if (is_first_pass):
		return 1
	return "02"

def INCBC(is_first_pass):
	if (is_first_pass):
		return 1
	return "03"

def INCB(is_first_pass):
	if (is_first_pass):
		return 1
	return "04"

def DECB(is_first_pass):
	if (is_first_pass):
		return 1
	return "05"

def LDBN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "06"+dire

def RLCA(is_first_pass):
	if (is_first_pass):
		return 1
	return "07"

def EXAFAF(is_first_pass):
	if (is_first_pass):
		return 1
	return "08"

def ADDHLBC(is_first_pass):
	if (is_first_pass):
		return 1
	return "09"

def LDABC(is_first_pass):
	if (is_first_pass):
		return 1
	return "0A"

def DECBC(is_first_pass):
	if (is_first_pass):
		return 1
	return "0B"

def INCC(is_first_pass):
	if (is_first_pass):
		return 1
	return "0C"

def DECC(is_first_pass):
	if (is_first_pass):
		return 1
	return "0D"

def LDCN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "0E"+dire

def RRCA(is_first_pass):
	if (is_first_pass):
		return 1
	return "0F"

def DJNZDIS(is_first_pass):
	if (is_first_pass):
		return 2
	return "102E"

def LDDENN(is_first_pass):
	if (is_first_pass):
		return 3
	return "118405"

def LDDEA(is_first_pass):
	if (is_first_pass):
		return 1
	return "12"

def INCDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "13"

def INCD(is_first_pass):
	if (is_first_pass):
		return 1
	return "14"

def DECD(is_first_pass):
	if (is_first_pass):
		return 1
	return "15"

def LDDN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "16"+dire

def RLA(is_first_pass):
	if (is_first_pass):
		return 1
	return "17"

def JRDIS(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "18"+dire

def ADDHLDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "19"

def LDADE(is_first_pass):
	if (is_first_pass):
		return 1
	return "1A"

def DECDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "1B"

def INCE(is_first_pass):
	if (is_first_pass):
		return 1
	return "1C"

def DECE(is_first_pass):
	if (is_first_pass):
		return 1
	return "1D"

def LDEN(is_first_pass):
	if (is_first_pass):
		return 2
	return "1E20"

def RRA(is_first_pass):
	if (is_first_pass):
		return 1
	return "1F"

def JRNZDIS(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "20"+dire

def LDHLNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "218405"

def LDNNHL(is_first_pass):
	if (is_first_pass):
		return 3
	return "228405"

def INCHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "23"

def INCH(is_first_pass):
	if (is_first_pass):
		return 1
	return "24"

def DECH(is_first_pass):
	if (is_first_pass):
		return 1
	return "25"

def LDHN(is_first_pass):
	if (is_first_pass):
		return 2
	return "2620"

def DAA(is_first_pass):
	if (is_first_pass):
		return 1
	return "27"

def JRZDIS(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "28"+dire

def ADDHLHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "29"

def LDHLNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "2A8405"

def DECHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "2B"

def INCL(is_first_pass):
	if (is_first_pass):
		return 1
	return "2C"

def DECL(is_first_pass):
	if (is_first_pass):
		return 1
	return "2D"

def LDLN(is_first_pass):
	if (is_first_pass):
		return 2
	return "2E20"

def CPL(is_first_pass):
	if (is_first_pass):
		return 1
	return "2F"

def JRNCDIS(is_first_pass):
	if (is_first_pass):
		return 2
	return "302E"

def LDSPNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "318405"

def LDNNA(is_first_pass,dire):
	if (is_first_pass):
		return 3
	return "32"+dire

def INCSP(is_first_pass):
	if (is_first_pass):
		return 1
	return "33"

def INCHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "34"

def DECHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "35"

def LDHLN(is_first_pass):
	if (is_first_pass):
		return 2
	return "3620"

def SCF(is_first_pass):
	if (is_first_pass):
		return 1
	return "37"

def JRCDIS(is_first_pass):
	if (is_first_pass):
		return 2
	return "382E"

def ADDHLSP(is_first_pass):
	if (is_first_pass):
		return 1
	return "39"

def LDANN(is_first_pass,dire):
	if (is_first_pass):
		return 3
	return "3A"+dire

def DECSP(is_first_pass):
	if (is_first_pass):
		return 1
	return "3B"

def INCA(is_first_pass):
	if (is_first_pass):
		return 1
	return "3C"

def DECA(is_first_pass):
	if (is_first_pass):
		return 1
	return "3D"

def LDAN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "3E"+dire

def CCF(is_first_pass):
	if (is_first_pass):
		return 1
	return "3F"

def LDBB(is_first_pass):
	if (is_first_pass):
		return 1
	return "40"

def LDBC(is_first_pass):
	if (is_first_pass):
		return 1
	return "41"

def LDBD(is_first_pass):
	if (is_first_pass):
		return 1
	return "42"

def LDBE(is_first_pass):
	if (is_first_pass):
		return 1
	return "43"

def LDBHNN(is_first_pass):
	if (is_first_pass):
		return 1
	return "44"

def LDBL(is_first_pass):
	if (is_first_pass):
		return 1
	return "45"

def LDBHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "46"

def LDBA(is_first_pass):
	if (is_first_pass):
		return 1
	return "47"

def LDCB(is_first_pass):
	if (is_first_pass):
		return 1
	return "48"

def LDCC(is_first_pass):
	if (is_first_pass):
		return 1
	return "49"

def LDCD(is_first_pass):
	if (is_first_pass):
		return 1
	return "4A"

def LDCE(is_first_pass):
	if (is_first_pass):
		return 1
	return "4B"

def LDCH(is_first_pass):
	if (is_first_pass):
		return 1
	return "4C"

def LDCL(is_first_pass):
	if (is_first_pass):
		return 1
	return "4D"

def LDCHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "4E"

def LDCA(is_first_pass):
	if (is_first_pass):
		return 1
	return "4F"

def LDDB(is_first_pass):
	if (is_first_pass):
		return 1
	return "50"

def LDDC(is_first_pass):
	if (is_first_pass):
		return 1
	return "51"

def LDDD(is_first_pass):
	if (is_first_pass):
		return 1
	return "52"

def LDDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "53"

def LDDH(is_first_pass):
	if (is_first_pass):
		return 1
	return "54"

def LDDL(is_first_pass):
	if (is_first_pass):
		return 1
	return "55"

def LDDHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "56"

def LDDA(is_first_pass):
	if (is_first_pass):
		return 1
	return "57"

def LDEB(is_first_pass):
	if (is_first_pass):
		return 1
	return "58"

def LDEC(is_first_pass):
	if (is_first_pass):
		return 1
	return "59"

def LDED(is_first_pass):
	if (is_first_pass):
		return 1
	return "5A"

def LDEE(is_first_pass):
	if (is_first_pass):
		return 1
	return "5B"

def LDEH(is_first_pass):
	if (is_first_pass):
		return 1
	return "5C"

def LDEL(is_first_pass):
	if (is_first_pass):
		return 1
	return "5D"

def LDEHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "5E"

def LDEA(is_first_pass):
	if (is_first_pass):
		return 1
	return "5F"

def LDHB(is_first_pass):
	if (is_first_pass):
		return 1
	return "60"

def LDHC(is_first_pass):
	if (is_first_pass):
		return 1
	return "61"

def LDHD(is_first_pass):
	if (is_first_pass):
		return 1
	return "62"

def LDHE(is_first_pass):
	if (is_first_pass):
		return 1
	return "63"

def LDHH(is_first_pass):
	if (is_first_pass):
		return 1
	return "64"

def LDHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "65"

def LDHHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "66"

def LDHA(is_first_pass):
	if (is_first_pass):
		return 1
	return "67"

def LDLB(is_first_pass):
	if (is_first_pass):
		return 1
	return "68"

def LDLC(is_first_pass):
	if (is_first_pass):
		return 1
	return "69"

def LDLD(is_first_pass):
	if (is_first_pass):
		return 1
	return "6A"

def LDLE(is_first_pass):
	if (is_first_pass):
		return 1
	return "6B"

def LDLH(is_first_pass):
	if (is_first_pass):
		return 1
	return "6C"

def LDLL(is_first_pass):
	if (is_first_pass):
		return 1
	return "6D"

def LDLHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "6E"

def LDLA(is_first_pass):
	if (is_first_pass):
		return 1
	return "6F"

def LDHLB(is_first_pass):
	if (is_first_pass):
		return 1
	return "70"

def LDHLC(is_first_pass):
	if (is_first_pass):
		return 1
	return "71"

def LDHLD(is_first_pass):
	if (is_first_pass):
		return 1
	return "72"

def LDHLE(is_first_pass):
	if (is_first_pass):
		return 1
	return "73"

def LDHLH(is_first_pass):
	if (is_first_pass):
		return 1
	return "74"

def LDHLL(is_first_pass):
	if (is_first_pass):
		return 1
	return "75"

def HALT(is_first_pass):
	if (is_first_pass):
		return 1
	return "76"

def LDHLA(is_first_pass):
	if (is_first_pass):
		return 1
	return "77"

def LDAB(is_first_pass):
	if (is_first_pass):
		return 1
	return "78"

def LDAC(is_first_pass):
	if (is_first_pass):
		return 1
	return "79"

def LDAD(is_first_pass):
	if (is_first_pass):
		return 1
	return "7A"

def LDAE(is_first_pass):
	if (is_first_pass):
		return 1
	return "7B"

def LDAH(is_first_pass):
	if (is_first_pass):
		return 1
	return "7C"

def LDAL(is_first_pass):
	if (is_first_pass):
		return 1
	return "7D"

def LDAHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "7E"

def LDAA(is_first_pass):
	if (is_first_pass):
		return 1
	return "7F"

def ADDAB(is_first_pass):
	if (is_first_pass):
		return 1
	return "80"

def ADDAC(is_first_pass):
	if (is_first_pass):
		return 1
	return "81"

def ADDAD(is_first_pass):
	if (is_first_pass):
		return 1
	return "82"

def ADDAE(is_first_pass):
	if (is_first_pass):
		return 1
	return "83"

def ADDAH(is_first_pass):
	if (is_first_pass):
		return 1
	return "84"

def ADDAL(is_first_pass):
	if (is_first_pass):
		return 1
	return "85"

def ADDAHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "86"

def ADDAA(is_first_pass):
	if (is_first_pass):
		return 1
	return "87"

def ADCAB(is_first_pass):
	if (is_first_pass):
		return 1
	return "88"

def ADCAC(is_first_pass):
	if (is_first_pass):
		return 1
	return "89"

def ADCAD(is_first_pass):
	if (is_first_pass):
		return 1
	return "8A"

def ADCAE(is_first_pass):
	if (is_first_pass):
		return 1
	return "8B"

def ADCAH(is_first_pass):
	if (is_first_pass):
		return 1
	return "8C"

def ADCAL(is_first_pass):
	if (is_first_pass):
		return 1
	return "8D"

def ADCAHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "8E"

def ADCAA(is_first_pass):
	if (is_first_pass):
		return 1
	return "8F"

def SUBB(is_first_pass):
	if (is_first_pass):
		return 1
	return "90"

def SUBC(is_first_pass):
	if (is_first_pass):
		return 1
	return "91"

def SUBD(is_first_pass):
	if (is_first_pass):
		return 1
	return "92"

def SUBE(is_first_pass):
	if (is_first_pass):
		return 1
	return "93"

def SUBH(is_first_pass):
	if (is_first_pass):
		return 1
	return "94"

def SUBL(is_first_pass):
	if (is_first_pass):
		return 1
	return "95"

def SUBHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "96"

def SUBA(is_first_pass):
	if (is_first_pass):
		return 1
	return "97"

def SBCAB(is_first_pass):
	if (is_first_pass):
		return 1
	return "98"

def SBCAC(is_first_pass):
	if (is_first_pass):
		return 1
	return "99"

def SBCAD(is_first_pass):
	if (is_first_pass):
		return 1
	return "9A"

def SBCAE(is_first_pass):
	if (is_first_pass):
		return 1
	return "9B"

def SBCAH(is_first_pass):
	if (is_first_pass):
		return 1
	return "9C"

def SBCAL(is_first_pass):
	if (is_first_pass):
		return 1
	return "9D"

def SBCAHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "9E"

def SBCAA(is_first_pass):
	if (is_first_pass):
		return 1
	return "9F"

def ANDB(is_first_pass):
	if (is_first_pass):
		return 1
	return "A0"

def ANDC(is_first_pass):
	if (is_first_pass):
		return 1
	return "A1"

def ANDD(is_first_pass):
	if (is_first_pass):
		return 1
	return "A2"

def ANDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "A3"

def ANDH(is_first_pass):
	if (is_first_pass):
		return 1
	return "A4"

def ANDL(is_first_pass):
	if (is_first_pass):
		return 1
	return "A5"

def ANDHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "A6"

def ANDA(is_first_pass):
	if (is_first_pass):
		return 1
	return "A7"

def XORB(is_first_pass):
	if (is_first_pass):
		return 1
	return "A8"

def XORC(is_first_pass):
	if (is_first_pass):
		return 1
	return "A9"

def XORD(is_first_pass):
	if (is_first_pass):
		return 1
	return "AA"

def XORE(is_first_pass):
	if (is_first_pass):
		return 1
	return "AB"

def XORH(is_first_pass):
	if (is_first_pass):
		return 1
	return "AC"

def XORL(is_first_pass):
	if (is_first_pass):
		return 1
	return "AD"

def XORHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "AE"

def XORA(is_first_pass):
	if (is_first_pass):
		return 1
	return "AF"

def ORB(is_first_pass):
	if (is_first_pass):
		return 1
	return "B0"

def ORC(is_first_pass):
	if (is_first_pass):
		return 1
	return "B1"

def ORD(is_first_pass):
	if (is_first_pass):
		return 1
	return "B2"

def ORE(is_first_pass):
	if (is_first_pass):
		return 1
	return "B3"

def ORH(is_first_pass):
	if (is_first_pass):
		return 1
	return "B4"

def ORL(is_first_pass):
	if (is_first_pass):
		return 1
	return "B5"

def ORHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "B6"

def ORA(is_first_pass):
	if (is_first_pass):
		return 1
	return "B7"

def CPB(is_first_pass):
	if (is_first_pass):
		return 1
	return "B8"

def CPC(is_first_pass):
	if (is_first_pass):
		return 1
	return "B9"

def CPD(is_first_pass):
	if (is_first_pass):
		return 1
	return "BA"

def CPE(is_first_pass):
	if (is_first_pass):
		return 1
	return "BB"

def CPH(is_first_pass):
	if (is_first_pass):
		return 1
	return "BC"

def CPL(is_first_pass):
	if (is_first_pass):
		return 1
	return "BD"

def CPHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "BE"

def CPA(is_first_pass):
	if (is_first_pass):
		return 1
	return "BF"

def RETNZ(is_first_pass):
	if (is_first_pass):
		return 1
	return "C0"

def POPBC(is_first_pass):
	if (is_first_pass):
		return 1
	return "C1"

def JPNZNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "C28405"

def JPNN(is_first_pass,dire):
	if (is_first_pass):
		return 3
	return "C3"+dire

def CALLNZNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "C48405"

def PUSHBC(is_first_pass):
	if (is_first_pass):
		return 1
	return "C5"

def ADDAN(is_first_pass):
	if (is_first_pass):
		return 2
	return "C620"

def RST0(is_first_pass):
	if (is_first_pass):
		return 1
	return "C7"

def RETZ(is_first_pass):
	if (is_first_pass):
		return 1
	return "C8"

def RET(is_first_pass):
	if (is_first_pass):
		return 1
	return "C9"

def JPZNN(is_first_pass,dire):
	if (is_first_pass):
		return 3
	return "CA"+dire

def CALLZNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "CC8405"

def CALLNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "CD8405"

def ADCAN(is_first_pass):
	if (is_first_pass):
		return 2
	return "CE20"

def RST8(is_first_pass):
	if (is_first_pass):
		return 1
	return "CF"

def RETNC(is_first_pass):
	if (is_first_pass):
		return 1
	return "D0"

def POPDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "D1"

def JPNCNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "D28405"

def OUTNA(is_first_pass):
	if (is_first_pass):
		return 2
	return "D320"

def CALLNCNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "D48405"

def PUSHDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "D5"

def SUBN(is_first_pass):
	if (is_first_pass):
		return 2
	return "D620"

def RST10H(is_first_pass):
	if (is_first_pass):
		return 1
	return "D7"

def RETC(is_first_pass):
	if (is_first_pass):
		return 1
	return "D8"

def EXX(is_first_pass):
	if (is_first_pass):
		return 1
	return "D9"

def JPCNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "DA8405"

def INAN(is_first_pass):
	if (is_first_pass):
		return 2
	return "DB20"

def CALLCN(is_first_pass):
	if (is_first_pass):
		return 3
	return "DC8405"

def SBCAN(is_first_pass):
	if (is_first_pass):
		return 2
	return "DE20"

def RST18H(is_first_pass):
	if (is_first_pass):
		return 1
	return "DF"

def RETPO(is_first_pass):
	if (is_first_pass):
		return 1
	return "E0"

def POPHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "E1"

def JPPONN(is_first_pass):
	if (is_first_pass):
		return 3
	return "E28405"

def EXSPHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "E3"

def CALLPONN(is_first_pass):
	if (is_first_pass):
		return 3
	return "E48405"

def PUSHHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "E5"

def ANDN(is_first_pass):
	if (is_first_pass):
		return 2
	return "E620"

def RST20H(is_first_pass):
	if (is_first_pass):
		return 1
	return "E7"

def RETPE(is_first_pass):
	if (is_first_pass):
		return 1
	return "E8"

def JPHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "E9"

def JEPENN(is_first_pass):
	if (is_first_pass):
		return 3
	return "EA8405"

def EXDEHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "EB"

def CALLPENN(is_first_pass):
	if (is_first_pass):
		return 3
	return "EC8405"

def XORN(is_first_pass):
	if (is_first_pass):
		return 2
	return "EE20"

def RST28H(is_first_pass):
	if (is_first_pass):
		return 1
	return "EF"

def RETP(is_first_pass):
	if (is_first_pass):
		return 1
	return "F0"

def POPAF(is_first_pass):
	if (is_first_pass):
		return 1
	return "F1"

def JPPNN(is_first_pass,dire):
	if (is_first_pass):
		return 3
	return "F2"+dire

def DI(is_first_pass):
	if (is_first_pass):
		return 1
	return "F3"

def CALLPNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "F48405"

def PUSHAF(is_first_pass):
	if (is_first_pass):
		return 1
	return "F5"

def ORN(is_first_pass):
	if (is_first_pass):
		return 2
	return "F620"

def RST30H(is_first_pass):
	if (is_first_pass):
		return 1
	return "F7"

def RETM(is_first_pass):
	if (is_first_pass):
		return 1
	return "F8"

def LDSPHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "F9"

def JPMNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "FA8405"

def EI(is_first_pass):
	if (is_first_pass):
		return 1
	return "FB"

def CALLMNN(is_first_pass):
	if (is_first_pass):
		return 3
	return "FC8405"

def CPN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "FE"+dire

def RST38H(is_first_pass):
	if (is_first_pass):
		return 1
	return "FF"

def RLCB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB00"

def RLCC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB01"

def RLCD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB02"

def RLCE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB03"

def RLCH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB04"

def RLCL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB05"

def RLCHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB06"

def RLC_A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRC_B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB08"

def RRC_C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB09"

def RRC_D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB0A"

def RRC_E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB0B"

def RRC_H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB0C"

def RRC_L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB0D"

def RRC_HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB0E"

def RRC_A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB0F"

def RLB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB10"

def RLC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB11"

def RLD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB12"

def RLE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB13"

def RLH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB14"

def RLL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB15"

def RLHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB16"

def RLA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB17"

def RRB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB18"

def RRC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB19"

def RRD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1A"

def RRE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1B"

def RRH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1C"

def RRL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1D"

def RRHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1E"

def RRA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1F"

def SLAB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB20"

def SLAC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB21"

def SLAD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB22"

def SLAE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB23"

def SLAH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB24"

def SLAL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB25"

def SLAHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB26"

def SLAA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB27"

def SRAB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB28"

def SRAC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB29"

def SRAD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB2A"

def SRAE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB2B"

def SRAH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB2C"

def SRAL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB2D"

def SRAHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB2E"

def SRAA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB2F"

def SRLB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB38"

def SRLC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB39"

def SRLD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB3A"

def SRLE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB3B"

def SRLH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB3C"

def SRLL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB3D"

def SRLHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB3E"

def SRLA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB3F"

def BIT0B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB40"

def BIT0C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB41"

def BIT0D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB42"

def BIT0E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB43"

def BIT0H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB44"

def BIT0L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB45"

def BIT0HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB46"

def BIT0A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB47"

def BIT1B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB48"

def BIT1C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB49"

def BIT1D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB4A"

def BIT1E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB4B"

def BIT1H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB4C"

def BIT1L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB4D"

def BIT1HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB4E"

def BIT1A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB4F"

def BIT2B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB50"

def BIT2C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB51"

def BIT2D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB52"

def BIT2E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB53"

def BIT2H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB54"

def BIT2L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB55"

def BIT2HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB56"

def BIT2A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB57"

def BIT3B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB58"

def BIT3C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB59"

def BIT3D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB5A"

def BIT3E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB5B"

def BIT3H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB5C"

def BIT3L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB5D"

def BIT3HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB5E"

def BIT3A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB5F"

def BIT4B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB60"

def BIT4C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB61"

def BIT4D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB62"

def BIT4E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB63"

def BIT4H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB64"

def BIT4L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB65"

def BIT4HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB66"

def BIT4A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB67"

def BIT5B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB68"

def BIT5C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB69"

def BIT5D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB6A"

def BIT5E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB6B"

def BIT5H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB6C"

def BIT5L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB6D"

def BIT5HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB6E"

def BIT5A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB6F"

def BIT6B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB70"

def BIT6C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB71"

def BIT6D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB72"

def BIT6E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB73"

def BIT6H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB74"

def BIT6L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB75"

def BIT6HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB76"

def BIT6A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB77"

def BIT7B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB78"

def BIT7C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB79"

def BIT7D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB7A"

def BIT7E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB7B"

def BIT7H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB7C"

def BIT7L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB7D"

def BIT7HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB7E"

def BIT7A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB7F"

def RES0B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB80"

def RES0C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB81"

def RES0D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB82"

def RES0E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB83"

def RES0H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB84"

def RES0L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB85"

def RES0HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB86"

def RES0A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB87"

def RES1B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB88"

def RES1C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB89 "

def RES1D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB8A"

def RES1E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB8B"

def RES1H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB8C"

def RES1L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB8D"

def RES1HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB8E"

def RES1A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB8F"

def RES2B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB90"

def RES2C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB91"

def RES2D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB92"

def RES2E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB93"

def RES2H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB94"

def RES2L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB95"

def RES2HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB96"

def RES2A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB97"

def RES3B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB98"

def RES3C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB99"

def RES3D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB9A"

def RES3E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB9B"

def RES3H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB9C"

def RES3L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB9D"

def RES3HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB9E"

def RES3A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB9F"

def RES4B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA0"

def RES4C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA1"

def RES4D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA2"

def RES4E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA3"

def RES4H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA4"

def RES4L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA5"

def RES4HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA6"

def RES4A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA7"

def RES5B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA8"

def RES5C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBA9"

def RES5D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBAA"

def RES5E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBAB"

def RES5H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBAC"

def RES5L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBAD"

def RES5HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBAE"

def RES5A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBAF"

def RES6B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB0"

def RES6C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB1"

def RES6D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB2"

def RES6E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB3"

def RES6H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB4"

def RES6L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB5"

def RES6HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB6"

def RES6A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB7"

def RES7B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB8"

def RES7C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBB9"

def RES7D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBBA"

def RES7E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBBB"

def RES7H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBBC"

def RES7L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBBD"

def RES7HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBBE"

def RES7A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBBF"

def SET0B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC0"

def SET0C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC1"

def SET0D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC2"

def SET0E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC3"

def SET0H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC4"

def SET0L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC5"

def SET0HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC6"

def SET0A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC7"

def SET1B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC8"

def SET1C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBC9"

def SET1D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBCA"

def SET1E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBCB"

def SET1H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBCC"

def SET1L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBCD"

def SET1HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBCE"

def SET1A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBCF"

def SET2B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD0"

def SET2C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD1"

def SET2D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD2"

def SET2E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD3"

def SET2H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD4"

def SET2L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD5"

def SET2HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD6"

def SET2A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD7"

def SET3B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD8"

def SET3C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBD9"

def SET3D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBDA"

def SET3E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBDB"

def SET3H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBDC"

def SET3L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBDD"

def SET3HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBDE"

def SET3A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBDF"

def SET4B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE0"

def SET4C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE1"

def SET4D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE2"

def SET4E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE3"

def SET4H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE4"

def SET4L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE5"

def SET4HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE6"

def SET4A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE7"

def SET5B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE8"

def SET5C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBE9"

def SET5D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBEA"

def SET5E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBEB"

def SET5H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBEC"

def SET5L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBED"

def SET5HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBEE"

def SET5A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBEF"

def SET6B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF0"

def SET6C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF1"

def SET6D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF2"

def SET6E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF3"

def SET6H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF4"

def SET6L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF5"

def SET6HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF6"

def SET6A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF7"

def SET7B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF8"

def SET7C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBF9"

def SET7D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBFA"

def SET7E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBFB"

def SET7H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBFC"

def SET7L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBFD"

def SET7HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBFE"

def SET7A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CBFF"

def ADDIXBC(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD09"

def ADDIXDE(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD19"

def LDIXNN(is_first_pass):
	if (is_first_pass):
		return 4
	return "DD218405"

def LDNNIX(is_first_pass):
	if (is_first_pass):
		return 4
	return "DD228405"

def INCIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD23"

def ADDIXIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD29"

def LDIXNN(is_first_pass):
	if (is_first_pass):
		return 4
	return "DD2A8405"

def DECIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD2B"

def INCIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD3405"

def DECIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD3505"

def LDIXdN(is_first_pass,dire):
	if (is_first_pass):
		return 4
	return "DD36"+dire

def ADDIXSP(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD39"

def LDBIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD4605"

def LDCIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD4E05"

def LDDIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD5605"

def LDEIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD5E05"

def LDHIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD6605"

def LDLIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD6E05"

def LDIXdB(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD7005"

def LDIXdC(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD7105"

def LDIXdD(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD7205"

def LDIXdE(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD7305"

def LDIXdH(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD7405"

def LDIXdL(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD7505"

def LDIXdA(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD7705"

def LDAIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD7E05"

def ADDAIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD8605"

def ADCAIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD8E05"

def SUBIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD9605"

def SBCAIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DD9E05"

def ANDIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DDA605"

def XORIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DDAE05"

def ORIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DDB605"

def CPIXd(is_first_pass):
	if (is_first_pass):
		return 3
	return "DDBE05"

def POPIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DDE1"

def EXSPIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DDE3"

def PUSHIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DDE5"

def JPIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DDE9"

def LDSPIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DDF9"

def RLCIXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB0506"

def RRCIXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB050E"

def RLIXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB0516"

def RRIXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB051E"

def SLAIXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB0526"

def SRAIXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB052E"

def SRLIXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB053E"

def BIT0IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB0546"

def BIT1IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB054E"

def BIT2IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB0556"

def BIT3IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB055E"

def BIT4IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB0566"

def BIT5IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB056E"

def BIT6IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB0576"

def BIT7IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB057E"

def RES0IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB0586"

def RES1IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB058E"

def RES2IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB0596"

def RES3IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB059E"

def RES4IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05A6"

def RES5IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05AE"

def RES6IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05B6"

def RES7IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05BE"

def SET0IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05C6"

def SET1IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05CE"

def SET2IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05D6"

def SET3IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05DE"

def SET4IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05E6"

def SET5IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05EE"

def SET6IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05F6"

def SET7IXd(is_first_pass):
	if (is_first_pass):
		return 4
	return "DDCB05FE"

def INBC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED40"

def OUTCB(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED41"

def SBCHLBC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED42"

def LSNNBC(is_first_pass):
	if (is_first_pass):
		return 4
	return "ED438405"

def NEG(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED44"

def RETN(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED45"

def IM0(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED46"

def LDIA(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED47"

def INCCC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED48"

def OUTCC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED49"

def ADCHLBC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED4A"

def LDBCNN(is_first_pass):
	if (is_first_pass):
		return 4
	return "ED4B8405"

def RETI(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED4D"

def INCDC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED50"

def OUTCD(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED51"

def SBCHLDE(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED52"

def LDDENN(is_first_pass):
	if (is_first_pass):
		return 4
	return "ED538405"

def IM2(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED5E"

def INHC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED60"

def OUTCH(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED61"

def SBCHLHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED62"

def RRD(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED67"

def INLC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED68"

def OUTCL(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED69"

def ADCHLHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED6A"

def RLD(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED6F"

def SBCHLSP(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED72"

def LDNNSP(is_first_pass):
	if (is_first_pass):
		return 4
	return "ED738405"

def INAC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED78"

def OUTCA(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED79"

def ADCHLSP(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED7A"

def LDSPNN(is_first_pass):
	if (is_first_pass):
		return 4
	return "ED7B8405"

def LDI(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDA0"

def CPI(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDA1"

def INI(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDA2"

def OUTI(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDA3"

def LDD(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDA8"

def CPD(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDA9"

def IND(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDAA"

def OUTD(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDAB"

def LDIR(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDB0"

def CPIR(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDB1"

def INIR(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDB2"

def OTIR(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDB3"

def LDDR(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDB8"

def PCDR(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDB9"

def INDR(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDBA"

def OTDR(is_first_pass):
	if (is_first_pass):
		return 2
	return "EDBB"

def ADDIYBC(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD09"

def ADDIYDE(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD19"

def LDIYNN(is_first_pass):
	if (is_first_pass):
		return 4
	return "FD218405"

def LDNNIY(is_first_pass):
	if (is_first_pass):
		return 4
	return "FD228405"

def INCIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD23"

def ADDIYIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD29"

def LDIYNN(is_first_pass):
	if (is_first_pass):
		return 4
	return "FD2A8405"

def DECIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD2B"

def INCIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD3405"

def DECIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD3505"

def LDIYdN(is_first_pass,dire):
	if (is_first_pass):
		return 4
	return "FD36"+dire

def ADDIYSP(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD39"

def LDBIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD4605"

def LDCIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD4E05"

def LDDIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD5605"

def LDEIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD5E05"

def LDHIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD6605"

def LDLIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD6E05"

def LDIYdB(is_first_pass):
	if (is_first_pass):
		return 3
	return "FF7005"

def LDIYdC(is_first_pass):
	if (is_first_pass):
		return 3
	return "FF7105"

def LDIYdD(is_first_pass):
	if (is_first_pass):
		return 3
	return "FF7205"

def LDIYdE(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD7305"

def LDIYdH(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD7405"

def LDIYdL(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD7505"

def LDIYdA(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD7705"

def LDAIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD7E05"

def ADDAIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD8605"

def ADCAIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD8E05"

def SUBIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD9605"

def SBCAIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FD9E05"

def ANDIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FDA605"

def XORIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FDAE05"

def ORIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FDB605"

def CPIYd(is_first_pass):
	if (is_first_pass):
		return 3
	return "FDBE05"

def POPIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FDE1"

def EXSPIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FDE3"

def PUSHIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FDE5"

def JPIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FDE9"

def LDSPIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FDF9"

def RLCIYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB0506"

def RRCIYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB050E"

def RLIYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB0516"

def RRIYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB051E"

def SLAIYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB0526"

def SRAIYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB052E"

def SRLIYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB053E"

def BIT0IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB0546"

def BIT1IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB054E"

def BIT2IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB0556"

def BIT3IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB055E"

def BIT4IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB0566"

def BIT5IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB056E"

def BIT6IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB0576"

def BIT7IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB057E"

def RES0IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB0586"

def RES1IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB058E"

def RES2IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB0596"

def RES3IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB059E"

def RES4IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05A6"

def RES5IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05AE"

def RES6IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05B6"

def RES7IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05BE"

def SET0IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05C6"

def SET1IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05CE"

def SET2IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05D6"

def SET3IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05DE"

def SET4IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05E6"

def SET5IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05EE"

def SET6IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05F6"

def SET7IYd(is_first_pass):
	if (is_first_pass):
		return 4
	return "FDCB05FE"


##Esto hay que llenarlo con todas las funciones de arriba
#MappnngOpcodes
map_mnem={
 "NOP": NOP, "LD (BC),A": LDBCA,"INC BC": INCBC, "INC B": INCB, "DEC B": DECB, "LD B,n": LDBN,
 "RLCA": RLCA, "EX AF,AF'": EXAFAF, "ADD HL,BC": ADDHLBC, "LD A,(BC)": LDABC, "DEC BC": DECBC,
 "INC C":INCC, "DEC C": DECC, "LD C,n":LDCN, "RRCA": RRCA, "DJNZ e": DJNZDIS, "LD DE,nn":LDDENN,
 "LD (DE),A": LDDEA, "INC DE": INCDE, "INC D": INCD, "DEC D": DECD, "LD D,n":LDDN, "RLA": RLA,
 "JR e": JRDIS, "ADD HL,DE": ADDHLDE, "LD A,(DE)": LDADE, "DEC DE": DECDE, "INC E": INCE, "DEC E":DECE,
 "LD E,n": LDEN, "RRA":RRA, "JR nz,e": JRNZDIS, "LD HL,nn": LDHLNN, "LD (nn),HL": LDNNHL,
 "INC HL": INCHL, "INC H": INCH, "DEC H": DECH,
 "LD A,(nn)": LDANN,
 "LD A,A": LDAA, "LD A,B": LDAB, "LD A,C":LDAC, "JP p,nn":JPPNN ,"JP nn":JPNN,
 "LD A,n": LDAN,"LD D,B": LDDB, "JP p,nn":JPPNN,
 "LD (IX+d),n": LDIXdN, "LD (IY+d),n": LDIYdN,
 "DEC B": DECB, "DB n": DB,"EQU n": EQU, "CP n": CPN, "JP z,nn": JPZNN, "LD B,A": LDBA,
 "JR z,e": JRZDIS, "CP B": CPB, "JP P,nn": JPPNN, "LD E,A": LDEA, "LD D,A":LDDA,
 "LD E,B": LDEB, "DEC E": DECE, "ADD D": ADDAD, "LD (nn),A": LDNNA, "HALT":HALT, "END": END,"JR nz,e":JRNZDIS,
 "LD A,D": LDAD, "LD A,E": LDAE, "LD A,H": LDAH,
}



