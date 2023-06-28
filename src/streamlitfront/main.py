"""
Renders the website using streamlit. Run this for website.
"""

import streamlit as st
import graphviz

from src.roadmapgpt import ai    # exposes the LLM endpoints to streamlit 

def display(content):
    graph = graphviz.Digraph()
    st.graphviz_chart(content.choices[0].message["content"])

with st.form("Input form"):
    with st.sidebar:
        api_key = st.sidebar.text_input(label = "Enter your OpenAI API Key", placeholder = "Enter the key here ..", type="password")
        user_prompt = st.sidebar.text_input(label = "Enter a domain to generate roadmap", placeholder = "I want to make cool webapps ..")
        submitted = st.form_submit_button("Submit")

    if submitted and api_key != '' and user_prompt != '':
        llm_output = ai.getOutput(user_prompt, api_key)
        display(llm_output)