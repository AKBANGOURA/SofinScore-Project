Markdown

# 🚀 SofinScore - Moteur de Scoring Crédit End-to-End

Ce projet présente une solution complète de **Credit Scoring** développée pour simuler les problématiques d'octroi de crédit chez **Sofinco**. L'objectif est de fournir une évaluation en temps réel du risque de défaut client en s'appuyant sur des modèles de Machine Learning.

## 🎯 Objectifs du Projet
* **Industrialisation** : Passage d'un modèle statistique à une application interactive.
* **Scoring de Risque** : Prédiction de la probabilité de défaut basée sur des données socio-démographiques et financières.
* **Aide à la Décision** : Interface visuelle pour les conseillers avec des seuils d'acceptation automatiques.

## 🛠️ Stack Technique
* **Langage** : Python 3.11
* **Machine Learning** : Scikit-learn (Random Forest Classifier)
* **API Framework** : FastAPI (Structure prête pour l'industrialisation)
* **Interface** : Streamlit
* **Versioning** : Git / GitHub

## 📊 Pipeline de Données
Le modèle utilise des variables clés pour évaluer la solvabilité :
1. **Revenu Mensuel** & **Montant du Prêt** : Pour calculer le ratio d'endettement.
2. **Âge** : Facteur de stabilité.
3. **Historique de Crédit** : Variable majeure pour la détection de fraude ou d'impayés passés.

## 🚀 Installation et Utilisation Locale

1. **Cloner le dépôt** :
   ```bash
   git clone [https://github.com/TON_NOM_UTILISATEUR/SofinScore-Project.git](https://github.com/TON_NOM_UTILISATEUR/SofinScore-Project.git)
Installer les dépendances :

Bash

pip install -r requirements.txt
Lancer l'application :

Bash

streamlit run app_streamlit.py
📈 Évolutions Futures (MLOps)
Pour répondre pleinement aux exigences de l'offre (Octroi & Scores) :

Airflow : Mise en place d'un pipeline de réentraînement automatique du modèle.

MLflow : Tracking des versions du modèle et monitoring du "Data Drift".

Docker : Conteneurisation pour un déploiement robuste sur Kubernetes.


Projet réalisé par Almamy Kalla BANGOURA dans le cadre d'une candidature pour le poste de Data Scientist.
