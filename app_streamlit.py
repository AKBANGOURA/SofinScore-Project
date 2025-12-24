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
# Ces fichiers doivent être dans un dossier nommé 'models' sur ton GitHub
@st.cache_resource # Pour charger le modèle une seule fois et gagner en rapidité
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

# --- LOGIQUE DE PRÉDICTION ---
# Le bouton déclenche le calcul
if st.sidebar.button("Évaluer le Dossier"):
    # 1. Feature Engineering (Ratio d'endettement)
    ratio_dette = montant / (revenu * 12)
    
    # 2. Préparation des données (Doit correspondre exactement à l'entraînement)
    # Features : revenu_mensuel, age, montant_pret, historique_credit, ratio_dette
    features = np.array([[revenu, age, montant, historique, ratio_dette]])
    
    # 3. Normalisation et Prédiction
    features_scaled = scaler.transform(features)
    probability = model.predict_proba(features_scaled)[0][1]
    score_fiabilite = round(float(1 - probability) * 100, 1)

    # --- AFFICHAGE DES RÉSULTATS ---
    st.subheader("🎯 Résultat de l'Analyse")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Score de Fiabilité", value=f"{score_fiabilite}/100")
    
    with col2:
        prob_percent = round(probability * 100, 2)
        st.write(f"**Probabilité de défaut :** {prob_percent}%")
        
    with col3:
        if probability < 0.35:
            st.success("DÉCISION : APPROUVÉ")
        elif probability < 0.60:
            st.warning("DÉCISION : REVUE MANUELLE")
        else:
            st.error("DÉCISION : REFUSÉ")

    # Petit conseil pédagogique pour le recruteur
    st.info(f"Note technique : Ce score est calculé en temps réel via le modèle Random Forest stocké dans `/models`.")

else:
    st.info("Utilisez le panneau de gauche pour remplir les données du client et cliquez sur 'Évaluer le Dossier'.")

# --- GRAPHIQUES DE DÉMONSTRATION ---
st.divider()
st.subheader("📊 Aperçu Statistique du Portefeuille")

col_a, col_b = st.columns(2)

with col_a:
    # Simulation d'un graphique de distribution des scores
    chart_data = pd.DataFrame(
        np.random.normal(70, 15, size=1000),
        columns=['Distribution des Scores']
    )
    st.area_chart(chart_data)

with col_b:
    # Répartition des décisions
    data_sim = pd.DataFrame({
        'Catégorie': ['Approuvés', 'Revue Manuelle', 'Refusés'],
        'Volume': [750, 150, 100]
    })
    st.bar_chart(data=data_sim, x='Catégorie', y='Volume')