

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


#Creating a list of todos os melhores jogos of lotofacil, the first is 0
f1 = open('test.txt','r')
indexallComb = []
allCombListFinal = []
allCombListFirst1 = f1.read().split()
allCombListFirst1 = [int(j) for j in allCombListFirst1]

indexallComb.append(0)
for i in range(len(allCombListFirst1)-1):
	if allCombListFirst1[i] > allCombListFirst1[i+1]:
		indexallComb.append(i+1)
indexallComb.append(len(allCombListFirst1))

for i in range(len(indexallComb)-1):
	allCombListFinal.append(allCombListFirst1[indexallComb[i]:indexallComb[i+1]])

#----------------------------------------------------------------------
tam=len(allCombListFinal)
distList = []
distList1 = []
distList2 = []

for i in range(tam):
	
	a = allCombListFinal[i]

	for j in range(tam):
		result = []
		dist = []
		b = allCombListFinal[j]

		if b == a:
			continue

		if a[0] <= b[0]:
			result.append(a[0])
			for k in range(300):
				c = [x for x in b if x > result[-1]]
				if len(c) == 0:
					break
				result.append(c[0])
				d = [y for y in a if y > result[-1]]
				if len(d) == 0:
					break
				result.append(d[0])
			
		if a[0] > b[0]:
			result.append(b[0])
			for k in range(300):
				c = [x for x in a if x > result[-1]]
				if len(c) == 0:
					break
				result.append(c[0])
				d = [y for y in b if y > result[-1]]
				if len(d) == 0:
					break
				result.append(d[0])
			
		for m in range(len(result)-1):
			distance = result[m+1] - result[m]
			dist.append(distance)

		dist1 = heapq.nlargest(15, dist)

		distList1.append(max(dist))

		#if max(dist) < 27:
			
		distList2.append(i+1)
		distList2.append(j+1)
		distList2.append(dist1)

		print i

dist10 = heapq.nsmallest(20, distList1)

print dist10

'''

for i in range(len(dist10)):
	index = distList.index(dist10[i])
	j1 = distList[index-2]
	j2 = distList[index-1]
	print ("%s e %s, maior dist: %s" % (j1, j2, dist10[i]))
	distList.remove(dist10[i])
'''



#Writing in a txt the final combinations
file = open('testDist1.txt', 'w')
for i in range(len(distList2)):
	file.write(str(distList2[i]) + "\n") 
file.close()

'''
#Writing in a txt the final combinations
file = open('testDist.txt', 'w')
for i in range(len(result)):
	file.write(str(result[i]) + "\n") 
file.close()

'''

