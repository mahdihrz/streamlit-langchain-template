import streamlit as st

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Setup variables
# os.environ['LANGCHAIN_TRACING_V2'] = st.secrets["openai_api_key"]["tracing"]
#-----------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------
st.set_page_config(
    page_title="Langchain-demo",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': 'http://34.120.236.56',
        'About': open("README.md", "r").read()
    }
)


## Pages

def about_demo():
    import streamlit as st
    st.markdown(open("README.md", "r").read())
    st.stop()


def work_page():
    import streamlit as st
    st.title("Streamlit & Langchain template 📝")
    st.caption("Using the power of LLMs")
    systemMessageQuestion = st.text_area("SystemMessage", value ="You are a helpful python, langchain and openai programmer.")
    humanMessageQuestion = st.text_area("HumanMessage", value ="Suggest some basic ideas of usage of langchain and openai and generate their code.")

    if 'openai_api_key' not in st.session_state:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    if not systemMessageQuestion:
        st.info("Please enter a SystemMessage to continue ...")
    if not humanMessageQuestion:
        st.info("Please enter a MessageQuestion to continue ...")        
    elif st.button("🚄 Perform Request"):
        # Do what to do
        st.info("Performing")
        chat = ChatOpenAI(temperature=st.session_state["temperature"], model_name=st.session_state['model_to_use'], openai_api_key=st.session_state["openai_api_key"])

        messages = [
                    SystemMessage(
                        content=systemMessageQuestion
                    ),
                    HumanMessage(
                        content=humanMessageQuestion
                    ),
                ]

        # Add a message and get a response
        response=chat(messages)

        st.markdown(response.content)
    st.stop()


### Main Code
    
with st.sidebar:
    st.title("Getting started")

    if ("openai_api_key" not in st.secrets or
        "openai_api_key" in st.secrets and
        st.secrets["openai_api_key"] == "your key here"):
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        if openai_api_key and 'openai_api_key' not in st.session_state:
            st.session_state['openai_api_key'] = openai_api_key
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    else:
        st.session_state['openai_api_key'] = st.secrets["openai_api_key"]

    st.divider()

    options = st.container()
    options.title("Options ⚙️")

    model_to_use = options.selectbox("Select model", ["gpt-3.5-turbo-16k", "gpt-3.5-turbo-1106", "gpt-4-32k-0613", "gpt-4-1106-preview"], index=1)
    st.session_state['model_to_use'] = model_to_use
    temperature = options.slider('Model Temperature?',min_value=0.0,     max_value=1.0,     step=0.1,     value=0.7)
    st.session_state['temperature'] = temperature
    st.divider()

    ## -------- Pages  ----------
    page_names_to_funcs = {
        "Work": work_page,
        "About": about_demo,
    }
    demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys(), index=0)
    
    st.divider()
    st.markdown("Made with ❤️ by [Mahdi HARZALLAH](https://www.linkedin.com/in/mahdi-harzallah/)")

page_names_to_funcs[demo_name]()