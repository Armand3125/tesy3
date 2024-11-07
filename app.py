import streamlit as st

# Ajouter du CSS pour personnaliser l'apparence des boutons
st.markdown("""
    <style>
        /* Style personnalisé pour le bouton rouge */
        .button-red {
            background-color: #e74c3c; /* Rouge */
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            width: 100%;
        }

        /* Style personnalisé pour le bouton vert */
        .button-green {
            background-color: #2ecc71; /* Vert */
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            width: 100%;
        }

        /* Style personnalisé pour le bouton bleu */
        .button-blue {
            background-color: #3498db; /* Bleu */
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            width: 100%;
        }

        /* Effet de survol pour chaque bouton */
        .button-red:hover, .button-green:hover, .button-blue:hover {
            opacity: 0.8;
        }
    </style>
""", unsafe_allow_html=True)

# Variables pour suivre l'état du bouton sélectionné
if 'selected_button' not in st.session_state:
    st.session_state.selected_button = None

# Créer trois boutons avec des styles personnalisés
col1, col2, col3 = st.columns(3)

# Gestion de l'état du bouton cliqué
with col1:
    if st.button("Rouge", key="red"):
        st.session_state.selected_button = "Rouge"

with col2:
    if st.button("Vert", key="green"):
        st.session_state.selected_button = "Vert"

with col3:
    if st.button("Bleu", key="blue"):
        st.session_state.selected_button = "Bleu"

# Afficher la couleur du bouton sélectionné
if st.session_state.selected_button:
    st.write(f"Vous avez sélectionné le bouton {st.session_state.selected_button} !")
