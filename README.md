#  Projet IA : Prédiction du prix de biens immobiliers à Paris

Ce projet a pour objectif de développer un modèle de machine learning capable de prédire le prix de vente de biens immobiliers à Paris, à partir de caractéristiques comme la surface, l’arrondissement, la localisation GPS, le nombre de pièces, etc. Une application simple servira de démonstration

---

##  Objectifs

- Développer un modèle prédictif performant.
- Intégrer ce modèle dans une application simple pour illustrer un cas d’usage.

---
## Dataset

Le dataset provenant de data.gouv [data.gouv](https://explore.data.gouv.fr/fr/immobilier?onglet=carte&filtre=tous&lat=48.87186&lng=2.33964&zoom=13.73&code&level=section) est télécharchable au format csv. Nous nous sommes interessés dans ce projet aux données de Paris, mais les notebooks fonctionneront également avec les données d'autres départements. Toutefois, il faudrais réadapter en prenant en compte le type (Appartement ou Maison) qui n'est pas présent dans notre modèle étant donné du faible nombre de maison dans le dataset.


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
  Contient les fichiers bruts `dvf.csv` et nettoyés `data_cleaned.csv` au format CSV.

- **`asset/`**  
  Contient les fichiers nécessaires pour utiliser certains outils. `arrondissement.geojson` permet d'avoir les coordonnées de chacun des arrondissements de Paris

- **`experiments/`**  
  Regroupe les expérimentations réalisées (modèles, encodage, fine-tuning) pour identifier le modèle le plus performant.
  - `analyse-arrondissement.ipynb` premier modèle de prédiction en prédisant par la moyenne par arrondissements
  - `encodage.ipynb` comparasion entre un encodage OneHot et l'encodage entier déjà disponible dans notre dataset
  - `models_testing.ipynb` comparaison entre différents modèles
  - `fine-tuning.ipynb` fine-tuning des meilleurs modèles séléctionnés

- **`notebooks/`**  
  Contient les notebooks finaux :
  - `data_wrangling.ipynb` : analyse et nettoyage des données
  - `training.ipynb` : encodage, entraînement et sauvegarde du meilleur modèle pour l'app


  ## App

  ### Pre-requis

  Installer un environnement virtuel avec les bibliothèques nécessaires
  ```bash 
  pip install -r requirements.txt
  ```

  Télécharger les modèles `model.pkl` et `encoder.pkl`.
  Pour cela executer le notebook `encodage.ipynb`. Vérifier qu'ils se sont bien chargés dans le dossier models

  ### Pour lancer l'app

  ```bash 
  streamlit run demo-app.py
  ```

  ![Demo APP](asset/app.png)
  