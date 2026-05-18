from .physics_model import energie_chemin

def chemin_opti(Gc, colis):
    Min = energie_chemin(Gc, [k for k in range(len(Gc))], colis) # chemin zéro [0,1,2,3,...,n-1]
    ChemOpti = [k for k in range(len(Gc))]
    Perm = []
    permutations(Perm, [k for k in range(1, len(Gc))])
    for chemin in Perm:
        if energie_chemin(Gc, chemin, colis) < Min:
            Min = energie_chemin(Gc, chemin, colis)
            ChemOpti = chemin
    return [ChemOpti, Min]

# Modifie la liste perm pour y ajouter les permutations de deb
def permutations(perm, deb, fin=[]): # deb = liste des sommets sans le point de départ
    if len(deb) == 0:
        perm.append([0] + fin)
    else:
        for i in range(len(deb)):
            permutations(perm, deb[:i] + deb[i+1:], fin + deb[i:i+1])