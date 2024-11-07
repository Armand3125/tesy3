import streamlit as st

# Récupérer la couleur primaire définie dans le fichier config.toml
primaryColor = st.get_option("theme.primaryColor")
secondaryColor = "#ff6347"  # Exemple de couleur secondaire (Tomato)
tertiaryColor = "#32cd32"    # Exemple de couleur tertiaire (LimeGreen)

# Appliquer la couleur du thème au bouton via CSS
st.markdown(f"""
<style>
/* Premier bouton (Couleur primaire) */
div.stButton > button:first-child {{
    background-color: {primaryColor};  /* couleur de fond du bouton principal */
    color: white;  /* couleur du texte */
    font-size: 20px;  /* taille de la police */
    height: 3em;  /* hauteur du bouton */
    width: 15em;  /* largeur du bouton */
    border-radius: 10px;  /* arrondir les coins du bouton */
}}

/* Deuxième bouton (Couleur secondaire) */
div.stButton > button:nth-of-type(2) {{
    background-color: {secondaryColor};  /* couleur de fond du bouton secondaire */
    color: white;  /* couleur du texte */
    font-size: 20px;  /* taille de la police */
    height: 3em;  /* hauteur du bouton */
    width: 15em;  /* largeur du bouton */
    border-radius: 10px;  /* arrondir les coins du bouton */
}}

/* Troisième bouton (Couleur tertiaire) */
div.stButton > button:nth-of-type(3) {{
    background-color: {tertiaryColor};  /* couleur de fond du bouton tertiaire */
    color: white;  /* couleur du texte */
    font-size: 20px;  /* taille de la police */
    height: 3em;  /* hauteur du bouton */
    width: 15em;  /* largeur du bouton */
    border-radius: 10px;  /* arrondir les coins du bouton */
}}

/* Effet de survol sur tous les boutons */
div.stButton > button:hover {{
    background-color: #00ff00;  /* couleur de fond lorsque l'on survole le bouton */
    color: #ff0000;  /* couleur du texte lorsqu'on survole */
}}
</style>
""", unsafe_allow_html=True)

# Créer trois boutons avec trois couleurs différentes
if st.button("Bouton Bleu"):
    st.write("Bouton bleu cliqué !")

if st.button("Bouton Rouge"):
    st.write("Bouton rouge cliqué !")

if st.button("Bouton Vert"):
    st.write("Bouton vert cliqué !")
