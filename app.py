for palette in combined_palettes:
    num_clusters = len(palette)
    palette_colors = [pal[color] for color in palette]

    # Processus d'image pour chaque palette
    resized_image, img_arr, labels, sorted_indices, new_width, new_height = process_image(image, num_clusters=num_clusters)

    recolored_image = recolor_image(img_arr, labels, sorted_indices, palette_colors)

    # Convert recolored image to buffer for upload
    img_buffer = io.BytesIO()
    recolored_image.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    # Upload to Cloudinary
    cloudinary_url = upload_to_cloudinary(img_buffer)

    # Generate Shopify cart URL if upload is successful
    if cloudinary_url:
        shopify_cart_url = generate_shopify_cart_url(cloudinary_url, num_colors=num_clusters)
        add_to_cart_button = f"<a href='{shopify_cart_url}' class='shopify-link' target='_blank'>Ajouter au panier</a>"
    else:
        shopify_cart_url = None
        add_to_cart_button = "Erreur lors de l'ajout au panier."

    with cols_display[col_count % 2]:
        st.image(recolored_image, use_container_width=True, width=350)
        if cloudinary_url:
            # Centrer le bouton "Ajouter au panier" sous l'image
            st.markdown(f"<div class='add-to-cart-button'>{add_to_cart_button}</div>", unsafe_allow_html=True)
        else:
            st.error("Erreur lors de l'upload de l'image.")

    col_count += 1

    # Ajouter un espace après chaque paire d'images
    if col_count % 2 == 0:
        st.markdown("<br>", unsafe_allow_html=True)
