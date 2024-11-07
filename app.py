import streamlit as st

# Titre de l'application
st.title('Exemple avec trois boutons')

# Boutons
if st.button('Bouton 1'):
    st.write('Vous avez cliqué sur le Bouton 1')
    
if st.button('Bouton 2'):
    st.write('Vous avez cliqué sur le Bouton 2')
    
if st.button('Bouton 3'):
    st.write('Vous avez cliqué sur le Bouton 3')
