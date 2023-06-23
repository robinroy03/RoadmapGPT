# this module returns the graph node relationships

import openai

from dotenv import load_dotenv
from os import getenv

from utils import sys_prompt

# TOKEN ACCESS
load_dotenv()
openai.api_key = str(getenv("TOKEN"))

def get_completion(messages):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 0
    )
    return response

messages = [
    {'role' : 'system', 'content' : sys_prompt},    # SYSTEM PROMPT
]

def getOutput(user_prompt : str):
    messages.append({'role' : 'user', 'content' : user_prompt})
    sysOutput = get_completion(messages)

    return sysOutput