#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	programa que crea una classe Persona i unes subclasses Alumne i Professor.abs
#   mostra el funcionament senzill de la POO amb Python
#	autor: sergi.grau@fje.edu
#	versió: 15.02.2017
#


class Persona:
    """classe que representa una persona"""
    nom = ''
    dni = 0

    def mostrarDades(self):
        return self.nom

    def __init__(self, nom, dni):
        self.nom = nom
        self.dni = dni


class Alumne(Persona):
    curs = ''

    def mostrarDades(self):
        return self.nom + self.curs

    def __init__(self, nom, dni, curs):
        super(Alumne, self).__init__(nom, dni)
        self.curs = curs


persona = Persona('Sergi', 1234)
alumne = Alumne('Joan', 1234, 'DAM2')
print(alumne.mostrarDades())
