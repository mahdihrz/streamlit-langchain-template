import streamlit as st

from SystemHumanMessage import work_page
from ArticleGenerator import article_generator_core_ui

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

def about_demo():
    import streamlit as st
    st.markdown(open("README.md", "r").read())
    st.stop()

with st.sidebar:
    st.title("Getting started")

    if ("openai_api_key" not in st.secrets or
        "openai_api_key" in st.secrets and
            st.secrets["openai_api_key"] == "your key here"):
        openai_api_key = st.text_input(
            "OpenAI API Key", key="chatbot_api_key", type="password")
        if openai_api_key and 'openai_api_key' not in st.session_state:
            st.session_state['openai_api_key'] = openai_api_key
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    else:
        st.session_state['openai_api_key'] = st.secrets["openai_api_key"]

    # -------- Pages  ----------
    page_names_to_funcs = {
        "Work": work_page,
        "Article Generator" : article_generator_core_ui,
        "About": about_demo,
    }
    demo_name = st.sidebar.selectbox(
        "Choose a demo", page_names_to_funcs.keys(), index=0)

    st.divider()

    options = st.container()
    options.title("Options ⚙️")

    model_to_use = options.selectbox("Select model", [
                                     "gpt-3.5-turbo-16k", "gpt-3.5-turbo-1106", "gpt-4-32k-0613", "gpt-4-1106-preview"], index=1)

    st.session_state['model_to_use'] = model_to_use
    temperature = options.slider(
        'Model Temperature?', min_value=0.0,     max_value=1.0,     step=0.1,     value=0.7)
    st.session_state['temperature'] = temperature
    st.divider()
    st.markdown(
        "Made with ❤️ by [Mahdi HARZALLAH](https://www.linkedin.com/in/mahdi-harzallah/)")

page_names_to_funcs[demo_name]()
