from tqdm import tqdm
import networkx as nx

# acquiert les plus courts chemins et les trajets entre un sommet de départ et tous les autres sommets donnés
def dijkstra(D, dep, L): # (Dictionnaire, point de départ, liste de sommets)
    assert all(D[u][v] >= 0 for u in D.keys() for v in D[u].keys())
    
    precedent = {i: None for i in D.keys()} # Dictionnaire des antécedents
    dejaTraite = {i: False for i in D.keys()} # Dictionnaire de connaissance ou non des chemins les plus courts
    distance = {i: float('inf') for i in D.keys()} # Dictionnaire de la longueur des chemins
    
    distance[dep] = 0
    a_traiter = [(0, dep)]
    
    while False in [dejaTraite[i] for i in L]:
        dist_noeud, noeud = a_traiter.pop()
        if not dejaTraite[noeud]:
            dejaTraite[noeud] = True
            for voisin in D[noeud].keys():
                dist_voisin = dist_noeud + D[noeud][voisin]
                if dist_voisin < distance[voisin]:
                    distance[voisin] = dist_voisin
                    precedent[voisin] = noeud
                    a_traiter.append((dist_voisin, voisin))
            a_traiter.sort(reverse=True)
            
    return [distance, precedent]

# transforme Matrice en dictionnaire
def dictionnaire(M): # (matrice d'adjacence (sparce matrice))
    D={} # Dictionnaire d'adjacence
    rows, cols = M.nonzero()
    L = [[] for _ in range(M.shape[0])]
    for i, j in zip(rows, cols):
        L[i].append(j)
        
    for i in range(M.shape[0]):
        d = {j: M[i,j] for j in L[i]}
        D[i] = d
        
    return D

# acquiert le poids des plus courts chemins et les trajets entre chaque couple de sommets à livrer
def completion(M, L): # (matrice d'adjacence (sparce matrice), Liste de sommets)
    D = dictionnaire(M)
    M2 = [[0 for i in range(len(L))] for j in range(len(L))] #Mat d'adjacence
    M3 = [[[] for i in range(len(L))] for j in range(len(L))] #Mat des chemins
    Poids = []
    Chemins = []
    
    for i in tqdm(range(len(L))):
        A = dijkstra(D, L[i], L)
        Poids.append(A[0])
        Chemins.append(A[1])
        
    for i in range(len(L)):
        for j in range(i, len(L)):
            M2[i][j] = Poids[i][L[j]]
            
    for i in range(len(L)):
        for j in range(i, len(L)):
            M2[j][i] = M2[i][j]
            
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            v = L[j]
            while v != None:
                if Chemins[i][v] != None:
                    M3[i][j].append(Chemins[i][v])
                v = Chemins[i][v]
            M3[i][j].reverse()
            M3[i][j].append(L[j])
            
    return M2, M3