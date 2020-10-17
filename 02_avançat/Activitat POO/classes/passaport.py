from identificadorLegal import IndentificadorLegal
class Passaport(IndentificadorLegal):
    def __init__(self, numero=0, pais=''):
        IndentificadorLegal.__init__(self,numero)
        self.__pais=pais
    @property
    def pais(self):
        return self.__pais
    @pais.setter
    def pais(self, pais):
        self.__pais=pais

    def getNumero(self):
        return IndentificadorLegal.getNumero(self)
    
    def setNumero(self, numero): 
        IndentificadorLegal.setNumero(numero)

    def __str__(self):
        return str(self.getNumero())+'-'+self.pais

if __name__ == "__main__":
    print('Joc de proves')
    pass1 = Passaport(12345,'USA')
    print(pass1)