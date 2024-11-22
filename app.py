import streamlit as st

# Load the HTML content from the file
with open("index.html", "r") as f:
    html_string = f.read()

# Display the HTML in Streamlit
st.components.v1.html(html_string, height=600)
