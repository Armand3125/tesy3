import streamlit as st

# Palette de couleurs
pal = {
    "NC": (0, 0, 0), "BJ": (255, 255, 255),
    "JO": (228, 189, 104), "BC": (0, 134, 214),
    "VL": (174, 150, 212), "VG": (63, 142, 67),
    "RE": (222, 67, 67), "BM": (0, 120, 191),
    "OM": (249, 153, 99), "VGa": (59, 102, 94),
    "BG": (163, 216, 225), "VM": (236, 0, 140),
    "GA": (166, 169, 170), "VB": (94, 67, 183),
}

st.title("Sélection de Couleurs")

# CSS pour masquer les labels et ajuster l'apparence des cases
css = """
    <style>
        /* Cacher les textes des boutons radio */
        .stRadio div [data-testid="stMarkdownContainer"] p {
            display: none;
        }
        .radio-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 0;  /* Supprimer les marges entre les éléments */
        }
        .color-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .first-color-box {
            margin-top: 30px;  /* Décalage de 30px pour le premier rectangle */
        }
        /* Ajout de la bordure noire autour des rectangles */
        .color-box {
            border: 3px solid black;  /* Bordure noire */
        }
        /* Réduire les marges entre les colonnes */
        .stColumn {
            padding: 0 !important;  /* Retirer le padding par défaut */
        }
        /* Ajustement de la mise en page pour les écrans plus petits */
        @media (max-width: 768px) {
            .stColumn {
                width: 100% !important;  /* Occupe toute la largeur disponible */
                margin-bottom: 10px;  /* Ajoute un petit espace entre les éléments */
            }
            .radio-container {
                flex-direction: row;  /* Aligner les boutons radio horizontalement */
            }
            .color-container {
                flex-direction: row;  /* Afficher les couleurs en ligne sur petits écrans */
            }
            .color-box {
                width: 40px;  /* Ajuster la taille des cases de couleur sur mobile */
                height: 15px; 
            }
            .first-color-box {
                margin-top: 0px;  /* Enlever le décalage pour les petits écrans */
            }
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Afficher les boutons "4 Couleurs" et "6 Couleurs" sur la même ligne
col1, col2 = st.columns(2)

# Bouton pour 4 couleurs
with col1:
    if st.button("4 Couleurs"):
        num_selections = 4
    else:
        num_selections = 4  # Par défaut 4 couleurs sélectionnées

# Bouton pour 6 couleurs
with col2:
    if st.button("6 Couleurs"):
        num_selections = 6
    else:
        num_selections = num_selections  # Garde la sélection précédente si le bouton 6 couleurs n'est pas pressé

# Calculer la largeur des rectangles en fonction du nombre de colonnes
if num_selections == 4:
    rectangle_width = 100  # Largeur des rectangles pour 4 couleurs
elif num_selections == 6:
    rectangle_width = 70  # Largeur des rectangles pour 6 couleurs
else:
    rectangle_width = 100  # Par défaut (au cas où il y a plus de 6 colonnes)

rectangle_height = 20  # Garder la hauteur constante

# Créer les colonnes en fonction de la sélection du bouton
cols = st.columns(num_selections * 2)  # On double le nombre pour inclure les couleurs

# Options de couleurs disponibles
color_options = list(pal.keys())

# Afficher les sélecteurs de couleurs et les rectangles correspondants
for i in range(num_selections):
    # Colonne pour afficher les rectangles de toutes les couleurs
    with cols[i * 2]:
        st.markdown("<div class='color-container'>", unsafe_allow_html=True)
        
        # Décalage du premier rectangle de couleur de 30px
        for idx, (color_name, color_rgb) in enumerate(pal.items()):
            if idx == 0:  # Pour le premier rectangle, ajouter le décalage
                st.markdown(
                    f"<div class='first-color-box color-box' style='background-color: rgb{color_rgb}; width: {rectangle_width}px; height: {rectangle_height}px; border-radius: 5px; margin-bottom: 4px;'></div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<div class='color-box' style='background-color: rgb{color_rgb}; width: {rectangle_width}px; height: {rectangle_height}px; border-radius: 5px; margin-bottom: 4px;'></div>",
                    unsafe_allow_html=True
                )
        st.markdown("</div>", unsafe_allow_html=True)

    # Colonne pour le bouton radio de sélection de couleur sans texte
    with cols[i * 2 + 1]:
        with st.container():
            st.markdown("<div class='radio-container'>", unsafe_allow_html=True)
            selected_color_name = st.radio("", color_options, key=f"radio_{i}")
            if selected_color_name:
                rgb = pal[selected_color_name]
                st.markdown(
                    f"<div style='background-color: rgb{rgb}; width: {rectangle_width}px; height: {rectangle_width // 4}px; border-radius: 5px;'></div>",
                    unsafe_allow_html=True
                )
            st.markdown("</div>", unsafe_allow_html=True)
