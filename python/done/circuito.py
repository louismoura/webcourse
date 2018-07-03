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
numJogos = 1000
tamJogo = 15
tamAmostra = 100
offset = 3
tamCircuito = 10

#VARIAVEIS FIXAS
inicioIndex = tourn - numJogos
somaSaiu = 0.0 
somaTamanho = 0.0
circuito = 1.0
premios1 = 0.0
escolhido = [1, 2, 3, 5, 7, 8, 11, 13, 17, 18, 20, 23, 24, 25, 10]
escolhido1 = [1, 2, 3, 5, 7, 8, 11, 13, 17, 18, 20, 23, 24, 14, 22]
sobra = [4, 6, 9, 10, 12, 15, 16, 19, 21, 25]

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


def getEscolhido(goodnumbers, escolhido):
	theNine = []
	a = 0
	while len(theNine) < 9:
		if goodnumbers[a] in escolhido:
			theNine.append(goodnumbers[a])
		a += 1

	return theNine

def getSobra(goodnumbers, sobra):
	theSix = []
	a = 0
	while len(theSix) < 6:
		if goodnumbers[a] in sobra:
			theSix.append(goodnumbers[a])
		a += 1

	return theSix

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
	newGame = GetNewGame(goodnumbers)

	nineGnEscolhido = getEscolhido(goodnumbers, escolhido)
	sixGnSobra = getSobra(goodnumbers, sobra)

	print ("--------------------------------------------------------------------------")
	print ("NewGame: %s" % (newGame))
	print ("GN: %s" % goodnumbers)
	print ("9: %s" % nineGnEscolhido)
	print ("6: %s" % sixGnSobra)
	print ("Circuito: %s" % (circuito))
	print ("--------------------------------------------------------------------------\n")
	premios = 0


	for i in range(tamCircuito):
		

		#newGame = escolhido[:]

		if inicioIndex + i == tourn + 1:
			break


		#if i > 2:
		#	newGame = escolhido1[:]




		acertos = [item for item in newGame if item in databaseListFinal[inicioIndex - 1 + i]]
		erros = [item for item in newGame if item not in databaseListFinal[inicioIndex - 1 + i]]

		somaSaiu += float(len(acertos)) 
		somaTamanho += len(newGame)
		mediaInstant = float(len(acertos)/len(newGame))

		print ("NewGame: %s" % (newGame))
		print ("Torneio: %s: %s" % (inicioIndex + i, databaseListFinal[inicioIndex - 1 + i]))
		print ("Saiu: %s dos %s (%0.2f%%)" % (len(acertos), len(newGame), mediaInstant*100))
		print ("Nao saiu do NewGame: %s" % erros)
		print ("\n")


		if len(acertos) > 10 and premios == 0:
			premios = 1
			
	premios1 += premios

	inicioIndex += tamCircuito
	circuito += 1


print ("Acertos: %0.2f" % (premios1/circuito))

