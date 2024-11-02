import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Rostyslav Gnat")
    content = """
    Hi, my name is Rostyk and i build my first site which supposed to be my first portfolio showcase. And i hope that will be not last ahaha.
    """
    st.info(content)