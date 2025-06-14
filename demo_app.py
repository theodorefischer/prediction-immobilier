import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Charger le modèle, l'encodeur et les données
@st.cache_resource
def load_resources():
    model = joblib.load("models/model.pkl")
    encoder = joblib.load("models/encoder.pkl")
    df = pd.read_csv("data/data_cleaned.csv")
    return model, encoder, df

model, encoder, df_data = load_resources()

# Fonction pour approximer latitude, longitude et arrondissement en fonction des données de notre dataframe
def approx_coords_arrondissement(df, numero, rue):
    rue = rue.lower().strip()
    df_rue = df[df["adresse_nom_voie"].str.lower().str.strip() == rue]
    if df_rue.empty:
        return None, None, None

    nums_dispos = df_rue["adresse_numero"].dropna().astype(int).sort_values().unique()

    if numero in nums_dispos:
        match = df_rue[df_rue["adresse_numero"] == numero].iloc[0]
        return match["latitude"], match["longitude"], match["arrondissement"]
    else:
        plus_proches = [n for n in nums_dispos if abs(n - numero) <= 10]
        if len(plus_proches) >= 1:
            df_voisins = df_rue[df_rue["adresse_numero"].isin(plus_proches)]
            lat = df_voisins["latitude"].mean()
            lon = df_voisins["longitude"].mean()
            arr = df_voisins["arrondissement"].mode().iloc[0]
            return lat, lon, arr

    return None, None, None

st.title("Estimation du prix d'un appartement à Paris")

# Entrée utilisateur
numero = st.number_input("Numéro dans la rue", min_value=1, max_value=300, value=27)
rue = st.text_input("Nom de la rue", value="rue de Rivoli")
surface = st.number_input("Surface en m²", min_value=5.0, max_value=300.0, value=50.0)
n_pieces = st.number_input("Nombre de pièces", min_value=1, max_value=10, value=2)
annee = st.number_input("Année de la mutation", min_value=2000, max_value=2100, value=2024)

if st.button("Estimer le prix"):
    latitude, longitude, arrdt = approx_coords_arrondissement(df_data, numero, rue)

    if latitude is None:
        st.error("Impossible de trouver cette adresse dans le dataset.")
    else:
        # Nettoyage de la rue pour correspondre au prétraitement
        rue_clean = rue.lower().strip()

        try:
            # Encodage de la rue (peut échouer si catégorie inconnue et encoder mal entraîné)
            rue_encoded = encoder.transform(pd.DataFrame([[rue_clean]], columns=["adresse_nom_voie"]))
        except ValueError:
            st.warning("Nom de rue inconnu dans l'encodeur, encodage remplacé par des zéros.")
            ####### A modifier mais en gros n'utilise pas la rue pour la predicition si il ne la trouve pas 
            rue_encoded = [[0] * len(encoder.get_feature_names_out(['adresse_nom_voie']))]

        encoded_rue_df = pd.DataFrame(rue_encoded, columns=encoder.get_feature_names_out(['adresse_nom_voie']))

        input_df = pd.DataFrame({
            "lot1_surface_carrez": [surface],
            "nombre_pieces_principales": [n_pieces],
            "longitude": [longitude],
            "latitude": [latitude],
            "année": [annee],
            "arrondissement": [arrdt]
        })

        input_final = pd.concat([input_df, encoded_rue_df], axis=1)

        # Ajout des colonnes manquantes
        for col in model.feature_names_in_:
            if col not in input_final.columns:
                input_final[col] = 0

        input_final = input_final[model.feature_names_in_]

        prix_m2 = model.predict(input_final)[0]
        prix_total = prix_m2 * surface

        st.success(f"Prix estimé : {prix_total:,.0f} €")
        st.write(f"(soit environ {prix_m2:,.0f} €/m²)")

        # Affichage carte
        df_point = pd.DataFrame({
            "latitude": [latitude],
            "longitude": [longitude],
            "prix_au_m2": [prix_m2],
            "label": [f"{int(prix_m2):,} €/m²"]
        })

        fig = px.scatter_mapbox(
            df_point,
            lat="latitude",
            lon="longitude",
            size=[50], 
            color="prix_au_m2",
            hover_name="label",
            color_continuous_scale="Reds",
            range_color=(0, 30000),
            height=600,
            width=600,
            zoom=14
        )
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig)