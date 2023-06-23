# this module renders the graph 

import streamlit as st
import graphviz

st.sidebar.text_input(label = "Enter your OpenAI API Key", placeholder = "Enter the key here ..")
st.sidebar.text_input(label = "Enter a domain to generate roadmap", placeholder = "I want to make cool webapps ..")

graph = graphviz.Digraph()

st.graphviz_chart('''
    digraph{Algebra->Calculus Algebra->Geometry Algebra->NumberTheory Calculus->DifferentialEquations Calculus->MultivariableCalculus Geometry->Trigonometry Geometry->Topology NumberTheory->Combinatorics NumberTheory->GraphTheory}
''')
