import streamlit as st

# CSS pour personnaliser l'apparence des boutons
st.markdown("""
    <style>
        .button-red {
            background-color: #e74c3c;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            width: 100%;
        }

        .button-green {
            background-color: #2ecc71;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            width: 100%;
        }

        .button-blue {
            background-color: #3498db;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            width: 100%;
        }

        .button-red:hover, .button-green:hover, .button-blue:hover {
            opacity: 0.8;
        }
    </style>
""", unsafe_allow_html=True)

# Créer trois boutons avec des couleurs différentes
col1, col2, col3 = st.columns(3)

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
if 'selected_button' in st.session_state:
    st.write(f"Vous avez sélectionné le bouton {st.session_state.selected_button} !")
