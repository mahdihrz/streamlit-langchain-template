import streamlit as st
from openai import OpenAI


def generate_section(prompt, model_name, temperature, openai_api_key, max_token):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(model=model_name,
        messages=[
            {"role": "system", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_token)
    return response.choices[0].message.content


def article_generator_core(subject, num_sections, max_token):
    # Set your OpenAI API key and model parameters
    openai_api_key = st.session_state["openai_api_key"]
    model_name = st.session_state['model_to_use']
    temperature = st.session_state["temperature"]

    # Generate the introductory section
    intro_prompt = f"Write an introductory section for an article about '{subject}'."
    article = generate_section(intro_prompt, model_name, temperature, openai_api_key, max_token)

    # Dynamically generate subsequent sections
    for _ in range(num_sections):
        # Generate prompt for the next section based on the article so far
        next_section_prompt = f"Based on the following article content:\n\n{article}\n\nWhat is the next important aspect to cover about '{subject}'?"
        next_topic = generate_section(next_section_prompt, model_name, temperature, openai_api_key, max_token)

        # Check if a logical conclusion has been reached or if no new topic is suggested
        if "conclusion" in next_topic.lower() or not next_topic.strip():
            break

        # Generate the content for the next topic
        content_prompt = f"Discuss the following topic in the context of '{subject}': {next_topic}"
        next_section_content = generate_section(content_prompt, model_name, temperature, openai_api_key, max_token)
        article += "\n\n" + next_section_content
    # Output the final article
    return article


def article_generator_core_ui():
    st.title("Article generator 📝")
    st.caption("In this example we use SingleChain to generate an article")
    subject = st.text_area("Subject")
    number_of_sections = st.number_input('Number of sections', min_value = 1, max_value= 5, value = 2, step = 1)
    max_token = st.number_input('Max tokens per section', min_value = 100, max_value= 10000, value = 150, step = 10)

    if 'openai_api_key' not in st.session_state:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    if not subject:
        st.info("Please write the subject of you article to continue.")
        st.stop()
    elif st.button("🚄 Perform Request"):
        st.info("Performing")
        st.session_state["response"] = article_generator_core(subject, number_of_sections, max_token)
        st.markdown(st.session_state["response"])
        if st.session_state["response"]:
            st.download_button(
                label="Download the last response",
                data=st.session_state["response"],
                file_name='article.md',
                mime='text/markdown',)
    st.stop()
