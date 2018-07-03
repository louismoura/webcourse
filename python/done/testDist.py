#see the best distance between TWO games

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
f1 = open('test.txt','r')
testListFinal = []
testListFirst = f1.read().split()
testListFirst = [int(i) for i in testListFirst]
tourn1 = len(testListFirst)/15
#print tourn
for i in range(tourn1):
	testListFinal.append(testListFirst[(15*i):((15*i)+15)])

total = []
total1 = []
total2 = []
result = []

for i in range(len(testListFinal)):
	a = testListFinal[i]
	indexfirsta = []

	for j in range(len(databaseListFinal)):
		acertosa = [item for item in a if item in databaseListFinal[j]]

		if len(acertosa) > 10:
			indexfirsta.append(j)

	

	for k in range(len(testListFinal)):
		dist = []
		indexfirstb = []
		b = testListFinal[k]


		for l in range(len(databaseListFinal)):
			acertosb = [item1 for item1 in b if item1 in databaseListFinal[l]]

			if len(acertosb) > 10:
				indexfirstb.append(l)

		#print indexfirsta
		#print indexfirstb

		indexFinal = sorted(list(set(indexfirsta + indexfirstb)))

		#print indexFinal

		for m in range(len(indexFinal)-1):
			distance = indexFinal[m+1] - indexFinal[m]
			dist.append(distance)

		dist10 = heapq.nlargest(20, dist)

		if 9 in dist10:
			total1.append(i+1)
			total1.append(k+1)

		if dist10.count(10) > 6:
			total2.append(i+1)
			total2.append(k+1)

		result.append(i+1)
		result.append(k+1)
		result.append(dist10)
		#print ("%s e %s, max = %s" % (i+1, k+1, dist10))
		total.append(dist10.count(10))

print max(total)
print total2
print total1

#Writing in a txt the final combinations
file = open('testDist.txt', 'w')
for i in range(len(result)):
	file.write(str(result[i]) + "\n") 
file.close()



