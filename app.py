import streamlit as st
from sklearn.cluster import KMeans
from scipy.spatial import distance
from PIL import Image
import numpy as np

# Palette de couleurs définie
pal = {
    "Noir_Charbon": (0, 0, 0), "Blanc_Jade": (255, 255, 255),
    "Jaune_Or": (228, 189, 104), "Bleu_Cyan": (0, 134, 214),
    "Violet_Lila": (174, 150, 212), "Vert_Gui": (63, 142, 67),
    "Rouge_Ecarlate": (222, 67, 67), "Bleu_Marine": (0, 120, 191),
    "Orange_Mandarine": (249, 153, 99), "Vert_Galaxie": (59, 102, 94),
    "Bleu_Glacier": (163, 216, 225), "Violet_Magenta": (236, 0, 140),
    "Gris_Argent": (166, 169, 170), "Violet_Basic": (94, 67, 183),
}

# Calculer les couleurs les plus proches
def proches(c, pal):
    dists = [(n, distance.euclidean(c, col)) for n, col in pal.items()]
    return sorted(dists, key=lambda x: x[1])

def proches_lim(c, pal, n):
    return [n for n, _ in proches(c, pal)[:n]]

# Créer une nouvelle image en mappant les clusters aux couleurs de la palette
def nouvelle_img(img_arr, labels, cl_proches, selected_colors, pal):
    color_map = {i: pal[cl_proches[i][selected_colors[i]]] for i in range(len(cl_proches))}
    img_mapped = np.array([color_map[label] for label in labels])
    return img_mapped.reshape(img_arr.shape)

# Traiter l'image pour clustering et application de la palette
def traiter_img(img, Nc, Nd, dim_max):
    try:
        img = Image.open(img).convert('RGB')
        img.thumbnail((dim_max, dim_max))
        img_arr = np.array(img)

        pixels = img_arr.reshape(-1, 3)
        kmeans = KMeans(n_clusters=Nc, random_state=0).fit(pixels)
        labels = kmeans.labels_

        uniq, counts = np.unique(labels, return_counts=True)
        total_px = pixels.shape[0]
        cl_counts = dict(zip(uniq, counts))

        sorted_cls = sorted(cl_counts.items(), key=lambda x: x[1], reverse=True)
        cl_proches = [proches_lim(kmeans.cluster_centers_[i], pal, Nd) for i in cl_counts.keys()]

        if 'selected_colors' not in st.session_state:
            st.session_state.selected_colors = [0] * Nc
        elif len(st.session_state.selected_colors) != Nc:
            st.session_state.selected_colors = [0] * Nc

        new_img_arr = nouvelle_img(img_arr, labels, cl_proches, st.session_state.selected_colors, pal)
        st.session_state.modified_image = new_img_arr.astype('uint8')

        for idx, (cl, count) in enumerate(sorted_cls):
            percentage = (count / total_px) * 100
            st.write(f"Cluster {idx + 1} - {percentage:.2f}%")
            col_options = cl_proches[cl]
            cols = st.columns(len(col_options))

            # Afficher les cases à cocher pour chaque couleur dans la palette
            for j, color in enumerate(col_options):
                rgb = pal[color]
                rgb_str = f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})"
                
                # Affichage des cases à cocher pour chaque couleur
                checkbox_key = f'checkbox_{idx}_{j}_{color}'
                if cols[j].checkbox(label=color, key=checkbox_key, value=(st.session_state.selected_colors[cl] == j)):
                    st.session_state.selected_colors[cl] = j
                    new_img_arr = nouvelle_img(img_arr, labels, cl_proches, st.session_state.selected_colors, pal)
                    st.session_state.modified_image = new_img_arr.astype('uint8')

    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")

# Interface Streamlit
st.title("Tylice")
uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])
Nc = st.slider("Nombre de Clusters", 2, 7, 4)
Nd = 14  # Fixer le nombre de couleurs de la palette à 14

# Fixer la dimension maximale de l'image à 400
dim_max = 400  

if uploaded_file is not None:
    traiter_img(uploaded_file, Nc, Nd, dim_max)

if 'modified_image' in st.session_state:
    st.image(st.session_state.modified_image, caption="Image Modifiée", width=int(1.5 * dim_max))import streamlit as st

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

st.title("Sélection de Couleurs par Cluster")

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

# Barre de sélection pour choisir le nombre de clusters (entre 2 et 7)
num_clusters = st.slider("Nombre de clusters de couleur", min_value=2, max_value=7, value=4)

# Créer les colonnes en fonction du nombre de clusters
cols = st.columns(num_clusters) 

# Options de couleurs disponibles
color_options = list(pal.keys())

# Afficher les sélecteurs de couleurs et les rectangles correspondants pour chaque cluster
for i in range(num_clusters):
    # Colonne pour afficher le sélecteur de couleurs pour chaque cluster
    with cols[i]:
        st.markdown(f"<div class='color-container'>", unsafe_allow_html=True)
        
        # Afficher toutes les couleurs disponibles sous forme de rectangles
        for idx, (color_name, color_rgb) in enumerate(pal.items()):
            if idx == 0:  # Ajouter un décalage pour le premier rectangle
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

        # Sélecteur de couleur spécifique à chaque cluster avec un bouton radio
        selected_color_name = st.radio(f"Choix de couleur pour Cluster {i + 1}", color_options, key=f"cluster_{i}")
        
        # Afficher la couleur sélectionnée sous forme de rectangle
        if selected_color_name:
            rgb = pal[selected_color_name]
            st.markdown(
                f"<div style='background-color: rgb{rgb}; width: 50px; height: 50px; border-radius: 5px; margin-top: 10px;'></div>",
                unsafe_allow_html=True
            )
