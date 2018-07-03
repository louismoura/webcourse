import itertools
import math
import heapq

#Creating a list of todos os melhores jogos of lotofacil, the first is 0
f = open('allComb20.txt','r')
allCombList = []
allCombListFinal = []
allCombListFirst = f.read().split()
for i in range(len(allCombListFirst)):
	allCombListFinal.append(allCombListFirst[i].strip(', ( )')) 
lenght = len(allCombListFinal)/16
#print tourn
for i in range(lenght):
	allCombList.append(allCombListFinal[(16*i):((16*i)+16)])

results = []

for i in range(len(allCombList)):
	results.append(allCombList[i][15])

results20max = heapq.nlargest(40, results)

games = []

for i in range(len(allCombList)):
	if allCombList[i][15] in results20max:
		games.append(allCombList[i])

for i in range(len(games)):
	games[i].pop()

#print games
#print len(games)

#Writing in a txt the final combinations
file = open('allCombFinal.txt', 'w')
for i in range(len(games)):
	line = ""
	for j in range(15):
		line1 = str(games[i][j]) + "\t"
		line = line + line1
	file.write(line + "\n") 
file.close()