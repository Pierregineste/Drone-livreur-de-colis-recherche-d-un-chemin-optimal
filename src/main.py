import matplotlib.pyplot as plt
import networkx as nx
from tqdm import tqdm

# Importation des modules personnalisés
from src.graph_builder import charger_graphe_ville
from src.algorithms import completion
from src.optimization import chemin_opti

def main():
    # 1. Chargement des données géographiques
    print("Chargement des données de la ville...")
    # Assure-toi de placer ton fichier CSV dans un dossier 'data/'
    C, M = charger_graphe_ville("data/toulouse_streets.csv")

    # 2. Filtrage de la zone de simulation (Fenêtre de Toulouse)
    print("Filtrage de la zone d'étude...")
    G2 = nx.Graph()
    C2 = []
    L2 = []
    for i in tqdm(C):
        if 1.399145 < i[0] < 1.503258 and 43.573202 < i[1] < 43.617040:
            C2.append(i)
            L2.append(C.index(i))
            
    G2.add_nodes_from(L2)
    posito3 = {}
    for i in L2:
        posito3[i] = C[i]
        
    rows, cols = M.nonzero()
    for i, j in zip(rows, cols):
        if i <= j:
            if i in L2 and j in L2:
                G2.add_edge(i, j, weight=M[i,j])

    # 3. Initialisation des colis et points de livraison
    colis = ['Départ', '15 kg', '0.5 kg', '0.1 kg', '1 kg']
    coord_colis = [
        [1.475334438274966, 43.57870959790727], 
        [1.426947462227057, 43.66792337544156], 
        [1.447825719178776, 43.595436979947015], 
        [1.478582454254292, 43.605983760146], 
        [1.414944282469067, 43.583407510802695]
    ]
    
    J = nx.Graph()
    J.add_nodes_from(colis)
    posito = {}
    for i in colis:
        posito[i] = coord_colis[colis.index(i)]
        
    # 4. Dessin initial
    plt.figure(figsize=(10, 8))
    nx.draw(J, posito, with_labels=True, node_size=1800, node_color='#FFCA08')
    nx.draw_networkx_edges(G2, posito3, width=0.9, alpha=0.5)
    plt.title("Carte des livraisons sur Toulouse")
    plt.show()

    # 5. Calcul des plus courts chemins (Dijkstra)
    print("Calcul des chemins optimaux via Dijkstra...")
    L = [C.index(i) for i in coord_colis]
    B, _ = completion(M, L)

    # 6. Recherche du chemin optimal global
    print("Recherche de l'ordre de livraison optimal...")
    masses_colis = [0, 15, 0.5, 0.1, 1]
    CHO = chemin_opti(B, masses_colis)
    ChemOpti = CHO[0]

    # 7. Tracé du résultat final
    S = nx.Graph()
    S.add_nodes_from([k for k in range(1, len(B))])
    S.add_node('Départ')
    
    position = {}
    position['Départ'] = coord_colis[0]
    for l in range(1, len(B)):
        position[l] = coord_colis[ChemOpti[l]]

    plt.figure(figsize=(10, 8))
    nx.draw(S, position, node_size=1800, with_labels=True, node_color='#FFCA08')
    plt.title("Ordre Optimal de Livraison")
    plt.show()

if __name__ == "__main__":
    main()