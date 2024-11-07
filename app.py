import streamlit as st

# CSS pour styliser les boutons
button_red_style = """
<style>
    .button-red {
        background-color: #e74c3c; /* Rouge */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }
    .button-red:hover {
        opacity: 0.8;
    }
</style>
"""

button_green_style = """
<style>
    .button-green {
        background-color: #2ecc71; /* Vert */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }
    .button-green:hover {
        opacity: 0.8;
    }
</style>
"""

button_blue_style = """
<style>
    .button-blue {
        background-color: #3498db; /* Bleu */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }
    .button-blue:hover {
        opacity: 0.8;
    }
</style>
"""

# Injecter les styles
st.markdown(button_red_style, unsafe_allow_html=True)
st.markdown(button_green_style, unsafe_allow_html=True)
st.markdown(button_blue_style, unsafe_allow_html=True)

# Afficher les boutons avec leur style
if st.markdown('<button class="button-red">Bouton Rouge</button>', unsafe_allow_html=True):
    st.write("Le bouton rouge a été cliqué!")

if st.markdown('<button class="button-green">Bouton Vert</button>', unsafe_allow_html=True):
    st.write("Le bouton vert a été cliqué!")

if st.markdown('<button class="button-blue">Bouton Bleu</button>', unsafe_allow_html=True):
    st.write("Le bouton bleu a été cliqué!")
