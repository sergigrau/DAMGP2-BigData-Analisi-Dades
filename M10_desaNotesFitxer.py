#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	programa que pregunta les notes d'un conjunt d'alumnes d'un curs. 
# 	El programa desa en una estructura de dades del tipus diccionari 
#	la informació corresponen al nom de l'alumne i de la seva nota de curs.
#	Per indicar que no queden més alumnes, utilitzem el mot FI. 
#	Finalment mostra una llista de les qualificacions, de més a menys, així com la mitjana de les notes.
#	autor: sergi.grau@fje.edu
#	versió: 15.02.2017
#
nom=''
nota=''
suma=0
ALUMNES={}

def desarDades(llista):
	f = open('exercici14.txt','a') 
	for x in llista:
		f.write(x+"-"+str(llista[w])+"\n")
	f.close()

def recuperarDades():
	f = open('exercici14.txt') 
	cadena = f.read()
	print (cadena)
	
recuperarDades()

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

desarDades(ALUMNES)
