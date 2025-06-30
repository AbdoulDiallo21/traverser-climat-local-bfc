# --- ETP ---
import numpy as np
import pandas as pd
import calendar
from statsmodels.nonparametric.smoothers_lowess import lowess
import plotly.graph_objects as go
import streamlit as st
import warnings

# --- Prétraitement annuel ETP ---
@st.cache_data
def pretraiter_etp_annuelle(df):
    resumyear = []
    for idP in df["idPoint"].unique():
        tmp = df[df["idPoint"] == idP].copy()
        tmp["ETP_Q"] = pd.to_numeric(tmp["ETP_Q"], errors="coerce")
        tmp["date"] = pd.to_datetime(tmp["time"], errors="coerce")
        tmp.dropna(subset=["date"], inplace=True)

        if not tmp.empty and tmp["ETP_Q"].notna().any():
            tmp.set_index("date", inplace=True)
            ann_sum = tmp["ETP_Q"].resample("YE").sum(min_count=1)
            resumyear.append(pd.DataFrame({
                "year": ann_sum.index.year,
                "ETP_Q": ann_sum.values,
                "idPoint": idP
            }))

    if resumyear:
        return pd.concat(resumyear, ignore_index=True)
    else:
        return pd.DataFrame(columns=["year", "ETP_Q", "idPoint"])

# --- Affichage annuel ETP ---
def afficher_etp_annuelle(resumyear, df, nom_commune, an_debut=1959, an_fin=2024, an_reference=True, periode_ref=(1959, 1987)):
    tmpcomm = df[df['Nom_commun'] == nom_commune][['idPoint', 'Ratio_Comm']]
    test = pd.merge(resumyear, tmpcomm, on='idPoint')
    test['ETP_Qp'] = test['ETP_Q'] * test['Ratio_Comm']

    rtest = test.groupby('year').apply(
        lambda x: pd.Series({
            'ETP_Qmp': x['ETP_Qp'].sum() / x['Ratio_Comm'].sum() if x['Ratio_Comm'].sum() != 0 else np.nan
        })
    ).reset_index()

    rtest['Nom_commun'] = nom_commune
    rtest['Year'] = rtest['year'].astype(int)

    df_periode = rtest[(rtest['Year'] >= an_debut) & (rtest['Year'] <= an_fin)]
    moyenne_periode = df_periode['ETP_Qmp'].mean()

    moyenne_ref = None
    if an_reference:
        df_ref = rtest[(rtest['Year'] >= periode_ref[0]) & (rtest['Year'] <= periode_ref[1])]
        moyenne_ref = df_ref['ETP_Qmp'].mean()

    loess_smoothed = lowess(df_periode['ETP_Qmp'], df_periode['Year'], frac=0.3)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_periode['Year'], y=df_periode['ETP_Qmp'], mode='lines+markers', name="ETP annuelle"))
    fig.add_trace(go.Scatter(x=loess_smoothed[:, 0], y=loess_smoothed[:, 1], mode='lines', name='Lissage LOESS', line=dict(color='black')))

    if moyenne_periode:
        fig.add_hline(y=moyenne_periode, line_dash="dot", line_color="blue", annotation_text="Moyenne période choisie", annotation_position="top left")
    if moyenne_ref:
        fig.add_hline(y=moyenne_ref, line_dash="dash", line_color="red", annotation_text="Moyenne réf. (1959–1987)", annotation_position="top right")

    fig.update_layout(
        title=f"Variabilité interannuelle de l'ETP<br>({an_debut}–{an_fin})",
        xaxis_title="Année",
        yaxis_title="ETP cumulée (mm)",
        height=500,
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9',
        font=dict(family='Arial', size=14),
        title_x=0.1,
        xaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        yaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Prétraitement mensuel ETP ---
@st.cache_data
def pretraiter_etp_mensuel(df, an_debut, an_fin):
    resummonth = []
    df = df.copy()
    df["date"] = pd.to_datetime(df["time"], errors="coerce")
    df["ETP_Q"] = pd.to_numeric(df["ETP_Q"], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df = df[(df["year"] >= an_debut) & (df["year"] <= an_fin)]

    for idP in df["idPoint"].unique():
        tmp = df[df["idPoint"] == idP].copy()
        tmp.dropna(subset=["ETP_Q", "date"], inplace=True)
        tmp.set_index("date", inplace=True)

        if not tmp.empty:
            monthly_sum = tmp["ETP_Q"].resample("M").sum(min_count=1)
            resummonth.append(pd.DataFrame({
                "year": monthly_sum.index.year,
                "month": monthly_sum.index.month,
                "ETP_Q": monthly_sum.values,
                "idPoint": idP
            }))

    return pd.concat(resummonth, ignore_index=True) if resummonth else pd.DataFrame(columns=["year", "month", "ETP_Q", "idPoint"])

# --- Calcul du cycle mensuel pondéré ---
def calculer_etp_mensuel_commune(df_monthly, df_ratio, nom_commune):
    month_abb = list(calendar.month_abbr)[1:]
    tmpcomm = df_ratio[df_ratio["Nom_commun"] == nom_commune][["idPoint", "Ratio_Comm"]]
    test = pd.merge(df_monthly, tmpcomm, on="idPoint")
    test["ETP_Qp"] = test["ETP_Q"] * test["Ratio_Comm"]

    sum_test = test.groupby("month")["ETP_Qp"].sum().reset_index(name="sum_ETP_Qp")
    sum_ratios = test.groupby("month")["Ratio_Comm"].sum().reset_index(name="sum_ratio")

    rcycle = pd.merge(sum_test, sum_ratios, on="month")
    rcycle["ETP_Qmp"] = rcycle.apply(lambda row: row["sum_ETP_Qp"] / row["sum_ratio"] if row["sum_ratio"] != 0 else np.nan, axis=1)
    rcycle["Month"] = rcycle["month"].astype(int)
    rcycle["Month_name"] = pd.Categorical(
        [calendar.month_abbr[m] for m in rcycle["Month"]],
        categories=month_abb,
        ordered=True
    )
    return rcycle.sort_values("Month")

# --- Affichage du cycle ETP mensuel ---
def afficher_etp_mensuel(rcycle, nom_commune, an_debut, an_fin, rcycle_ref=None):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=rcycle['Month_name'],
        y=rcycle['ETP_Qmp'],
        mode='lines+markers',
        name=f"Période définie: {an_debut}–{an_fin}",
        line=dict(color='blue')
    ))

    if rcycle_ref is not None:
        fig.add_trace(go.Scatter(
            x=rcycle_ref['Month_name'],
            y=rcycle_ref['ETP_Qmp'],
            mode='lines+markers',
            name="Référence 1959–1987",
            line=dict(color='red', dash='dash')
        ))

    fig.update_layout(
        title=f"Cycle annuel moyen de l'ETP<br>({an_debut}–{an_fin})",
        xaxis_title="Mois",
        yaxis_title="ETP (mm)",
        height=500,
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9',
        font=dict(family='Arial', size=14),
        title_x=0.1,
        xaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        yaxis=dict(showgrid=True, gridcolor='#e5e5e5'),
        margin=dict(t=80, b=40, l=30, r=30),
        legend=dict(orientation="h", yanchor="bottom", y=-0.4, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Titre principal ---
def afficher_titre_etp(nom_commune):
    st.markdown(f"""
        <div style='background-color:#e3f2fd; padding: 16px; border-left: 6px solid #2196F3;
                    border-radius: 8px; margin-bottom: 0.5em; box-shadow: 0 2px 6px rgba(0,0,0,0.05);'>
            <h3 style='text-align:center; color:#1b2b40; margin: 0; font-family: Arial, sans-serif;'>
                Évapotranspiration potentielle (ETP) – {nom_commune}
            </h3>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color: #f5f5f5; padding: 20px; border-left: 6px solid #9e9e9e;
                    border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.05); margin-top: 1em; margin-bottom: 1em; font-size: 0.95em;">
            <p>
            L’évapotranspiration potentielle (ETP) est la demande ou quantité maximale d'eau qui serait évapotranspirée 
            par les plantes et le sol par une surface donnée si les précipitations et l'humidité du sol étaient suffisantes.
            </p>
            <p><strong>Exemple :</strong> une augmentation de l'ETP de 10 mm/m² correspond à 100 m³ d'eau par hectare.</p>
            <p>La période de référence définie (1959–1987) est celle avant le réchauffement actuel.</p>
        </div>""", unsafe_allow_html=True)

# --- Simulateur ETP ---
def afficher_simulateur_etp():
    st.markdown("##### 💧 Simulateur de besoin en eau selon l'ETP")

    if st.checkbox("🔘 Afficher le calcul du besoin en eau par hectare"):
        ecart_etp = st.slider("Choisis un écart d’ETP (en mm)", min_value=1, max_value=100, value=10)
        besoin_l_m2 = ecart_etp
        besoin_m3_ha = ecart_etp * 10

        st.markdown(f"""
        ### 🌱 Résultat

        - 📏 Écart d’ETP : **{ecart_etp} mm**
        - 💧 Besoin en eau = **{besoin_l_m2} L/m²**
        - 🌾 Pour 1 hectare : **{besoin_m3_ha} m³ d’eau** (soit **{besoin_m3_ha * 1000:.0f} litres**)

        ---
        > Une augmentation de {ecart_etp} mm d'ETP signifie qu’il faudrait **{besoin_m3_ha} m³ d’eau supplémentaires** par hectare pour compenser ce déficit climatique.
        """)
