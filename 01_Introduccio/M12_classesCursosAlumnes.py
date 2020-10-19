#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	programa que crea una classe Persona i unes subclasses Alumne i Professor.abs
#   mostra el funcionament senzill de la POO amb Python
#	autor: sergi.grau@fje.edu
#	versió: 15.02.2020
#


class Persona:
    """classe que representa una persona"""
    
    def mostrarDades(self):
        return self.__nom

    def __init__(self, nom:str, dni:str):
        self.__nom = nom
        self.__dni = dni


class Alumne(Persona):

    def mostrarDades(self)->str:
        return self.__nom + self.__curs

    def __init__(self, nom:str, dni:int, curs:str):
        super(Alumne, self).__init__(nom, dni)
        self.__curs = curs


persona = Persona('Sergi', 1234)
alumne = Alumne('Joan', 1234, 'DAM2')
print(alumne.mostrarDades())
