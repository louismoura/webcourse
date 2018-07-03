import itertools
import math
import heapq
from random import *

def ha(x): return x >= 1

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
numJogos = 1000
tamJogo = 15
tamAmostra = 100
offset = 3

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
		#print ("%s: \t%0.5f" % (i+1, perNum))

	#print ("\n%s" % listPercentNumberPre)
	#print ("\n%s" % listPercentNumberPre1)

	listPercentNumberPre1 = heapq.nlargest(25, listPercentNumberPre1)

	#print ("\n%s" % listPercentNumberPre1)

	for i in range(len(listPercentNumberPre1)):
		for j in range(len(listPercentNumberPre)):
			if listPercentNumberPre1[i] == listPercentNumberPre[j]:
				if listPercentNumberPre[j-1] not in listPercentNumberFinal:
					listPercentNumberFinal.append(listPercentNumberPre[j-1])

	#The 25 numbers em ordem decrescente de saida
	#print ("%s" % listPercentNumberFinal)

	#saindoFinal = listPercentNumberFinal[0+offset:tamJogo+offset]

	#print ("GN: %s" % saindoFinal)

	#list1 = [item for item in previousTorn if item in saindoFinal]

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


while (inicioIndex <= tourn):

	newGamea = GetGame(inicioIndex)
	newGameb = GetGame(inicioIndex-1)
	newGamec = GetGame(inicioIndex-2)

	newGame1 = GetGameNew(newGamea)
	newGame2 = GetGameNew(newGameb)
	newGame3 = GetGameNew(newGamec)
	

	Saiu = 0.0

	for i in range(len(newGame1)):
		if newGame1[i] in databaseListFinal[inicioIndex - 1]:
			Saiu += 1

	list1 = [item for item in newGame1 if item not in databaseListFinal[inicioIndex - 1]]

	somaSaiu += float(Saiu) 
	somaTamanho += len(newGame1)
	mediaInstant = Saiu/len(newGame1)
	numJogosReal += 1

	print ("GN3: %s" % newGamec)
	print ("GN2: %s" % newGameb)
	print ("GN1: %s" % newGamea)
	print ("GN: %s" % sorted(newGame1))
	print ("Torneio: %s: %s" % (inicioIndex, databaseListFinal[inicioIndex - 1]))
	print ("Saiu: %s dos %s (%0.2f%%)" % (Saiu, len(newGame1), mediaInstant*100))
	print ("Nao saiu do GN1: %s" % list1)
	print ("\n")
	inicioIndex += 1

print ("Saiu: %0.2f de %0.2f" % ((somaSaiu/numJogosReal),(somaTamanho/numJogosReal)))

