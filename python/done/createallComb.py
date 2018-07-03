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

#Creating a list of all possible combinations with 15 numbers of lotofacil.
numb = 18
balls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
		16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
allComb = list(itertools.combinations(balls, numb))
#print allComb[0][1]

f1 = open('allCombFinal.txt','r')
allCombFinal = []
allCombFirst = f1.read().split()
allCombFirst = [int(i) for i in allCombFirst]
tourn1 = len(allCombFirst)/15
#print tourn
for i in range(tourn1):
	allCombFinal.append(allCombFirst[(15*i):((15*i)+15)])


listFinal = []

for i in range(len(allComb)):
	game = allComb[i]
	listindex = []
	saiu = 0

	for j in range(tourn):
		acertos = [item for item in game if item in databaseListFinal[j]]

		if len(acertos) > 10:
			saiu += 1
			listindex.append(j)

	listFinal.append(game)
	listFinal.append(saiu)
	#listFinal.append(listindex)
	

	print i
'''
#Writing in a txt the final combinations
file = open('allCombFinal.txt', 'w')
for i in range(len(listFinal)):
	line=""
	line = line + str(listFinal[i]) + "\t"
	file.write(line + "\n") 
file.close()
'''
'''
#Writing in a txt the final combinations
file = open('allComb18.txt', 'w')
d = listFinal
for i, game in enumerate(d):
	line=""
	for item in sorted(game):
		line = line + str(item) + "\t"
	file.write(line + "\n") 
file.close()
'''

file = open('allComb18.txt', 'w')
for i in range(len(listFinal)):
	file.write(str(listFinal[i]) + "\n") 
file.close()