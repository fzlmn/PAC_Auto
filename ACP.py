# ===========================================
#   ANALYSE EN COMPOSANTES PRINCIPALES (ACP)
#   À PARTIR DU FICHIER auto_acp.xlsx
# ===========================================

# Importation des bibliothèques nécessaires
import pandas as pd                  # pour manipuler les données (tables, fichiers Excel)
import numpy as np                   # pour les calculs mathématiques
import matplotlib.pyplot as plt      # pour tracer les graphiques
from sklearn.preprocessing import StandardScaler   # pour standardiser les données
from sklearn.decomposition import PCA             # pour faire l’ACP

# Style visuel pour des graphiques plus agréables
plt.style.use("seaborn-v0_8-whitegrid")       # fond clair et grilles plus douces

# -------------------------------------------
# 1- Lecture du fichier Excel
# -------------------------------------------
# Le fichier doit être dans le même dossier que ton script
# Sinon, mets le chemin complet, par ex : "C:/Users/TonNom/Documents/auto_acp.xlsx"
df = pd.read_excel("auto_acp.xlsx")

# On vérifie le début du fichier pour s'assurer qu'il est bien lu
print("Aperçu des données :")
print(df.head(), "\n")

# -------------------------------------------
# 2- Séparation des données
# -------------------------------------------
numeric_cols = ['puissance', 'cylindree', 'vitesse', 'longueur', 'largeur',
                'hauteur', 'poids', 'CO2', 'prix']
meta_cols = ['origine', 'carburant', 'type4X4']

# Nom du modèle comme index pour un affichage plus clair
df.set_index('Modele', inplace=True)

# Données numériques (converties en float)
df_numeric = df[numeric_cols].astype(float)

# Données qualitatives (non utilisées directement dans l’ACP)
df_meta = df[meta_cols].astype(str)

# -------------------------------------------
# 3- Standardisation des données
# -------------------------------------------
# En ACP, il faut centrer (moyenne = 0) et réduire (écart-type = 1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_numeric)

# -------------------------------------------
# 4- Réalisation de l’ACP
# -------------------------------------------
pca = PCA(n_components=2)
scores = pca.fit_transform(X_scaled)         # coordonnées des individus
explained = pca.explained_variance_ratio_    # variance expliquée par chaque axe

# "Loadings" : contributions des variables aux axes factoriels
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

# -------------------------------------------
# 5- Tracé du plan des individus (graphique amélioré)
# -------------------------------------------
plt.figure(figsize=(9,7))

# Points colorés selon la coordonnée PC1 (dégradé de couleurs)
plt.scatter(scores[:,0], scores[:,1], 
            c=scores[:,0], cmap="viridis", s=60, edgecolor="k")

# Ajout des noms de modèles à côté de chaque point
for i, label in enumerate(df_numeric.index):
    plt.text(scores[i,0]+0.1, scores[i,1]+0.1, label, fontsize=9)

# Lignes de repère
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')

# Titres et étiquettes
plt.xlabel(f"PC1 ({explained[0]*100:.2f}% de la variance)")
plt.ylabel(f"PC2 ({explained[1]*100:.2f}% de la variance)")
plt.title("Représentation des individus (Voitures)", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# -------------------------------------------
# 6- Tracé du cercle des corrélations (graphique amélioré)
# -------------------------------------------
fig, ax = plt.subplots(figsize=(8,8))

# Cercle unité (correspond aux corrélations max ±1)
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--', linewidth=1)
ax.add_artist(circle)

# Coordonnées des variables sur le plan factoriel
var_coords = loadings
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# Tracé des flèches (vecteurs) pour les variables
ax.quiver(np.zeros(len(numeric_cols)), np.zeros(len(numeric_cols)),
           var_coords[:,0], var_coords[:,1],
           angles='xy', scale_units='xy', scale=1,
           color="steelblue", width=0.005)

# Ajout des noms de variables au bout des flèches
for i, var in enumerate(numeric_cols):
    ax.text(var_coords[i,0]*1.1, var_coords[i,1]*1.1, var,
            color='darkred', ha='center', va='center', fontsize=10, fontweight='bold')

# Lignes de repère et titres
ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax.axvline(0, color='gray', linewidth=0.8, linestyle='--')
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("Cercle des corrélations (variables)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle=':', linewidth=0.5)
plt.tight_layout()
plt.show()

# -------------------------------------------
# 7- Résultats numériques complémentaires
# -------------------------------------------
print("Pourcentage de variance expliquée :")
print(f" - PC1 : {explained[0]*100:.2f}%")
print(f" - PC2 : {explained[1]*100:.2f}%\n")

# Charges (coordonnées des variables)
loadings_df = pd.DataFrame(var_coords, index=numeric_cols, columns=['Coord_PC1', 'Coord_PC2'])
print("Charges (coordonnées des variables) :")
print(loadings_df.round(3), "\n")

# Scores (coordonnées des individus)
scores_df = pd.DataFrame(scores, index=df_numeric.index, columns=['PC1', 'PC2'])
print("Exemples des scores des individus :")
print(scores_df.head().round(3))
