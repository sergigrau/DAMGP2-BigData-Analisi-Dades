# Exercici que troba la similitud de 2 pref de persones amb distancia euclidiana
# author sergi.grau@fje.edu
# version 1.0 20.2.2017
from math import sqrt
from M01_preferencies import critiques

# Funció que retorna la distància euclidiana que indica la similitud entre
# 2 persones
def sim_distancia(prefs, persona1, persona2):
    # llista amb les pelis comuns
    items_comuns = {}
    for item in prefs[persona1]:
        if item in prefs[persona2]:
            items_comuns[item] = 1
    # si no hi ha puntuació en comú, return 0
    if len(items_comuns) == 0:
        return 0
    # distancia euclidiana
    suma_quadrats = sum([pow(prefs[persona1][item] - prefs[persona2][item], 2)
                          for item in prefs[persona1] if item in prefs[persona2]])
    return 1 / (1 + suma_quadrats)


print(critiques['Sergi'])
print(critiques['Sergi']['Alien'])

print(sim_distancia(critiques,'Laura','Sergi'))