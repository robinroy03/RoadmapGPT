"""
Renders the website using streamlit. Run this for website.
"""

import streamlit as st
import streamlit.components.v1 as components

from src.roadmapgpt import ai    # exposes the LLM endpoints to streamlit 

api_key = st.secrets.TOKEN

def mermaid(code: str) -> None:
    # Doing with a mermaid.js code I found from the web. It does what it should and I won't touch this again for some time. 
    
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

def display(content):
    mermaid(content.choices[0].message['content'])

with st.sidebar:
    st.markdown("""
        # RoadmapGPT 🗺️\n
        RoadmapGPT aims to give you a customized and comprehensive roadmap for all topics, helping you learn faster and better.\n
        Enter a keyword for one domain you would like to know more about.
    """)

with st.form("Input form"):
    with st.sidebar:
        user_prompt = st.sidebar.text_input(label = "Enter a domain to generate roadmap", placeholder = "Machine Learning, C++ ..")
        submitted = st.form_submit_button("Submit")

    if submitted and user_prompt != '':
        llm_output = ai.getOutput(user_prompt, api_key)
        display(llm_output)

with st.sidebar:
    st.markdown("""
        ---

        We are Open Source!\n
        To contribute, please see the [github repo](https://github.com/robinroy03/RoadmapGPT) 
    """)