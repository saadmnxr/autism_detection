import streamlit as st
from PIL import Image
from template import css,index

st.write(css,unsafe_allow_html=True)
st.write(index, unsafe_allow_html=True)


img = Image.open("fotu.png")
st.image(img,caption='signs',width = 700)

# st.video(data)