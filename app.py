import streamlit as st
from sklearn.cluster import KMeans
from scipy.spatial import distance
from PIL import Image
import numpy as np
import io

pal = {
    "Noir_Charbon": (0, 0, 0), "Blanc_Jade": (255, 255, 255),
    "Jaune_Or": (228, 189, 104), "Bleu_Cyan": (0, 134, 214),
    "Violet_Lila": (174, 150, 212), "Vert_Gui": (63, 142, 67),
    "Rouge_Ecarlate": (222, 67, 67), "Bleu_Marine": (0, 120, 191),
    "Orange_Mandarine": (249, 153, 99), "Vert_Galaxie": (59, 102, 94),
    "Bleu_Glacier": (163, 216, 225), "Violet_Magenta": (236, 0, 140),
    "Gris_Argent": (166, 169, 170), "Violet_Basic": (94, 67, 183),
}

def proches(c, pal):
    dists = [(n, distance.euclidean(c, col)) for n, col in pal.items()]
    return sorted(dists, key=lambda x: x[1])

def proches_lim(c, pal, n):
    return [n for n, _ in proches(c, pal)[:n]]

def process_image(image, Nc=4, Nd=3, dim_max=400):
    img = image.convert('RGB')
    img.thumbnail((dim_max, dim_max))
    img_arr = np.array(img)

    pixels = img_arr.reshape(-1, 3)
    kmeans = KMeans(n_clusters=Nc, random_state=0).fit(pixels)
    cl_centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    uniq, counts = np.unique(labels, return_counts=True)
    cl_counts = dict(zip(uniq, counts))
    total_px = pixels.shape[0]
    global sorted_cls
    sorted_cls = sorted(cl_counts.keys(), key=lambda x: cl_counts[x], reverse=True)

    cl_proches = [proches_lim(cl_centers[i], pal, Nd) for i in sorted_cls]
    initial_img_arr = np.zeros_like(img_arr)
    for i in range(img_arr.shape[0]):
        for j in range(img_arr.shape[1]):
            lbl = labels[i * img_arr.shape[1] + j]
            initial_img_arr[i, j] = cl_centers[lbl]

    initial_img = Image.fromarray(initial_img_arr.astype('uint8'))
    return initial_img

# Interface utilisateur de Streamlit
st.title("Tylice")

# Sélection du nombre de couleurs
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

# Affichage des cases de sélection de couleurs
cols = st.columns(num_selections * 2)
color_options = list(pal.keys())

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
        if selected_color_name:
            rgb = pal[selected_color_name]
            st.markdown(
                f"<div style='background-color: rgb{rgb}; width: {rectangle_width}px; height: {rectangle_width // 4}px; border-radius: 5px;'></div>",
                unsafe_allow_html=True
            )

# Sélection et traitement de l'image
uploaded_image = st.file_uploader("Télécharger une image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    
    # Appliquer le traitement KMeans pour extraire les couleurs dominantes
    processed_image = process_image(image)

    # Afficher l'image traitée
    st.image(processed_image, caption="Image traitée", use_column_width=False)
