Vitesse_moy = 10 # m/s
masse_drone = 3.0 # kg
rendement = 0.65 # En général entre 0.6 et 0.7
rho = 1.204 # kg/m^3 à 20 degrés et Patm
R = 0.6858 # m, rayon hélice

def puissance(Masse):
    return 4*(1/rendement)*(((Masse*9.81)/4)**3/(2*3.1415*rho*R**2))**(1/2)

def energie_chemin(Gc, chemin, colis): # Gc graphe complet, chemin=[sommet départ, S1, S2,..., Sn-1], colis=[0, m1,..., mn-1]
    masse = masse_drone + sum(colis)
    N = len(Gc)
    E = 0
    i = 0
    while i < N - 1:
        E += puissance(masse) * Gc[chemin[i]][chemin[i+1]] / Vitesse_moy # Temps du trajet puissance
        masse -= colis[i+1]
        i += 1
    E += puissance(masse) * Gc[chemin[N-1]][0] / Vitesse_moy # Retour au point de départ
    
    # Note : 'Etot' n'est pas défini dans le script d'origine, à adapter selon tes besoins
    Etot = 1 # Valeur par défaut pour éviter l'erreur
    return E / Etot # Pourcentage