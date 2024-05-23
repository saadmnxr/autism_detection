# Pagetwo contents 

import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(initial_sidebar_state="expanded")




page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://img.freepik.com/premium-photo/bright-puzzles-kids-white_23-2147689859.jpg?w=1060");
}


[data-testid="stHeader"] {
background-color : rgba(0,0,0,0.4);
}

[data-testid="stVerticalBlock"]{
background-color : rgba(0,0,0,0.5);
border-radius: 13px;
box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
padding-right : 53em;
padding-left : 3em;
backdrop-filter: blur(10px);
-webkit-backdrop-filter: blur(4px);
}

[data-testid="stSidebar"]{
background-color : rgba(0,0,0,0.6);
border-radius: 13px;
box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
backdrop-filter: blur(10px);
-webkit-backdrop-filter: blur(4px);
}

[data-testid="stForm"]{
background-color : rgb(0,0,0);
}

st.title {
background-color : rgb(244,233,44);
}

</style>
"""

st.markdown(page_bg_img,unsafe_allow_html=True)

new_title = '<p style="font-size: 49px;">Some Statistics about Autism</p>'
st.markdown(new_title, unsafe_allow_html=True)

new_title = '<p style="font-size: 35px;">Autism Statistics 2023</p>'
st.markdown(new_title, unsafe_allow_html=True)

image = Image.open('chart3.jpg')
st.image(image,caption='Autism Statistics 2023',width = 800)



new_title = '<p style="font-size: 35px;">Rising prevelance</p>'
st.markdown(new_title, unsafe_allow_html=True)
image = Image.open('chart.jpeg')
st.image(image,caption='Rising prevelance',width = 800)



new_title = '<p style="font-size: 35px;">Key Autism Statistics</p>'
st.markdown(new_title, unsafe_allow_html=True)
image = Image.open('chart2.jpg')
st.image(image,caption='Key Autism Statistics',width = 800)

new_title = '<p style="font-size: 35px;"> Autism Diagnosis by Every Year</p>'
st.markdown(new_title, unsafe_allow_html=True)
image = Image.open('us2.jpg')
st.image(image,caption='Autism Diagnosis by Every Year',width = 600)


