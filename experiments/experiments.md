# Résultats 

## Préliminaire (Data-Wrangling)

- Ajouter le filtre sur les lots
- Voir si possible de croiser avec des données types écoles/métro/etc... pour augmenter la pertinence des modèles 



## Partie 1 : Baseline et baseline par arrondissement :

- Ajouter une prédiction baseline a analys-arrondissement pour comparer les modèles
- Comparer avec les données rééels

## Partie 2 : Encodage :

- OneHot pour les rues ("adresse_nom_voie") meilleur que encodage entier ("code_nom_voie") déjà présent mais bien plus couteux
- OneHot pour les arrondissement bien meilleur que encodage entier pour les arrondissement (même si logique de proximité "circulaire", OneHot bien plus pertinent)

---

- To test : Normalisation (notamment pour KNN ou les resultats ne sont pas pertinents du tout pour l'instant)
- results : normalisation --> meilleur pour KNN pas pour DecisionTree

- OneHot uniquement sur arrondissement test de la diff en perf (theoriquement moins bien) et en temps de clacul

---

## Partie 3 et 4:

#### TO DO :

- Tester tout les modèles avec OneHot uniquement sur arr/ uniquement sur adresse/ et sur les deux
- idem pour normaliser
- améliorer le fine-tuning
- entrainer un modèle linéaire avec la distance au centre


## En plus pour affiner le modèle

- Voir si il est possible de forcer une évolution du prix avec la date parcque pour l'instant la date n'a aucune importance

## Pour simplifier le projet 

créér des fichier pythons dans outils plutot que des notebooks

## cleaning.py

À priori très peu d'erreur de frappe dans les noms des rues contrairement à ce qu'on pensait donc très peu de rue sont doublées (st à la place de saint manque de tirets, etc...)