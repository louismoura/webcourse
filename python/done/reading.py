import itertools
import math

#Function to count all odd numbers in a list
def GetOddCount(inputList):
    return sum(1-n%2 for n in inputList)

def GetXCount(inputList):
	return ((1 in inputList) + (7 in inputList) + (13 in inputList) + (19 in inputList) + (25 in inputList) + 
			(21 in inputList) + (17 in inputList) + (9 in inputList) + (5 in inputList))

def GetNACount(inputList, index):
	previous = databaseListFinal[index - 2]
	previous1 = [item for item in inputList if item in previous]
	return len(previous1)

def GetComb(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

#Creating a list of all tournaments of lotofacil, the first is 0
f = open('database.txt','r')
databaseListFinal = []
databaseListFirst = f.read().split()
databaseListFirst = [int(i) for i in databaseListFirst]
tourn = len(databaseListFirst)/15
#print tourn
for i in range(tourn):
	databaseListFinal.append(databaseListFirst[(15*i):((15*i)+15)])


#print ("Torneio: %s" % ( databaseListFinal[1564]))


#Creating a list of all possible combinations with 15 numbers of lotofacil.
# numb = 15
# balls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
# 		16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

numb = 2
balls = [4, 9, 10, 12, 14, 19, 21, 22, 25]
allComb = list(itertools.combinations(balls, numb))
print len(allComb)
print allComb
'''
#Checking sum possibility
sumComb = []
for i in range(len(allComb)):
	sumNumb = sum(allComb[i])
	if sumNumb > 169 and sumNumb < 220:
	 	sumComb.append(allComb[i])
print len(sumComb)

#Checking parity possibility
parComb = []
for i in range(len(sumComb)):
	odd = GetOddCount(sumComb[i])
	if odd > 5 and odd < 10:
	 	parComb.append(sumComb[i])
print len(parComb)

#Checking X possibility
XComb = []
for i in range(len(parComb)):
	xcount = GetXCount(parComb[i])
	if xcount > 3 and xcount < 8:
	 	XComb.append(parComb[i])
print len(XComb)


#Writing in a txt the final combinations
file = open('allComb.txt', 'w')
d = allComb
for i, game in enumerate(d):
	line=""
	for item in sorted(game):
		line = line + str(item) + "\t"
	file.write(line + "\n") 
file.close()

'''