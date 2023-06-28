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

with st.sidebar:
    st.markdown("""
        # RoadmapGPT 🗺️\n
        RoadmapGPT aims to give you a customized and comprehensive roadmap for all topics, helping you learn faster and better.\n
        Enter a keyword for one domain you would like to know more about.
    """)

with st.form("Input form"):
    with st.sidebar:
        api_key = st.sidebar.text_input(label = "Enter your OpenAI API Key", placeholder = "Enter the key here ..", type="password")
        user_prompt = st.sidebar.text_input(label = "Enter a domain to generate roadmap", placeholder = "Web Development, Python Programming ..")
        submitted = st.form_submit_button("Submit")

    if submitted and api_key != '' and user_prompt != '':
        llm_output = ai.getOutput(user_prompt, api_key)
        st.sidebar.write(llm_output)    # I think it's a good idea to give the user this info
        display(llm_output)


with st.sidebar:
    st.markdown(""" 
        ---
        
        You must have a valid OpenAI API key to use this application. The token usage and related info will be displayed to you after running.
        
        ---
        A project by [Robin Roy](https://twitter.com/_RobinRoy)
        To contribute, please see the [github repo](https://github.com/robinroy03/RoadmapGPT) 
    """)