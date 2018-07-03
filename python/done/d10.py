import itertools
import math
import heapq
from random import *


#Creating a list of all tournaments of lotofacil, the first is 0
f = open('d10.txt','r')
databaseListFinal = []
databaseListFirst = f.read().split()
databaseListFirst = [int(i) for i in databaseListFirst]
tourn = len(databaseListFirst)/15
#print tourn
for i in range(tourn):
	databaseListFinal.append(databaseListFirst[(15*i):((15*i)+15)])

soma = []

for i in range(len(databaseListFinal)):
	soma = soma + databaseListFinal[i]

print sorted(list(set(soma)))