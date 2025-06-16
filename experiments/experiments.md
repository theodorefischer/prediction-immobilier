# Résultats 

## Préliminaire (Data-Wrangling)

- Ajouter le filtre sur les lots
- Voir si possible de croiser avec des données types écoles/métro/etc... pour augmenter la pertinence des modèles 



## Partie 1 : Baseline et baseline par arrondissement :

- Ajouter une prédiction baseline a analys-arrondissement pour comparer les modèles

## Partie 2 : Encodage :

- OneHot pour les rues ("adresse_nom_voie") meilleur que encodage entier ("code_nom_voie") déjà présent mais bien plus couteux
- OneHot pour les arrondissement bien meilleur que encodage entier pour les arrondissement (même si logique de proximité "circulaire", OneHot bien plus pertinent)

---

- To test : Normalisation (notamment pour KNN ou les resultats ne sont pas pertinents du tout pour l'instant)
- OneHot uniquement sur arrondissement test de la diff en perf (theoriquement moins bien) et en temps de clacul

---

## Partie 3 et 4:

#### TO DO :

- Tester tout les modèles avec OneHot uniquement sur arr/ uniquement sur adresse/ et sur les deux
- idem pour normaliser
- améliorer le fine-tuning


