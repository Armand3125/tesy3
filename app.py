import streamlit as st

# CSS pour styliser les boutons
button_red_style = """
<style>
    .stButton>button {
        background-color: #e74c3c; /* Rouge */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }
    .stButton>button:hover {
        opacity: 0.8;
    }
</style>
"""

button_green_style = """
<style>
    .stButton>button {
        background-color: #2ecc71; /* Vert */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }
    .stButton>button:hover {
        opacity: 0.8;
    }
</style>
"""

button_blue_style = """
<style>
    .stButton>button {
        background-color: #3498db; /* Bleu */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }
    .stButton>button:hover {
        opacity: 0.8;
    }
</style>
"""

# Injection des styles dans l'application Streamlit
st.markdown(button_red_style, unsafe_allow_html=True)
st.markdown(button_green_style, unsafe_allow_html=True)
st.markdown(button_blue_style, unsafe_allow_html=True)

# Boutons Streamlit avec des couleurs différentes
if st.button("Bouton Rouge"):
    st.write("Le bouton rouge a été cliqué!")

if st.button("Bouton Vert"):
    st.write("Le bouton vert a été cliqué!")

if st.button("Bouton Bleu"):
    st.write("Le bouton bleu a été cliqué!")
