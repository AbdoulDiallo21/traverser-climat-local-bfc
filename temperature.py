# --- TEMPERATURE ---
# temperature.py

import numpy as np
import pandas as pd
import calendar
import plotly.graph_objects as go
from statsmodels.nonparametric.smoothers_lowess import lowess
import streamlit as st

# --- Prétraitement annuel TEMP ---
@st.cache_data
def pretraiter_temp_annuelle(df, an_debut, an_fin):
    resumyear = []
    df['date'] = pd.to_datetime(df['time'], errors='coerce')
    df['T_Q'] = pd.to_numeric(df['T_Q'], errors='coerce')
    df = df[df['date'].dt.year.between(an_debut, an_fin)]

    for idp, group in df.groupby("idPoint"):
        annual = group.set_index("date").resample("YE")["T_Q"].mean()
        df_tmp = pd.DataFrame({
            'year': annual.index.year,
            'T_Q': annual.values,
            'idPoint': idp
        })
        resumyear.append(df_tmp)

    return pd.concat(resumyear, ignore_index=True)

# --- Prétraitement mensuel TEMP ---
@st.cache_data
def pretraiter_temp_mensuel(df, an_debut, an_fin):
    resummonth = []
    df["date"] = pd.to_datetime(df["time"], errors="coerce")
    df["T_Q"] = pd.to_numeric(df["T_Q"], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    df = df[(df["year"] >= an_debut) & (df["year"] <= an_fin)].copy()

    for idP in df["idPoint"].unique():
        tmp = df[df["idPoint"] == idP].copy()
        if tmp["T_Q"].isna().sum() > 0:
            st.warning(f"Valeurs NA détectées pour idPoint = {idP}")

        tmp = tmp.dropna(subset=["T_Q"])
        tmp = tmp.set_index("date")

        if not tmp.empty:
            monthly_mean = tmp["T_Q"].resample("ME").mean()
            df_month = pd.DataFrame({
                "year": monthly_mean.index.year,
                "month": monthly_mean.index.month,
                "T_Q": monthly_mean.values,
                "idPoint": idP
            })
            resummonth.append(df_month)

    return pd.concat(resummonth, ignore_index=True)

# --- Affichage annuel TEMP ---
def afficher_temp_annuelle(resumyear, df, nom_commune, an_debut=1959, an_fin=2024, an_reference=True, periode_ref=(1959, 1987), resum_ref=None):
    tmpcomm = df[df['Nom_commun'] == nom_commune][['idPoint', 'Ratio_Comm']]
    test = pd.merge(resumyear, tmpcomm, on='idPoint')
    test['T_Qp'] = test['T_Q'] * test['Ratio_Comm']
    test['year'] = test['year'].astype(int)

    rtest = (
        test.groupby(['year'])
        .apply(lambda df: pd.Series({
            'T_Qmp': (df['T_Qp'].sum() / df['Ratio_Comm'].sum()) if df['Ratio_Comm'].sum() != 0 else float('nan')
        }))
        .reset_index()
    )

    rtest['Nom_commun'] = nom_commune
    rtest['Year'] = rtest['year'].astype(int)
    df_periode = rtest[(rtest['Year'] >= an_debut) & (rtest['Year'] <= an_fin)].copy()
    moyenne_periode = df_periode['T_Qmp'].mean()

    if an_reference and resum_ref is not None:
        test_ref = pd.merge(resum_ref, tmpcomm, on='idPoint')
        test_ref['T_Qp'] = test_ref['T_Q'] * test_ref['Ratio_Comm']
        test_ref['year'] = test_ref['year'].astype(int)

        rtest_ref = (
            test_ref.groupby(['year'])
            .apply(lambda df: pd.Series({
                'T_Qmp': (df['T_Qp'].sum() / df['Ratio_Comm'].sum()) if df['Ratio_Comm'].sum() != 0 else float('nan')
            }))
            .reset_index()
        )
        df_ref = rtest_ref[(rtest_ref['year'] >= periode_ref[0]) & (rtest_ref['year'] <= periode_ref[1])]
        moyenne_ref = df_ref['T_Qmp'].mean()
    else:
        moyenne_ref = None

    loess_smoothed = lowess(df_periode['T_Qmp'], df_periode['Year'], frac=0.3)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_periode['Year'], y=df_periode['T_Qmp'], mode='lines+markers', name="Température annuelle"))
    fig.add_trace(go.Scatter(x=loess_smoothed[:, 0], y=loess_smoothed[:, 1], mode='lines', name='Lissage LOESS', line=dict(color='black')))

    if moyenne_periode:
        fig.add_hline(y=moyenne_periode, line_dash="dot", line_color="blue", annotation_text="Moyenne période choisie", annotation_position="top left")
    if moyenne_ref:
        fig.add_hline(y=moyenne_ref, line_dash="dash", line_color="red", annotation_text="Moyenne réf. (1959–1987)", annotation_position="top right")

    fig.update_layout(
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9',
        font=dict(family='Arial', size=14),
        title=f"Variabilité interannuelle de la température moyenne<br>({an_debut}–{an_fin})",
        xaxis_title="Année",
        yaxis_title="Température moyenne (°C)",
        title_x=0.1,
        height=500,
        xaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        yaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
    )

    st.plotly_chart(fig, use_container_width=True)

# --- Affichage mensuel TEMP ---
def afficher_temp_mensuel(df_month, df_ratio, nom_commune, an_debut, an_fin, df_month_ref=None):
    month_abb = list(calendar.month_abbr)[1:]
    tmpcomm = df_ratio[df_ratio["Nom_commun"] == nom_commune][["idPoint", "Ratio_Comm"]]
    test = pd.merge(df_month, tmpcomm, on="idPoint")
    test["T_Qp"] = test["T_Q"] * test["Ratio_Comm"]

    sum_test = test.groupby("month")["T_Qp"].sum().reset_index(name="sum_T_Qp")
    sum_weights = test.groupby("month")["Ratio_Comm"].sum().reset_index(name="sum_ratio")

    rcycle = pd.merge(sum_test, sum_weights, on="month")
    rcycle["T_Qmp"] = rcycle["sum_T_Qp"] / rcycle["sum_ratio"]
    rcycle["Month"] = rcycle["month"].astype(int)
    rcycle["Month_name"] = pd.Categorical(
        [calendar.month_abbr[m] for m in rcycle["Month"]],
        categories=month_abb,
        ordered=True
    )
    rcycle.sort_values("Month", inplace=True)

    if df_month_ref is not None:
        test_ref = pd.merge(df_month_ref, tmpcomm, on="idPoint")
        test_ref["T_Qp"] = test_ref["T_Q"] * test_ref["Ratio_Comm"]

        sum_test_ref = test_ref.groupby("month")["T_Qp"].sum().reset_index(name="sum_T_Qp")
        sum_weights_ref = test_ref.groupby("month")["Ratio_Comm"].sum().reset_index(name="sum_ratio")

        rcycle_ref = pd.merge(sum_test_ref, sum_weights_ref, on="month")
        rcycle_ref["T_Qmp"] = rcycle_ref["sum_T_Qp"] / rcycle_ref["sum_ratio"]
        rcycle_ref["Month"] = rcycle_ref["month"].astype(int)
        rcycle_ref["Month_name"] = pd.Categorical(
            [calendar.month_abbr[m] for m in rcycle_ref["Month"]],
            categories=month_abb,
            ordered=True
        )
        rcycle_ref.sort_values("Month", inplace=True)
    else:
        rcycle_ref = None

    # Affichage graphique
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=rcycle["Month_name"],
        y=rcycle["T_Qmp"],
        mode="lines+markers",
        name=f"{an_debut}–{an_fin}",
        line=dict(color="blue")
    ))

    if rcycle_ref is not None:
        fig.add_trace(go.Scatter(
            x=rcycle_ref["Month_name"],
            y=rcycle_ref["T_Qmp"],
            mode="lines+markers",
            name="Référence 1959–1987",
            line=dict(dash="dash", color="red")
        ))

    fig.update_layout(
        plot_bgcolor="#f9f9f9",
        paper_bgcolor="#f9f9f9",
        font=dict(family="Arial", size=14),
        title=f"Cycle annuel moyen de la température<br>({an_debut}–{an_fin})",
        xaxis_title="Mois",
        yaxis_title="Température moyenne mensuelle (°C)",
        title_x=0.1,
        height=500,
        xaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
        yaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
        margin=dict(t=80, b=40, l=30, r=30),
        legend=dict(orientation="h", yanchor="bottom", y=-0.40, xanchor="center", x=0.5)
    )

    st.plotly_chart(fig, use_container_width=True)

# --- Titre principal TEMP ---
def afficher_titre_temp(nom_commune):
    st.markdown(
        f"""
        <div style='background-color:#e3f2fd; padding: 16px; border-left: 6px solid #2196F3;
                    border-radius: 8px; margin-bottom: 0.5em; box-shadow: 0 2px 6px rgba(0,0,0,0.05);'>
            <h3 style='text-align:center; color:#1b2b40; margin: 0; font-family: Arial, sans-serif;'>
                🌡️ Température moyenne – {nom_commune}
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
            <p>
            La température moyenne permet d’évaluer les tendances climatiques à long terme pour un lieu donné.
            </p>
            <p>
            La période de référence définie (1959–1987) est celle avant le réchauffement actuel.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
