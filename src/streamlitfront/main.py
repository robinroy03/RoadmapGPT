"""
Renders the website using streamlit. Run this for website.
"""

import streamlit as st

import graphviz

from src.roadmapgpt import ai    # exposes the LLM endpoints to streamlit 

api_key = st.sidebar.text_input(label = "Enter your OpenAI API Key", placeholder = "Enter the key here ..")
user_prompt = st.sidebar.text_input(label = "Enter a domain to generate roadmap", placeholder = "I want to make cool webapps ..")

graph = graphviz.Digraph()

llm_output = ai.getOutput(user_prompt, api_key)

# st.graphviz_chart('''
#     digraph{Algebra->Calculus Algebra->Geometry Algebra->NumberTheory Calculus->DifferentialEquations Calculus->MultivariableCalculus Geometry->Trigonometry Geometry->Topology NumberTheory->Combinatorics NumberTheory->GraphTheory}
# ''')

st.graphviz_chart(f"digraph\{{llm_output\}}")