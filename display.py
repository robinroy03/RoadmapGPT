# not linked with the LLM, i was cooking some streamlit for fun ... but the UI/UX is 7/10 rn (in <10 lines!)

import streamlit as st
import graphviz

st.sidebar.text_input(label = "Enter your OpenAI API Key", placeholder = "Enter the key here ..")
st.sidebar.text_input(label = "Enter a domain to generate roadmap", placeholder = "I want to make cool webapps ..")

# Create a graphlib graph object
graph = graphviz.Digraph()

graph.edge('Arrays and Hashing', 'Two Pointers')
graph.edge('Arrays and Hashing', 'Stack')
graph.edge('Two Pointers', 'Binary Search')
graph.edge('Two Pointers', 'Sliding Window')
graph.edge('Two Pointers', 'Linked List')
graph.edge('Binary Search', 'Trees')
graph.edge('Linked List', 'Trees')
graph.edge('Trees', 'Tries')
graph.edge('Trees', 'Heap / Priority Queue')
graph.edge('Trees', 'Backtracking')
graph.edge('Heap / Priority Queue', 'Intervals')
graph.edge('Heap / Priority Queue', 'Greedy')
graph.edge('Heap / Priority Queue', 'Advanced Graphs')
graph.edge('Backtracking', 'Graphs')
graph.edge('Backtracking', '1-D DP')
graph.edge('Graphs', 'Advanced Graphs')
graph.edge('Graphs', 'Math and Geometry')
graph.edge('Graphs', '2-D DP')
graph.edge('1-D DP', '2-D DP')
graph.edge('1-D DP', 'Bit Manipulation')

st.graphviz_chart(graph)
