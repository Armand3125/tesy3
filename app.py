import streamlit as st

# CSS pour styliser les boutons
button_style = """
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

    .button-green {
        background-color: #2ecc71; /* Vert */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }

    .button-blue {
        background-color: #3498db; /* Bleu */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }

    .button-red:hover, .button-green:hover, .button-blue:hover {
        opacity: 0.8;
    }
</style>
"""

# Injecter le CSS
st.markdown(button_style, unsafe_allow_html=True)

# Créer les boutons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Bouton Rouge', key='red'):
        st.write("Le bouton rouge a été cliqué!")

with col2:
    if st.button('Bouton Vert', key='green'):
        st.write("Le bouton vert a été cliqué!")

with col3:
    if st.button('Bouton Bleu', key='blue'):
        st.write("Le bouton bleu a été cliqué!")
