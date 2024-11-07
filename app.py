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
    border: none;  /* Enlever la bordure par défaut */
    box-shadow: none;  /* Enlever l'ombre portée par défaut */
}}

/* Deuxième bouton (Couleur secondaire) */
div.stButton > button:nth-of-type(2) {{
    background-color: {secondaryColor};  /* couleur de fond du bouton secondaire */
    color: white;  /* couleur du texte */
    font-size: 20px;  /* taille de la police */
    height: 3em;  /* hauteur du bouton */
    width: 15em;  /* largeur du bouton */
    border-radius: 10px;  /* arrondir les coins du bouton */
    border: none;  /* Enlever la bordure par défaut */
    box-shadow: none;  /* Enlever l'ombre portée par défaut */
}}

/* Troisième bouton (Couleur tertiaire) */
div.stButton > button:nth-of-type(3) {{
    background-color: {tertiaryColor};  /* couleur de fond du bouton tertiaire */
    color: white;  /* couleur du texte */
    font-size: 20px;  /* taille de la police */
    height: 3em;  /* hauteur du bouton */
    width: 15em;  /* largeur du bouton */
    border-radius: 10px;  /* arrondir les coins du bouton */
    border: none;  /* Enlever la bordure par défaut */
    box-shadow: none;  /* Enlever l'ombre portée par défaut */
}}

/* Effet de survol sur tous les boutons */
div.stButton > button:hover {{
    opacity: 0.8;  /* Rendre les boutons légèrement transparents lorsqu'on les survole */
    color: #ffffff;  /* Changer la couleur du texte */
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
