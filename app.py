from googletrans import Translator
import streamlit as st
st.set_page_config(page_title='Nik Translator', page_icon=":earth_asia:")
st.title("Text Translator ❤")
st.subheader("Type your text here ")
sent=st.text_input("Write here")
lan1=st.selectbox("Select Language from",["English","Hindi","Spanish","French","German","Japanese"])
lan2=st.selectbox("Translate to ",["English","Hindi","Spanish","French","German","Japanese"])

translator=  Translator()
translation = translator.translate(sent,dest=lan2.lower()[0:2],src=lan1.lower()[0:2])
page_bg_img = '''
 <style>
    .stApp {
    background-image: url("https://images-na.ssl-images-amazon.com/images/I/61+oIVFF7FL.png");
    background-size: cover;
    }
    </style>
    '''

st.markdown(page_bg_img, unsafe_allow_html=True)

if(st.button("TRANSLATE")): 
    st.header(' ')
    st.header(translation.text)
