from abc import ABC, ABCMeta, abstractmethod
class IndentificadorLegal(ABC):
    def __init__(self, numero=0):
        self.__numero=numero

    @abstractmethod
    def getNumero(self):
        return self.__numero
    
    @abstractmethod    
    def setNumero(self, numero):
         self.__numero=numero