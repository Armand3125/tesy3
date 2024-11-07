import streamlit as st

# Titre de l'application
st.title("Trois Boutons et Trois Rectangles")

# Créer trois boutons
if st.button("Bouton Rouge"):
    st.write("Vous avez cliqué sur le bouton rouge.")

if st.button("Bouton Vert"):
    st.write("Vous avez cliqué sur le bouton vert.")

if st.button("Bouton Bleu"):
    st.write("Vous avez cliqué sur le bouton bleu.")

# Créer trois rectangles de différentes couleurs
st.markdown("""
<style>
.rectangle {
    width: 300px;
    height: 100px;
    margin-bottom: 20px;
    border-radius: 10px;
}

.red {
    background-color: red;
}

.green {
    background-color: green;
}

.blue {
    background-color: blue;
}
</style>
""", unsafe_allow_html=True)

# Affichage des rectangles avec des couleurs différentes
st.markdown('<div class="rectangle red"></div>', unsafe_allow_html=True)
st.markdown('<div class="rectangle green"></div>', unsafe_allow_html=True)
st.markdown('<div class="rectangle blue"></div>', unsafe_allow_html=True)
