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

# Utilisation de session_state pour savoir quel bouton a été cliqué
if 'selected_button' not in st.session_state:
    st.session_state.selected_button = None

# Boutons HTML dans les colonnes
col1, col2, col3 = st.columns(3)

# HTML pour les boutons avec gestion des clics
with col1:
    if st.markdown('<button class="red-button">Bouton Rouge</button>', unsafe_allow_html=True):
        st.session_state.selected_button = "Rouge"

with col2:
    if st.markdown('<button class="green-button">Bouton Vert</button>', unsafe_allow_html=True):
        st.session_state.selected_button = "Vert"

with col3:
    if st.markdown('<button class="blue-button">Bouton Bleu</button>', unsafe_allow_html=True):
        st.session_state.selected_button = "Bleu"

# Affichage du bouton sélectionné
if st.session_state.selected_button:
    st.write(f"Vous avez sélectionné le bouton {st.session_state.selected_button} !")
