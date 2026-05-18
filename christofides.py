## Détermination d'un arbre couvrant de poids minimal

def plus_proche_sommet(M, distances, tstTraite):
    min_val = float("Inf")
    min_index = -1
    for v in range(len(M)):
        if distances[v] < min_val and not tstTraite[v]:
            min_val = distances[v]
            min_index = v
    return min_index

def prim(M): # Matrice d'adjacence complète
    distances = [float("Inf")] * len(M)
    distances[0] = 0
    parent = [None] * len(M)
    tstTraite = [False] * len(M)
    parent[0] = -1
    
    for _ in range(len(M)):
        u = plus_proche_sommet(M, distances, tstTraite)
        tstTraite[u] = True
        for v in range(len(M)):
            if distances[v] > M[u][v] > 0 and not tstTraite[v]:
                distances[v] = M[u][v]
                parent[v] = u
                
    return [[parent[i], i, M[i][parent[i]]] for i in range(1, len(M))]

def Arbrecouvrant(M): # Matrice d'adjacence complète
    M2 = [[0 for i in range(len(M))] for j in range(len(M))]
    for i in prim(M):
        M2[i[0]][i[1]] = i[2]
        M2[i[1]][i[0]] = i[2]
    return M2

def degre_noeud(M, i):
    v = 0
    for j in M[i]:
        if j != 0:
            v += 1
    if v % 2 == 1:
        return True
    else:
        return False

def barycentre(C, L, masse): # Nécessite de passer les coordonnées C
    abs_vals = [C[L[i]][0]*masse[i] for i in range(len(L))]
    ord_vals = [C[L[i]][1]*masse[i] for i in range(len(L))]
    return [sum(abs_vals)/sum(masse), sum(ord_vals)/sum(masse)]

def complete_couvrant(C, G, L, masse): 
    M = Arbrecouvrant(G)
    N = []
    for i in range(len(M)):
        if degre_noeud(M, i):
            N.append(i)
    n = len(N) / 2
    for i in range(int(n)):
        # La fonction 'distance' doit être importée ou définie (ex: distance euclidienne)
        import math
        def distance(p1, p2):
            return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
            
        MIN = [distance(C[L[j]], barycentre(C, L, masse)) for j in N]
        a = MIN.index(min(MIN))
        A = N[a]
        Z = [G[A][j] for j in N[:a]] + [float('inf')] + [G[A][j] for j in N[a+1:]]
        b = Z.index(min(Z))
        B = N[b]
        M[A][B], M[B][A] = G[A][B], G[B][A]
        N.remove(A)
        N.remove(B)
    return M

def Voisins(M, i):
    V = []
    for j in range(len(M)):
        if M[i][j] != 0:
            V.append(j)
    return V

def suppressionArc(graphe, sommet1, sommet2):
    graphe[sommet1].remove(sommet2)
    graphe[sommet2].remove(sommet1)

def ajoutArc(graphe, sommet1, sommet2):
    graphe[sommet1].append(sommet2)
    graphe[sommet2].append(sommet1)

def Parcours_Profondeur(graphe, origine, visite):
    visite[origine] = True
    for voisin in graphe[origine]:
        if not visite[voisin]:
            Parcours_Profondeur(graphe, voisin, visite)

def ArcValide(graphe, origine, voisin):
    if len(graphe[origine]) == 1:
        return True
    else:
        visiteAvecArc = [False] * len(graphe)
        Parcours_Profondeur(graphe, origine, visiteAvecArc)
        suppressionArc(graphe, origine, voisin)
        visiteSansArc = [False] * len(graphe)
        Parcours_Profondeur(graphe, origine, visiteSansArc)
        ajoutArc(graphe, origine, voisin)
        return sum(visiteAvecArc) == sum(visiteSansArc)

# Attention: 'chemin' doit être initialisé avant d'appeler cette fonction
def Cycle_Eulerien(chemin, graphe, origine):
    for voisin in graphe[origine]:
        if ArcValide(graphe, origine, voisin):
            chemin.append(voisin)
            suppressionArc(graphe, origine, voisin)
            Cycle_Eulerien(chemin, graphe, voisin)

def coupe_chemin(C):
    L = []
    for i in C:
        if i not in L:
            L.append(i)
    return L