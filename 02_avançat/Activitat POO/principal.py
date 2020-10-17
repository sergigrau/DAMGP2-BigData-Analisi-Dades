__author__ = 'sgraul@uoc.edu'

import sys
sys.path.append("./classes")

from classes.persona import Persona
from classes.alumne import Alumne
from classes.NIF import NIF

if __name__ == "__main__":
    alumnes=[]
    alumne1 = Alumne()
    alumne1.setNom('sergi')
    alumne1.setNom('angel')
    nif1=NIF(12345678)
    alumne1.assignarIdentificador(nif1)
    print(alumne1.obtenirIdentificador())
    alumne2 = Alumne('joan', 1)
    alumne2.assignarIdentificador(nif1)
    alumnes.append(alumne1)
    alumnes.append(alumne2)
    for a in alumnes:
        print(a)
    
    print(Persona.obtenirComptador())
    print(alumne1==alumne2)