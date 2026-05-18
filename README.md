# Energy-Optimal Drone Delivery Routing

## English Version

This repository contains the source code and research developed for a CPGE MP TIPE (Travail d'Initiative Personnelle Encadrée). The goal of this project is to determine the most energy-efficient route for a drone delivering multiple packages in an urban environment.

> **Note on visuals and context:** For all diagrams, theoretical background, graphs of the city of Toulouse, and visual steps of the algorithms, please refer to the attached presentation and MCOT(french) documents.

### Context and Objectives
The rise of urban delivery leads to increased pollution and traffic congestion. Automated drone delivery is a promising alternative. Since the delivery order depends on how packages are arranged under the drone, the main question is: **In what order should they be delivered to minimize energy consumption?**

### Physics Model and Algorithms

#### 1. Physics Modeling
The energy cost calculation considers the direct impact of the packages' mass on the power required by the motors.
* The study is based on **Rankine's ideal propeller model** and Bernoulli's principle.
* The power $P$ required for hovering or constant-speed flight is calculated using the total mass and the propeller radius.
* Total energy is estimated by integrating this power over the flight duration, assuming a constant speed of 40 km/h.

#### 2. Pathfinding Implementation
Based on Bellman's principle of optimality, the problem is divided into two phases:
1. **Generating the complete graph (Dijkstra's Algorithm):** Geographical coordinates of Toulouse's roads are imported from a dataset. Dijkstra is used to find the shortest paths between every pair of delivery points.
2. **Finding the optimal tour:**
   * **Exact Resolution (Brute Force):** Calculates the energy cost of all possible permutations. Unfeasible for $n > 12$ packages.
   * **Christofides Heuristic:** Used for larger deliveries. This algorithm (based on a minimum spanning tree and perfect matching) has an $O(n^3)$ complexity. The resulting path is on average 15% longer than the absolute optimal path but can be computed incredibly faster.

### Results
A real-world experiment with a drone lifting varying weights (20g to 120g) validated the physical model, showing a strong correlation between simulated and measured energy expenditure. Furthermore, the study shows that in one hour, a drone consumes roughly 1 kWh to deliver 30 packages, compared to 20 kWh for a traditional truck delivering 15 packages.

---

## Version Française

# Drone livreur de colis, recherche d'un chemin optimal

Ce dépôt héberge le code source et les recherches développés dans le cadre d'un TIPE de CPGE MP. Le but de ce projet est de déterminer le trajet impliquant une consommation énergétique minimale pour un drone livrant un certain nombre de colis dans une ville.

> **Note sur les visuels et le contexte :** Pour tous les schémas, le contexte théorique, les graphes de la ville de Toulouse et les étapes visuelles des algorithmes, veuillez vous référer à la présentation et au document MCOT joints.

### Contexte et Objectifs
L'essor de la livraison urbaine engendre pollution et engorgement des routes. La livraison par drones est une alternative prometteuse. L'ordre de livraison étant défini par le placement des colis sous le drone, la question principale est : **Dans quel ordre les livrer pour minimiser la consommation d'énergie ?**

### Modèle Physique et Algorithmes

#### 1. Modélisation Physique
Le calcul du coût énergétique prend en compte l'impact direct de la masse des colis sur la puissance demandée aux moteurs. 
* L'étude s'appuie sur le **modèle de l'hélice de Rankine** et le théorème de Bernoulli.
* La puissance $P$ nécessaire au vol stationnaire ou à vitesse constante est calculée en fonction de la masse totale et du rayon des hélices.
* L'énergie totale est estimée en intégrant cette puissance sur la durée du vol, avec une vitesse constante supposée de 40 km/h.

#### 2. Implémentation Algorithmique
En s'appuyant sur le principe d'optimalité de Bellman, le problème est divisé en deux phases :
1. **Génération du graphe complet (Algorithme de Dijkstra) :** Les coordonnées géographiques des routes de Toulouse sont importées depuis un jeu de données. Dijkstra est utilisé pour trouver les plus courts chemins entre chaque paire de points de livraison.
2. **Recherche de la tournée optimale :**
   * **Résolution exacte (Force Brute) :** Calcule le coût énergétique de toutes les permutations possibles. Inenvisageable pour $n > 12$ colis.
   * **Heuristique de Christofides :** Utilisée pour les livraisons plus importantes. Cet algorithme (basé sur un arbre couvrant de poids minimal et un couplage parfait) offre une complexité en $O(n^3)$. Le trajet obtenu est en moyenne 15% plus long que le trajet optimal absolu, mais se calcule infiniment plus vite.

### Résultats
Une expérience en conditions réelles avec un drone soulevant différentes masses (20g à 120g) a validé le modèle physique, montrant une forte corrélation entre la dépense énergétique simulée et celle mesurée. De plus, l'étude montre qu'en une heure, un drone consomme environ 1 kWh pour livrer 30 colis, contre 20 kWh pour un camion classique livrant 15 colisLe calcul du coût énergétique prend en compte l'impact direct de la masse des colis sur la puissance demandée aux moteurs. 
* L'étude s'appuie sur le **modèle de l'hélice de Rankine** et le théorème de Bernoulli.
* La puissance $P$ nécessaire au vol stationnaire ou à vitesse constante est donnée par $P = \sqrt{\frac{(\frac{mg}{4})^3}{2\pi\rho R^2}}$.
* L'énergie totale est calculée en intégrant cette puissance sur la durée du trajet, à une vitesse supposée constante de $40\text{ km/h}$.

#### 2. Implémentation Algorithmique
Le problème est séparé en deux phases distinctes, en s'appuyant sur le principe d'optimalité de Bellman:

1. **Génération du graphe complet (Algorithme de Dijkstra) :** Les coordonnées des routes de Toulouse sont importées depuis un fichier `.csv` (`data.gouv.fr`). Dijkstra est appliqué pour trouver les plus courts chemins reliant chaque paire de points de livraison.

2. **Recherche de la tournée optimale :**
   * **Force brute par permutations :** Calcul du coût énergétique de tous les chemins possibles. Totalement inenvisageable pour un nombre de colis $n > 12$. 
   * **Heuristique de Christofides :** Pour les livraisons plus massives ($n > 12$), nous approchons le chemin parfait. L'algorithme (basé sur un arbre couvrant de poids minimal et un couplage parfait des sommets de degré impair) offre une complexité en $O(n^3)$. Le chemin est en moyenne 15% plus long que le chemin optimal strict, mais calculable très rapidement.

### Résultats et Expérience
Une expérience en conditions réelles avec un drone (type Mavic) soulevant des masses allant de 20g à 120g a été menée pour valider le modèle. Les résultats montrent une corrélation forte entre la dépense énergétique simulée et celle mesurée sur le terrain. De plus, le bilan montre qu'à l'heure, un drone consomme environ 1 kWh pour 30 colis livrés, contre 20 kWh pour 15 colis avec un camion de livraison classique.

### Sources Principales
* R. Bellman, *Dynamic Programming* (1957)
* E.W. Dijkstra, *A short introduction to the art of programming*
* Historique et droit : Encyclopaedia Universalis & A. Cassart
* Données géographiques : data.gouv.fr / module Python `NetworkX`
*(La liste exhaustive est disponible dans le MCOT joint au projet).*
