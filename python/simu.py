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
numJogos = 100
tamJogo1 = 18
tamJogo = 15
tamAmostra = 100
offset = 0

tamCircuito = 4
quantJogosInicio = 5

#VARIAVEIS FIXAS
inicioIndex = tourn - numJogos
somaSaiu = 0.0 
somaTamanho = 0.0

quantCircuitos = 1

lucro = 0.0
onze = 0.0
doze = 0.0
treze = 0.0
catorze = 0.0
quinze = 0.0

premio11 = 4
premio12 = 8
premio13 = 20
premio14 = 1000
premio15 = 500000

if tamJogo == 15:
	valordoJogo = 2
if tamJogo == 16:
	valordoJogo = 32
if tamJogo == 17:
	valordoJogo = 272
if tamJogo == 18:
	valordoJogo = 1632


def CalculoLucro(numSaidos, j):
	#print numSaidos, j
	if (numSaidos < 11):
		return valordoJogo*quantJogosInicio*(3**j)*(-1)

	if (numSaidos == 11) and tamJogo == 15:
		return (1*premio11*quantJogosInicio*(3**j) - valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 11) and tamJogo == 16:
		return (5*premio11*quantJogosInicio*(3**j) - valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 11) and tamJogo == 17:
		return (15*premio11*quantJogosInicio*(3**j) - valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 11) and tamJogo == 18:
		return (35*premio11*quantJogosInicio*(3**j) - valordoJogo*quantJogosInicio*(3**j))

	if (numSaidos == 12) and tamJogo == 15:
		return (1*premio12*quantJogosInicio*(3**j) + 0*premio11*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 12) and tamJogo == 16:
		return (4*premio12*quantJogosInicio*(3**j) + 12*premio11*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 12) and tamJogo == 17:
		return (10*premio12*quantJogosInicio*(3**j) + 60*premio11*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 12) and tamJogo == 18:
		return (20*premio12*quantJogosInicio*(3**j) + 180*premio11*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))

	if (numSaidos == 13) and tamJogo == 15:
		return (1*premio13*quantJogosInicio*(3**j) + 0*premio12*quantJogosInicio*(3**j) 
				+ 0*premio11*quantJogosInicio*(3**j) - valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 13) and tamJogo == 16:
		return (3*premio13*quantJogosInicio*(3**j) + 13*premio12*quantJogosInicio*(3**j) 
				+ 0*premio11*quantJogosInicio*(3**j) - valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 13) and tamJogo == 17:
		return (6*premio13*quantJogosInicio*(3**j) + 52*premio12*quantJogosInicio*(3**j) 
				+ 78*premio11*quantJogosInicio*(3**j) - valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 13) and tamJogo == 18:
		return (10*premio13*quantJogosInicio*(3**j) + 130*premio12*quantJogosInicio*(3**j) 
				+ 390*premio11*quantJogosInicio*(3**j) - valordoJogo*quantJogosInicio*(3**j))

	if (numSaidos == 14) and tamJogo == 15:
		return (1*premio14*quantJogosInicio*(3**j) + 0*premio13*quantJogosInicio*(3**j) 
				+ 0*premio12*quantJogosInicio*(3**j) + 0*premio11*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 14) and tamJogo == 16:
		return (2*premio14*quantJogosInicio*(3**j) + 14*premio13*quantJogosInicio*(3**j) 
				+ 0*premio12*quantJogosInicio*(3**j) + 0*premio11*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 14) and tamJogo == 17:
		return (3*premio14*quantJogosInicio*(3**j) + 42*premio13*quantJogosInicio*(3**j) 
				+ 91*premio12*quantJogosInicio*(3**j) + 0*premio11*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 14) and tamJogo == 18:
		return (4*premio14*quantJogosInicio*(3**j) + 84*premio13*quantJogosInicio*(3**j) 
				+ 364*premio12*quantJogosInicio*(3**j) + 364*premio11*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))

	if (numSaidos == 15) and tamJogo == 15:
		return (1*premio15*quantJogosInicio*(3**j) + 0*premio14*quantJogosInicio*(3**j) 
				+ 0*premio13*quantJogosInicio*(3**j) + 0*premio12*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 15) and tamJogo == 16:
		return (1*premio15*quantJogosInicio*(3**j) + 15*premio14*quantJogosInicio*(3**j) 
				+ 0*premio13*quantJogosInicio*(3**j) + 0*premio12*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 15) and tamJogo == 17:
		return (1*premio15*quantJogosInicio*(3**j) + 30*premio14*quantJogosInicio*(3**j) 
				+ 105*premio13*quantJogosInicio*(3**j) + 0*premio12*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))
	if (numSaidos == 15) and tamJogo == 18:
		return (1*premio15*quantJogosInicio*(3**j) + 45*premio14*quantJogosInicio*(3**j) 
				+ 315*premio13*quantJogosInicio*(3**j) + 455*premio12*quantJogosInicio*(3**j) 
				- valordoJogo*quantJogosInicio*(3**j))


def GetGame(inicioIndex):

	#Porcentagem atual que esta saindo o numero
	listPercentNumber = [0 for i in range(25)]
	for i in range(tamAmostra):
		index = inicioIndex - tamAmostra + i + 1
		#print index
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
	#print ("\n%s" % listPercentNumberFinal)

	#saindoFinal = listPercentNumberFinal[0+offset:tamJogo1+offset]

	#print ("%s" % saindoFinal)
	
	return listPercentNumberFinal

def GetGameNew(newGame1, newGame2):
	newGameA = newGame1[0+offset:tamJogo1+offset]
	newGameB = newGame2[0+offset:tamJogo1+offset]
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
	print ("NewGame: %s" % sorted(newGameB))
	return newGameB


while ( (inicioIndex +tamCircuito-1) < tourn):

	print ("--------------------------------------------------------")

	quantCircuitos += 1

	for j in range(tamCircuito):

		newGame1 = GetGame(inicioIndex + j - 1)
		newGame2 = GetGame(inicioIndex + j)

		newGame = GetGameNew(newGame1, newGame2)
		#print ("\nJogo %s" % (newGame))

		Saiu = 0.0

		for i in range(len(newGame)):
			if newGame[i] in databaseListFinal[inicioIndex + j]:
				Saiu += 1

		if Saiu == 11:
			onze += 1
		if Saiu == 12:
			doze += 1
		if Saiu == 13:
			treze += 1
		if Saiu == 14:
			catorze += 1
		if Saiu == 15:
			quinze += 1

		mediaInstant = Saiu/len(newGame)

		print ("Torneio: %s: %s" % (inicioIndex + j + 1, databaseListFinal[inicioIndex + j]))
		print ("Saiu: %s dos %s (%0.2f%%)" % (Saiu, len(newGame), mediaInstant*100))

		#Calculando lucro atual
		lucro += CalculoLucro(Saiu, j)
		print ("lucro atual: %s\n" % lucro)

		if Saiu > 10:
			inicioIndex = inicioIndex - tamCircuito + 1 + j
			break

	inicioIndex += tamCircuito
	print ("\n")


print ("Lucro Final: %s reais \n" % lucro)
print onze
print doze
print treze
print catorze
print quinze
print (onze+doze+treze+catorze+quinze)/numJogos
print ("\n")