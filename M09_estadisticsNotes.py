#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	Fes un programa que pregunti les 3 notes trimestrals d'un alumnes, i mosti la seva mitjana i desviació estàndard.
#	autor: sergi grau
#	versió: 21.01.2011
#
import math

NOTES=[]
mitjana=0
varianza=0
for i in range(3): 
	NOTES.append(int(input('entra una nota')))

mitjana=sum(NOTES)/len(NOTES)	
print('la nota mitjana és ',mitjana)

for i in range(3):
	varianza += (NOTES[i]-mitjana)**2
print('la desviació estàndard és ', math.sqrt(varianza))
