"""
Utility tools
"""

# zero-shot prompt, the output looks to be always returning in a specific format, so I'm writing a parser for that. 
# TODO: if the output is in a different format, we'll have to put it over another LLM chain
sys_prompt = """
You are a very smart book author. Make a book index page with all the titles and sub-titles for the book name provided by the user.
"""