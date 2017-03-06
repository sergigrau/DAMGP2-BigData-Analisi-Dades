# Exercici que troba la similitud de 2 pref de persones amb coef. Pearson
# author sergi.grau@fje.edu
# version 1.0 20.2.2017
from math import sqrt
from M01_preferencies import critiques

# Returna el coeficient de correlació de Pearson
def sim_pearson(prefs, p1, p2):
    # llista de les pelis mutuament puntuades
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # troba el nombre d'elements
    n = len(si)
    # si no hi ha puntiació en comú, retorna 0
    if n == 0:
        return 0
    # suma de les preferències
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # suma dels quadrats
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # suma dels productes
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    # coef de Pearson
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


print(sim_pearson(critiques,'Laura','Sergi'))
