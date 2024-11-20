if uploaded_image is not None:
    # Chargement et redimensionnement de l'image
    image = Image.open(uploaded_image).convert("RGB")
    width, height = image.size
    if width > height:
        new_width = 400
        new_height = int((new_width / width) * height)
    else:
        new_height = 400
        new_width = int((new_height / height) * width)

    resized_image = image.resize((new_width, new_height))
    img_arr = np.array(resized_image)

    if img_arr.shape[-1] == 3:  # Assurez-vous que l'image est RGB
        pixels = img_arr.reshape(-1, 3)

        # KMeans pour trouver les clusters de couleurs
        kmeans = KMeans(n_clusters=num_selections, random_state=0).fit(pixels)
        labels = kmeans.labels_
        centers = kmeans.cluster_centers_

        centers_rgb = np.array(centers, dtype=int)
        pal_rgb = np.array(list(pal.values()), dtype=int)
        distances = np.linalg.norm(centers_rgb[:, None] - pal_rgb[None, :], axis=2)

        ordered_colors_by_cluster = []
        for i in range(num_selections):
            closest_colors_idx = distances[i].argsort()
            ordered_colors_by_cluster.append([list(pal.keys())[idx] for idx in closest_colors_idx])

        # Calcul des pourcentages de présence des clusters
        cluster_counts = np.bincount(labels)
        total_pixels = len(labels)
        cluster_percentages = (cluster_counts / total_pixels) * 100

        # Trier les clusters par pourcentage décroissant
        sorted_indices = np.argsort(-cluster_percentages)  # Indices triés du plus grand au plus petit
        sorted_percentages = cluster_percentages[sorted_indices]
        sorted_ordered_colors_by_cluster = [ordered_colors_by_cluster[i] for i in sorted_indices]

        # Affichage des pourcentages dans des colonnes distinctes
        for i, percentage in enumerate(sorted_percentages):
            with cols_percentages[i]:
                st.markdown(f"<div class='percentage-container'><b>{percentage:.2f}%</b></div>", unsafe_allow_html=True)

        selected_colors = []
        for i, cluster_index in enumerate(sorted_indices):
            with cols[i * 2]:
                st.markdown("<div class='color-container'>", unsafe_allow_html=True)
                for j, color_name in enumerate(sorted_ordered_colors_by_cluster[i]):
                    color_rgb = pal[color_name]
                    margin_class = "first-box" if j == 0 else ""
                    st.markdown(
                        f"<div class='color-box {margin_class}' style='background-color: rgb{color_rgb}; width: {rectangle_width}px; height: {rectangle_height}px; border-radius: 5px; margin-bottom: 4px;'></div>",
                        unsafe_allow_html=True
                    )
                st.markdown("</div>", unsafe_allow_html=True)

            with cols[i * 2 + 1]:
                selected_color_name = st.radio("", sorted_ordered_colors_by_cluster[i], key=f"radio_{i}", label_visibility="hidden")
                selected_colors.append(pal[selected_color_name])

        # Nouvelle image recolorisée
        new_img_arr = np.zeros_like(img_arr)
        for i in range(img_arr.shape[0]):
            for j in range(img_arr.shape[1]):
                lbl = labels[i * img_arr.shape[1] + j]
                new_color_index = np.where(sorted_indices == lbl)[0][0]  # Mapper l'ancien index au nouveau trié
                new_img_arr[i, j] = selected_colors[new_color_index]

        new_image = Image.fromarray(new_img_arr.astype('uint8'))
        width, height = new_image.size
        resized_image = new_image.resize((int(width * 1.1), int(height * 1.1)))

        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            st.image(resized_image, caption=f"Image avec {num_selections} couleurs", use_column_width=True)
    else:
        st.error("L'image doit être en RGB (3 canaux) pour continuer.")
