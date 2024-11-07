import streamlit as st

# Appliquer le CSS pour personnaliser l'apparence des boutons
st.markdown("""
    <style>
        /* Personnalisation des boutons */
        .stButton>button {
            font-size: 16px;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
        }
        
        .stButton>button:nth-child(1) {
            background-color: #e74c3c; /* Rouge */
            color: white;
            border: 2px solid #d63031;
        }

        .stButton>button:nth-child(2) {
            background-color: #2ecc71; /* Vert */
            color: white;
            border: 2px solid #27ae60;
        }

        .stButton>button:nth-child(3) {
            background-color: #3498db; /* Bleu */
            color: white;
            border: 2px solid #2980b9;
        }

        /* Effet au survol des boutons */
        .stButton>button:hover {
            opacity: 0.8;
        }
    </style>
""", unsafe_allow_html=True)

# Application Streamlit
st.title("Application avec Boutons Colorés")

# Variables de session pour suivre l'état du bouton sélectionné
if 'selected_button' not in st.session_state:
    st.session_state.selected_button = None

# Création de trois boutons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Bouton Rouge"):
        st.session_state.selected_button = "Rouge"

with col2:
    if st.button("Bouton Vert"):
        st.session_state.selected_button = "Vert"

with col3:
    if st.button("Bouton Bleu"):
        st.session_state.selected_button = "Bleu"

# Affichage de la couleur sélectionnée
if st.session_state.selected_button:
    st.write(f"Vous avez sélectionné le bouton {st.session_state.selected_button} !")
