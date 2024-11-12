import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

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
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Initialisation de la sélection du nombre de couleurs
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

# Affichage des cases de couleurs sans texte
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
        # Pas de texte pour les cases à cocher, juste des cases radio
        selected_color_name = st.radio("", color_options, key=f"radio_{i}")
        selected_colors.append(pal[selected_color_name])  # Enregistrer la couleur sélectionnée

# Ajouter l'outil de sélection d'image
uploaded_image = st.file_uploader("Télécharger une image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    
    # Redimensionner l'image à 400px dans la dimension la plus grande
    width, height = image.size
    if width > height:
        new_width = 400
        new_height = int((new_width / width) * height)
    else:
        new_height = 400
        new_width = int((new_height / height) * width)
    
    resized_image = image.resize((new_width, new_height))

    # Traitement KMeans
    img_arr = np.array(resized_image)
    pixels = img_arr.reshape(-1, 3)

    # Appliquer KMeans pour le nombre de clusters en fonction de la sélection
    kmeans = KMeans(n_clusters=num_selections, random_state=0).fit(pixels)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    # Remplacer les pixels par la couleur de leur cluster sélectionnée
    new_img_arr = np.zeros_like(img_arr)
    for i in range(img_arr.shape[0]):
        for j in range(img_arr.shape[1]):
            lbl = labels[i * img_arr.shape[1] + j]
            new_img_arr[i, j] = selected_colors[lbl]

    # Convertir l'image transformée en image PIL pour l'afficher
    new_image = Image.fromarray(new_img_arr.astype('uint8'))

    # Afficher uniquement l'image après traitement KMeans
    st.image(new_image, caption=f"Image après traitement KMeans ({num_selections} couleurs)", use_column_width=False)
