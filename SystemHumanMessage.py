import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

def apply_template():
    if "Langchain programmer" == st.session_state['templateSystem']:
        st.session_state['systemMessageQuestion']= "You are a helpful python, langchain and openai programmer."
        st.session_state['HumanMessageQuestion']= "Suggest some basic ideas of usage of langchain and openai and generate their code."
    elif "Java programmer" == st.session_state['templateSystem']:
            st.session_state['systemMessageQuestion'] = "You are a helpful java programmer."
            st.session_state['HumanMessageQuestion']= "Suggest some basic ideas of usage of Java and Spring framework, and generate their code."
    elif "Expo.io & React Native programmer" == st.session_state['templateSystem']:
        st.session_state['systemMessageQuestion'] = "You are a helpful Expo.io and React Native programmer."
        st.session_state['HumanMessageQuestion']= "Suggest some basic ideas of usage of Expo.io framework, and generate their code."
    elif "Travel Planner" == st.session_state['templateSystem']:
        st.session_state['systemMessageQuestion'] = "You are a helpful Travel Planner."
        st.session_state['HumanMessageQuestion']= "I am traveling to Bali suggest a plan for visit."

def work_page():
    import streamlit as st
    st.title("Streamlit & Langchain template 📝")
    st.caption("Using the power of LLMs")
    
    st.session_state['templateSystem'] = st.selectbox("Select System Message Template", ["Langchain programmer", "Java programmer", "Expo.io & React Native programmer", "Travel Planner"], index=0)
    apply_template()

    systemMessageQuestion = st.text_area("SystemMessage", value =st.session_state['systemMessageQuestion'])
    humanMessageQuestion = st.text_area("HumanMessage", value =st.session_state['HumanMessageQuestion'])

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
        st.session_state["response"] = response.content

        st.markdown(st.session_state["response"])
        if st.session_state["response"]:
            st.download_button(
            label="Download the last response",
            data=st.session_state["response"],
            file_name='report.md',
            mime='text/markdown',)
    st.stop()