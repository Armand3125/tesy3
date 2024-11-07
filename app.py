import streamlit as st

# Insérer du CSS pour personnaliser l'apparence du bouton
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;  /* couleur de fond du bouton */
    color: #ffffff;  /* couleur du texte */
    font-size: 20px;  /* taille de la police */
    height: 3em;  /* hauteur du bouton */
    width: 15em;  /* largeur du bouton */
    border-radius: 10px;  /* arrondir les coins du bouton */
}

div.stButton > button:hover {
    background-color: #00ff00;  /* couleur de fond lorsque l'on survole le bouton */
    color: #ff0000;  /* couleur du texte lorsqu'on survole */
}
</style>
""", unsafe_allow_html=True)

# Créer un bouton
if st.button("Cliquez ici"):
    st.write("Bouton cliqué !")
