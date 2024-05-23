import streamlit as st
from PIL import Image
from template import css,index

st.write(css,unsafe_allow_html=True)
st.write(index, unsafe_allow_html=True)

st.set_page_config(initial_sidebar_state="expanded")





