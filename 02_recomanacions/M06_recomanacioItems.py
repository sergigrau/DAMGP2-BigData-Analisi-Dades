# Exercicis que mostra filtratge per items i no per persones
# author sergi.grau@fje.edu
# version 1.0 17.3.2017
from math import sqrt
from M01_preferencies import critiques
from M02_distancia_euclidiana import sim_distancia
from M04_personesMesSemblants import mesSemblants

# funció que inverteix el conjunt de dades inicials.


def invertirPrefs(prefs):
    resultat = {}
    for persona in prefs:
        for item in prefs[persona]:
            resultat.setdefault(item, {})
            resultat[item][persona] = prefs[persona][item]
    return resultat


# funció que calcula els items més similars
def calcularItemsSimilars(prefs, n=10):
    resultat = {}
    # inverteix items<->critics
    itemPrefs = invertirPrefs(prefs)
    c = 0
    for item in itemPrefs:
        # Troba els items mes similars
        puntacions = mesSemblants(itemPrefs, item, n=n, similar=sim_distancia)
        resultat[item] = puntacions
    return resultat


def obtenirItemsRecomanats(prefs,itemsSimilars,usuari):
    classificacioUsuari=prefs[usuari]
    puntuacions={}
    totalSim={}
    # itera sobre els items puntuats per l'usuari
    for (item,rating) in classificacioUsuari.items():
        #per cadascun itera
        for (similar,item2) in itemsSimilars[item]:
        # Ignore if this user has already rated this item
            if item2 in classificacioUsuari: continue
            # calcula el pes relatiu per la preferencia mostrada per l'usuari
            puntuacions.setdefault(item2,0)
            puntuacions[item2]+=similar*rating
            # sumatori de les similituds
            totalSim.setdefault(item2,0)
            totalSim[item2]+=similar
    # divideix la puntuació total pel seu pes relatiu i obté una mitjana
    rankings=[(score/totalSim[item],item) for item,score in puntuacions.items()]
    # retorna els rankings ordenats
    rankings.sort( )
    rankings.reverse( )
    return rankings

itemsim=calcularItemsSimilars(critiques)
print(obtenirItemsRecomanats(critiques,itemsim,'Sergi'))
