# Réorganisation des couleurs par proximité aux centres des clusters
ordered_colors_by_cluster = []
for i in range(num_selections):
    # Tri des couleurs par proximité avec le centre du cluster
    closest_colors_idx = distances[i].argsort()  # Tri des indices
    ordered_colors_by_cluster.append([list(pal.keys())[idx] for idx in closest_colors_idx])

# Affichage des cases à cocher avec les couleurs triées
selected_colors = []
for i in range(num_selections):
    with cols[i * 2]:
        st.markdown("<div class='color-container'>", unsafe_allow_html=True)

        # Utiliser l'ordre des couleurs les plus proches de chaque cluster
        for idx in ordered_colors_by_cluster[i]:
            color_rgb = pal[idx]
            st.markdown(
                f"<div class='color-box' style='background-color: rgb{color_rgb}; width: {rectangle_width}px; height: {rectangle_height}px; border-radius: 5px; margin-bottom: 4px;'></div>",
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

    with cols[i * 2 + 1]:
        # Afficher les couleurs triées par ordre de proximité pour chaque cluster
        # Créer une clé unique avec l'index i et l'index de la couleur
        for j, color_name in enumerate(ordered_colors_by_cluster[i]):
            selected_color_name = st.radio("", ordered_colors_by_cluster[i], key=f"radio_{i}_{j}")
            selected_colors.append(pal[selected_color_name])
