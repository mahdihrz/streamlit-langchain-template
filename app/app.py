import streamlit as st

# Setup variables
# os.environ['LANGCHAIN_TRACING_V2'] = st.secrets["openai_api_key"]["tracing"]

#Menu
WORK_MENU = "Work"
ABOUT_MENU = "About"

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

with st.sidebar:
    st.title("Getting started")
    menu = st.selectbox("Select pages", [WORK_MENU, ABOUT_MENU], index=0)

    if ("openai_api_key" not in st.secrets or
        "openai_api_key" in st.secrets and
        st.secrets["openai_api_key"] == "your key here"):
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        if openai_api_key and 'openai_api_key' not in st.session_state:
            st.session_state['openai_api_key'] = openai_api_key
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    else:
        st.session_state['openai_api_key'] = st.secrets["openai_api_key"]

    #files = st.file_uploader("Upload your data", accept_multiple_files=True, type=['txt', 'md'])
    st.divider()
    
    options = st.container()
    options.title("Options ⚙️")

    model_to_use = options.selectbox("Select model", ["gpt-3.5-turbo-16k", "gpt-4-1106-preview"], index=0)
    st.session_state['model_to_use'] = model_to_use
    temperature = options.slider('Model Temperature?',min_value=0.0,     max_value=1.0,     step=0.1,     value=0.7)
    st.session_state['temperature'] = temperature
    
    st.divider()
    st.markdown("Made with ❤️ by [Mahdi HARZALLAH](https://www.linkedin.com/in/mahdi-harzallah/)")

if menu == ABOUT_MENU:
    st.markdown(open("README.md", "r").read())
    st.stop()

if menu == WORK_MENU:
    st.title("Streamlit & Langchain template 📝")
    st.caption("Using the power of LLMs")
    question = st.text_area("Research question", placeholder="Question "
                            "to be  "
                            "asked?")

    if not question:
        st.info("Please enter a question to continue ...")
    elif st.button("🚄 Perform Request"):
        # Do what to do
        st.info("Performing")
    st.stop()

#if not files:
#    st.info("Please upload some qualitative data in the sidebar")
#    st.stop()

if 'openai_api_key' not in st.session_state:
    st.info("Please add your OpenAI API key to continue.")
    st.stop()


    # --- 
    # TODO

    # --- 
    # DONE