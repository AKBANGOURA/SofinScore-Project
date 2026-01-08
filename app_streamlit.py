import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="SofinScore - Dashboard Décisionnel",
    page_icon="🚀",
    layout="wide"
)

# --- CHARGEMENT DU MODÈLE ET DU SCALER ---
@st.cache_resource 
def load_assets():
    model = joblib.load("models/credit_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler

try:
    model, scaler = load_assets()
except Exception as e:
    st.error(f"Erreur de chargement des modèles : {e}")
    st.stop()

# --- INTERFACE UTILISATEUR ---
st.title("🚀 SofinScore : Outil d'Aide à la Décision Crédit")
st.markdown("""
Cette interface simule l'outil utilisé par les conseillers **Sofinco** pour évaluer un risque de crédit en temps réel.
* **Modèle :** Random Forest (Scoring de risque)
* **Statut :** Démonstration technique (End-to-End)
""")

st.divider()

# --- BARRE LATÉRALE (ENTRÉES) ---
st.sidebar.header("📋 Paramètres du Client")
st.sidebar.write("Modifiez les curseurs pour tester le score.")

revenu = st.sidebar.number_input("Revenu mensuel (€)", min_value=500, max_value=20000, value=2500, step=100)
age = st.sidebar.slider("Âge du client", 18, 90, 35)
montant = st.sidebar.number_input("Montant du prêt demandé (€)", min_value=1000, max_value=100000, value=15000, step=500)
historique = st.sidebar.selectbox(
    "Historique de crédit", 
    options=[0, 1], 
    format_func=lambda x: "Bon (Pas de défaut)" if x == 1 else "Mauvais (Défauts passés)"
)

# --- BOUTON D'ACTION (PLACÉ AVANT L'AUTEUR) ---
predict_btn = st.sidebar.button("Évaluer le Dossier")

# --- SECTION AUTEUR (PLACÉE TOUT EN BAS) ---
st.sidebar.divider()
st.sidebar.header("🎓 À propos de l'auteur")
st.sidebar.write("**Auteur :** Almamy Kalla BANGOURA")
st.sidebar.write("**Expertise :** Consultant Data | Chargé d'études statistiques")

# --- LOGIQUE DE PRÉDICTION ---
if predict_btn:
    # 1. Feature Engineering
    ratio_dette = montant / (revenu * 12)
    
    # 2. Préparation des données
    features = np.array([[revenu, age, montant, historique, ratio_dette]])
    
    #
