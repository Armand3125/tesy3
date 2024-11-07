import streamlit as st

# Récupérer la couleur primaire définie dans le fichier config.toml
primaryColor = st.get_option("theme.primaryColor")

# Appliquer la couleur du thème au bouton via CSS
st.markdown(f"""
<style>
div.stButton > button:first-child {{
    background-color: {primaryColor};  /* couleur de fond du bouton */
    color: white;  /* couleur du texte */
    font-size: 20px;  /* taille de la police */
    height: 3em;  /* hauteur du bouton */
    width: 15em;  /* largeur du bouton */
    border-radius: 10px;  /* arrondir les coins du bouton */
}}

div.stButton > button:hover {{
    background-color: #00ff00;  /* couleur de fond lorsque l'on survole le bouton */
    color: #ff0000;  /* couleur du texte lorsqu'on survole */
}}
</style>
""", unsafe_allow_html=True)

# Créer un bouton
if st.button("Cliquez ici"):
    st.write("Bouton cliqué !")
