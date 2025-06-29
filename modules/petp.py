import numpy as np
import pandas as pd
import calendar
import plotly.graph_objects as go
import streamlit as st
from statsmodels.nonparametric.smoothers_lowess import lowess
from matplotlib.ticker import MaxNLocator
import warnings

# --- 1. Prétraitement annuel ---
@st.cache_data
def pretraiter_bilan_annuelle(df, an_debut, an_fin):
    resumyear = []
    df['date'] = pd.to_datetime(df['time'], errors='coerce')
    df['P_ETP'] = pd.to_numeric(df['P_ETP'], errors='coerce')
    df = df[df['date'].dt.year.between(an_debut, an_fin)]

    for idp, group in df.groupby("idPoint"):
        annual = group.set_index("date").resample("YE")["P_ETP"].sum(min_count=1)
        df_tmp = pd.DataFrame({
            "year": annual.index.year,
            "P_ETP": annual.values,
            "idPoint": idp
        })
        resumyear.append(df_tmp)

    return pd.concat(resumyear, ignore_index=True)

# --- 2. Affichage annuel ---
def afficher_bilan_annuelle(resumyear, df, nom_commune, an_debut=1959, an_fin=2024, an_reference=True, periode_ref=(1959, 1987), resum_ref=None):
    tmpcomm = df[df["Nom_commun"] == nom_commune][["idPoint", "Ratio_Comm"]]
    test = pd.merge(resumyear, tmpcomm, on="idPoint")
    test["P_ETP_p"] = test["P_ETP"] * test["Ratio_Comm"]
    test["year"] = test["year"].astype(int)

    rtest = test.groupby("year").agg(
        sum_P_ETP_p=('P_ETP_p', 'sum'),
        sum_ratio=('Ratio_Comm', 'sum')
    ).reset_index()
    rtest['P_ETP_mp'] = rtest['sum_P_ETP_p'] / rtest['sum_ratio']
    rtest['Year'] = rtest['year']
    rtest['Nom_commun'] = nom_commune

    df_periode = rtest[(rtest["Year"] >= an_debut) & (rtest["Year"] <= an_fin)]
    moyenne_periode = df_periode["P_ETP_mp"].mean()

    moyenne_ref = None
    if an_reference and resum_ref is not None:
        test_ref = pd.merge(resum_ref, tmpcomm, on="idPoint")
        test_ref["P_ETP_p"] = test_ref["P_ETP"] * test_ref["Ratio_Comm"]
        test_ref["year"] = test_ref["year"].astype(int)
        rtest_ref = test_ref.groupby("year").agg(
            sum_P_ETP_p=('P_ETP_p', 'sum'),
            sum_ratio=('Ratio_Comm', 'sum')
        ).reset_index()
        rtest_ref['P_ETP_mp'] = rtest_ref['sum_P_ETP_p'] / rtest_ref['sum_ratio']
        df_ref = rtest_ref[(rtest_ref['year'] >= periode_ref[0]) & (rtest_ref['year'] <= periode_ref[1])]
        moyenne_ref = df_ref["P_ETP_mp"].mean()

    loess_smoothed = lowess(df_periode["P_ETP_mp"], df_periode["Year"], frac=0.3)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_periode["Year"], y=df_periode["P_ETP_mp"], mode="lines+markers", name="P - ETP annuel"))
    fig.add_trace(go.Scatter(x=loess_smoothed[:, 0], y=loess_smoothed[:, 1], mode="lines", name="Lissage LOESS", line=dict(color="black")))

    if moyenne_periode:
        fig.add_hline(y=moyenne_periode, line_dash="dot", line_color="blue", annotation_text="Moyenne période", annotation_position="top left")
    if moyenne_ref:
        fig.add_hline(y=moyenne_ref, line_dash="dash", line_color="red", annotation_text="Moyenne réf. (1959–1987)", annotation_position="top right")

    fig.update_layout(
        plot_bgcolor="#f9f9f9",
        paper_bgcolor="#f9f9f9",
        font=dict(family="Arial", size=14),
        title=f"Variation interannuelle du bilan hydrique<br>({an_debut}–{an_fin})",
        title_x=0.1,
        xaxis_title="Année",
        yaxis_title="Bilan hydrique annuel (mm)",
        height=500,
        xaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
        yaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
        legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig, use_container_width=True)

# --- 3. Prétraitement mensuel ---
@st.cache_data
def pretraiter_bilan_mensuel(df, an_debut, an_fin):
    resummonth = []
    df['date'] = pd.to_datetime(df['time'], errors='coerce')
    df['P_ETP'] = pd.to_numeric(df['P_ETP'], errors='coerce')
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    df = df[(df['year'] >= an_debut) & (df['year'] <= an_fin)].copy()

    for idP in df['idPoint'].unique():
        tmp = df[df['idPoint'] == idP].copy()

        if tmp['P_ETP'].isna().sum() > 0:
            warnings.warn(f"Valeurs NA détectées pour idPoint = {idP}")

        tmp = tmp.dropna(subset=['P_ETP'])
        tmp = tmp.set_index('date')

        if not tmp.empty:
            monthly_sum = tmp['P_ETP'].resample('ME').sum(min_count=1)
            df_month = pd.DataFrame({
                'year': monthly_sum.index.year,
                'month': monthly_sum.index.month,
                'P_ETP': monthly_sum.values,
                'idPoint': idP
            })
            resummonth.append(df_month)

    return pd.concat(resummonth, ignore_index=True)

# --- 4. Affichage mensuel ---
def afficher_bilan_mensuel(resummonth, df_ratio, nom_commune, an_debut, an_fin, df_month_ref=None):
    month_abb = list(calendar.month_abbr)[1:]
    tmpcomm = df_ratio[df_ratio['Nom_commun'] == nom_commune][['idPoint', 'Ratio_Comm']]
    test = pd.merge(resummonth, tmpcomm, on='idPoint')
    test['P_ETPp'] = test['P_ETP'] * test['Ratio_Comm']

    sum_test = test.groupby("month")["P_ETPp"].sum().reset_index(name="sum_P_ETPp")
    sum_ratios = test.groupby("month")["Ratio_Comm"].sum().reset_index(name="sum_ratio")

    rcycle = pd.merge(sum_test, sum_ratios, on="month")
    rcycle['P_ETPmp'] = rcycle['sum_P_ETPp'] / rcycle['sum_ratio']
    rcycle['Month'] = rcycle['month'].astype(int)
    rcycle['Month_name'] = pd.Categorical(
        [calendar.month_abbr[m] for m in rcycle['Month']],
        categories=month_abb,
        ordered=True
    )
    rcycle.sort_values('Month', inplace=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=rcycle['Month_name'],
        y=rcycle['P_ETPmp'],
        mode='lines+markers',
        name=f"{an_debut}–{an_fin}",
        line=dict(color='blue')
    ))

    if df_month_ref is not None:
        test_ref = pd.merge(df_month_ref, tmpcomm, on='idPoint')
        test_ref['P_ETPp'] = test_ref['P_ETP'] * test_ref['Ratio_Comm']

        sum_test_ref = test_ref.groupby("month")["P_ETPp"].sum().reset_index(name="sum_P_ETPp")
        sum_ratios_ref = test_ref.groupby("month")["Ratio_Comm"].sum().reset_index(name="sum_ratio")

        rcycle_ref = pd.merge(sum_test_ref, sum_ratios_ref, on="month")
        rcycle_ref['P_ETPmp'] = rcycle_ref['sum_P_ETPp'] / rcycle_ref['sum_ratio']
        rcycle_ref['Month'] = rcycle_ref['month'].astype(int)
        rcycle_ref['Month_name'] = pd.Categorical(
            [calendar.month_abbr[m] for m in rcycle_ref['Month']],
            categories=month_abb,
            ordered=True
        )
        rcycle_ref.sort_values('Month', inplace=True)

        fig.add_trace(go.Scatter(
            x=rcycle_ref['Month_name'],
            y=rcycle_ref['P_ETPmp'],
            mode='lines+markers',
            name="Référence 1959–1987",
            line=dict(dash='dash', color='red')
        ))

    fig.update_layout(
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9',
        font=dict(family='Arial', size=14),
        title=f"Cycle annuel moyen du bilan hydrique<br>({an_debut}–{an_fin})",
        title_x=0.1,
        xaxis_title="Mois",
        yaxis_title="P - ETP moyen (mm)",
        height=500,
        xaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        yaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        margin=dict(t=80, b=40, l=30, r=30),
        legend=dict(orientation="h", yanchor="bottom", y=-0.40, xanchor="center", x=0.5)
    )

    st.plotly_chart(fig, use_container_width=True)


# --- 6. Titre général pour affichage combiné ---
def afficher_titre_petp(nom_commune):
    st.markdown(
        f"""
        <div style='background-color:#e3f2fd; padding: 16px; border-left: 6px solid #2196F3;
                    border-radius: 8px; margin-bottom: 0.5em; box-shadow: 0 2px 6px rgba(0,0,0,0.05);'>
            <h3 style='text-align:center; color:#1b2b40; margin: 0; font-family: Arial, sans-serif;'>
                Bilan hydrique climatique (P–ETP) – {nom_commune}
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
            Le bilan hydrique climatique (P–ETP), exprimé en millimètres, correspond à la différence entre les précipitations (P) 
            et l'évapotranspiration potentielle (ETP). Il représente la quantité d'eau ajoutée ou prélevée dans le réservoir d'eau du sol.
            </p>
            <p>La période de référence définie (1959–1987) est celle avant le réchauffement actuel.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

