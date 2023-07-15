"""
Renders the website using streamlit. Run this for website.
"""

import streamlit as st
import streamlit.components.v1 as components

from src.roadmapgpt import ai    # exposes the LLM endpoints to streamlit 
from src.roadmapgpt.utils import (output_sanitizer, dict_to_mermaid, store_to_gsheet)

api_key = st.secrets.TOKEN

def mermaid(code: str) -> None:
    """
    Renders with mermaid.js, builds an html component over streamlit and render js over it.
    """    
    components.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        # TODO : There must be a better way, something like pinch to zoom. Now the website is huge when rendered. 
        width = 5000, height = 5000
    )

def display(user_prompt, content):
    output = content.choices[0].message['content']
    output = output_sanitizer(output)

    if output == {}:
        st.write("""
                 Output Parsing Error. Try again with a similar sounding prompt. 
                """)
        
        store_to_gsheet(content, user_prompt = user_prompt, error = True, **st.secrets.gspread_credentials)        # passing google sheet credentials
    else:
        output = dict_to_mermaid(output)
        store_to_gsheet(content, user_prompt = user_prompt, error = False, **st.secrets.gspread_credentials)    
        mermaid(output)

with st.sidebar:
    st.markdown("""
        # RoadmapGPT 🗺️\n
        RoadmapGPT aims to give you a customized and comprehensive roadmap for all topics, helping you learn faster and better.\n
        Enter a keyword for one domain you would like to know more about.
    """)

with st.form("Input form"):
    with st.sidebar:
        user_prompt = st.sidebar.text_input(label = "Enter a domain to generate roadmap", placeholder = "Machine Learning, Chess ..")
        submitted = st.form_submit_button("Submit")

    if submitted and user_prompt != '':
        llm_output = ai.getOutput(user_prompt, api_key)
        display(user_prompt, llm_output)

with st.sidebar:
    st.markdown("""
        ---
                
        __General Tips:__\n
        If the output fails to parse, try a similar sounding different prompt.\n
        Try Machine Learning advanced, introduction to c++ and so on to get personalized roadmaps.
                
        ---

        We are Open Source!\n
        To contribute, please see the [github repo](https://github.com/robinroy03/RoadmapGPT) 
    """)