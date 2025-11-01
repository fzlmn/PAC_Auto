# ===========================================
#   ANALYSE EN COMPOSANTES PRINCIPALES (ACP)
#   À PARTIR DU FICHIER auto_acp.xlsx
# ===========================================

# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Style visuel agréable
plt.style.use("seaborn-v0_8-whitegrid")

# -------------------------------------------
# 1- Lecture du fichier Excel
# -------------------------------------------
df = pd.read_excel("auto_acp.xlsx")
print("Aperçu des données :")
print(df.head(), "\n")

# -------------------------------------------
# 2- Séparation des données
# -------------------------------------------
numeric_cols = ['puissance', 'cylindree', 'vitesse', 'longueur', 'largeur',
                'hauteur', 'poids', 'CO2', 'prix']
meta_cols = ['origine', 'carburant', 'type4X4']

df.set_index('Modele', inplace=True)
df_numeric = df[numeric_cols].astype(float)
df_meta = df[meta_cols].astype(str)

# -------------------------------------------
# 3- Standardisation des données
# -------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_numeric)

# -------------------------------------------
# 4- Réalisation de l’ACP
# -------------------------------------------
pca = PCA(n_components=2)
scores = pca.fit_transform(X_scaled)  # coordonnées des individus
explained = pca.explained_variance_ratio_  # variance expliquée (%)
eigenvalues = pca.explained_variance_      # valeurs propres

# "Loadings" : coefficients des variables (corrélations avec les axes)
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

# -------------------------------------------
# 5- Calculs théoriques demandés
# -------------------------------------------

# === (1) Valeurs propres ===
# Elles représentent la variance expliquée par chaque composante principale.
print("\n=== VALEURS PROPRES ===")
for i, val in enumerate(eigenvalues):
    print(f" - Axe {i+1} : {val:.4f}")

# === (2) Formule de calcul des axes PC1 et PC2 ===
print("\n=== FORMULES DES COMPOSANTES ===")
print("PC1 et PC2 sont des combinaisons linéaires normalisées des variables initiales :")
print("PC1 = a1*puissance + a2*cylindree + ... + a9*prix")
print("où a1..a9 sont les coefficients (loadings) de la 1ère composante principale.\n")

# === (3) Contribution des variables à la formation des axes ===
# Chaque variable contribue proportionnellement au carré de sa corrélation avec l’axe.
# Formule : (loading^2 / somme des loading^2 de l’axe) * 100
contrib_vars = (loadings ** 2)
contrib_vars = contrib_vars / contrib_vars.sum(axis=0) * 100
contrib_vars_df = pd.DataFrame(contrib_vars, index=numeric_cols,
                               columns=['Contrib_PC1(%)', 'Contrib_PC2(%)'])

print("=== CONTRIBUTION DES VARIABLES AUX AXES ===")
print(contrib_vars_df.round(2), "\n")

# === (4) Contribution des individus à la formation des axes ===
# Formule : (score^2 / somme(score^2 de l’axe)) * 100
scores_squared = scores ** 2
contrib_indiv = scores_squared / np.sum(scores_squared, axis=0) * 100
contrib_indiv_df = pd.DataFrame(contrib_indiv, index=df.index,
                                columns=['Contrib_PC1(%)', 'Contrib_PC2(%)'])

print("=== CONTRIBUTION DES INDIVIDUS AUX AXES ===")
print(contrib_indiv_df.head().round(2), "\n")

# -------------------------------------------
# 6- Tracé du plan des individus
# -------------------------------------------
plt.figure(figsize=(9,7))
plt.scatter(scores[:,0], scores[:,1], c=scores[:,0], cmap="viridis", s=60, edgecolor="k")

for i, label in enumerate(df_numeric.index):
    plt.text(scores[i,0]+0.1, scores[i,1]+0.1, label, fontsize=9)

plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')
plt.xlabel(f"PC1 ({explained[0]*100:.2f}% de la variance)")
plt.ylabel(f"PC2 ({explained[1]*100:.2f}% de la variance)")
plt.title("Représentation des individus (Voitures)", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# -------------------------------------------
# 7- Tracé du cercle des corrélations
# -------------------------------------------
fig, ax = plt.subplots(figsize=(8,8))
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--', linewidth=1)
ax.add_artist(circle)

var_coords = loadings
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

ax.quiver(np.zeros(len(numeric_cols)), np.zeros(len(numeric_cols)),
        var_coords[:,0], var_coords[:,1],
        angles='xy', scale_units='xy', scale=1,
        color="steelblue", width=0.005)

for i, var in enumerate(numeric_cols):
    ax.text(var_coords[i,0]*1.1, var_coords[i,1]*1.1, var,
            color='darkred', ha='center', va='center', fontsize=10, fontweight='bold')

ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax.axvline(0, color='gray', linewidth=0.8, linestyle='--')
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("Cercle des corrélations (variables)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle=':', linewidth=0.5)
plt.tight_layout()
plt.show()

# -------------------------------------------
# 8- Résumé des résultats numériques
# -------------------------------------------
print("=== RÉSUMÉ ===")
print(f"PC1 explique {explained[0]*100:.2f}% de la variance totale.")
print(f"PC2 explique {explained[1]*100:.2f}% de la variance totale.\n")

print("Charges (coordonnées des variables sur les axes) :")
loadings_df = pd.DataFrame(var_coords, index=numeric_cols, columns=['Coord_PC1', 'Coord_PC2'])
print(loadings_df.round(3), "\n")

print("Exemples des scores des individus :")
scores_df = pd.DataFrame(scores, index=df_numeric.index, columns=['PC1', 'PC2'])
print(scores_df.head().round(3))
