# PageOne contents 

import streamlit as st
from PIL import Image
# https://static.vecteezy.com/system/resources/previews/006/852/804/non_2x/abstract-blue-background-simple-design-for-your-website-free-vector.jpg

st.set_page_config(initial_sidebar_state="expanded")


# title = "<h1>What is Autism spectrum disorder (ASD) ?</h1>"
# st.markdown(title, unsafe_allow_html=True)






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



