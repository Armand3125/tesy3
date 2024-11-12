import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances  # Assurez-vous d'importer correctement cette fonction

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

st.title("Tylice")

# Custom CSS for style
css = """
    <style>
        .stRadio div [data-testid="stMarkdownContainer"] p { display: none; }
        .radio-container { display: flex; flex-direction: column; align-items: center; margin: 0; }
        .color-container { display: flex; flex-direction: column; align-items: center; }
        .color-box { border: 3px solid black; }
        .stColumn { padding: 0 !important; }
        @media (max-width: 768px) {
            .stColumn { width: 100% !important; margin-bottom: 10px; }
            .radio-container { flex-direction: row; }
            .color-container { flex-direction: row; }
            .color-box { width: 40px; height: 15px; }
        }
        .center-image {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

uploaded_image = st.file_uploader("Télécharger une image", type=["jpg", "jpeg", "png"])

if "num_selections" not in st.session_state:
    st.session_state.num_selections = 4

col1, col2 = st.columns([1, 5])

with col1:
    if st.button("4 Couleurs"):
        st.session_state.num_selections = 4

with col2:
    if st.button("6 Couleurs"):
        st.session_state.num_selections = 6

num_selections = st.session_state.num_selections
rectangle_width = 80 if num_selections == 4 else 50
rectangle_height = 20
cols = st.columns(num_selections * 2)
color_options = list(pal.keys())

selected_colors = []
for i in range(num_selections):
    with cols[i * 2]:
        st.markdown("<div class='color-container'>", unsafe_allow_html=True)
        for idx, (color_name, color_rgb) in enumerate(pal.items()):
            margin_top = "15px" if idx == 0 else "0px"
            st.markdown(
                f"<div class='color-box' style='background-color: rgb{color_rgb}; width: {rectangle_width}px; height: {rectangle_height}px; border-radius: 5px; margin-bottom: 4px; margin-top: {margin_top};'></div>",
                unsafe_allow_html=True
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with cols[i * 2 + 1]:
        selected_color_name = st.radio("", color_options, key=f"radio_{i}")
        selected_colors.append(pal[selected_color_name])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    width, height = image.size
    new_width = 400 if width > height else int((400 / height) * width)
    new_height = 400 if width <= height else int((400 / width) * height)
    resized_image = image.resize((new_width, new_height))

    img_arr = np.array(resized_image)
    pixels = img_arr.reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_selections, random_state=0).fit(pixels)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    new_img_arr = np.zeros_like(img_arr)
    for i in range(img_arr.shape[0]):
        for j in range(img_arr.shape[1]):
            lbl = labels[i * img_arr.shape[1] + j]
            new_img_arr[i, j] = selected_colors[lbl]

    new_image = Image.fromarray(new_img_arr.astype('uint8'))
    resized_image = new_image.resize((int(new_width * 1.3), int(new_height * 1.3)))

    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.image(resized_image, caption=f"Image après traitement KMeans agrandie ({num_selections} couleurs)", use_column_width=True)

    centers_rgb = np.array(centers, dtype=int)
    pal_rgb = np.array(list(pal.values()), dtype=int)

    distances = pairwise_distances(centers_rgb, pal_rgb)  # Utilisation correcte de pairwise_distances

    st.subheader("Couleurs les plus proches des centres des clusters")
    color_cols = st.columns(num_selections)

    # Trie des couleurs pour chaque cluster en fonction de leur proximité
    ordered_colors_by_cluster = []
    for i in range(num_selections):
        # Trie les couleurs en fonction de leur proximité avec chaque centre de cluster
        closest_colors_idx = distances[i].argsort()  # Tri des indices
        ordered_colors_by_cluster.append([list(pal.keys())[idx] for idx in closest_colors_idx])

    # Affichage des couleurs triées pour chaque cluster
    for i in range(num_selections):
        with color_cols[i]:
            st.write(f"Cluster {i+1}:")
            for color_name in ordered_colors_by_cluster[i]:
                color_rgb = pal[color_name]
                st.markdown(f"<div class='color-box' style='background-color: rgb{color_rgb}; width: {rectangle_width}px; height: {rectangle_height}px; border-radius: 5px;'></div>", unsafe_allow_html=True)
                st.text(color_name)
