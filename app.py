import streamlit as st

# Titre de l'application
st.title('Exemple avec trois boutons dans les zones de couleur')

# Créer 3 colonnes pour aligner les boutons
col1, col2, col3 = st.columns(3)

# Initialiser une variable de sélection
selected_color = None

# Boutons et zones de couleur dans chaque colonne
with col1:
    if st.button('Bouton 1'):
        selected_color = 'red'
    st.markdown(
        f'<div style="height:100px; background-color:red; border: 2px solid { "black" if selected_color == "red" else "transparent" }; display: flex; justify-content: center; align-items: center; margin-top: 10px;">'
        '</div>',
        unsafe_allow_html=True)

with col2:
    if st.button('Bouton 2'):
        selected_color = 'blue'
    st.markdown(
        f'<div style="height:100px; background-color:blue; border: 2px solid { "black" if selected_color == "blue" else "transparent" }; display: flex; justify-content: center; align-items: center; margin-top: 10px;">'
        '</div>',
        unsafe_allow_html=True)

with col3:
    if st.button('Bouton 3'):
        selected_color = 'green'
    st.markdown(
        f'<div style="height:100px; background-color:green; border: 2px solid { "black" if selected_color == "green" else "transparent" }; display: flex; justify-content: center; align-items: center; margin-top: 10px;">'
        '</div>',
        unsafe_allow_html=True)
