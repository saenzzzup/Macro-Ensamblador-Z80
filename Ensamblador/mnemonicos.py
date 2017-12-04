
#ValidOperands
v_ops=[
"A","B","C","D","E","H","L","R","I","BC","DE","HL","AF","AF'","SP","IX","IY",
"NZ","Z","NC","C","PO","PE","P","M","(HL)","(BC)","(DE)","(SP)","(C)", "(IX)","(IY)","PE"
]

#ValidMnemonicos
v_mnemonicos = ["LD","PUSH","POP","EX","EXX","LDI","LDIR","LDD","LDDR","CPI","CPIR","CPD",
"CPDR","ADD","ADC","SUB","SBC","AND","OR","XOR","CP","INC","DEC","DAA","CPL","NEG",
"CCF","SCF","NOP","HALT","DI","EI","IM","RLCA","RLA","RRCA","RRA","RLC","RL","RRC",
"RR","SLA","SRA","SRL","RLD","RRD","BIT","SET","RES","JP","JR","DJNZ","CALL","RET",
"RETI","RETN","RST","IN","INI","INIR","IND","INDR","OUT","OUTI","OUTIR","OUTD","OTDR",
"ORG","END","DB","DW","DL","EQU","LS","OTIR","CPDR"
]

#Valid directives
v_directives = ["ORG","END","DB","DW","DL","EQU"]

mne_aux = ["BIT","RES","SET"]

p = {"00":"000","08": "001", "10": "010", "18": "011", "20":"100", "28":"101","30": "110", "38": "111"}

b = {"0":"000","1": "001", "2": "010", "3": "011", "4":"100", "5":"101","6": "110", "7": "111"}


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

def END(is_first_pass,value):
	if (is_first_pass):
		return 0
	return ""

def NOP(is_first_pass):
	if (is_first_pass):
		return 1
	return "00"

def LDBCNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "01" + dire

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

def LDBN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "06" + dire

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

def LDCN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "0E" + dire

def RRCA(is_first_pass):
	if (is_first_pass):
		return 1
	return "0F"

def DJNZNN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "10"+ dire

def LDDENN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "11" + dire

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

def LDDN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "16" + dire

def RLA(is_first_pass):
	if (is_first_pass):
		return 1
	return "17"

def JRNN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "18" + dire

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

def LDEN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "1E" + dire

def RRA(is_first_pass):
	if (is_first_pass):
		return 1
	return "1F"

def JRNZNN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "20" + dire

def LDHLNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "21" + dire

def LD_NN_HL(is_first_pass,dire):
	if (is_first_pass):
		return 3
	return "22" + dire

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

def LDHN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "26" + dire

def DAA(is_first_pass):
	if (is_first_pass):
		return 1
	return "27"

def JRZNN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "28" + dire

def ADDHLHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "29"

def LDHL_NN_(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "2A" + dire

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

def LDLN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "2E" + dire

def CPL(is_first_pass):
	if (is_first_pass):
		return 1
	return "2F"

def JRNCNN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "30" + dire

def LDSPNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "31" + dire

def LD_NN_A(is_first_pass,dire):
	if (is_first_pass):
		return 3
	return "32"+dire

def INCSP(is_first_pass):
	if (is_first_pass):
		return 1
	return "33"

def INC_HL_(is_first_pass):
	if (is_first_pass):
		return 1
	return "34"

def DEC_HL_(is_first_pass):
	if (is_first_pass):
		return 1
	return "35"

def LDHLN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "36" + dire

def SCF(is_first_pass):
	if (is_first_pass):
		return 1
	return "37"

def JRCNN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "38" + dire

def ADDHLSP(is_first_pass):
	if (is_first_pass):
		return 1
	return "39"

def LDA_NN_(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "3A" + dire

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

def LDAN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "3E" + dire

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

def LDBH(is_first_pass):
	if (is_first_pass):
		return 1
	return "44"

def LDBL(is_first_pass):
	if (is_first_pass):
		return 1
	return "45"

def LDB_HL_(is_first_pass):
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

def ADDB(is_first_pass):
	if (is_first_pass):
		return 1
	return "80"

def ADDC(is_first_pass):
	if (is_first_pass):
		return 1
	return "81"

def ADDD(is_first_pass):
	if (is_first_pass):
		return 1
	return "82"

def ADDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "83"

def ADDH(is_first_pass):
	if (is_first_pass):
		return 1
	return "84"

def ADDL(is_first_pass):
	if (is_first_pass):
		return 1
	return "85"

def ADDHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "86"

def ADDA(is_first_pass):
	if (is_first_pass):
		return 1
	return "87"

def ADCB(is_first_pass):
	if (is_first_pass):
		return 1
	return "88"

def ADCC(is_first_pass):
	if (is_first_pass):
		return 1
	return "89"

def ADCD(is_first_pass):
	if (is_first_pass):
		return 1
	return "8A"

def ADCE(is_first_pass):
	if (is_first_pass):
		return 1
	return "8B"

def ADCH(is_first_pass):
	if (is_first_pass):
		return 1
	return "8C"

def ADCL(is_first_pass):
	if (is_first_pass):
		return 1
	return "8D"

def ADCHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "8E"

def ADCA(is_first_pass):
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

def SBCB(is_first_pass):
	if (is_first_pass):
		return 1
	return "98"

def SBCC(is_first_pass):
	if (is_first_pass):
		return 1
	return "99"

def SBCD(is_first_pass):
	if (is_first_pass):
		return 1
	return "9A"

def SBCE(is_first_pass):
	if (is_first_pass):
		return 1
	return "9B"

def SBCH(is_first_pass):
	if (is_first_pass):
		return 1
	return "9C"

def SBCL(is_first_pass):
	if (is_first_pass):
		return 1
	return "9D"

def SBCHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "9E"

def SBCA(is_first_pass):
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

def CP_L(is_first_pass):
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

def JPNZNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "C2" + dire

def JPNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "C3" + dire

def CALLNZNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "C4" + dire

def PUSHBC(is_first_pass):
	if (is_first_pass):
		return 1
	return "C5"

def ADDN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "C6" + dire

## 000H 08H 10H 18H 20H 28H 30H 38H
def RSTNN(is_first_pass,dire):
	if (is_first_pass):
		return 1
	else:
		if dire in p.keys():
			dire = "11" + p[dire] + "111"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None

	return dire

def RETZ(is_first_pass):
	if (is_first_pass):
		return 1
	return "C8"

def RET(is_first_pass):
	if (is_first_pass):
		return 1
	return "C9"

def JPZNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "CA" + dire

def CALLZNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "CC" + dire

def CALLNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "CD" + dire

def ADCN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "CE" + dire

def RETNC(is_first_pass):
	if (is_first_pass):
		return 1
	return "D0"

def POPDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "D1"

def JPNCNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "D2" + dire

def OUTNA(is_first_pass,dire):
	if (is_first_pass):
		return 2
	return "D3"

def CALLNCNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "D4" + dire

def PUSHDE(is_first_pass):
	if (is_first_pass):
		return 1
	return "D5"

def SUBN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "D6" + dire

def RETC(is_first_pass):
	if (is_first_pass):
		return 1
	return "D8"

def EXX(is_first_pass):
	if (is_first_pass):
		return 1
	return "D9"

def JPCNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DA" + dire

def INA_NN_(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DB" + dire

def CALLCNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DC" + dire

def SBCN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DE" + dire

def RETPO(is_first_pass):
	if (is_first_pass):
		return 1
	return "E0"

def POPHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "E1"

def JPPONN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "E2" + dire

def EXSPHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "E3"

def CALLPONN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "E4" + dire

def PUSHHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "E5"

def ANDN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "E6" + dire

def RETPE(is_first_pass):
	if (is_first_pass):
		return 1
	return "E8"

def JPHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "E9"

def JPPENN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "EA" + dire

def EXDEHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "EB"

def CALLPENN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "EC" + dire

def XORN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "EE" + dire

def RETP(is_first_pass):
	if (is_first_pass):
		return 1
	return "F0"

def POPAF(is_first_pass):
	if (is_first_pass):
		return 1
	return "F1"

def JPPNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "F2" + dire

def DI(is_first_pass):
	if (is_first_pass):
		return 1
	return "F3"

def CALLPNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "F4" + dire

def PUSHAF(is_first_pass):
	if (is_first_pass):
		return 1
	return "F5"

def ORN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "F6" + dire

def RETM(is_first_pass):
	if (is_first_pass):
		return 1
	return "F8"

def LDSPHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "F9"

def JPMNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FA" + dire

def EI(is_first_pass):
	if (is_first_pass):
		return 1
	return "FB"

def CALLMNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FC" + dire

def CPN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FE" + dire

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
	return "CB07"

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

def RL_B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB10"

def RL_C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB11"

def RL_D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB12"

def RL_E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB13"

def RL_H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB14"

def RL_L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB15"

def RL_HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB16"

def RL_A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB17"

def RR_B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB18"

def RR_C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB19"

def RR_D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1A"

def RR_E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1B"

def RR_H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1C"

def RR_L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB1D"

def RR_HL(is_first_pass):
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

#N = 1 2 3 4 5 6 7
def BITNB(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "01" + b[dire] + "000"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None

	return "CB" + dire

def BITNC(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "01" + b[dire] + "001"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def BITND(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "01" + b[dire] + "010"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def BITNE(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "01" + b[dire] + "011"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def BITNH(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "01" + b[dire] + "100"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def BITNL(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "01" + b[dire] + "101"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def BITNHL(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "01" + b[dire] + "110"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def BITNA(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "01" + b[dire] + "111"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

#N = 1 2 3 4 5 6 7
def RESNB(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "10" + b[dire] + "000"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def RESNC(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "10" + b[dire] + "001"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def RESND(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "10" + b[dire] + "010"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def RESNE(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "10" + b[dire] + "011"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def RESNH(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "10" + b[dire] + "100"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def RESNL(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "10" + b[dire] + "101"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def RESNHL(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "10" + b[dire] + "110"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def RESNA(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "10" + b[dire] + "111"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

# N = 1 2 3 4 5 6 7
def SETNB(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "11" + b[dire] + "000"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def SETNC(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "11" + b[dire] + "001"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def SETND(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "11" + b[dire] + "010"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def SETNE(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "11" + b[dire] + "011"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def SETNH(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "11" + b[dire] + "100"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def SETNL(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "11" + b[dire] + "101"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def SETNHL(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "11" + b[dire] + "110"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def SETNA(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		dire = dire[1:]
		if dire in b.keys():
			dire = "11" + b[dire] + "111"
			dire = hex(int(dire,2))[2:].upper()
		else:
			return None
			
	return "CB" + dire

def ADDIXBC(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD09"

def ADDIXDE(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD19"

def LDIXNN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD21" + dire

def LD_NN_IX(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD22" + dire

def INCIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD23"

def ADDIXIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD29"

def LDIX_NN_(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD2A" + dire

def DECIX(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD2B"

def INCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD34" + dire

def DECIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD35" + dire

def LDIXdN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD36" + dire

def ADDIXSP(is_first_pass):
	if (is_first_pass):
		return 2
	return "DD39"

def LDBIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD46" + dire

def LDCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD4E" + dire

def LDDIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD56" + dire

def LDEIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD5E" + dire

def LDHIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD66" + dire

def LDLIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD6E" + dire

def LDIXdB(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD70" + dire

def LDIXdC(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD71" + dire

def LDIXdD(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD72" + dire

def LDIXdE(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD73" + dire

def LDIXdH(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD74" + dire

def LDIXdL(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD75" + dire

def LDIXdA(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD77" + dire

def LDAIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD7E" + dire

def ADDIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD86" + dire

def ADCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD8E" + dire

def SUBIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD96" + dire

def SBCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD9E" + dire

def ANDIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DDA6" + dire

def XORIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DDAE" + dire

def ORIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DDB6" + dire

def CPIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DDBE" + dire

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

def RLCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DDCB" + dire + "06"

def RRCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DDCB" + dire + "0E"

def RLIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DDCB" + dire + "16"

def RRIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DDCB" + dire + "1E"

def SLAIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DDCB" + dire + "26"

def SRAIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DDCB" + dire + "2E"

def SRLIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DDCB" + dire + "3E"

##
def BITNIXd(is_first_pass,num,dire):
	if (is_first_pass):
		return 4
	else:
		if num in b.keys():
			num = "01" + b[num] + "110"
			num = hex(int(num,2))[2:].upper()
		else:
			return None
			
	return "DDCB" + dire + num

def RESNIXd(is_first_pass,num,dire):
	if (is_first_pass):
		return 4
	else:
		if num in b.keys():
			num = "10" + b[num] + "110"
			num = hex(int(num,2))[2:].upper()
		else:
			return None
			
	return "DDCB" + dire + num

def SETNIXd(is_first_pass,num,dire):
	if (is_first_pass):
		return 4
	else:
		if num in b.keys():
			num = "11" + b[num] + "110"
			num = hex(int(num,2))[2:].upper()
		else:
			return None
			
	return "DDCB" + dire + num

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

def LS_NN_BC(is_first_pass,dire):
	if (is_first_pass):
		return 4
	return "ED43"+dire

def NEG(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED44"

def RETN(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED45"

def IMN(is_first_pass,dire):
	if (is_first_pass):
		return 2
	else:
		if dire == "01":
			dire = "ED56"
		elif dire == "00":
			dire = "ED46"
		elif dire == "02":
			dire = "ED5E"
	return dire

def LDIA(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED47"

def INC_C_(is_first_pass):
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

def LDBC_NN_(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "ED4B" + dire

def RETI(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED4D"

def INDC(is_first_pass):
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

def LDDE_NN_(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "ED53" + dire

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

def LD_NN_SP(is_first_pass,dire):
	if (is_first_pass):
		return 4
	return "ED73"+dire

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

def LDSP_NN_(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "ED7B" + dire

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

def CP_D(is_first_pass):
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

def CPDR(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED89"

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

def LDIYNN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD21" + dire

def LD_NN_IY(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD22" + dire

def INCIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD23"

def ADDIYIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD29"

def LDIY_NN_(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD2A" + dire

def DECIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD2B"

def INCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD34" + dire

def DECIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD35" + dire

def LDIYdN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD36" + dire

def ADDIYSP(is_first_pass):
	if (is_first_pass):
		return 2
	return "FD39"

def LDBIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD46" + dire

def LDCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD4E" + dire

def LDDIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD56" + dire

def LDEIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD5E" + dire

def LDHIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD66" + dire

def LDLIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD6E" + dire

def LDIYdB(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD70" + dire

def LDIYdC(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD71" + dire

def LDIYdD(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD72" + dire

def LDIYdE(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD73" + dire

def LDIYdH(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD74" + dire

def LDIYdL(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD75" + dire

def LDIYdA(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD77" + dire

def LDAIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD7E" + dire

def ADDIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD86" + dire

def ADCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD8E" + dire

def SUBIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD96" + dire

def SBCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD9E" + dire

def ANDIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FDA6" + dire

def XORIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FDAE" + dire

def ORIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FDB6" + dire

def CPIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FDBE" + dire

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
	return "FDE5"

def LDSPIY(is_first_pass):
	if (is_first_pass):
		return 2
	return "FDF9"

def RLCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FDCB" + dire + "06"

def RRCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FDCB" + dire + "0E"

def RLIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FDCB" + dire + "16"

def RRIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FDCD" + dire + "1E"

def SLAIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FDCB" + dire + "26"

def SRAIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FDCB" + dire +"2E"

def SRLIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FDCB" + dire + "3E"

##
def BITNIYd(is_first_pass,num,dire):
	if (is_first_pass):
		return 4
	else:
		if num in b.keys():
			num = "01" + b[num] + "110"
			num = hex(int(num,2))[2:].upper()
		else:
			return None
			
	return "FDCB" + dire + num

def RESNIYd(is_first_pass,num,dire):
	if (is_first_pass):
		return 4
	else:
		if num in b.keys():
			num = "10" + b[num] + "110"
			num = hex(int(num,2))[2:].upper()
		else:
			return None
			
	return "FDCB" + dire + num

def SETNIYd(is_first_pass,num,dire):
	if (is_first_pass):
		return 4
	else:
		if num in b.keys():
			num = "11" + b[num] + "110"
			num = hex(int(num,2))[2:].upper()
		else:
			return None
			
	return "FDCB" + dire + num

#MappNgOpcodes
map_mnem = {
	"DB N":DB,
	"END NN":END,
	"EQU N":EQU,
	"DL N":DL,
	"NOP":NOP,
	"LD BC, NN": LDBCNN,
	"LD (BC), A":LDBCA,
	"INC BC":INCBC,
	"INC B":INCB,
	"DEC B":DECB,
	"LD B, N":LDBN,
	"RLCA":RLCA,
	"EX AF, AF'":EXAFAF,
	"ADD HL, BC":ADDHLBC,
	"LD A, (BC)":LDABC,
	"DEC BC":DECBC,
	"INC C":INCC,
	"DEC C":DECC,
	"LD C, N":LDCN,
	"RRCA":RRCA,
	"DJNZ NN":DJNZNN,
	"LD DE, NN":LDDENN,
	"LD (DE), A":LDDEA,
	"INC DE":INCDE,
	"INC D":INCD,
	"DEC D":DECD,
	"LD D, N":LDDN,
	"RLA":RLA,
	"JR NN":JRNN,
	"ADD HL, DE":ADDHLDE,
	"LD A, (DE)":LDADE,
	"DEC DE":DECDE,
	"INC E":INCE,
	"DEC E":DECE,
	"LD E, N":LDEN,
	"RRA":RRA,
	"JR NZ, NN":JRNZNN,
	"LD HL, NN":LDHLNN,
	"LD (NN), HL":LD_NN_HL,
	"INC HL":INCHL,
	"INC H":INCH,
	"DEC H":DECH,
	"LD H, N":LDHN,
	"DAA":DAA,
	"JR Z, NN":JRZNN,
	"ADD HL, HL":ADDHLHL,
	"LD HL, (NN)":LDHL_NN_,
	"DEC HL":DECHL,
	"INC L":INCL,
	"DEC L":DECL,
	"LD L, N":LDLN,
	"CPL":CPL,
	"JR NC, NN":JRNCNN,
	"LD SP, NN":LDSPNN,
	"LD (NN), A":LD_NN_A,
	"INC SP":INCSP,
	"INC (HL)":INC_HL_,
	"DEC (HL)":DEC_HL_,
	"LD (HL), N":LDHLN,
	"SCF":SCF,
	"JR C, NN": JRCNN,
	"ADD HL, SP":ADDHLSP,
	"LD A, N": LDAN,
	"LD A, NN": LDAN,
	"LD A, (NN)":LDA_NN_,
	"DEC SP":DECSP,
	"INC A":INCA,
	"DEC A":DECA,
	"CCF":CCF,
	"LD B, B":LDBB,
	"LD B, C":LDBC,
	"LD B, D":LDBD,
	"LD B, E":LDBE,
	"LD B, H":LDBH,
	"LD B, L":LDBL,
	"LD B, (HL)":LDB_HL_,
	"LD B, A":LDBA,
	"LD C, B":LDCB,
	"LD C, C":LDCC,
	"LD C, D":LDCD,
	"LD C, E":LDCE,
	"LD C, H":LDCH,
	"LD C, L":LDCL,
	"LD C, (HL)":LDCHL,
	"LD C, A":LDCA,
	"LD D, B":LDDB,
	"LD D, C":LDDC,
	"LD D, D":LDDD,
	"LD D, E":LDDE,
	"LD D, H":LDDH,
	"LD D, L":LDDL,
	"LD D, (HL)":LDDHL,
	"LD D, A":LDDA,
	"LD E, B":LDEB,
	"LD E, C":LDEC,
	"LD E, D":LDED,
	"LD E, E":LDEE,
	"LD E, H":LDEH,
	"LD E, L":LDEL,
	"LD E, (HL)":LDEHL,
	"LD E, A":LDEA,
	"LD H, B":LDHB,
	"LD H, C":LDHC,
	"LD H, D":LDHD,
	"LD H, E":LDHE,
	"LD H, H":LDHH,
	"LD H, L":LDHL,
	"LD H, (HL)":LDHHL,
	"LD H, A":LDHA,
	"LD L, B":LDLB,
	"LD L, C":LDLC,
	"LD L, D":LDLD,
	"LD L, E":LDLE,
	"LD L, H":LDLH,
	"LD L, L":LDLL,
	"LD L, (HL)":LDLHL,
	"LD L, A":LDLA,
	"LD (HL), B":LDHLB,
	"LD (HL), C":LDHLC,
	"LD (HL), D":LDHLD,
	"LD (HL), E":LDHLE,
	"LD (HL), H":LDHLH,
	"LD (HL), L":LDHLL,
	"HALT":HALT,
	"LD (HL), A":LDHLA,
	"LD A, B":LDAB,
	"LD A, C":LDAC,
	"LD A, D":LDAD,
	"LD A, E":LDAE,
	"LD A, H":LDAH,
	"LD A, L":LDAL,
	"LD A, (HL)":LDAHL,
	"LD A, A":LDAA,
	"ADD B":ADDB,
	"ADD C":ADDC,
	"ADD D":ADDD,
	"ADD E":ADDE,
	"ADD H":ADDH,
	"ADD L":ADDL,
	"ADD (HL)":ADDHL,
	"ADD A":ADDA,
	"ADC B":ADCB,
	"ADC C":ADCC,
	"ADC D":ADCD,
	"ADC E":ADCE,
	"ADC H":ADCH,
	"ADC L":ADCL,
	"ADC (HL)":ADCHL,
	"ADC A":ADCA,
	"SUB B":SUBB,
	"SUB C":SUBC,
	"SUB D":SUBD,
	"SUB E":SUBE,
	"SUB H":SUBH,
	"SUB L":SUBL,
	"SUB (HL)":SUBHL,
	"SUB A":SUBA,
	"SBC B":SBCB,
	"SBC C":SBCC,
	"SBC D":SBCD,
	"SBC E":SBCE,
	"SBC H":SBCH,
	"SBC L":SBCL,
	"SBC (HL)":SBCHL,
	"SBC A":SBCA,
	"AND B":ANDB,
	"AND C":ANDC,
	"AND D":ANDD,
	"AND E":ANDE,
	"AND H":ANDH,
	"AND L":ANDL,
	"AND (HL)":ANDHL,
	"AND A":ANDA,
	"XOR B":XORB,
	"XOR C":XORC,
	"XOR D":XORD,
	"XOR E":XORE,
	"XOR H":XORH,
	"XOR L":XORL,
	"XOR (HL)":XORHL,
	"XOR A":XORA,
	"OR B":ORB,
	"OR C":ORC,
	"OR D":ORD,
	"OR E":ORE,
	"OR H":ORH,
	"OR L":ORL,
	"OR (HL)":ORHL,
	"OR A":ORA,
	"CP B":CPB,
	"CP C":CPC,
	"CP D":CPD,
	"CP E":CPE,
	"CP H":CPH,
	"CP L":CP_L,
	"CP (HL)":CPHL,
	"CP A":CPA,
	"RET NZ":RETNZ,
	"POP BC":POPBC,
	"JP NZ, NN":JPNZNN,
	"JP NN":JPNN,
	"CALL NZ, NN":CALLNZNN,
	"PUSH BC":PUSHBC,
	"ADD N":ADDN,
	"RST NN":RSTNN,
	"RET Z":RETZ,
	"RET":RET,
	"JP Z, NN":JPZNN,
	"CALL Z, NN":CALLZNN,
	"CALL NN":CALLNN,
	"ADC N":ADCN,
	"RET NC":RETNC,
	"POP DE":POPDE,
	"JP NC, NN":JPNCNN,
	"OUT (NN), A":OUTNA,
	"CALL NC, NN":CALLNCNN,
	"PUSH DE":PUSHDE,
	"SUB NN":SUBN,
	"RET C":RETC,
	"EXX":EXX,
	"JP C, NN":JPCNN,
	"IN A, (NN)":INA_NN_,
	"CALL C, NN":CALLCNN,
	"SBC N":SBCN,
	"RET PO":RETPO,
	"POP HL":POPHL,
	"JP PO, NN":JPPONN,
	"EX (SP), HL":EXSPHL,
	"CALL PO, NN":CALLPONN,
	"PUSH HL":PUSHHL,
	"AND N":ANDN,
	"RET PE":RETPE,
	"JP (HL)":JPHL,
	"JP PE, NN":JPPENN,
	"EX DE, HL":EXDEHL,
	"CALL PE, NN":CALLPENN,
	"XOR N":XORN,
	"RET P":RETP,
	"POP AF":POPAF,
	"JP P, NN":JPPNN,
	"DI":DI,
	"CALL P, NN":CALLPNN,
	"PUSH AF":PUSHAF,
	"OR NN":ORN,
	"RET M":RETM,
	"LD SP, HL":LDSPHL,
	"JP M, NN":JPMNN,
	"EI":EI,
	"CALL M, NN":CALLMNN,
	"CP N": CPN,
	"CP NN":CPN,
	"RLC B":RLCB,
	"RLC C":RLCC,
	"RLC D":RLCD,
	"RLC E":RLCE,
	"RLC H":RLCH,
	"RLC L":RLCL,
	"RLC (HL)":RLCHL,
	"RLC A":RLC_A,
	"RRC B":RRC_B,
	"RRC C":RRC_C,
	"RRC D":RRC_D,
	"RRC E":RRC_E,
	"RRC H":RRC_H,
	"RRC L":RRC_L,
	"RRC (HL)":RRC_HL,
	"RRC A":RRC_A,
	"RL B":RL_B,
	"RL C":RL_C,
	"RL D":RL_D,
	"RL E":RL_E,
	"RL H":RL_H,
	"RL L":RL_L,
	"RL (HL)":RL_HL,
	"RL A":RL_A,
	"RR B":RR_B,
	"RR C":RR_C,
	"RR D":RR_D,
	"RR E":RR_E,
	"RR H":RR_H,
	"RR L":RR_L,
	"RR (HL)":RR_HL,
	"RR A":RRA,
	"SLA B":SLAB,
	"SLA C":SLAC,
	"SLA D":SLAD,
	"SLA E":SLAE,
	"SLA H":SLAH,
	"SLA L":SLAL,
	"SLA (HL)":SLAHL,
	"SLA A":SLAA,
	"SRA B":SRAB,
	"SRA C":SRAC,
	"SRA D":SRAD,
	"SRA E":SRAE,
	"SRA H":SRAH,
	"SRA L":SRAL,
	"SRA (HL)":SRAHL,
	"SRA A":SRAA,
	"SRL B":SRLB,
	"SRL C":SRLC,
	"SRL D":SRLD,
	"SRL E":SRLE,
	"SRL H":SRLH,
	"SRL L":SRLL,
	"SRL (HL)":SRLHL,
	"SRL A":SRLA,
	"BIT N, B":BITNB,
	"BIT N, C":BITNC,
	"BIT N, D":BITND,
	"BIT N, E":BITNE,
	"BIT N, H":BITNH,
	"BIT N, L":BITNL,
	"BIT N, (HL)":BITNHL,
	"BIT N, A":BITNA,
	"RES N, B":RESNB,
	"RES N, C":RESNC,
	"RES N, D":RESND,
	"RES N, E":RESNE,
	"RES N, H":RESNH,
	"RES N, L":RESNL,
	"RES N, (HL)":RESNHL,
	"RES N, A":RESNA,
	"SET N, B":SETNB,
	"SET N, C":SETNC,
	"SET N, D":SETND,
	"SET N, E":SETNE,
	"SET N, H":SETNH,
	"SET N, L":SETNL,
	"SET N, (HL)":SETNHL,
	"SET N, A":SETNA,
	"ADD IX, BC":ADDIXBC,
	"ADD IX, DE":ADDIXDE,
	"LD IX, NN":LDIXNN,
	"LD (NN), IX":LD_NN_IX,
	"INC IX":INCIX,
	"ADD IX, IX":ADDIXIX,
	"LD IX, (NN)":LDIX_NN_,
	"DEC IX":DECIX,
	"INC (IX + d)":INCIXd,
	"DEC (IX + d)":DECIXd,
	"LD (IX + d), N":LDIXdN,
	"ADD IX, SP":ADDIXSP,
	"LD B, (IX + d)":LDBIXd,
	"LD C, (IX + d)":LDCIXd,
	"LD D, (IX + d)":LDDIXd,
	"LD E, (IX + d)":LDEIXd,
	"LD H, (IX + d)":LDHIXd,
	"LD L, (IX + d)":LDLIXd,
	"LD (IX + d), B":LDIXdB,
	"LD (IX + d), C":LDIXdC,
	"LD (IX + d), D":LDIXdD,
	"LD (IX + d), E":LDIXdE,
	"LD (IX + d), H":LDIXdH,
	"LD (IX + d), L":LDIXdL,
	"LD (IX + d), A":LDIXdA,
	"LD A, (IX + d)":LDAIXd,
	"ADD (IX + d)":ADDIXd,
	"ADC (IX + d)":ADCIXd,
	"SUB (IX + d)":SUBIXd,
	"SBC (IX + d)":SBCIXd,
	"AND (IX + d)":ANDIXd,
	"XOR (IX + d)":XORIXd,
	"OR (IX + d)":ORIXd,
	"CP (IX + d)":CPIXd,
	"POP IX":POPIX,
	"EX (SP), IX":EXSPIX,
	"PUSH IX":PUSHIX,
	"JP (IX)":JPIX,
	"LD SP, IX":LDSPIX,
	"RLC (IX + d)":RLCIXd,
	"RRC (IX + d)":RRCIXd,
	"RL (IX + d)":RLIXd,
	"RR (IX + d)":RRIXd,
	"SLA (IX + d)":SLAIXd,
	"SRA (IX + d)":SRAIXd,
	"SRL (IX + d)":SRLIXd,
	"BIT N, (IX + d)":BITNIXd,
	"RES N, (IX + d)":RESNIXd,
	"SET N, (IX + d)":SETNIXd,
	"IN B, (C)":INBC,
	"OUT (C), B":OUTCB,
	"SBC HL, BC":SBCHLBC,
	"LS (NN), BC":LS_NN_BC,
	"NEG":NEG,
	"RETN":RETN,
	"IM N":IMN,
	"LD I, A":LDIA,
	"IN C, (C)":INC_C_,
	"OUT (C), C":OUTCC,
	"ADC HL, BC":ADCHLBC,
	"LD BC, (NN)":LDBC_NN_,
	"RETI":RETI,
	"IN D, (C)":INDC,
	"OUT (C), D":OUTCD,
	"SBC HL, DE":SBCHLDE,
	"LD DE, (NN)":LDDE_NN_,
	"IN H, (C)":INHC,
	"OUT (C), H":OUTCH,
	"SBC HL, HL":SBCHLHL,
	"RRD":RRD,
	"IN L, (C)":INLC,
	"OUT (C), L":OUTCL,
	"ADC HL, HL":ADCHLHL,
	"RLD":RLD,
	"SBC HL, SP":SBCHLSP,
	"LD (NN), SP":LD_NN_SP,
	"IN A, (C)":INAC,
	"OUT (C), A":OUTCA,
	"ADC HL, SP":ADCHLSP,
	"LD SP, (NN)":LDSP_NN_,
	"LDI":LDI,
	"CPI":CPI,
	"INI":INI,
	"OUTI":OUTI,
	"LDD":LDD,
	"CPD":CP_D,
	"IND":IND,
	"OUTD":OUTD,
	"LDIR":LDIR,
	"CPIR":CPIR,
	"INIR":INIR,
	"OTIR":OTIR,
	"LDDR":LDDR,
	"CPDR":CPDR,
	"INDR":INDR,
	"OTDR":OTDR,
	"ADD IY, BC":ADDIYBC,
	"ADD IY, DE":ADDIYDE,
	"LD IY, NN":LDIYNN,
	"LD (NN), IY":LD_NN_IY,
	"INC IY":INCIY,
	"ADD IY, IY":ADDIYIY,
	"LD IY, (NN)":LDIY_NN_,
	"DEC IY":DECIY,
	"INC (IY + d)":INCIYd,
	"DEC (IY + d)":DECIYd,
	"LD (IY + d), N":LDIYdN,
	"ADD IY, SP":ADDIYSP,
	"LD B, (IY + d)":LDBIYd,
	"LD C, (IY + d)":LDCIYd,
	"LD D, (IY + d)":LDDIYd,
	"LD E, (IY + d)":LDEIYd,
	"LD H, (IY + d)":LDHIYd,
	"LD L, (IY + d)":LDLIYd,
	"LD (IY + d), B":LDIYdB,
	"LD (IY + d), C":LDIYdC,
	"LD (IY + d), D":LDIYdD,
	"LD (IY + d), E":LDIYdE,
	"LD (IY + d), H":LDIYdH,
	"LD (IY + d), L":LDIYdL,
	"LD (IY + d), A":LDIYdA,
	"LD A, (IY + d)":LDAIYd,
	"ADD (IY + d)":ADDIYd,
	"ADC (IY + d)":ADCIYd,
	"SUB (IY + d)":SUBIYd,
	"SBC (IY + d)":SBCIYd,
	"AND (IY + d)":ANDIYd,
	"XOR (IY + d)":XORIYd,
	"OR (IY + d)":ORIYd,
	"CP (IY + d)":CPIYd,
	"POP IY":POPIY,
	"EX (SP), IY":EXSPIY,
	"PUSH IY":PUSHIY,
	"JP (IY)":JPIY,
	"LD SP, IY":LDSPIY,
	"RLC (IY + d)":RLCIYd,
	"RRC (IY + d)":RRCIYd,
	"RL (IY + d)":RLIYd,
	"RR (IY + d)":RRIYd,
	"SLA (IY + d)":SLAIYd,
	"SRA (IY + d)":SRAIYd,
	"SRL (IY + d)":SRLIYd,
	"BIT N, (IY + d)":BITNIYd,
	"RES N, (IY + d)":RESNIYd,
	"SET N, (IY + d)":SETNIYd,
}

