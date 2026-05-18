# Energy-Optimal Drone Delivery Routing / Drone livreur de colis recherche d'un chemin optimal

## 🇬🇧 English Version

[cite_start]This repository contains the code and research for a CPGE MP TIPE (Travail d'Initiative Personnelle Encadrée)[cite: 7]. [cite_start]The project aims to find the most energy-efficient delivery route for a drone operating in an urban environment (Toulouse, France)[cite: 4, 45, 148].

### 🎯 Project Objectives
[cite_start]The rise of urban delivery has led to increased pollution and traffic congestion caused by delivery trucks[cite: 5, 33]. [cite_start]Automated drone delivery presents an innovative alternative[cite: 6]. [cite_start]This project models a drone's energy consumption and determines the optimal sequence for delivering multiple packages to minimize energy usage[cite: 35, 45]. 

[cite_start]**Note on visuals:** For all diagrams, graphs, and illustrations regarding the physics model and algorithmic pathfinding, please refer to the attached [Presentation Document (Présentation TIPE - GINESTE Pierre.pdf)](Présentation TIPE - GINESTE Pierre.pdf)[cite: 66, 156, 177, 241].

### ⚙️ How It Works

#### 1. Physics Model
[cite_start]We estimate the drone's power consumption based on the load it carries[cite: 40]. [cite_start]The calculation relies on **Rankine's perfect propeller model**[cite: 99, 124].
* [cite_start]By equating the power supplied by the propeller to the kinetic energy gained by the air, we determine the power required for flight: $P = \sqrt{(mg/4)^3 / (2\pi\rho R^2)}$[cite: 428, 429].
* [cite_start]We assume a constant flight speed of 10 m/s (40 km/h)[cite: 332, 806].

#### 2. Pathfinding Algorithms
[cite_start]To calculate the optimal delivery sequence, the problem is divided into two steps based on **Bellman's principle of optimality**[cite: 39, 138]:
1. [cite_start]**Dijkstra's Algorithm:** Used to extract the shortest paths between all delivery points using geographical graph data representing the streets of Toulouse (data from `data.gouv.fr`)[cite: 39, 158, 342, 629].
2. **Traveling Salesperson Problem (TSP) Resolution:**
   * **Exact approach (Brute Force):** Calculates the cost of all permutations. [cite_start]Feasible only for $n \le 12$ packages[cite: 219, 220].
   * **Heuristic approach (Christofides):** Used for $n > 12$ packages. [cite_start]It uses a Minimum Spanning Tree and perfect matching to find a route in $O(n^3)$ complexity, resulting in a path approximately 15% longer than the absolute minimum but computed in reasonable time[cite: 236, 239].

---

## 🇫🇷 Version Française

# Drone Livreur de Colis : Recherche d'un chemin optimal énergétique 🚁📦

[cite_start]Ce dépôt héberge le code source et les recherches développés dans le cadre d'un TIPE de CPGE MP[cite: 7]. [cite_start]Le but de ce projet est de déterminer le trajet impliquant une consommation énergétique minimale pour un drone livrant un certain nombre de colis dans une ville[cite: 45].

> [cite_start]📚 **Pour plus de contexte et d'informations théoriques :** Veuillez consulter le document [MCOT](MCOT_48955_34278.pdf) qui détaille le positionnement thématique, la bibliographie complète et les enjeux réglementaires liés à l'espace aérien[cite: 10, 24, 36].
> 
> [cite_start]🖼️ **Pour accéder aux schémas et visualisations :** Le code ne générant pas nativement les images dans ce README, veuillez consulter le diaporama [Présentation TIPE](Présentation TIPE - GINESTE Pierre.pdf) pour visualiser le modèle physique du drone, les graphes de la ville de Toulouse et les différentes étapes de l'algorithme de Christofides[cite: 66, 156, 177, 241, 281].

### 🎯 Problématique
[cite_start]L'essor de la livraison urbaine engendre pollution et engorgement des routes[cite: 5]. [cite_start]La livraison par drones (expérimentée par des entreprises comme Wing ou DPD) est une alternative prometteuse[cite: 28, 29]. [cite_start]L'ordre de livraison étant défini par le placement des colis sous le drone, la question se pose : **Dans quel ordre les disposer pour effectuer le trajet le moins coûteux énergétiquement ?** [cite: 35]

### 🔬 Fonctionnement et Modélisation

#### 1. Modélisation Physique
[cite_start]Le calcul du coût énergétique prend en compte l'impact direct de la masse des colis sur la puissance demandée aux moteurs[cite: 40]. 
* [cite_start]L'étude s'appuie sur le **modèle de l'hélice de Rankine** et le théorème de Bernoulli[cite: 99, 403].
* [cite_start]La puissance $P$ nécessaire au vol stationnaire ou à vitesse constante est donnée par $P = \sqrt{\frac{(\frac{mg}{4})^3}{2\pi\rho R^2}}$[cite: 126, 429].
* [cite_start]L'énergie totale est calculée en intégrant cette puissance sur la durée du trajet, à une vitesse supposée constante de $40\text{ km/h}$[cite: 332].

#### 2. Implémentation Algorithmique
[cite_start]Le problème est séparé en deux phases distinctes, en s'appuyant sur le principe d'optimalité de Bellman[cite: 39]:

1. [cite_start]**Génération du graphe complet (Algorithme de Dijkstra) :** Les coordonnées des routes de Toulouse sont importées depuis un fichier `.csv` (`data.gouv.fr`)[cite: 342, 603]. [cite_start]Dijkstra est appliqué pour trouver les plus courts chemins reliant chaque paire de points de livraison[cite: 48, 158].

2. **Recherche de la tournée optimale :**
   * **Force brute par permutations :** Calcul du coût énergétique de tous les chemins possibles. [cite_start]Totalement inenvisageable pour un nombre de colis $n > 12$[cite: 219, 220]. 
   * **Heuristique de Christofides :** Pour les livraisons plus massives ($n > 12$), nous approchons le chemin parfait. [cite_start]L'algorithme (basé sur un arbre couvrant de poids minimal et un couplage parfait des sommets de degré impair) offre une complexité en $O(n^3)$[cite: 236, 239, 432]. [cite_start]Le chemin est en moyenne 15% plus long que le chemin optimal strict, mais calculable très rapidement[cite: 239].

### 📊 Résultats et Expérience
[cite_start]Une expérience en conditions réelles avec un drone (type Mavic) soulevant des masses allant de 20g à 120g a été menée pour valider le modèle[cite: 283, 284]. [cite_start]Les résultats montrent une corrélation forte entre la dépense énergétique simulée et celle mesurée sur le terrain[cite: 289, 310, 311]. [cite_start]De plus, le bilan montre qu'à l'heure, un drone consomme environ 1 kWh pour 30 colis livrés, contre 20 kWh pour 15 colis avec un camion de livraison classique[cite: 314].

### 📚 Sources Principales
* [cite_start]R. Bellman, *Dynamic Programming* (1957) [cite: 61]
* [cite_start]E.W. Dijkstra, *A short introduction to the art of programming* [cite: 62]
* [cite_start]Historique et droit : Encyclopaedia Universalis & A. Cassart [cite: 53, 58]
* [cite_start]Données géographiques : data.gouv.fr / module Python `NetworkX` [cite: 342, 518]
*(La liste exhaustive est disponible dans le MCOT joint au projet).*
