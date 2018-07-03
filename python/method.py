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
print tourn
for i in range(tourn):
	databaseListFinal.append(databaseListFirst[(15*i):((15*i)+15)])

"""
Esse metodo calcula o numero de acertos dependendo da montagem de good numbers escolhida
"""

#VARIAVEIS QUE PODEM SER ALTERADAS
numJogos = 10
tamJogo = 18
tamAmostra = 100
offset = 0
quantJogosInicio = 10

#VARIAVEIS FIXAS
inicioIndex = tourn - numJogos
somaSaiu = 0.0 
somaTamanho = 0.0
listSaiu = []

lucro = 0.0
premio11 = 4
premio12 = 8
premio13 = 20
premio14 = 1000
premio15 = 500000
valordoJogo = 2

def CalculoLucro(numSaidos):
	if (numSaidos < 11):
		return valordoJogo*quantJogosInicio*(-1)

	if (numSaidos == 11):
		return quantJogosInicio*premio11

	if (numSaidos == 12):
		return quantJogosInicio*premio12

	if (numSaidos == 13):
		return quantJogosInicio*premio13

	if (numSaidos == 14):
		return quantJogosInicio*premio14

	if (numSaidos == 15):
		return quantJogosInicio*premio15

def GetGame(inicioIndex):

	#Porcentagem atual que esta saindo o numero
	listPercentNumber = [0 for i in range(25)]
	for i in range(tamAmostra):
		index = inicioIndex - tamAmostra + i
		#print index + 1
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

def GetGameNew(newGame1, newGame2):
	newGameA = newGame1[0+offset:tamJogo+offset]
	newGameB = newGame2[0+offset:tamJogo+offset]
	inclu = newGame2[15:25]
	#print inclu

	print ("GN1: %s" % newGameA)
	print ("GN2: %s" % newGameB)
	newGame3 = []

	if (newGameA != newGameB):
		for i in range(len(newGameB)):
			if newGameA[i] in newGameB:
				if newGameA.index(newGameA[i]) < newGameB.index(newGameA[i]):
					newGame3.append(newGame1[i])

	for i in range(len(newGame3)):
		newGameB.remove(newGame3[i])

	while len(newGameB) > 15:
		newGameB.pop()

	while len(newGameB) < 15:
		b = inclu.pop()
		newGameB.append(b)

	print ("Retirados: %s" % newGame3)
	print ("NewGame: %s" % newGameB)
	return newGameB


def getMaxDist(listSaiu):
	listSaiu1 = []

	for i in range(len(listSaiu)-1):
		dist = listSaiu[i+1] - listSaiu[i]
		listSaiu1.append(dist)

	return listSaiu1


while (inicioIndex < tourn):

	newGame1 = GetGame(inicioIndex-1)
	newGame2 = GetGame(inicioIndex)

	newGame = GetGameNew(newGame1, newGame2)

	test = []
	Saiu = 0.0

	for i in range(len(newGame)):
		if newGame[i] in databaseListFinal[inicioIndex]:
			test.append(newGame[i])
			Saiu += 1

	list1 = [item for item in newGame if item not in test]

	if Saiu > 10:
		listSaiu.append(inicioIndex + 1)

	

	somaSaiu += float(Saiu) 
	somaTamanho += len(newGame)
	mediaInstant = Saiu/len(newGame)

	print ("Torneio: %s: %s" % (inicioIndex + 1, databaseListFinal[inicioIndex]))
	print ("Saiu: %s dos %s (%0.2f%%)" % (Saiu, len(newGame), mediaInstant*100))
	print ("Nao saiu do NewGame: %s" % list1)
	#Calculando lucro atual
	lucro += CalculoLucro(Saiu)
	print ("lucro atual: %s\n" % lucro)
	print ("\n")
	inicioIndex += 1

maxDist = getMaxDist(listSaiu)

print ("Saiu: %0.2f de %0.2f" % ((somaSaiu/numJogos),(somaTamanho/numJogos)))
print maxDist
print max(maxDist)
print ("Lucro Final: %s reais \n" % lucro)
print ("\n")