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

def nouvelle_img(img_arr, labels, cl, idx, pal):
    new_img_arr = np.zeros_like(img_arr)
    for i in range(img_arr.shape[0]):
        for j in range(img_arr.shape[1]):
            lbl = labels[i * img_arr.shape[1] + j]
            cl_idx = np.where(sorted_cls == lbl)[0][0]
            color_idx = idx[cl_idx]
            new_img_arr[i, j] = pal[cl[cl_idx][color_idx]]
    return new_img_arr

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

st.title("Tylice - Traitement d'Image")

uploaded_image = st.file_uploader("Télécharger une image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    
    # Appliquer le traitement KMeans
    processed_image = process_image(image)

    # Afficher l'image traitée
    st.image(processed_image, caption="Image traitée", use_column_width=False)
