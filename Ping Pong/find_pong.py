#!/usr/bin/env python3

resultat = ""
with open("output.txt", "r") as f:
	for line in f: 
		if "O" in line :
			resultat += str("0")
		elif "I" in line :
			resultat += str("1")
output = bin(int(resultat))
print(resultat)
