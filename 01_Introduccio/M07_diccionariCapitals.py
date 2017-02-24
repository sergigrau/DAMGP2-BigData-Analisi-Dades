#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	Definiu un diccionari amb les capitals de 5 estats europeus. 
#	Mostreu un llistat de tot el diccionari, dels països, de les capitals,
#	dels països ordenats i les seves capitals, i finalment de les capitals ordenades i els països als que corresponen.
#	autor: sergi.grau@fje.edu
#	versió: 15.02.2017
#       
D = {'Espanya': 'Madrid', 'Fransa': 'Paris', 'Italia': 'Roma', 'Regne Unit': 'Londres', 'Alemania': 'Berlin'}
print (D) #mostra tot
Ks = list(D.keys()) 
print (Ks)
for clau in Ks: 
	print(clau) 
 
print ('######################')

for clau in Ks: 
 print(D[clau]) 

print ('######################')

for clau in sorted(D):
 print(clau)

print ('######################')

Vs = list(D.values())  
for valor in sorted(Vs): 
 print(valor) 

