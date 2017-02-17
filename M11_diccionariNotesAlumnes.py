#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	programa que pregunta les notes d'un conjunt d'alumnes d'un curs. 
# 	El programa desa en una estructura de dades del tipus diccionari 
#	la informació corresponen al nom de l'alumne i de la seva nota de curs.
#	Per indicar que no queden més alumnes, utilitzem el mot FI. 
#	Finalment mostra una llista de les qualificacions, de més a menys, així com la mitjana de les notes.
#	autor: sergi grau
#	versió: 21.01.2011
#
nom=''
nota=''
suma=0
ALUMNES={}
while True: 
	nom =  input('entra un nom')
	if nom=='FI':
		break
	try:
		 nota =input('entra una nota')
		 ALUMNES[nom]= int(nota)
	except:
		print ('problemes amb la nota')

for w in sorted(ALUMNES, key=ALUMNES.get, reverse=True): #retorna una nova llista, i accepta qualsevol tipus de dada
	print (w, ALUMNES[w])
	suma+=ALUMNES[w]

print ('la mitjana es', suma/len(ALUMNES))
