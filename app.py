import streamlit as st

# Titre de l'application
st.title('Exemple avec trois boutons sur la même ligne')

# Créer 3 colonnes pour aligner les boutons
col1, col2, col3 = st.columns(3)

# Boutons dans chaque colonne
with col1:
    if st.button('Bouton 1'):
        st.write('Vous avez cliqué sur le Bouton 1')

with col2:
    if st.button('Bouton 2'):
        st.write('Vous avez cliqué sur le Bouton 2')

with col3:
    if st.button('Bouton 3'):
        st.write('Vous avez cliqué sur le Bouton 3')
