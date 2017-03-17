# Exercicis que mostra les persones amb grau de similitud més alt
# author sergi.grau@fje.edu
# version 1.0 20.2.2017
from math import sqrt
from M01_preferencies import critiques
from M03_coeficient_pearson import sim_pearson

#funció que retorna les n-persones més semblants
def mesSemblants(prefs,persona,n=5,similar=sim_pearson):
    puntuacions=[(similar(prefs,persona,altre),altre) for altre in prefs if altre!=persona]
    puntuacions.reverse( )
    return puntuacions[0:n]


print(mesSemblants(critiques,'Sergi'))