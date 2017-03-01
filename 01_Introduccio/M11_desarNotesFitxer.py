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
import os

def desarDades(llista, dirPath):
	f = open(dirPath+'/M11_desarNotesFitxer.txt','a') 
	for x in llista:
		f.write(x+"-"+str(llista[x])+"\n")
	f.close()

def recuperarDades(dirPath):
	f = open(dirPath+'/M10_desarNotesFitxer.txt') 
	cadena = f.read()
	print (cadena)

def main():	

	realPath = os.path.realpath(__file__)  # /home/user/test/my_script.py
	dirPath = os.path.dirname(realPath)  # /home/user/test
	nom=''
	nota=''
	suma=0
	ALUMNES={}

	recuperarDades(dirPath)

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

	desarDades(ALUMNES, dirPath)

if __name__ == "__main__":
    main()
