import streamlit as st
import requests

# URL du fichier CSS hébergé sur GitHub
css_url = "https://raw.githubusercontent.com/Armand3125/tesy3/main/style.css"

# Fonction pour charger le CSS
def load_css(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête est réussie
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors du chargement du fichier CSS : {e}")
        return ""

# Charger et appliquer le CSS
css = load_css(css_url)
if css:
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Application Streamlit
st.title("Application avec Boutons Colorés")

# Afficher trois boutons avec HTML pour styliser chaque bouton différemment
col1, col2, col3 = st.columns(3)

# Utiliser Markdown pour injecter du HTML et appliquer des styles CSS
with col1:
    st.markdown('<button class="red-button">Bouton Rouge</button>', unsafe_allow_html=True)

with col2:
    st.markdown('<button class="green-button">Bouton Vert</button>', unsafe_allow_html=True)

with col3:
    st.markdown('<button class="blue-button">Bouton Bleu</button>', unsafe_allow_html=True)
