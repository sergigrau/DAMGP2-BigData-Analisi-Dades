from persona import Persona
from NIF import NIF
class Alumne(Persona):
    def __init__(self, nom='', num_alumne=0):
        Persona.__init__(self,nom)
        self.__num_alumne=num_alumne

    def getNumeroAlumne(self):
        return self.__num_alumne
    
    def setNumeroAlumne(self, numero):
        self.__num_alumne=numero

    def getNom(self):
        return Persona.getNom(self)

    def setNom(self, nom):
        Persona.setNom(self, nom)

    def __str__(self):
        return self.getNom()+'-'+(str(self.getNumeroAlumne()))
    
    def __eq__(self, altre):
        return self.obtenirIdentificador()==altre.obtenirIdentificador()
    
if __name__ == "__main__":
    print('Joc de proves')
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