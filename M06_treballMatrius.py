#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	Crea una matriu de 3x3 i mostra la informació dels següents elements: 
#	tota la matriu, element cantonada esquerra, cantonada dreta, primera fila i última columna.
#	seleccioneu els elements de la diagonal
#	autor: sergi.grau@fje.edu
#	versió: 15.02.2017
#       
M = [	[1, 2, 3], 
		[4, 5, 6],
		[7, 8, 9] ]
print(M)
print(M[0][0])
print(M[2][2])
print(M[0])
print([fila[2] for fila in M] )
print([M[i][i] for i in [0, 1, 2]] )
G=(sum(row) for row in M)
print (next(G))
print (next(G))
print ({sum(fila) for fila in M})
