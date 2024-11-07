import streamlit as st

# Access the primary color from the Streamlit theme
primary_color = st.get_option("theme.primaryColor")

# Define the CSS to style the button with the primary color
button_style = f"""
<style>
div.stButton > button:first-child {{
    background-color: {primary_color};
    color: white;
    font-size: 20px;
    height: 3em;
    width: 15em;
    border-radius: 10px;
}}
div.stButton > button:hover {{
    background-color: {primary_color};
    color: white;
}}
</style>
"""

# Inject the custom CSS into the Streamlit app
st.markdown(button_style, unsafe_allow_html=True)

# Create a button and handle its behavior
if st.button("Click here"):
    st.write("Great!")
