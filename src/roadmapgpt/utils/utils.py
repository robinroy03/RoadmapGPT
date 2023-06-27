"""
Utility tools
"""

sys_prompt = """
I want you to make a graph for me, it must be directed and should be simple. The goal is to make a roadmap for a domain. A prompt for a domain will be given, you must find all the other domains/subdomains the user must know before venturing into that domain, to gain mastery. 
For example, when a user prompt "Data Structures and Algorithms", you should return back all the topics the user should master to have a "decent" understanding of the topic, these include Arrays, hashing, 2 pointer, stack, binary search, sliding window, linked list, trees, tries and so on. 

Example: 
The format you must return it is (and only return this, no other text):

digraph{ArraysandHashing->TwoPointers ArraysandHashing->Stack TwoPointers->BinarySearch TwoPointers->SlidingWindow}

Keep the graph broad and concise, go over all the major topics from that domain. 
"""