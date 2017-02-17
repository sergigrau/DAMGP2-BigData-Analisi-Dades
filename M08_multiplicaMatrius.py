#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	Multipliqueu per dos tota la matriu de l'exercici 6
#	autor: sergi grau
#	versi—: 21.01.2011
#       
M = [	[1, 2, 3], 
		[4, 5, 6],
		[7, 8, 9] ]
print(M)
i=0
j=0
while (i<3):
	while(j<3):
		M[i][j]*=2
		j+=1
	i+=1
	
print (M)
		
