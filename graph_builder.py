import json
import numpy as np
import pandas as pd
from scipy.sparse import lil_matrix

def charger_graphe_ville(filepath):
    ## Convertir Base de donnée en matrice d'adjacence
    data = pd.read_csv(filepath, sep=";")
    T = pd.DataFrame(data, columns=["Geo Shape", "longueur"])

    # Supprimer les lignes avec une valeur NaN dans la colonne 'Geo Shape'
    T.dropna(subset=["Geo Shape"], inplace=True)

    # Conversion des chaines de caractère JSON en dictionnaires
    T["Geo Shape"] = T["Geo Shape"].apply(json.loads)
    # geo shape: dictionnaire avec clé ['coordonnées', 'type'].
    # 'type' ne nous intéresse pas donc on ne garde que les coordonnées
    T["Geo Shape"] = T["Geo Shape"].apply(
        lambda x: x["coordinates"][0]
        if isinstance(x, dict) and "coordinates" in x
        else None)

    # Convertion de la colonne "Geo Shape" en un array numpy
    geo_shapes = np.array(T["Geo Shape"])

    # récupérer la première et la dernière coordonnée de chaque ligne
    first_coords = [shape[0] for shape in geo_shapes]
    last_coords = [shape[-1] for shape in geo_shapes]

    # Création du tableau [coord départ, coord arrivée, longueur chemin] pour chaque sommet
    T = [[first, last, length]
         for first, last, length in zip(first_coords, last_coords, T["longueur"])]

    C=[] # Juste les coordonnées des sommets
    coordinate_set = set()

    for line in T:
        start_coord, end_coord, length = line[0], line[1], line[2]
        start_coord_tuple = tuple(start_coord)
        if start_coord_tuple not in coordinate_set:
            C.append(start_coord)
            coordinate_set.add(start_coord_tuple)
        
        end_coord_tuple = tuple(end_coord)
        if end_coord_tuple not in coordinate_set:
            C.append(end_coord)
            coordinate_set.add(end_coord_tuple)

    n = len(C)

    # Création de la matrice d'adjacence M
    M = lil_matrix((n, n))
    coord_to_index = {tuple(coord): index for index, coord in enumerate(C)}

    for i in T:
        a = coord_to_index[tuple(i[0])]
        b = coord_to_index[tuple(i[1])]
        if a != b:
            M[a, b] = i[2]
            M[b, a] = i[2]
            
    return C, M