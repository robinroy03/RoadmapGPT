"""
Main LLM entry point. Returns the LLM responses. 
"""

import openai

from src.roadmapgpt.utils import sys_prompt

def get_completion(messages):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 0
    )
    
    return response

def getOutput(user_prompt : str, key : str):
    openai.api_key = key
    
    messages = [{'role' : 'system', 'content' : sys_prompt}]
    messages.append({'role' : 'user', 'content' : user_prompt})
    
    sysOutput = get_completion(messages)

    return sysOutput