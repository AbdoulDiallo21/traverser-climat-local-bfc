# --- SWI ---
import numpy as np
import pandas as pd
import calendar
import plotly.graph_objects as go
from statsmodels.nonparametric.smoothers_lowess import lowess
import streamlit as st
import warnings

# --- 1. Prétraitement annuel SWI ---
@st.cache_data
def pretraiter_swi_annuel(df, an_debut, an_fin):
    resumyear = []
    df['date'] = pd.to_datetime(df['time'], errors='coerce')
    df['SWI_Q'] = pd.to_numeric(df['SWI_Q'], errors='coerce')
    df = df[df['date'].dt.year.between(an_debut, an_fin)]

    for idp, group in df.groupby("idPoint"):
        annual = group.set_index("date").resample("YE")['SWI_Q'].mean()
        resumyear.append(pd.DataFrame({
            'year': annual.index.year,
            'SWI_Q': annual.values,
            'idPoint': idp
        }))
    
    return pd.concat(resumyear, ignore_index=True)

# --- 2. Prétraitement mensuel SWI ---
@st.cache_data
def pretraiter_swi_mensuel(df, an_debut, an_fin):
    df = df.copy()
    df["date"] = pd.to_datetime(df["time"], errors="coerce")
    df["SWI_Q"] = pd.to_numeric(df["SWI_Q"], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df = df[(df["year"] >= an_debut) & (df["year"] <= an_fin)]

    resummonth = []
    for idP in df["idPoint"].unique():
        tmp = df[df["idPoint"] == idP].copy()
        tmp = tmp.dropna(subset=["SWI_Q"])
        tmp = tmp.set_index("date")
        if not tmp.empty:
            monthly = tmp["SWI_Q"].resample("ME").mean()
            resummonth.append(pd.DataFrame({
                "year": monthly.index.year,
                "month": monthly.index.month,
                "SWI_Q": monthly.values,
                "idPoint": idP
            }))
    return pd.concat(resummonth, ignore_index=True)

# --- 3. Affichage annuel SWI ---
def afficher_swi_annuel(resumyear, df, nom_commune, an_debut=1959, an_fin=2024, an_reference=True, periode_ref=(1959, 1987), resum_ref=None):
    tmp = df[df['Nom_commun'] == nom_commune][['idPoint', 'Ratio_Comm']]
    test = pd.merge(resumyear, tmp, on='idPoint')
    test['SWI_Qp'] = test['SWI_Q'] * test['Ratio_Comm']

    rtest = test.groupby('year').apply(
        lambda g: pd.Series({
            'SWI_Qmp': g['SWI_Qp'].sum() / g['Ratio_Comm'].sum()
        })
    ).reset_index()
    rtest['Nom_commun'] = nom_commune
    rtest['Year'] = rtest['year'].astype(int)

    df_periode = rtest[(rtest['Year'] >= an_debut) & (rtest['Year'] <= an_fin)].copy()
    moyenne_periode = df_periode['SWI_Qmp'].mean()

    moyenne_ref = None
    if an_reference and resum_ref is not None:
        test_ref = pd.merge(resum_ref, tmp, on='idPoint')
        test_ref['SWI_Qp'] = test_ref['SWI_Q'] * test_ref['Ratio_Comm']
        rtest_ref = test_ref.groupby('year').apply(
            lambda g: pd.Series({
                'SWI_Qmp': g['SWI_Qp'].sum() / g['Ratio_Comm'].sum()
            })
        ).reset_index()
        df_ref = rtest_ref[(rtest_ref['year'] >= periode_ref[0]) & (rtest_ref['year'] <= periode_ref[1])]
        moyenne_ref = df_ref['SWI_Qmp'].mean()

    loess_smoothed = lowess(df_periode['SWI_Qmp'], df_periode['Year'], frac=0.3)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_periode['Year'], y=df_periode['SWI_Qmp'], mode='lines+markers', name="SWI annuel"))
    fig.add_trace(go.Scatter(x=loess_smoothed[:, 0], y=loess_smoothed[:, 1], mode='lines', name='Lissage LOESS', line=dict(color='black')))

    if moyenne_periode:
        fig.add_hline(y=moyenne_periode, line_dash="dot", line_color="blue", annotation_text="Moyenne période choisie", annotation_position="top left")
    if moyenne_ref:
        fig.add_hline(y=moyenne_ref, line_dash="dash", line_color="red", annotation_text="Moyenne réf. (1959–1987)", annotation_position="top right")

    fig.update_layout(
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9',
        font=dict(family='Arial', size=14),
        title=f"Variation interannuelle de SWI – {nom_commune}<br>({an_debut}–{an_fin})",
        title_x=0.1,
        xaxis_title="Année",
        yaxis_title="SWI moyen",
        height=500,
        xaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        yaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        legend=dict(orientation="h", yanchor="bottom", y=-0.4, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig, use_container_width=True)

# --- 4. Affichage mensuel SWI ---
def afficher_swi_mensuel(df_month, df, nom_commune, an_debut, an_fin, df_month_ref=None):
    tmp = df[df["Nom_commun"] == nom_commune][["idPoint", "Ratio_Comm"]]
    test = pd.merge(df_month, tmp, on="idPoint")
    test["SWI_Qp"] = test["SWI_Q"] * test["Ratio_Comm"]

    sum_test = test.groupby("month")["SWI_Qp"].sum().reset_index(name="sum_SWI_Qp")
    sum_weights = test.groupby("month")["Ratio_Comm"].sum().reset_index(name="sum_ratio")
    rcycle = pd.merge(sum_test, sum_weights, on="month")
    rcycle["SWI_Qmp"] = rcycle["sum_SWI_Qp"] / rcycle["sum_ratio"]
    rcycle["Month"] = rcycle["month"].astype(int)
    rcycle["Month_name"] = pd.Categorical(
        [calendar.month_abbr[m] for m in rcycle["Month"]],
        categories=calendar.month_abbr[1:], ordered=True
    )
    rcycle.sort_values("Month", inplace=True)

    rcycle_ref = None
    if df_month_ref is not None:
        test_ref = pd.merge(df_month_ref, tmp, on="idPoint")
        test_ref["SWI_Qp"] = test_ref["SWI_Q"] * test_ref["Ratio_Comm"]

        sum_test_ref = test_ref.groupby("month")["SWI_Qp"].sum().reset_index(name="sum_SWI_Qp")
        sum_weights_ref = test_ref.groupby("month")["Ratio_Comm"].sum().reset_index(name="sum_ratio")

        rcycle_ref = pd.merge(sum_test_ref, sum_weights_ref, on="month")
        rcycle_ref["SWI_Qmp"] = rcycle_ref["sum_SWI_Qp"] / rcycle_ref["sum_ratio"]
        rcycle_ref["Month"] = rcycle_ref["month"].astype(int)
        rcycle_ref["Month_name"] = pd.Categorical(
            [calendar.month_abbr[m] for m in rcycle_ref["Month"]],
            categories=calendar.month_abbr[1:], ordered=True
        )
        rcycle_ref.sort_values("Month", inplace=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rcycle["Month_name"], y=rcycle["SWI_Qmp"], mode="lines+markers", name=f"{an_debut}–{an_fin}", line=dict(color="blue")))

    if rcycle_ref is not None:
        fig.add_trace(go.Scatter(x=rcycle_ref["Month_name"], y=rcycle_ref["SWI_Qmp"], mode="lines+markers", name="Référence 1959–1987", line=dict(color="red", dash="dash")))

    fig.add_hline(y=0.4, line_dash="dash", line_color="black", annotation_text="Seuil SWI = 0.4", annotation_position="top right")

    fig.update_layout(
        plot_bgcolor="#f9f9f9",
        paper_bgcolor="#f9f9f9",
        font=dict(family="Arial", size=14),
        title=f"Cycle annuel moyen de SWI – {nom_commune}<br>({an_debut}–{an_fin})",
        xaxis_title="Mois",
        yaxis_title="SWI moyen",
        title_x=0.1,
        height=500,
        margin=dict(t=80, b=40, l=30, r=30),
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig, use_container_width=True)

# --- 5. Titre ---
def afficher_titre_swi(nom_commune):
    st.markdown(
        f"""
        <div style='background-color:#e3f2fd; padding: 16px; border-left: 6px solid #2196F3;
                    border-radius: 8px; margin-bottom: 0.5em; box-shadow: 0 2px 6px rgba(0,0,0,0.05);'>
            <h3 style='text-align:center; color:#1b2b40; margin: 0; font-family: Arial, sans-serif;'>
                🌱 Indice d'humidité du sol (SWI) – {nom_commune}
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="background-color: #f5f5f5; padding: 20px; border-left: 6px solid #9e9e9e;
                    border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.05); margin-top: 1em; margin-bottom: 1em; font-size: 0.95em;">
            <p>L’indice d’humidité du sol (SWI) reflète la quantité d’eau relative disponible dans le sol. Un SWI élevé (proche de 1) traduit une forte humidité, voire une saturation, tandis qu’un SWI bas (proche de 0 ou négatif) indique un stress hydrique du sol.</p>
            <p>Le seuil de 0.4 est un repère critique pour le fonctionnement des cultures.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
