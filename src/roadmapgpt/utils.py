"""
Utility tools
"""
import gspread  # to manipulate the google sheet

import json
from datetime import datetime
from pytz import timezone

# zero-shot prompt
# TODO: Experiment with function-calling api. May return better quality output.
sys_prompt = """
You are a very smart book author. Make a book index page with all the titles and sub-titles for the book name provided by the user.
Return the output in JSON format.
Example:
{
    "<chapter name>": [
        "<sub topic 1>", 
        "<sub topic 2>"
    ],
    "<chapter name>": [
        "<sub topic 1>", 
        "<sub topic 2>"
    ]
}
"""



def store_to_gsheet(prompt, error:bool = False, **credentials):
    """
    Storing the value to google sheets
    """
    """
    Format:
    DATE | TIME | TotalTokens | PROMPT | ERROR | LLMOutputDump
    """

    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open("RoadmapGPT").sheet1

    cur_date, cur_time = datetime.now(timezone("Asia/Kolkata")).strftime("%d/%m/%Y,%H:%M:%S").split(",")
    total_token = prompt.usage.total_tokens
    user_prompt = prompt.choices[0].message['content']

    sh.append_row([cur_date, cur_time, total_token, user_prompt, error, str(prompt)])



def output_sanitizer(prompt: str) -> dict:
    """
    return dictionary from llm output
    """
    begin = prompt.find("{")
    end = prompt.find("}")
    output = prompt[begin: end + 1]
    
    try:
        output = json.loads(output)
    except json.JSONDecodeError:
        return {}
    
    return output



def dict_style_changer(file: dict) -> dict: 
    """
    parses it in such a way so that mermaid won't crash due to semicolons and such
    """
    """
    {"1[a]" : ["2[b]", "3[c]"], "4[d]" : ["5[e]", "6[f]"]}
    """
    new = {}
    count = 1

    for k, v in file.items():
        new_key = f"{count}[{k}]"
        count += 1
        temp = []

        for i in v:
            new_value = f"{count}[{i}]"
            count += 1
            temp.append(new_value)
        
        new[new_key] = temp

    return new

def dict_to_mermaid(file: dict) -> str:
    """
    returns a mermaid.js syntax to be rendered for the roadmap
    """
    file = dict_style_changer(file)
    output = """
    flowchart TB\n\t
    """
    arrow = " --> "
    thick_arrow = " ==> "

    for k, v in file.items():
        output += f"subgraph {k}\n\t{arrow.join(v)}\n\tend\n\t"
    
    output += thick_arrow.join(list(file.keys()))

    return output

if __name__ == "__main__":
    
    test1 = "{\n    \"Chapter 1: Introduction to Python Programming\": [\n        \"1.1: What is Python?\",\n        \"1.2: History of Python\",\n        \"1.3: Features of Python\"\n    ],\n    \"Chapter 2: Getting Started with Python\": [\n        \"2.1: Installing Python\",\n        \"2.2: Running Python Programs\",\n        \"2.3: Python Syntax\"\n    ],\n    \"Chapter 3: Variables and Data Types\": [\n        \"3.1: Variables\",\n        \"3.2: Numeric Data Types\",\n        \"3.3: String Data Type\"\n    ],\n    \"Chapter 4: Control Flow and Loops\": [\n        \"4.1: Conditional Statements\",\n        \"4.2: Loops\",\n        \"4.3: Break and Continue Statements\"\n    ],\n    \"Chapter 5: Functions and Modules\": [\n        \"5.1: Defining Functions\",\n        \"5.2: Function Arguments\",\n        \"5.3: Modules and Packages\"\n    ],\n    \"Chapter 6: File Handling\": [\n        \"6.1: Opening and Closing Files\",\n        \"6.2: Reading and Writing Files\",\n        \"6.3: File Modes\"\n    ],\n    \"Chapter 7: Object-Oriented Programming\": [\n        \"7.1: Classes and Objects\",\n        \"7.2: Inheritance\",\n        \"7.3: Polymorphism\"\n    ],\n    \"Chapter 8: Error Handling and Exceptions\": [\n        \"8.1: Syntax Errors\",\n        \"8.2: Exceptions\",\n        \"8.3: Handling Exceptions\"\n    ],\n    \"Chapter 9: Advanced Topics\": [\n        \"9.1: List Comprehensions\",\n        \"9.2: Generators\",\n        \"9.3: Decorators\"\n    ],\n    \"Chapter 10: Python Libraries and Frameworks\": [\n        \"10.1: NumPy\",\n        \"10.2: Pandas\",\n        \"10.3: Django\"\n    ]\n}"
    
    test1 = output_sanitizer(test1)
    assert(type(test1)) == dict, "Output should be a dict"