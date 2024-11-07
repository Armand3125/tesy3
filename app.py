import streamlit as st
import requests

# URL du fichier CSS sur GitHub
css_url = "https://raw.githubusercontent.com/votre-compte/votre-repo/main/style.css"

# Fonction pour charger le CSS
def load_css(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        st.error("Le fichier CSS n'a pas pu être chargé.")
        return ""

# Charger et appliquer le CSS
css = load_css(css_url)
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Application Streamlit
st.title("Mon Application avec CSS depuis GitHub")

st.write('<p class="custom-text">Bienvenue sur mon application stylisée !</p>', unsafe_allow_html=True)

# Bouton stylisé
if st.button("Cliquez-moi !"):
    st.write("Vous avez cliqué sur un bouton stylisé.")

st.write("Ceci est un exemple de texte sans style particulier.")
