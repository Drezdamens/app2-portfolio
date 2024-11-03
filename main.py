import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Rostyslav Gnat")
    content = """
    Hi, my name is Rostyk and i build my first site which supposed to be my first portfolio showcase. And i hope that will be not last ahaha.
    """
    st.info(content)

content2 = """
Below you can find some of the apps i have built in Python. Feel free to contact me!
"""
st.write(content2)

df = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
