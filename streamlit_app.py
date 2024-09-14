import streamlit as st

st.title("La agria")
st.write(
    "Tira una foto"
)

st.camera_input(label="Camara", key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")