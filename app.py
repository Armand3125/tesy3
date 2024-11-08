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
            margin-top: 0px;
            margin-bottom: 15px;  /* Augmenter l'écart entre les cases à cocher */
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
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Barre de sélection pour choisir le nombre de colonnes (entre 2 et 7)
num_selections = st.slider("Nombre de sélections de couleur", min_value=2, max_value=7, value=4)

# Créer les colonnes en fonction de la sélection du slider
cols = st.columns(num_selections * 2)  # On double le nombre pour inclure les couleurs

# Options de couleurs disponibles
color_options = list(pal.keys())

# Sélection des couleurs
selected_colors = {}

# Afficher les sélecteurs de couleurs et les rectangles correspondants
for i in range(num_selections):
    # Colonne pour afficher les rectangles de toutes les couleurs
    with cols[i * 2]:
        st.markdown("<div class='color-container'>", unsafe_allow_html=True)
        
        # Décalage du premier rectangle de couleur de 30px
        for idx, (color_name, color_rgb) in enumerate(pal.items()):
            if idx == 0:  # Pour le premier rectangle, ajouter le décalage
                st.markdown(
                    f"<div class='first-color-box color-box' style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<div class='color-box' style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
                    unsafe_allow_html=True
                )
        st.markdown("</div>", unsafe_allow_html=True)

    # Colonne pour sélectionner une couleur avec un bouton
    with cols[i * 2 + 1]:
        with st.container():
            st.markdown("<div class='radio-container'>", unsafe_allow_html=True)
            
            # Affichage des couleurs sous forme de rectangles
            for color_name in color_options:
                color_rgb = pal[color_name]
                rgb_str = f"rgb({color_rgb[0]}, {color_rgb[1]}, {color_rgb[2]})"

                # Afficher un rectangle de couleur cliquable
                button_key = f'button_{i}_{color_name}'
                if st.button(label="", key=button_key, help=color_name):
                    selected_colors[i] = color_name  # Enregistrer la couleur sélectionnée
                    
            st.markdown("</div>", unsafe_allow_html=True)

# Afficher les couleurs sélectionnées
if selected_colors:
    st.write("Couleurs sélectionnées pour chaque cluster :")
    for cluster, color_name in selected_colors.items():
        st.write(f"Cluster {cluster + 1}: {color_name} ({pal[color_name]})")
