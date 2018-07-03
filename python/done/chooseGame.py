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

#Creating a list of text.txt
f1 = open('bestallComb.txt','r')
testListFinal = []
testListFirst = f1.read().split()
testListFirst = [int(i) for i in testListFirst]
tourn1 = len(testListFirst)/15
#print tourn
for i in range(tourn1):
	testListFinal.append(testListFirst[(15*i):((15*i)+15)])

torneioEscolhido = 1521

#print databaseListFinal[1510]
listk = []

for i in range(len(testListFinal)):
	a = testListFinal[i]
	acertos = 0

	for j in range(100):
		acertos = [item for item in a if item in databaseListFinal[torneioEscolhido - 2 - j]]

		if len(acertos) > 10:
			listk.append(j)
			break

print listk
print listk.index(max(listk)) + 1