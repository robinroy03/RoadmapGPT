"""
Renders the website using Streamlit. Run this for the website.
"""

import streamlit as st
from src.roadmapgpt import ai
from src.roadmapgpt.utils import (output_sanitizer, dict_to_mermaid, store_to_gsheet)

api_key = st.secrets.TOKEN

def mermaid(code: str) -> None:
    """
    Renders a Mermaid diagram using st.write.
    """
    st.write(
        f"""
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@latest/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """
    )

def display(user_prompt, content):
    output = content.choices[0].message['content']
    output = output_sanitizer(output)

    if output == {}:
        st.write("Output Parsing Error. Try again with a similar sounding prompt.")
        store_to_gsheet(content, user_prompt=user_prompt, error=True, **st.secrets.gspread_credentials)
    else:
        output = dict_to_mermaid(output)
        store_to_gsheet(content, user_prompt=user_prompt, error=False, **st.secrets.gspread_credentials)
        mermaid(output)

st.set_page_config(layout="wide")

with st.sidebar:
    st.markdown("""
        # RoadmapGPT 🗺️
        RoadmapGPT aims to give you a customized and comprehensive roadmap for all topics, helping you learn faster and better.
        Enter a keyword for one domain you would like to know more about.
    """)

with st.form("Input form"):
    with st.sidebar:
        user_prompt = st.sidebar.text_input(label="Enter a domain to generate roadmap", placeholder="Machine Learning, Chess ..")
        submitted = st.form_submit_button("Submit")

    if submitted and user_prompt != '':
        llm_output = ai.getOutput(user_prompt, api_key)
        display(user_prompt, llm_output)

with st.sidebar:
    st.markdown("""
        ---

        __General Tips:__
        If the output fails to parse, try a similar sounding different prompt.
        Try Machine Learning advanced, introduction to c++ and so on to get personalized roadmaps.

        ---

        We are Open Source!
        To contribute, please see the [GitHub repo](https://github.com/robinroy03/RoadmapGPT)
    """)
