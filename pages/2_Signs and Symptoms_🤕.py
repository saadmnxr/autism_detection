# PageOne contents 

import streamlit as st
from PIL import Image
# https://static.vecteezy.com/system/resources/previews/006/852/804/non_2x/abstract-blue-background-simple-design-for-your-website-free-vector.jpg


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
</style>
"""

st.markdown(page_bg_img,unsafe_allow_html=True)

st.title("Signs and Symptoms of ASD")
st.subheader("Signs of Asperger's syndrome")

image = Image.open('asp.jpg')
st.image(image,caption='Signs Of Autism',width = 800)


st.subheader("Signs of Rett syndrome")

image = Image.open('rett.jpg')
st.image(image,caption='signs',width = 400)

st.subheader("Some general signs")

image = Image.open('sign3.jpg')
st.image(image,caption='Signs',width = 800)

image = Image.open('signs2.jpg')
st.image(image,caption='Signs',width = 800)

image = Image.open('sign.jpg')
st.image(image,caption='Signs',width = 800)



