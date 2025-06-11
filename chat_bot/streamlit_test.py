import streamlit as st
import pygame as pg

MODELS = ["Model_1", "Model_2", "Model_3"]
#def detectEnter():
    #while True:

def pageConfig ():

    st.set_page_config(page_title="Chat Bot", page_icon=":robot:")
    st.title("Chat Bot")
    
    usrName = st.text_input("Your name is...\t")
    def validName():
        if(usrName == ""):
            return 0
        return 1
    

    if (st.button("Saludar")):
        if validName():
            st.write("Hello {}".format(usrName))
        else:
            st.text("Err. Invalid name")
    st.sidebar.title("Models")
    selectedModel = st.sidebar.selectbox(
        "Models",
        MODELS,
        index=0,
    )
pageConfig()