#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	 1. Realitza un programa que demana la quantitat de segons i mostra quantes hores i minuts són.
#	autor: sergi.grau@fje.edu
#	versió: 15.02.2017
#       
segons=int(input('entra un nombre de segons'))
hores = int(segons /3600)
minuts= int( (segons % 3600) /60)
segons_r= segons % 60


print (segons,' són', hores, 'hores' ,minuts , 'minut/s i', segons_r, ' segons')

