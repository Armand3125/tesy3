import streamlit as st

# Define CSS for buttons
button_style = """
<style>
    .button-red {
        background-color: #e74c3c; /* Red */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }

    .button-green {
        background-color: #2ecc71; /* Green */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }

    .button-blue {
        background-color: #3498db; /* Blue */
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
    }

    .button-red:hover, .button-green:hover, .button-blue:hover {
        opacity: 0.8;
    }
</style>
"""

# Inject the CSS
st.markdown(button_style, unsafe_allow_html=True)

# Create buttons using the custom classes
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Red', key='red'):
        st.session_state.selected_button = "Red"

with col2:
    if st.button('Green', key='green'):
        st.session_state.selected_button = "Green"

with col3:
    if st.button('Blue', key='blue'):
        st.session_state.selected_button = "Blue"

# Display which button was clicked
if 'selected_button' in st.session_state:
    st.write(f"You selected the {st.session_state.selected_button} button!")
