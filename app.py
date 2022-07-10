
from translate import Translator
import streamlit as st
st.set_page_config(page_title='Nik Translator', page_icon=":earth_asia:")
st.title("Text Translator ❤")
st.subheader("Type your text here ")
text=st.text_input("Write here")
lan1=st.selectbox("Select Language from",["English","Spanish","French","German","Japanese","Latin"])
lan2=st.selectbox("Translate to ",["Spanish","German","French","Latin","Japanese","English"])

translator=  Translator(from_lang=lan1.lower(),to_lang=lan2.lower())
translation = translator.translate(text)
page_bg_img = '''
 <style>
    .stApp,.e8zbici2 {
    background-image: url("https://images-na.ssl-images-amazon.com/images/I/61+oIVFF7FL.png");
    background-size: cover;
    }
    </style>
    '''

st.markdown(page_bg_img, unsafe_allow_html=True)

if(st.button("TRANSLATE")): 
    st.header(' ')
    st.header(translation)
