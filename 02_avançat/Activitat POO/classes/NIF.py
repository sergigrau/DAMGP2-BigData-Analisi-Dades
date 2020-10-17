
from identificadorLegal import IndentificadorLegal
class NIF(IndentificadorLegal):
    def __init__(self, numero=''):
        IndentificadorLegal.__init__(self,numero)
        self.__lletra=''
        self.determinarLletra()

    def determinarLletra(self):
        lletres="TRWAGMYFPDXBNJZSQVHLCKE"
        self.__lletra=lletres[self.getNumero()%23]

    def getLletra(self):
        return self.__lletra

    def getNumero(self):
        return IndentificadorLegal.getNumero(self)
    
    def setNumero(self, numero):
         IndentificadorLegal.setNumero(numero)

    def __str__(self):
        return str(self.getNumero())+'-'+self.getLletra()

if __name__ == "__main__":
    print('Joc de proves')
    nif1 = NIF(12_345_678)
    print(nif1)    