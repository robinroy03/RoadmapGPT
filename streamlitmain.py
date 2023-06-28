# streamlit community cloud entry point
# considering streamlit won't support relative imports natively smh

# TODO: this is too hacky, fix when a fix is available

from subprocess import Popen
import sys

Popen([f"{sys.executable}", '-m', 'streamlit', 'run', 'src/streamlitfront/main.py'])