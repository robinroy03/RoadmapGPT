import openai
from dotenv import load_dotenv
from os import getenv

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

sys_prompt = """
I want you to make a graph for me, it must be directed and should be simple. The goal is to make a roadmap for a domain. A prompt for a domain will be given, you must find all the other domains/subdomains the user must know before venturing into that domain, to gain mastery. 
For example, when a user prompt "Data Structures and Algorithms", you should return back all the topics the user should master to have a "decent" understanding of the topic, these include Arrays, hashing, 2 pointer, stack, binary search, sliding window, linked list, trees, tries and so on. 

Example: 
The format you must return it is (and only return this, no other text):

{
[Node_Name : " Arrays and Hashing", Difficulty: "Easy", Next_Nodes: ["2-pointers", "stack"],
[Node_Name : "2-pointers", Difficulty: "Intermediate", Next_Nodes: ["Binary Search", "Sliding Window", "Linked List"],
[Node_Name : "stack",  Difficulty: "Intermedia", Next_Nodes: ["None"]
}

In the above example, I've 3 variables for each node, Node name, level of difficulty and the next nodes. The next nodes point to the next nodes, and if None is mentioned, it points to nothing, it ends there.
The difficulty parameter is based on relative difficulty compared to the prior nodes, it is to give a rough overview to the user.
Keep the graph broad and concise, go over all the major topics from that domain. 
"""

messages = [
    {'role' : 'system', 'content' : sys_prompt},    # SYSTEM PROMPT
]

user_prompt = input("Enter your domain to study upon : ")

messages.append({'role' : 'user', 'content' : user_prompt})
a = get_completion(messages)

print(a)