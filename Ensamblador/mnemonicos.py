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

def DJNZDIS(is_first_pass):
	if (is_first_pass):
		return 2
	return "10"

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

def JRDIS(is_first_pass):
	if (is_first_pass):
		return 2
	return "18"

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

def JRNZDIS(is_first_pass):
	if (is_first_pass):
		return 2
	return "20"

def LDHLNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "21" + dire

def LDNNHL(is_first_pass):
	if (is_first_pass):
		return 3
	return "22"

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

def JRZDIS(is_first_pass):
	if (is_first_pass):
		return 2
	return "28"

def ADDHLHL(is_first_pass):
	if (is_first_pass):
		return 1
	return "29"

def LDHLNN(is_first_pass, dire):
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

def JRNCDIS(is_first_pass):
	if (is_first_pass):
		return 2
	return "30"

def LDSPNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "31" + dire

def LDNNA(is_first_pass):
	if (is_first_pass):
		return 3
	return "32"

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

def LDHLN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "36" + dire

def SCF(is_first_pass):
	if (is_first_pass):
		return 1
	return "37"

def JRCDIS(is_first_pass):
	if (is_first_pass):
		return 2
	return "38"

def ADDHLSP(is_first_pass):
	if (is_first_pass):
		return 1
	return "39"

def LDANN(is_first_pass, dire):
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

def LDBHNN(is_first_pass, dire):
	if (is_first_pass):
		return 1
	return "44" + dire

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

def ADDAN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "C6" + dire

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

def ADCAN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "CE" + dire

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

def JPNCNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "D2" + dire

def OUTNA(is_first_pass):
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

def JPCNN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DA" + dire

def INAN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DB" + dire

def CALLCN(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DC" + dire

def SBCAN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DE" + dire

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

def JEPENN(is_first_pass, dire):
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

def RST38H(is_first_pass):
	if (is_first_pass):
		return 1
	return "FF"

def RLCB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLCC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLCD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLCE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLCH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLCL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLCHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLCA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRCB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRCC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRCD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRCE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRCH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRCL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRCHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRCA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RLA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RRA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SLAB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SLAC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SLAD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SLAE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SLAH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SLAL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SLAHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SLAA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRAB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRAC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRAD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRAE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRAH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRAL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRAHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRAA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRLB(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRLC(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRLD(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRLE(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRLH(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRLL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRLHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SRLA(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT0B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT0C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT0D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT0E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT0H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT0L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT0HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT0A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT1B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT1C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT1D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT1E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT1H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT1L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT1HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT1A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT2B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT2C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT2D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT2E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT2H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT2L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT2HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT2A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT3B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT3C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT3D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT3E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT3H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT3L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT3HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT3A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT4B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT4C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT4D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT4E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT4H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT4L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT4HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT4A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT5B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT5C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT5D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT5E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT5H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT5L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT5HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT5A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT6B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT6C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT6D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT6E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT6H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT6L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT6HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT6A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT7B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT7C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT7D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT7E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT7H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT7L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT7HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def BIT7A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES0B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES0C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES0D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES0E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES0H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES0L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES0HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES0A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES1B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES1C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES1D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES1E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES1H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES1L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES1HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES1A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES2B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES2C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES2D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES2E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES2H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES2L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES2HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES2A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES3B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES3C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES3D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES3E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES3H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES3L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES3HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES3A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES4B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES4C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES4D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES4E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES4H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES4L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES4HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES4A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES5B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES5C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES5D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES5E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES5H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES5L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES5HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES5A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES6B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES6C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES6D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES6E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES6H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES6L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES6HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES6A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES7B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES7C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES7D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES7E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES7H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES7L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES7HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def RES7A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET0B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET0C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET0D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET0E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET0H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET0L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET0HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET0A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET1B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET1C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET1D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET1E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET1H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET1L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET1HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET1A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET2B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET2C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET2D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET2E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET2H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET2L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET2HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET2A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET3B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET3C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET3D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET3E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET3H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET3L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET3HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET3A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET4B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET4C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET4D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET4E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET4H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET4L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET4HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET4A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET5B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET5C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET5D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET5E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET5H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET5L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET5HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET5A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET6B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET6C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET6D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET6E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET6H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET6L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET6HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET6A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET7B(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET7C(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET7D(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET7E(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET7H(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET7L(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET7HL(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def SET7A(is_first_pass):
	if (is_first_pass):
		return 2
	return "CB"

def ADDIXBC(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def ADDIXDE(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def LDIXNN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def LDNNIX(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def INCIX(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def ADDIXIX(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def LDIXNN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def DECIX(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def INCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def DECIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDIXdN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def ADDIXSP(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def LDBIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDDIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDEIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDHIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDLIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDIXdB(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDIXdC(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDIXdD(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDIXdE(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDIXdH(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDIXdL(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDIXdA(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def LDAIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def ADDAIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def ADCAIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def SUBIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def SBCAIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def ANDIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def XORIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def ORIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def CPIXd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "DD" + dire

def POPIX(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def EXSPIX(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def PUSHIX(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def JPIX(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def LDSPIX(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "DD" + dire

def RLCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RRCIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RLIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RRIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SLAIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SRAIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SRLIXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def BIT0IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def BIT1IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def BIT2IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def BIT3IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def BIT4IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def BIT5IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def BIT6IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def BIT7IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RES0IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RES1IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RES2IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RES3IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RES4IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RES5IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RES6IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def RES7IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SET0IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SET1IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SET2IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SET3IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SET4IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SET5IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SET6IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def SET7IXd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "DD" + dire

def INBC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OUTCB(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def SBCHLBC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def LSNNBC(is_first_pass):
	if (is_first_pass):
		return 4
	return "ED"

def NEG(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def RETN(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "ED" + dire

def IM0(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def LDIA(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def INCCC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OUTCC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def ADCHLBC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def LDBCNN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "ED" + dire

def RETI(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def INCDC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OUTCD(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def SBCHLDE(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def LDDENN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "ED" + dire

def IM2(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def INHC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OUTCH(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def SBCHLHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def RRD(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def INLC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OUTCL(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def ADCHLHL(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def RLD(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def SBCHLSP(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def LDNNSP(is_first_pass):
	if (is_first_pass):
		return 4
	return "ED"

def INAC(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OUTCA(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def ADCHLSP(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def LDSPNN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "ED" + dire

def LDI(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def CPI(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def INI(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OUTI(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def LDD(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def CPD(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def IND(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OUTD(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def LDIR(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def CPIR(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def INIR(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OTIR(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def LDDR(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def PCDR(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def INDR(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def OTDR(is_first_pass):
	if (is_first_pass):
		return 2
	return "ED"

def ADDIYBC(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def ADDIYDE(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def LDIYNN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def LDNNIY(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def INCIY(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def ADDIYIY(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def LDIYNN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def DECIY(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def INCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def DECIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDIYdN(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def ADDIYSP(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def LDBIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDDIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDEIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDHIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDLIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDIYdB(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FF" + dire

def LDIYdC(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FF" + dire

def LDIYdD(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FF" + dire

def LDIYdE(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDIYdH(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDIYdL(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDIYdA(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def LDAIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def ADDAIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def ADCAIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def SUBIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def SBCAIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def ANDIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def XORIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def ORIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def CPIYd(is_first_pass, dire):
	if (is_first_pass):
		return 3
	return "FD" + dire

def POPIY(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def EXSPIY(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def PUSHIY(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def JPIY(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def LDSPIY(is_first_pass, dire):
	if (is_first_pass):
		return 2
	return "FD" + dire

def RLCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RRCIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RLIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RRIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SLAIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SRAIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SRLIYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def BIT0IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def BIT1IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def BIT2IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def BIT3IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def BIT4IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def BIT5IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def BIT6IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def BIT7IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RES0IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RES1IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RES2IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RES3IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RES4IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RES5IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RES6IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def RES7IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SET0IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SET1IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SET2IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SET3IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SET4IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SET5IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SET6IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire

def SET7IYd(is_first_pass, dire):
	if (is_first_pass):
		return 4
	return "FD" + dire



"""def DB(is_first_pass,value):
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
"""

##Esto hay que llenarlo con todas las funciones de arriba
#MappnngOpcodes

"""map_mnem={
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
}"""

map_mnem = {
	"NOP":NOP,
	"LD BC, NN":LDBCNN,
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
	"DJNZ DIS":DJNZDIS,
	"LD DE, NN":LDDENN,
	"LD (DE), A":LDDEA,
	"INC DE":INCDE,
	"INC D":INCD,
	"DEC D":DECD,
	"LD D, N":LDDN,
	"RLA":RLA,
	"JR DIS":JRDIS,
	"ADD HL, DE":ADDHLDE,
	"LD A, (DE)":LDADE,
	"DEC DE":DECDE,
	"INC E":INCE,
	"DEC E":DECE,
	"LD E, N":LDEN,
	"RRA":RRA,
	"JR NZ, DIS":JRNZDIS,
	"LD HL, NN":LDHLNN,
	"LD(NN), HL":LDNNHL,
	"INC HL":INCHL,
	"INC H":INCH,
	"DEC H":DECH,
	"LD H, N":LDHN,
	"DAA":DAA,
	"JR Z, DIS":JRZDIS,
	"ADD HL, HL":ADDHLHL,
	"LD (HL), (NN)":LDHLNN,
	"DEC HL":DECHL,
	"INC L":INCL,
	"DEC L":DECL,
	"LD L, N":LDLN,
	"CPL":CPL,
	"JR NC, DIS":JRNCDIS,
	"LD SP, NN":LDSPNN,
	"LD (NN), A":LDNNA,
	"INC SP":INCSP,
	"INC (HL)":INCHL,
	"DEC (HL)":DECHL,
	"LD (HL), N":LDHLN,
	"SCF":SCF,
	"JR C, DIS":JRCDIS,
	"ADD HL, SP":ADDHLSP,
	"LD A, (NN)":LDANN,
	"DEC SP":DECSP,
	"INC A":INCA,
	"DEC A":DECA,
	"LD A,N":LDAN,
	"CCF":CCF,
	"LD B, B":LDBB,
	"LD B, C":LDBC,
	"LD B, D":LDBD,
	"LD B, E":LDBE,
	"LD B, H, NN":LDBHNN,
	"LD B, L":LDBL,
	"LD B, (HL)":LDBHL,
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
	"ADD A, B":ADDAB,
	"ADD A, C":ADDAC,
	"ADD A, D":ADDAD,
	"ADD A, E":ADDAE,
	"ADD A, H":ADDAH,
	"ADD A, L":ADDAL,
	"ADD A, (HL)":ADDAHL,
	"ADD A, A":ADDAA,
	"ADC A, B":ADCAB,
	"ADC A, C":ADCAC,
	"ADC A, D":ADCAD,
	"ADC A, E":ADCAE,
	"ADC A, H":ADCAH,
	"ADC A, L":ADCAL,
	"ADC A, (HL)":ADCAHL,
	"ADC A, A":ADCAA,
	"SUB B":SUBB,
	"SUB C":SUBC,
	"SUB D":SUBD,
	"SUB E":SUBE,
	"SUB H":SUBH,
	"SUB L":SUBL,
	"SUB (HL)":SUBHL,
	"SUB A":SUBA,
	"SBC A, B":SBCAB,
	"SBC A, C":SBCAC,
	"SBC A, D":SBCAD,
	"SBC A, E":SBCAE,
	"SBC A, H":SBCAH,
	"SBC A, L":SBCAL,
	"SBC A, (HL)":SBCAHL,
	"SBC A, A":SBCAA,
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
	"CP L":CPL,
	"CP (HL)":CPHL,
	"CP A":CPA,
	"RET NZ":RETNZ,
	"POP BC":POPBC,
	"JP NZ, NN":JPNZNN,
	"JP NN":JPNN,
	"CALL NZ, NN":CALLNZNN,
	"PUSH BC":PUSHBC,
	"ADD A, N":ADDAN,
	"RST 0":RST0,
	"RET Z":RETZ,
	"RET":RET,
	"JP Z, NN":JPZNN,
	"CALL Z, NN":CALLZNN,
	"CALL NN":CALLNN,
	"ADC A, N":ADCAN,
	"RST 8":RST8,
	"RET NC":RETNC,
	"POP DE":POPDE,
	"JP NC, NN":JPNCNN,
	"OUT (N), A":OUTNA,
	"CALL NC, NN":CALLNCNN,
	"PUSH DE":PUSHDE,
	"SUB N":SUBN,
	"RST 10H":RST10H,
	"RET C":RETC,
	"EXX":EXX,
	"JP C, NN":JPCNN,
	"IN A, (N)":INAN,
	"CALL C, N":CALLCN,
	"SBC A, N":SBCAN,
	"RST 18H":RST18H,
	"RET PO":RETPO,
	"POP HL":POPHL,
	"JP PO, NN":JPPONN,
	"EX (SP), HL":EXSPHL,
	"CALL PO, NN":CALLPONN,
	"PUSH HL":PUSHHL,
	"AND N":ANDN,
	"RST 20 H":RST20H,
	"RET PE":RETPE,
	"JP (HL)":JPHL,
	"JE PE, NN":JEPENN,
	"EX DE, HL":EXDEHL,
	"CALL PE, NN":CALLPENN,
	"XOR N":XORN,
	"RST 28H":RST28H,
	"RET P":RETP,
	"POP AF":POPAF,
	"JP P, NN":JPPNN,
	"DI":DI,
	"CALL P, NN":CALLPNN,
	"PUSH AF":PUSHAF,
	"OR N":ORN,
	"RST 30H":RST30H,
	"RET M":RETM,
	"LD SP, HL":LDSPHL,
	"JP M, NN":JPMNN,
	"EI":EI,
	"CALL M, NN":CALLMNN,
	"CP N":CPN,
	"RST 38H":RST38H,
	"RLC B":RLCB,
	"RLC C":RLCC,
	"RLC D":RLCD,
	"RLC E":RLCE,
	"RLC H":RLCH,
	"RLC L":RLCL,
	"RLC (HL)":RLCHL,
	"RLC A":RLCA,
	"RRC B":RRCB,
	"RRC C":RRCC,
	"RRC D":RRCD,
	"RRC E":RRCE,
	"RRC H":RRCH,
	"RRC L":RRCL,
	"RRC (HL)":RRCHL,
	"RRC A":RRCA,
	"RL B":RLB,
	"RL C":RLC,
	"RL D":RLD,
	"RL E":RLE,
	"RL H":RLH,
	"RL L":RLL,
	"RL (HL)":RLHL,
	"RL A":RLA,
	"RR B":RRB,
	"RR C":RRC,
	"RR D":RRD,
	"RR E":RRE,
	"RR H":RRH,
	"RR L":RRL,
	"RR (HL)":RRHL,
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
	"BIT 0, B":BIT0B,
	"BIT 0, C":BIT0C,
	"BIT 0, D":BIT0D,
	"BIT 0, E":BIT0E,
	"BIT 0, H":BIT0H,
	"BIT 0, L":BIT0L,
	"BIT 0, (HL)":BIT0HL,
	"BIT 0, A":BIT0A,
	"BIT 1, B":BIT1B,
	"BIT 1, C":BIT1C,
	"BIT 1, D":BIT1D,
	"BIT 1, E":BIT1E,
	"BIT 1, H":BIT1H,
	"BIT 1, L":BIT1L,
	"BIT 1, (HL)":BIT1HL,
	"BIT 1, A":BIT1A,
	"BIT 2, B":BIT2B,
	"BIT 2, C":BIT2C,
	"BIT 2, D":BIT2D,
	"BIT 2, E":BIT2E,
	"BIT 2, H":BIT2H,
	"BIT 2, L":BIT2L,
	"BIT 2, (HL)":BIT2HL,
	"BIT 2, A":BIT2A,
	"BIT 3, B":BIT3B,
	"BIT 3, C":BIT3C,
	"BIT 3, D":BIT3D,
	"BIT 3, E  ":BIT3E,
	"BIT 3, H":BIT3H,
	"BIT 3, L":BIT3L,
	"BIT 3, (HL)":BIT3HL,
	"BIT 3, A":BIT3A,
	"BIT 4, B":BIT4B,
	"BIT 4, C":BIT4C,
	"BIT 4, D":BIT4D,
	"BIT 4, E":BIT4E,
	"BIT 4, H":BIT4H,
	"BIT 4, L":BIT4L,
	"BIT 4, (HL)":BIT4HL,
	"BIT 4, A":BIT4A,
	"BIT 5, B":BIT5B,
	"BIT 5, C":BIT5C,
	"BIT 5, D":BIT5D,
	"BIT 5, E":BIT5E,
	"BIT 5, H":BIT5H,
	"BIT 5, L":BIT5L,
	"BIT 5, (HL)":BIT5HL,
	"BIT 5, A":BIT5A,
	"BIT 6, B":BIT6B,
	"BIT 6, C":BIT6C,
	"BIT 6, D":BIT6D,
	"BIT 6, E":BIT6E,
	"BIT 6, H":BIT6H,
	"BIT 6, L":BIT6L,
	"BIT 6, (HL)":BIT6HL,
	"BIT 6, A":BIT6A,
	"BIT 7, B":BIT7B,
	"BIT 7, C":BIT7C,
	"BIT 7, D":BIT7D,
	"BIT 7, E":BIT7E,
	"BIT 7, H":BIT7H,
	"BIT 7, L":BIT7L,
	"BIT 7, (HL)":BIT7HL,
	"BIT 7, A":BIT7A,
	"RES 0, B":RES0B,
	"RES 0, C":RES0C,
	"RES 0, D":RES0D,
	"RES 0, E":RES0E,
	"RES 0, H":RES0H,
	"RES 0, L":RES0L,
	"RES 0, (HL)":RES0HL,
	"RES 0, A":RES0A,
	"RES 1, B":RES1B,
	"RES 1, C":RES1C,
	"RES 1, D":RES1D,
	"RES 1, E":RES1E,
	"RES 1, H":RES1H,
	"RES 1, L":RES1L,
	"RES 1, (HL)":RES1HL,
	"RES 1, A":RES1A,
	"RES 2, B":RES2B,
	"RES 2, C":RES2C,
	"RES 2, D":RES2D,
	"RES 2, E":RES2E,
	"RES 2, H":RES2H,
	"RES 2, L":RES2L,
	"RES 2, (HL)":RES2HL,
	"RES 2, A":RES2A,
	"RES 3, B":RES3B,
	"RES 3, C":RES3C,
	"RES 3, D":RES3D,
	"RES 3, E":RES3E,
	"RES 3, H":RES3H,
	"RES 3, L":RES3L,
	"RES 3, (HL)":RES3HL,
	"RES 3, A":RES3A,
	"RES 4, B":RES4B,
	"RES 4, C":RES4C,
	"RES 4, D":RES4D,
	"RES 4, E":RES4E,
	"RES 4, H":RES4H,
	"RES 4, L":RES4L,
	"RES 4, (HL)":RES4HL,
	"RES 4, A":RES4A,
	"RES 5, B":RES5B,
	"RES 5, C":RES5C,
	"RES 5, D":RES5D,
	"RES 5, E":RES5E,
	"RES 5, H":RES5H,
	"RES 5, L":RES5L,
	"RES 5, (HL)":RES5HL,
	"RES 5, A":RES5A,
	"RES 6, B":RES6B,
	"RES 6, C":RES6C,
	"RES 6, D":RES6D,
	"RES 6, E":RES6E,
	"RES 6, H":RES6H,
	"RES 6, L":RES6L,
	"RES 6, (HL)":RES6HL,
	"RES 6, A":RES6A,
	"RES 7, B":RES7B,
	"RES 7, C":RES7C,
	"RES 7, D":RES7D,
	"RES 7, E":RES7E,
	"RES 7, H":RES7H,
	"RES 7, L":RES7L,
	"RES 7, (HL)":RES7HL,
	"RES 7, A ":RES7A,
	"SET 0, B":SET0B,
	"SET 0, C":SET0C,
	"SET 0, D":SET0D,
	"SET 0, E":SET0E,
	"SET 0, H":SET0H,
	"SET 0, L":SET0L,
	"SET 0, (HL)":SET0HL,
	"SET 0, A":SET0A,
	"SET 1, B":SET1B,
	"SET 1, C":SET1C,
	"SET 1, D":SET1D,
	"SET 1, E":SET1E,
	"SET 1, H":SET1H,
	"SET 1, L":SET1L,
	"SET 1, (HL)":SET1HL,
	"SET 1, A":SET1A,
	"SET 2, B":SET2B,
	"SET 2, C":SET2C,
	"SET 2, D":SET2D,
	"SET 2, E":SET2E,
	"SET 2, H":SET2H,
	"SET 2, L ":SET2L,
	"SET 2, (HL)":SET2HL,
	"SET 2, A":SET2A,
	"SET 3, B":SET3B,
	"SET 3, C":SET3C,
	"SET 3, D":SET3D,
	"SET 3, E":SET3E,
	"SET 3, H":SET3H,
	"SET 3, L":SET3L,
	"SET 3, (HL)":SET3HL,
	"SET 3, A":SET3A,
	"SET 4, B":SET4B,
	"SET 4, C":SET4C,
	"SET 4, D":SET4D,
	"SET 4, E":SET4E,
	"SET 4, H":SET4H,
	"SET 4, L":SET4L,
	"SET 4, (HL)":SET4HL,
	"SET 4, A":SET4A,
	"SET 5, B":SET5B,
	"SET 5, C ":SET5C,
	"SET 5, D":SET5D,
	"SET 5, E":SET5E,
	"SET 5, H":SET5H,
	"SET 5, L":SET5L,
	"SET 5, (HL)":SET5HL,
	"SET 5, A":SET5A,
	"SET 6, B":SET6B,
	"SET 6, C":SET6C,
	"SET 6, D":SET6D,
	"SET 6, E":SET6E,
	"SET 6, H":SET6H,
	"SET 6, L":SET6L,
	"SET 6, (HL)":SET6HL,
	"SET 6, A":SET6A,
	"SET 7, B":SET7B,
	"SET 7, C":SET7C,
	"SET 7, D":SET7D,
	"SET 7, E":SET7E,
	"SET 7, H":SET7H,
	"SET 7, L":SET7L,
	"SET 7, (HL)":SET7HL,
	"SET 7, A":SET7A,
	"ADD IX, BC":ADDIXBC,
	"ADD IX, DE":ADDIXDE,
	"LD IX, NN":LDIXNN,
	"LD (NN), IX":LDNNIX,
	"INC IX":INCIX,
	"ADD IX, IX":ADDIXIX,
	"LD IX, (NN)":LDIXNN,
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
	"ADD A, (IX + d)":ADDAIXd,
	"ADC A, (IX + d)":ADCAIXd,
	"SUB (IX + d)":SUBIXd,
	"SBC A, (IX + d)":SBCAIXd,
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
	"BIT 0, (IX + d)":BIT0IXd,
	"BIT 1, (IX + d)":BIT1IXd,
	"BIT 2, (IX + d)":BIT2IXd,
	"BIT 3, (IX + d)":BIT3IXd,
	"BIT 4, (IX + d)":BIT4IXd,
	"BIT 5, (IX + d)":BIT5IXd,
	"BIT 6, (IX + d)":BIT6IXd,
	"BIT 7, (IX + d)":BIT7IXd,
	"RES 0, (IX + d)":RES0IXd,
	"RES 1, (IX + d)":RES1IXd,
	"RES 2, (IX + d)":RES2IXd,
	"RES 3, (IX + d)":RES3IXd,
	"RES 4, (IX + d)":RES4IXd,
	"RES 5, (IX + d)":RES5IXd,
	"RES 6, (IX + d)":RES6IXd,
	"RES 7, (IX + d)":RES7IXd,
	"SET 0, (IX + d)":SET0IXd,
	"SET 1, (IX + d)":SET1IXd,
	"SET 2, (IX + d)":SET2IXd,
	"SET 3, (IX + d)":SET3IXd,
	"SET 4, (IX + d)":SET4IXd,
	"SET 5, (IX + d)":SET5IXd,
	"SET 6, (IX + d)":SET6IXd,
	"SET 7, (IX + d)":SET7IXd,
	"IN B, (C)":INBC,
	"OUT (C), B":OUTCB,
	"SBC HL, BC":SBCHLBC,
	"LS (NN), BC":LSNNBC,
	"NEG":NEG,
	"RETN":RETN,
	"IM 0":IM0,
	"LD I, A":LDIA,
	"INC C, (C)":INCCC,
	"OUT (C), C":OUTCC,
	"ADC HL, BC":ADCHLBC,
	"LD BC, (NN)":LDBCNN,
	"RETI":RETI,
	"INC D, (C)":INCDC,
	"OUT (C), D":OUTCD,
	"SBC HL, DE":SBCHLDE,
	"LD DE, (NN)":LDDENN,
	"IM 2":IM2,
	"IN H, (C)":INHC,
	"OUT (C), H":OUTCH,
	"SBC HL, HL":SBCHLHL,
	"RRD":RRD,
	"IN L, (C)":INLC,
	"OUT (C), L":OUTCL,
	"ADC HL, HL":ADCHLHL,
	"RLD":RLD,
	"SBC HL, SP":SBCHLSP,
	"LD (NN), SP":LDNNSP,
	"IN A, (C)":INAC,
	"OUT (C), A":OUTCA,
	"ADC HL, SP":ADCHLSP,
	"LD SP, (NN)":LDSPNN,
	"LDI":LDI,
	"CPI":CPI,
	"INI":INI,
	"OUTI":OUTI,
	"LDD":LDD,
	"CPD":CPD,
	"IND":IND,
	"OUTD":OUTD,
	"LDIR":LDIR,
	"CPIR":CPIR,
	"INIR":INIR,
	"OTIR":OTIR,
	"LDDR":LDDR,
	"PCDR":PCDR,
	"INDR":INDR,
	"OTDR":OTDR,
	"ADD IY, BC":ADDIYBC,
	"ADD IY, DE":ADDIYDE,
	"LD IY, NN":LDIYNN,
	"LD (NN), IY":LDNNIY,
	"INC IY":INCIY,
	"ADD IY, IY":ADDIYIY,
	"LD IY, (NN)":LDIYNN,
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
	"ADD A, (IY + d)":ADDAIYd,
	"ADC A, (IY + d)":ADCAIYd,
	"SUB (IY + d)":SUBIYd,
	"SBC A, (IY + d)":SBCAIYd,
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
	"BIT 0, (IY + d)":BIT0IYd,
	"BIT 1, (IY + d)":BIT1IYd,
	"BIT 2, (IY + d)":BIT2IYd,
	"BIT 3, (IY + d)":BIT3IYd,
	"BIT 4, (IY + d)":BIT4IYd,
	"BIT 5, (IY + d)":BIT5IYd,
	"BIT 6, (IY + d)":BIT6IYd,
	"BIT 7, (IY + d)":BIT7IYd,
	"RES 0, (IY + d)":RES0IYd,
	"RES 1, (IY + d)":RES1IYd,
	"RES 2, (IY + d)":RES2IYd,
	"RES 3, (IY + d)":RES3IYd,
	"RES 4, (IY + d)":RES4IYd,
	"RES 5, (IY + d)":RES5IYd,
	"RES 6, (IY + d)":RES6IYd,
	"RES 7, (IY + d)":RES7IYd,
	"SET 0, (IY + d)":SET0IYd,
	"SET 1, (IY + d)":SET1IYd,
	"SET 2, (IY + d)":SET2IYd,
	"SET 3, (IY + d)":SET3IYd,
	"SET 4, (IY + d)":SET4IYd,
	"SET 5, (IY + d)":SET5IYd,
	"SET 6, (IY + d)":SET6IYd,
	"SET 7, (IY + d)":SET7IYd,
}