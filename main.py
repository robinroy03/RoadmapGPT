"""
Renders the website using streamlit. Run this for website.
"""

import streamlit as st
import graphviz

from src.roadmapgpt import ai    # exposes the LLM endpoints to streamlit 

api_key = st.secrets.TOKEN

def display(content):

    # TODO : we can't zoom this. If the generated diagram is too broad, it's almost impossible to figure out anything from it. 

    graph = graphviz.Digraph()
    st.graphviz_chart(f"digraph{{{content.choices[0].message['content']}}}")

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