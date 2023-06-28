import streamlit 

import subprocess

l = subprocess.Popen(['python3', '-m', 'streamlit', 'run', 'src/streamlitfront/main.py'])
streamlit.write("Hi")