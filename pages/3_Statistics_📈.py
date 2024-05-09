# Pagetwo contents 

import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://img.freepik.com/free-vector/gradient-abstract-background_23-2149123400.jpg?w=1060&t=st=1715263555~exp=1715264155~hmac=bccde9bc6a1fc8671e1fcee7f6e445872539c584689bf83e044f45ec263ca71c");
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


