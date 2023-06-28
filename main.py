"""
Renders the website using streamlit. Run this for website.
"""

import streamlit as st
import graphviz

from src.roadmapgpt import ai    # exposes the LLM endpoints to streamlit 

def display(content):

    # TODO : we can't zoom this. If the generated diagram is too broad, it's almost impossible to figure out anything from it. 

    graph = graphviz.Digraph()
    st.graphviz_chart(f"digraph{{{content.choices[0].message['content']}}}")

with st.form("Input form"):
    with st.sidebar:
        api_key = st.sidebar.text_input(label = "Enter your OpenAI API Key", placeholder = "Enter the key here ..", type="password")
        user_prompt = st.sidebar.text_input(label = "Enter a domain to generate roadmap", placeholder = "Web Development, Python Programming ..")
        submitted = st.form_submit_button("Submit")

    if submitted and api_key != '' and user_prompt != '':
        llm_output = ai.getOutput(user_prompt, api_key)
        st.sidebar.write(llm_output)    # I think it's a good idea to give the user this info
        display(llm_output)