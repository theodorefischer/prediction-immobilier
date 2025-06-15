### The goal of this file is to create a function to clean the name of the streets of Paris. 
### In fact it is hard to clean the mistakes in the names e.g. saint-sulpice is the same as st-sulpice, etc...

import pandas as pd
from difflib import SequenceMatcher


df = pd.read_csv("data/dvf.csv")
df = df[df['adresse_nom_voie'].apply(lambda x: isinstance(x, str))]
list_of_steets = df["adresse_nom_voie"].unique()
print(len(list_of_steets))

def clean_paris_streets(df : pd.DataFrame) -> list:
    """
    Prends en entrée un dataframe avec une liste de rue et retourne un dataframe avec le noms des rues nettoyées

    Args:
        df (pd.DataFrame): Le DataFrame contenant les noms des rues.

    Returns:
         df (pd.DataFrame): Le DataFrame contenant les noms des rues ici nettoyés.
        
    """
    list_of_steets = df["adresse_nom_voie"].unique()
    list_of_streets_cleaned = [list_of_steets[0]]
    for x in list_of_steets:
        if all(SequenceMatcher(None, x, y).ratio() < 0.85 for y in list_of_streets_cleaned):
            list_of_streets_cleaned.append(x)
    return list_of_streets_cleaned



def clean_paris_streets2(df: pd.DataFrame) -> tuple[list, list[tuple[str, str]]]:
    """
    Nettoie les noms de rues similaires (avec fautes ou variantes),
    et affiche en direct les correspondances supprimées.

    Args:
        df (pd.DataFrame): DataFrame avec la colonne 'adresse_nom_voie'.

    Returns:
        - Liste des noms de rues nettoyés
        - Liste des paires (supprimé, conservé)
    """
    list_of_streets = df["adresse_nom_voie"].dropna().astype(str).unique()
    list_of_streets_cleaned = []
    replacements = []

    for x in list_of_streets:
        match_found = False
        for y in list_of_streets_cleaned:
            ratio = SequenceMatcher(None, x.lower().strip(), y.lower().strip()).ratio()
            if ratio >= 0.85:
                print(f"Fusion détectée : '{x}' → '{y}' (similitude : {ratio:.2f})")
                replacements.append((x, y))
                match_found = True
                break
        if not match_found:
            list_of_streets_cleaned.append(x)

    return list_of_streets_cleaned, replacements

print(clean_paris_streets2(df=df))

#print(len(clean_paris_streets(df=df)))