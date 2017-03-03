# Diccionari amb les critiques de les pelis
# author sergi.grau@fje.edu
# version 1.0 20.2.2017
from math import sqrt

critiques = {'Laura': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
           'Pere': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
           'Sergi': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5},
           'Miquel': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
           'Jordi': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Carles': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}

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
    sum_of_squares = sum([pow(prefs[persona1][item] - prefs[persona2][item], 2)
                          for item in prefs[persona1] if item in prefs[persona2]])
    return 1 / (1 + sum_of_squares)


#print(critiques['Sergi'])
#print(critiques['Sergi']['Snakes on a Plane'])

print(sim_distancia(critiques,'Laura','Sergi'))