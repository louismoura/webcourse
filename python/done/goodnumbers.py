import itertools
import math
import heapq
from random import *

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
numJogos = 1663
tamJogo = 18
tamAmostra = 100
offset = 3

#VARIAVEIS FIXAS
inicioIndex = tourn - numJogos
somaSaiu = 0.0 
somaTamanho = 0.0
numJogosReal = 0.0
travado = [1, 2, 3, 5, 7, 8, 11, 13, 17, 18, 20, 23, 24]
indexes = []

def GetGoodNumbers(inicioIndex):

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

def GetNewGame(newGamea):
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

	goodnumbers = GetGoodNumbers(inicioIndex)
	#newGame = GetNewGame(goodnumbers)
	#newGame = [1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25]
	newGame = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
	#newGame = travado[:]

	a = 0
	while len(newGame) <= 14:
		if goodnumbers[a] not in newGame:
			newGame.append(goodnumbers[a])
		a += 1

	acertos = [item for item in newGame if item in databaseListFinal[inicioIndex - 1]]
	erros = [item for item in newGame if item not in databaseListFinal[inicioIndex - 1]]

	


	indexes.append(len(acertos))

	somaSaiu += float(len(acertos)) 
	somaTamanho += len(newGame)
	mediaInstant = len(acertos)/len(newGame)
	numJogosReal += 1

	print ("GN: %s" % goodnumbers)
	print ("NewGame: %s" % (newGame))
	print ("Torneio: %s: %s" % (inicioIndex, databaseListFinal[inicioIndex - 1]))
	print ("Saiu: %s dos %s (%0.2f%%)" % (len(acertos), len(newGame), mediaInstant*100))
	print ("Nao saiu do NewGame: %s" % erros)
	print ("\n")
	inicioIndex += 1

print ("Saiu: %0.2f de %0.2f" % ((somaSaiu/numJogosReal),(somaTamanho/numJogosReal)))
#print indexes

#Writing in a txt the final combinations
file = open('goodnumbers.txt', 'w')
for i in range(len(indexes)):
	file.write(str(indexes[i]) + "\n") 
file.close()