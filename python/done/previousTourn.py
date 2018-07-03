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
Esse metodo calcula o numero de acertos utilizando jogos passados
"""

#VARIAVEIS QUE PODEM SER ALTERADAS
numJogos = 1000
numPrevious = 1

#VARIAVEIS FIXAS
inicioIndex = tourn - numJogos
somaSaiu = 0.0 
somaTamanho = 0.0
numJogosReal = 0.0
listSaiu = []



def GetGamePrevious(index):
	previous = databaseListFinal[index - 1 - numPrevious]
	return previous


while (inicioIndex <= tourn):

	previousTorn = GetGamePrevious(inicioIndex)

	acertos = [item for item in previousTorn if item in databaseListFinal[inicioIndex - 1]]
	erros = [item for item in previousTorn if item not in databaseListFinal[inicioIndex - 1]]

	somaSaiu += float(len(acertos)) 
	somaTamanho += len(previousTorn)
	mediaInstant = len(acertos)/len(previousTorn)
	numJogosReal += 1

	print ("Previo: %s" % previousTorn)
	print ("Torneio: %s: %s" % (inicioIndex, databaseListFinal[inicioIndex - 1]))
	print ("Saiu: %s dos %s (%0.2f%%)" % (len(acertos), len(previousTorn), mediaInstant*100))
	print ("Nao saiu do previous: %s" % erros)
	print ("\n")
	inicioIndex += 1

print ("Saiu: %0.2f de %0.2f" % ((somaSaiu/numJogosReal),(somaTamanho/numJogosReal)))

