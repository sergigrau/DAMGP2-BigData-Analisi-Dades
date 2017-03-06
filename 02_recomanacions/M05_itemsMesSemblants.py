# Exercicis que mostra els items amb grau de similitud més alt
# author sergi.grau@fje.edu
# version 1.0 20.2.2017
from math import sqrt
from M01_preferencies import critiques
from M03_coeficient_pearson import sim_pearson

#funció que retorna els items més semblants
def obtenirRecomanacions(prefs,persona,similar=sim_pearson):
    totals={}
    simSums={}
    for altre in prefs:
        # no es compara amb si mateix
        if altre==persona: continue
        sim=similar(prefs,persona,altre)
        # ignora puntuacions <=0
        if sim<=0: continue
        for item in prefs[altre]:
            # només es consideren les pelis no vistes
            if item not in prefs[persona] or prefs[persona][item]==0:
                # similar * puntuacio 
                totals.setdefault(item,0) 
                totals[item]+=prefs[altre][item]*sim 
                # suma de similituds
                simSums.setdefault(item,0) 
                simSums[item]+=sim
    # llista normalitzada
    rankings=[(total/simSums[item],item) for item,total in totals.items()]
    # Retornem la llista ordenada 
    rankings.sort( ) 
    rankings.reverse( ) 
    return rankings


print(obtenirRecomanacions(critiques,'Sergi'))