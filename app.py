import streamlit as st
from sklearn.cluster import KMeans
from scipy.spatial import distance
from PIL import Image
import numpy as np

# Palette de couleurs définie
pal = {
    "NC": (0, 0, 0), "BJ": (255, 255, 255),
    "JO": (228, 189, 104), "BC": (0, 134, 214),
    "VL": (174, 150, 212), "VG": (63, 142, 67),
    "RE": (222, 67, 67), "BM": (0, 120, 191),
    "OM": (249, 153, 99), "VGa": (59, 102, 94),
    "BG": (163, 216, 225), "VM": (236, 0, 140),
    "GA": (166, 169, 170), "VB": (94, 67, 183),
}

# Fonction pour calculer les couleurs les plus proches de la palette
def proches(c, pal):
    dists = [(n, distance.euclidean(c, col)) for n, col in pal.items()]
    return sorted(dists, key=lambda x: x[1])

def proches_lim(c, pal, n):
    return [n for n, _ in proches(c, pal)[:n]]

# Fonction pour créer une nouvelle image avec les couleurs mappées
def nouvelle_img(img_arr, labels, cl_proches, selected_colors, pal):
    color_map = {i: pal[cl_proches[i][selected_colors[i]]] for i in range(len(cl_proches))}
    img_mapped = np.array([color_map[label] for label in labels])
    return img_mapped.reshape(img_arr.shape)

# Fonction pour traiter l'image et appliquer le clustering
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

        # Initialisation des couleurs sélectionnées
        if 'selected_colors' not in st.session_state:
            st.session_state.selected_colors = [0] * Nc
        elif len(st.session_state.selected_colors) != Nc:
            st.session_state.selected_colors = [0] * Nc

        new_img_arr = nouvelle_img(img_arr, labels, cl_proches, st.session_state.selected_colors, pal)
        st.session_state.modified_image = new_img_arr.astype('uint8')

        # Affichage des clusters et des cases à cocher pour la sélection de couleur
        for idx, (cl, count) in enumerate(sorted_cls):
            percentage = (count / total_px) * 100
            st.write(f"Cluster {idx + 1} - {percentage:.2f}%")
            col_options = cl_proches[cl]

            # Pour chaque couleur possible dans ce cluster, afficher une case à cocher
            selected_colors = st.session_state.selected_colors
            for j, color in enumerate(col_options):
                rgb = pal[color]
                rgb_str = f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})"
                
                # Affichage de la case à cocher pour chaque couleur du cluster
                color_label = f"Cluster {idx+1} - Couleur {j+1}: {color}"
                if st.checkbox(color_label, key=f"checkbox_{idx}_{j}"):
                    selected_colors[idx] = j  # L'utilisateur choisit la couleur à appliquer
                    new_img_arr = nouvelle_img(img_arr, labels, cl_proches, selected_colors, pal)
                    st.session_state.modified_image = new_img_arr.astype('uint8')

    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")

# Interface Streamlit
st.title("Sélection de Couleurs et Clustering d'Image")
uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])
Nc = st.slider("Nombre de Clusters", 2, 7, 4)
Nd = st.slider("Nombre de Couleurs dans la Palette", 2, len(pal), 6)

# Fixer la dimension maximale de l'image à 400
dim_max = 400  

if uploaded_file is not None:
    traiter_img(uploaded_file, Nc, Nd, dim_max)

# Affichage des couleurs sous forme de cases à cocher
st.title("Sélection de Couleurs")
css = """
    <style>
        .stCheckbox {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .color-box {
            border: 3px solid black;
            margin-bottom: 5px;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Affichage des couleurs sous forme de cases à cocher
num_selections = st.slider("Nombre de sélections de couleur", min_value=2, max_value=7, value=4)
cols = st.columns(num_selections)

# Affichage des couleurs sous forme de cases à cocher
for i in range(num_selections):
    with cols[i]:
        for idx, (color_name, color_rgb) in enumerate(pal.items()):
            rgb_str = f"rgb({color_rgb[0]}, {color_rgb[1]}, {color_rgb[2]})"
            color_label = f"{color_name}: {rgb_str}"

            # Affichage d'une case à cocher pour chaque couleur
            if st.checkbox(color_label, key=f"checkbox_{color_name}"):
                st.session_state.selected_colors.append(color_name)
                st.markdown(
                    f"<div class='color-box' style='background-color: {rgb_str}; width: 50px; height: 20px; border-radius: 5px;'></div>",
                    unsafe_allow_html=True
                )
