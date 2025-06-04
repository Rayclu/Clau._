import streamlit as st
from groq import Groq
#MODELS = ["Model_1", "Model_2", "Model_3"]
#def detectEnter():
    #while True:
MODELS = ['llama3-8b-8192', 'llama3-70b.8192', 'mixtral-8x7b-32768']
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

def crear_usuario()-> Groq:
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(api_key=clave_secreta)

def configModel(client, model, message):
    return client.chat.completions.create(
        model = model,
        messages = [{ "role" : "user", "content" : message }],
        stream = True,
    )

def initState():
    if "messages" not in st.session_state:
        st.session_state.message = []

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

def updateHistory(rol:str, contenido:str, avatar:str):
    st.session_state.mensajes.append({
        "role" : rol, 
        "content" : contenido, 
        "avatar" : avatar
        })

def mostrar_historial():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"], avatar= mensaje["avatar"]) :
            st.markdown(mensaje["content"])

def area_chat():
    contenedor = st.container(height=200, border=True)
    with contenedor : mostrar_historial()

def generateAnswer(AnswerIa):
    compAnswer = ""
    for frase in AnswerIa:
        if(frase.choices[0].delta.content):
            compAnswer += frase[0].delta.content
            yield frase.choices[0].delta.content
    return compAnswer

grqUsr = crear_usuario()
initState()
ActualModel = pageConfig()
message = st.chat_input("¿?")

# if(message):
#     resIa = configModel(grqUsr, ActualModel, message)

#     with st.chat_message("assistant"):
#         resIa = st.write_stream(generateAnswer(resIa))
#         updateHistory("assistant", resIa, "😎")
#         st.rerun()

if message:
    updateHistory("user", message, "😎")
    respuesta_ia = configModel(grqUsr, ActualModel, message)
    
    if respuesta_ia:
        with st.chat_message("assistant"):    
            respuesta_ia = st.write_stream(generateAnswer(respuesta_ia))
            updateHistory("assistant",respuesta_ia,"🤖")
            st.rerun()
