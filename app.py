import streamlit as st

# Titre de l'application
st.title('Exemple avec trois boutons et trois zones de couleur')

# Créer 3 colonnes pour aligner les boutons
col1, col2, col3 = st.columns(3)

# Boutons et zones de couleur dans chaque colonne
with col1:
    if st.button('Bouton 1'):
        st.write('Vous avez cliqué sur le Bouton 1')
        st.markdown('<div style="height:100px;background-color:red;"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="height:100px;"></div>', unsafe_allow_html=True)

with col2:
    if st.button('Bouton 2'):
        st.write('Vous avez cliqué sur le Bouton 2')
        st.markdown('<div style="height:100px;background-color:blue;"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="height:100px;"></div>', unsafe_allow_html=True)

with col3:
    if st.button('Bouton 3'):
        st.write('Vous avez cliqué sur le Bouton 3')
        st.markdown('<div style="height:100px;background-color:green;"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="height:100px;"></div>', unsafe_allow_html=True)
