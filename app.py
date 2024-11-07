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

# Afficher trois boutons avec des classes CSS pour les couleurs
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Bouton Rouge", key="red", use_container_width=True, css_class="red-button"):
        st.write("Vous avez cliqué sur le bouton rouge.")

with col2:
    if st.button("Bouton Vert", key="green", use_container_width=True, css_class="green-button"):
        st.write("Vous avez cliqué sur le bouton vert.")

with col3:
    if st.button("Bouton Bleu", key="blue", use_container_width=True, css_class="blue-button"):
        st.write("Vous avez cliqué sur le bouton bleu.")
