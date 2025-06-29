## Code principal ##
# tclimat_app.py

# --- Importation des packages ---
import numpy as np
import pandas as pd
import io
import os
import requests
import time
import calendar
import matplotlib as plt
import seaborn as sns
import plotly.express as px
from sklearn.linear_model import LinearRegression
import altair
import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import base64

from PIL import Image
# --- ⚠️ Configuration Streamlit (à mettre tout en haut) ---
st.set_page_config(page_title="Visualisation Climat", layout="wide", initial_sidebar_state="expanded")

# --- Import modules personnalisés ---
from etp import *
from petp import *
from precip import *
from swi import *
from temperature import *

# --- Habillage titre ---
HTML_BANNER = """
    <div style="background-color:#00a3a6;padding:6px;border-radius:6px">
    <h1 style="color:white;text-align:center;">Traverser</h1>
    </div>
    """

# --- Affichage du logo et du titre principal ---
def afficher_entete():
    file_path = "LOGO-vignette-turquoise.png"
    with open(file_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <div style="padding: 8px 0; border-radius: 6px; text-align: center;">
    <img src="data:image/png;base64,{encoded_image}" width="250"/>
    <h1 style="margin-top: 0.2em; font-weight: 700; font-size: 2.2em; color: #2c2c2c;"> Le climat 🌦️ 🌡️ ☀️ de ma commune 📍 entre 1959 et 2024</h1>
    <h3 style="margin-top: -0.5em; font-weight: normal; color: #444;">en Bourgogne Franche-Comté</h3>
    <p style='color:#4d4d4d; font-size:16px; margin-top: 0.8em;'>
        🧑‍🏫 <strong>Abdoul Diallo</strong> 🧑‍🔬 <strong>Wabby-Jha Charite</strong>
    </p> 
    </div>

    <div style="background-color: #e8f5e9; padding: 20px; border-left: 6px solid #43a047; border-radius: 8px;
                font-family: Arial, sans-serif; text-align: justify; box-shadow: 0 2px 6px rgba(0,0,0,0.08); margin-top: 20px;">
    <p style="margin: 0; font-size: 15px; color: #333;">
        Les communes présentes dans cette application correspondent à celles où des éleveurs et éleveuses de bovins viande et lait ont participé aux entretiens.
        Le développement de cette application a été réalisé par des ingénieurs en collaboration étroite avec des chercheurs et chercheuses du CRC et du CESAER.
        Les données utilisées sont celles de <a href="https://meteofrance.com" target="_blank" style="color:#1a73e8; text-decoration: none;">Météo-France</a> 
        et les traitements ont été réalisés par le CRC et le CESAER.<br><br>
        L’application permet de consulter cinq indicateurs climatiques calculés à l’échelle communale sur la période 1959–2024 :
        <ul style="margin-left: 1em; padding-left: 1em;">
            <li><strong>Évapotranspiration potentielle (ETP)</strong></li>
            <li><strong>Bilan hydrique climatique (P - ETP)</strong></li>
            <li><strong>Précipitations</strong></li>
            <li><strong>Indice d’humidité des sols (SWI)</strong></li>
            <li><strong>Température moyenne (°C)</strong></li>
        </ul>

    Il est possible de définir une période d’analyse personnalisée, d’au moins cinq ans, et de comparer les résultats à la période de référence (1959–1987).
    <br>
    <strong>⏳ Certains calculs peuvent prendre du temps et il est recommandé de patienter jusqu’à leur affichage complet.</strong>
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

def afficher_footer():
    st.markdown("---")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.image("logo-cesaer.png", width=150)#, use_container_width=True
    with col2:
        st.image("logo_iad.png", width=150)
    with col3:
        st.image("inrae.png", width=150)
    with col4:
        st.image("logo_CRC_transparent.png", width=150)
    with col5:
        st.image("logo-UBE-footer.png", width=150)
    with col6:
        st.image("logo-cnrs.png", width=120)

# --- Chargement du fichier fusionné depuis Google Drive ---
@st.cache_data()
def charger_donnees():
    file_id = "1I6aV6USh7SCVe5kqHyuyDOB2ot3Zu1I5"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    fichier_local = "data/Donnees_Climat_Merge.parquet"

    if not os.path.exists(fichier_local):
        response = requests.get(url)
        response.raise_for_status()
        with open(fichier_local, "wb") as f:
            f.write(response.content)

    return pd.read_parquet(fichier_local)

@st.cache_data()
def filtrer_commune(df, commune):
    return df[df["Nom_commun"] == commune].copy()

# --- Application principale ---
def main():
    #st.set_page_config(page_title="Visualisation Climat", layout="wide", initial_sidebar_state="expanded")
    afficher_entete()

    with st.spinner("⏳ Un petit instant, le calcul est en cours... 😊"):
        df = charger_donnees()

        with st.sidebar:
            st.markdown(
            """
            <div style="background-color:#FFF3E0; padding: 10px 15px; border-left: 4px solid #FB8C00; border-radius: 8px; margin-bottom: 1em;">
                <h4 style="margin:0; color:#FB8C00;">📌 Paramètres de visualisation</h4>
                <p style="margin:0; font-size: 0.9em; color:#333;">Choisissez les paramètres pour visualiser le climat passé</p>
            </div>
            """,
            unsafe_allow_html=True
        )
            st.markdown("---")
            st.markdown("""
                <div style="background-color: #e6f4ea; padding: 15px; border-left: 5px solid #34a853; border-radius: 8px;">
                    <h4 style="color: #0b8043; font-family: Arial, sans-serif;">
                        🔍 Sélectionnez une commune
                    </h4>
                </div>
            """, unsafe_allow_html=True)
                
            communes = sorted(df['Nom_commun'].dropna().unique())
            selected_commune = st.selectbox("Commune :", communes, index=0)

            st.markdown(
                """
                <div style="background-color:#f0f8ff; padding: 10px 15px; border-left: 4px solid #1E88E5; border-radius: 8px; margin-bottom: 1em;">
                    <h4 style="margin:0; color:#1E88E5;">📊 Sélectionnez un indicateur</h4>
                </div>
                """,
                unsafe_allow_html=True
              )
            
            indicateurs_disponibles = {
                "Évapotranspiration potentielle": "ETP_Q",
                "Bilan Hydrique climatique": "P_ETP",
                "Précipitations": "PRECIP",
                "Indice d'humidité du sol": "SWI",
                "Température (°C)": "TEMP",
            }
            selected_label = st.selectbox("Indicateur", list(indicateurs_disponibles.keys()))
            selected_indicateur = indicateurs_disponibles[selected_label]
            
            st.markdown("""
                <div style="background-color: #e6f4ea; padding: 15px; border-left: 5px solid #34a853; border-radius: 8px;">
                    <h4 style="color: #0b8043; font-family: Arial, sans-serif;">
                        📆 Choisissez une période
                    </h4>
                </div>
                """, unsafe_allow_html=True)
            
    
            an_min, an_max = int(df['Year'].min()), int(df['Year'].max())
            periode = st.slider("Période", min_value=an_min, max_value=an_max, value=(an_min, an_max), step=1)

            if periode[1] - periode[0] < 3:
                st.error("⛔ Veuillez sélectionner une période d'au moins 3 ans.")
                st.stop()

            afficher_reference = st.checkbox("📌 Période de référence (1959–1987)", value=True)

            st.markdown("<hr style='margin:1em 0;'>", unsafe_allow_html=True)

            # --- Lien discret en bas
            st.page_link("pages/Questions_Reponses.py", label="💬 Questions Réponses")

        df_commune = df[df['Nom_commun'] == selected_commune]

        if selected_indicateur == "ETP_Q":
            resumyear = pretraiter_etp_annuelle(df)
            df_monthly = pretraiter_etp_mensuel(df, an_debut=periode[0], an_fin=periode[1])
            rcycle = calculer_etp_mensuel_commune(df_monthly, df, selected_commune)

            rcycle_ref = None
            if afficher_reference:
                df_ref_mensuel = pretraiter_etp_mensuel(df, an_debut=1959, an_fin=1987)
                rcycle_ref = calculer_etp_mensuel_commune(df_ref_mensuel, df, selected_commune)

            afficher_titre_etp(selected_commune)
            col1, col2 = st.columns(2)
            with col1:
                afficher_etp_mensuel(rcycle, selected_commune,an_debut=periode[0], an_fin=periode[1],rcycle_ref=rcycle_ref)
                st.markdown("---")
                # ➕ Appel du simulateur
                afficher_simulateur_etp()
            with col2:
                afficher_etp_annuelle(resumyear, df, selected_commune,an_debut=periode[0], an_fin=periode[1],an_reference=afficher_reference,periode_ref=(1959, 1987))
                st.markdown("""
                <small>📈 <strong>Lissage LOESS ou Tendance générale</strong> : cette courbe noire permet de visualiser l’évolution moyenne de l’ETP au fil des années, sans les pics et creux annuels.</small>
                """, unsafe_allow_html=True)
            
        # ### PETP
        elif selected_indicateur == "P_ETP":
            resumyear_bilan = pretraiter_bilan_annuelle(df, an_debut=periode[0], an_fin=periode[1])
            resummonth_bilan = pretraiter_bilan_mensuel(df, an_debut=periode[0], an_fin=periode[1])

            resum_ref_bilan = None
            resummonth_ref_bilan = None
            if afficher_reference:
                resum_ref_bilan = pretraiter_bilan_annuelle(df, an_debut=1959, an_fin=1987)
                resummonth_ref_bilan = pretraiter_bilan_mensuel(df, an_debut=1959, an_fin=1987)

            afficher_titre_petp(selected_commune)
            col1, col2 = st.columns(2)
            with col1:
                afficher_bilan_mensuel(resummonth_bilan, df_ratio=df, nom_commune=selected_commune, an_debut=periode[0], an_fin=periode[1], df_month_ref=resummonth_ref_bilan)
            with col2:
                afficher_bilan_annuelle(resumyear_bilan, df, nom_commune=selected_commune,an_debut=periode[0], an_fin=periode[1],an_reference=afficher_reference, periode_ref=(1959, 1987),resum_ref=resum_ref_bilan)
                st.markdown("""
                <small>📈 <strong>Lissage LOESS ou Tendance générale</strong> : cette courbe noire permet de visualiser l’évolution moyenne de l’ETP au fil des années, sans les pics et creux annuels.</small>
                """, unsafe_allow_html=True)
        
        # ### PRECIP
        elif selected_indicateur == "PRECIP":
            resumyear = pretraiter_precip_annuelle(df, an_debut=periode[0], an_fin=periode[1])
            df_monthly = pretraiter_precip_mensuel(df, an_debut=periode[0], an_fin=periode[1])

            df_ref_monthly = None
            resum_ref = None
            if afficher_reference:
                df_ref_monthly = pretraiter_precip_mensuel(df, an_debut=1959, an_fin=1987)
                resum_ref = pretraiter_precip_annuelle(df, an_debut=1959, an_fin=1987)

            afficher_titre_precip(selected_commune)
            col1, col2 = st.columns(2)
            with col1:
                afficher_precip_mensuel(df_monthly,df,nom_commune=selected_commune,an_debut=periode[0],an_fin=periode[1],df_month_ref=df_ref_monthly)
            with col2:
                afficher_precip_annuelle(resumyear,df,nom_commune=selected_commune,an_debut=periode[0],an_fin=periode[1],an_reference=afficher_reference,periode_ref=(1959, 1987),resum_ref=resum_ref)
                st.markdown("""
                <small>📈 <strong>Lissage LOESS ou Tendance générale</strong> : cette courbe noire permet de visualiser l’évolution moyenne de l’ETP au fil des années, sans les pics et creux annuels.</small>
                """, unsafe_allow_html=True)
        
        # ### SWI
        elif selected_indicateur == "SWI":
            # Prétraitements principal
            resum_swi = pretraiter_swi_annuel(df, an_debut=periode[0], an_fin=periode[1])
            df_swi_mensuel = pretraiter_swi_mensuel(df, an_debut=periode[0], an_fin=periode[1])

            # Initialisation des références
            df_ref_mensuel_swi = None
            resum_ref_swi = None

            if afficher_reference:
                df_ref_mensuel_swi = pretraiter_swi_mensuel(df, an_debut=1959, an_fin=1987)
                resum_ref_swi = pretraiter_swi_annuel(df, an_debut=1959, an_fin=1987)
            afficher_titre_swi(selected_commune)

            col1, col2 = st.columns(2)
            with col1:
                afficher_swi_mensuel(df_month=df_swi_mensuel,df_ratio=df,nom_commune=selected_commune,an_debut=periode[0],an_fin=periode[1],df_month_ref=df_ref_mensuel_swi)
            with col2:
                afficher_swi_annuel(resumyear=resum_swi,df=df,nom_commune=selected_commune,an_debut=periode[0],an_fin=periode[1],periode_ref=(1959, 1987),resum_ref=resum_ref_swi)
                st.markdown("""
                <small>📈 <strong>Lissage LOESS ou Tendance générale</strong> : cette courbe noire permet de visualiser l’évolution moyenne de l’ETP au fil des années, sans les pics et creux annuels.</small>
                """, unsafe_allow_html=True)

        # ### TEMP  
        elif selected_indicateur == "TEMP":
            resumyear = pretraiter_temp_annuelle(df, an_debut=periode[0], an_fin=periode[1])
            df_monthly = pretraiter_temp_mensuel(df, an_debut=periode[0], an_fin=periode[1])
            rcycle = df_monthly 

            rcycle_ref = None
            resum_ref = None
            if afficher_reference:
                resum_ref = pretraiter_temp_annuelle(df, an_debut=1959, an_fin=1987)
                rcycle_ref = pretraiter_temp_mensuel(df, an_debut=1959, an_fin=1987)

            afficher_titre_temp(selected_commune)
            col1, col2 = st.columns(2)
            with col1:
                afficher_temp_mensuel(rcycle, df, selected_commune, an_debut=periode[0], an_fin=periode[1], df_month_ref=rcycle_ref)
            with col2:
                afficher_temp_annuelle(resumyear, df, selected_commune,an_debut=periode[0], an_fin=periode[1],an_reference=afficher_reference,periode_ref=(1959, 1987),resum_ref=resum_ref)
                st.markdown("""
                <small>📈 <strong>Lissage LOESS ou Tendance générale</strong> : cette courbe noire permet de visualiser l’évolution moyenne de l’ETP au fil des années, sans les pics et creux annuels.</small>
                """, unsafe_allow_html=True)

        # Appel du footer à la fin de la page
        afficher_footer()

# --- Exécution ---
if __name__ == '__main__':
    main()



