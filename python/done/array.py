import itertools
import math
import heapq
from random import *


#Function to count all odd numbers in a list
def GetOddCount(inputList):
    return sum(1-n%2 for n in inputList)

def GetXCount(inputList):
	return ((1 in inputList) + (7 in inputList) + (13 in inputList) + (19 in inputList) + (25 in inputList) + 
			(21 in inputList) + (17 in inputList) + (9 in inputList) + (5 in inputList))

def GetNACount(inputList, index):
	previous = databaseListFinal[index - 2]
	previous1 = [item for item in inputList if item in previous]
	return len(previous1)

def GetComb(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

#Creating a list of all tournaments of lotofacil, the first is 0
f = open('database.txt','r')
databaseListFinal = []
databaseListFirst = f.read().split()
databaseListFirst = [int(i) for i in databaseListFirst]
tourn = len(databaseListFirst)/15
#print tourn
for i in range(tourn):
	databaseListFinal.append(databaseListFirst[(15*i):((15*i)+15)])

"""
Esse metodo calcula o numero de acertos dependendo da montagem de good numbers escolhida
"""

#VARIAVEIS QUE PODEM SER ALTERADAS
numJogos = 30
tamJogo = 18
tamAmostra = 100
offset = 3
tamAnalise = 50

#VARIAVEIS FIXAS
inicioIndex = tourn - numJogos
somaSaiu = 0.0 
somaTamanho = 0.0
numJogosReal = 0.0
listSaiu = []



def GetGame(inicioIndex):

	#Porcentagem atual que esta saindo o numero
	listPercentNumber = [0 for i in range(25)]
	for i in range(tamAmostra):
		index = inicioIndex - tamAmostra + i - 1
		#print (" %s: %s" % (index, databaseListFinal[index]))
		for j in range(15):
			for k in range(25):
				if databaseListFinal[index][j] == (k+1):
					listPercentNumber[k] += 1
				
	listPercentNumberPre = []
	listPercentNumberPre1 = []
	listPercentNumberFinal = []
	for i in range(25):
		listPercentNumberPre.append(i + 1)
		perNum = float(listPercentNumber[i])/(15.0*tamAmostra)
		perNum = round(perNum, 5)
		listPercentNumberPre.append(perNum)
		listPercentNumberPre1.append(perNum)

	listPercentNumberPre1 = heapq.nlargest(25, listPercentNumberPre1)

	for i in range(len(listPercentNumberPre1)):
		for j in range(len(listPercentNumberPre)):
			if listPercentNumberPre1[i] == listPercentNumberPre[j]:
				if listPercentNumberPre[j-1] not in listPercentNumberFinal:
					listPercentNumberFinal.append(listPercentNumberPre[j-1])

	#The 25 numbers em ordem decrescente de saida
	#print ("%s" % listPercentNumberFinal)

	return listPercentNumberFinal

def GetGameNew(newGamea):
	newGN = newGamea[0+offset:tamJogo+offset]

	#newGN = newGamea[25-tamJogo-offset:25-offset]

	#newGN = newGamea[0+offset:tamJogo]
	#newGN1 = newGamea[25-offset:25]
	#newGN = newGN + newGN1

	#newGN = newGamea[25-tamJogo:25-offset]
	#newGN1 = newGamea[0:0+offset]
	#newGN = newGN + newGN1
	
	return newGN

def CreateArray(newGame1, index):
	tamJogoArray = 15
	allComb = list(itertools.combinations(newGame1, tamJogoArray))

	#Checking NA possibility
	NAComb = []
	for i in range(len(allComb)):
		nacount = GetNACount(allComb[i], index)
		#print nacount
		if nacount > 7 and nacount < 10:
		 	NAComb.append(allComb[i])

	#Checking X possibility
	XComb = []
	for i in range(len(NAComb)):
		xcount = GetXCount(NAComb[i])
		if xcount > 4 and xcount < 7:
		 	XComb.append(NAComb[i])

	#Checking parity possibility
	parComb = []
	for i in range(len(XComb)):
		odd = GetOddCount(XComb[i])
		if odd > 6 and odd < 9:
		 	parComb.append(XComb[i])

	#Checking sum possibility
	sumComb = []
	for i in range(len(parComb)):
		sumNumb = sum(parComb[i])
		if sumNumb > 179 and sumNumb < 210:
		 	sumComb.append(parComb[i])

	return sumComb

def GetNovoJogo(databaseArray, newGamea, index):
	databaseAcertos = []
	databaseAcertos1 = [0 for i in range(len(databaseArray))]
	listAcertos = [0 for i in range(tamAnalise)]

	for i in range(len(databaseArray)):
		Acertados = 0
		for j in range(tamAnalise):
			previous = databaseListFinal[index - 2 - j]
			previous1 = [item for item in databaseArray[i] if item in previous]
			if len(previous1) > 10:
				Acertados += 1
			listAcertos[j]= Acertados
		databaseAcertos.append(listAcertos)

	for i in range(len(databaseAcertos)):
		databaseAcertos1[i] = max(databaseAcertos[i])

	return databaseArray[0]

while (inicioIndex <= tourn):

	newGamea = GetGame(inicioIndex)
	newGame2 = GetGameNew(newGamea)

	databaseArray = CreateArray(newGame2, inicioIndex)
 	print len(databaseArray)

 	newGame1 = GetNovoJogo(databaseArray, newGamea, inicioIndex)
 	#print len(newGame2)
 	#print newGame2


	Saiu = 0.0

	for i in range(len(newGame1)):
		if newGame1[i] in databaseListFinal[inicioIndex - 1]:
			Saiu += 1

	list1 = [item for item in newGame1 if item not in databaseListFinal[inicioIndex - 1]]

	somaSaiu += float(Saiu) 
	somaTamanho += len(newGame1)
	mediaInstant = Saiu/len(newGame1)
	numJogosReal += 1

	print ("GN: %s" % newGamea)
	print ("GN1: %s" % sorted(newGame1))
	print ("Torneio: %s: %s" % (inicioIndex, databaseListFinal[inicioIndex - 1]))
	print ("Saiu: %s dos %s (%0.2f%%)" % (Saiu, len(newGame1), mediaInstant*100))
	print ("Nao saiu do GN1: %s" % list1)
	print ("\n")
	inicioIndex += 1

print ("Saiu: %0.2f de %0.2f" % ((somaSaiu/numJogosReal),(somaTamanho/numJogosReal)))

