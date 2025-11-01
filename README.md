# 🔍 Analyse en Composantes Principales (ACP) — Fichier auto_acp.xlsx
## 📘 Description du projet

Ce projet a pour objectif de réaliser une Analyse en Composantes Principales (ACP) à partir d’un fichier Excel contenant des caractéristiques techniques de différents modèles de voitures.
L’ACP permet de réduire la dimensionnalité des données tout en conservant l’essentiel de l’information, afin de mieux visualiser les relations entre les variables et les individus (modèles de voitures).

## 📂 Données utilisées

Le fichier auto_acp.xlsx contient :

Des variables quantitatives : puissance, cylindrée, vitesse, longueur, largeur, hauteur, poids, CO₂, prix

Des variables qualitatives : origine, carburant, type4x4

Une colonne identifiant chaque modèle (Modele)

## ⚙️ Étapes du programme
### 1️⃣ Lecture et préparation des données

Chargement du fichier Excel avec pandas

Séparation entre données numériques (utilisées pour l’ACP) et qualitatives (métadonnées)

Mise en index du nom du modèle pour un affichage clair

### 2️⃣ Standardisation

Avant l’ACP, toutes les variables numériques sont centrées (moyenne = 0) et réduites (écart-type = 1) grâce à StandardScaler de scikit-learn.

### 3️⃣ Réalisation de l’ACP

L’ACP est calculée avec PCA(n_components=2) pour extraire les deux premiers axes principaux (PC1 et PC2).

Le programme calcule :

Les valeurs propres (variance expliquée par chaque axe)

Les coordonnées des individus (scores)

Les charges (loadings) représentant la contribution des variables à la formation des axes

La contribution des individus à chaque axe (quantifie leur influence)

### 4️⃣ Visualisation graphique

Deux graphiques principaux sont générés :

Plan des individus (voitures)
Représente les modèles de voitures sur le plan défini par PC1 et PC2.

Cercle des corrélations
Montre la contribution et la corrélation de chaque variable aux axes principaux.

Les graphiques utilisent un style “seaborn whitegrid” pour une meilleure lisibilité et une palette de couleurs harmonieuse.

### 5️⃣ Résultats numériques affichés

Le programme affiche :

Le pourcentage de variance expliquée par PC1 et PC2

Les valeurs propres associées à chaque axe

Les coordonnées (charges) des variables sur chaque axe

La contribution (%) de chaque variable et individu à la formation des axes

## 📊 Interprétation rapide

PC1 (Axe 1) : regroupe les variables qui évoluent ensemble (ex. puissance, cylindrée, poids, CO₂).

PC2 (Axe 2) : peut représenter des dimensions orthogonales (ex. taille du véhicule vs performance).

Les flèches proches du cercle dans le graphe des corrélations indiquent une forte contribution.

Les points éloignés de l’origine dans le plan des individus sont ceux qui influencent le plus la construction des axes.

## 🧠 Bibliothèques utilisées

pandas — manipulation de données

numpy — calculs numériques

matplotlib — visualisation

scikit-learn — standardisation et PCA

## 🚀 Lancer le script

Place le fichier auto_acp.xlsx dans le même dossier que le script.

Exécute le programme :

python analyse_acp.py


Observe les sorties dans la console et les graphiques générés.

## 🖼️ Résultats visuels

### 1. Représentation des individus (voitures)
Voici la projection des individus sur les deux premières composantes principales :

<img width="1800" height="950" alt="image" src="https://github.com/user-attachments/assets/58868b4a-9c13-4e67-9bbc-ddc25ccad702" />


---

### 2. Cercle des corrélations (variables)
Représentation des variables dans le cercle des corrélations :

<img width="1800" height="950" alt="image" src="https://github.com/user-attachments/assets/b9cf4cfc-ca40-4294-b9a3-11e3aa245585" />


---

### 3. Résumé des résultats dans le terminal
Exemple de sortie texte avec les valeurs propres, les contributions et les scores :

<img width="1550" height="600" alt="image" src="https://github.com/user-attachments/assets/db3087e0-5b3c-4844-850e-bfed7708207d" />


