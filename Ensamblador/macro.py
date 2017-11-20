MDT = {}
CMDT = 0
MNT = {}
CMNT = 0
ALA = {}
CALA = 0
nombres = []
AMDT = []
AALA = []

def borrar(lista):

	for i in lista:
		if(i == " " or i == ""):
			lista.remove(i)

	for j in range(len(lista) - (len(lista)-1)):
		nombres.append(aux[0])
		lista = lista.pop(0)

	return lista

m = open("1.txt", "r")
macros = m.read().split("MEND")
macros = [item.replace("\t", "") for item in macros]
macros = [item.replace(":", "\n") for item in macros]

#MDT
for i in macros:
	if("MACRO" in i):
		aux = i.split("\n")
		borrar(aux)
		AMDT.append(len(aux))

		for j in aux:
			if(j != " " and j != ""):
				CMDT += 1
				MDT[CMDT] = j.strip()
	else:
		body = i.split("\n") #Cuerpo del programa, donde estan las macrollamadas

#ALA
d = {}
c = 0
 
for i in MDT.values(): #Variables usadas por cada MACRO #ax 
	if("MACRO" in i):
		aux2 = i.split("MACRO")
		n = nombres[c]
		d[n] = aux2[1].strip()
		c += 1 

for j in body:
	for k in nombres:
		if k in d.keys():
			if(j != " " and j != ""):
				argf = d[k] #Argumentos formales (#ax's)
				argf = argf.replace(",", "")
				lenf = len(argf.split(" "))
				if lenf not in AALA:
					AALA.append(lenf)
				if(k in j):
					arga = j.split(" ") #argumentos actuales
					arga = [item.replace(",", "") for item in arga]
					lena = len(arga)-1
					if(lenf == lena):
						for l in arga:
							if(l in k):
								a = 0
							else:
								p = argf.split(" ")
								CALA += 1
								q = (l, p[a]) #Tupla (actual,formal)
								ALA[CALA] = q
								a += 1


#MNT
x = 1
z = 1
b = 0
for k in nombres:
	if(k in d.keys()):
		CMNT += 1
		t = (k, x, z)
		MNT[CMNT] = t
		x += AMDT[b]
		z += AALA[b]
		b += 1



print("\n")
print("MDT: ", MDT)
print("\n")
print("ALA: ", ALA)
print("\n")
print("MNT: ", MNT)
print("\n")

				
