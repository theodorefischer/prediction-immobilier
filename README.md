#  Projet IA : Prédiction du prix de biens immobiliers à Paris

Ce projet a pour objectif de développer un modèle de machine learning capable de prédire le prix de vente de biens immobiliers à Paris, à partir de caractéristiques comme la surface, l’arrondissement, la localisation GPS, le nombre de pièces, etc. Une application simple servira de démonstration
---

##  Objectifs

- Comprendre les tendances du marché immobilier parisien.
- Développer un modèle prédictif performant.
- Intégrer ce modèle dans une application simple pour illustrer un cas d’usage.

---

##  Plan du projet

### 1. Exploration, nettoyage et préparation des données (`notebooks/data_wrangling.ipynb`)
- Traitement des valeurs manquantes.
- Normalisation ou standardisation des variables numériques.
- Encodage des variables catégorielles (arrondissement, type de bien...).
- Feature engineering (densité locale, proximité métro, etc.).
- Séparation train/test.

### 2. Modélisation et prédiction (`experiments`)
- Différents modèles testés : modèles linéaire, arbre de décision et forêt aléatoire, "boosting models" , KNN, MLP
- Comparaison des performances (MAE, RMSE, R²).
- Validation croisée.
- Optimisation des hyperparamètres.
- Optimisation du meilleur modèle (`notebooks/training.ipynb`).

### 3. Déploiement et démonstration (`demo_app.py`)
- Création d'une interface simple (avec Streamlit).
- Formulaire pour renseigner les caractéristiques du bien à prédire.
- Affichage de la prédiction du prix.


## Structure du Répertoire

- **`data/`**  
  Contient les fichiers bruts et nettoyés au format CSV.

- **`experiments/`**  
  Regroupe les expérimentations réalisées (modèles, encodage, fine-tuning) pour identifier le modèle le plus performant.

- **`notebooks/`**  
  Contient les notebooks finaux :
  - `data_wrangling.ipynb` : analyse et nettoyage des données
  - `training.ipynb` : encodage et entraînement du meilleur modèle