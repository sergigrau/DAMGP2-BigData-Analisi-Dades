from abc import ABC, ABCMeta, abstractmethod
class Persona(ABC):
    __comptador_persones=0

    def __init__(self, nom=''):
        self.__nom=nom
        Persona.__comptador_persones+=1
    
    @abstractmethod
    def getNom(self):
        return self.__nom
    
    @abstractmethod    
    def setNom(self, nom):
         self.__nom=nom

    def assignarIdentificador(self, identificador):
         self.__identificador:IdentificadorLegal=identificador
    
    def obtenirIdentificador(self):
         return self.__identificador

    @staticmethod
    def obtenirComptador():
        return Persona.__comptador_persones

    def __str__(self):
        pass
    def __eq__(self):
        pass

if __name__ == "__main__":
    print('Joc de proves')
    persones=[]
    persona1 = Persona()
    persona1.setNom('sergi')

    persona2 = Persona('joan')
    persones.append(persona1)
    persones.append(persona2)
    for p in persones:
        print(p.getNom())
    
    print(Persona.obtenirComptador())